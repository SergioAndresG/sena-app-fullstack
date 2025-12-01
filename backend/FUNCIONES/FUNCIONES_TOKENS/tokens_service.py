from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from connection import crear
from connection import get_db
from MODELS import Usuarios
from MODELS.token_blacklist import TokenBlacklist
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import uuid
import logging
from dotenv import load_dotenv
import os

load_dotenv()

# --- Configuración de Seguridad ---
SECRET_KEY = os.getenv("SECRET_KEY") # -> traemos la llave con que genramos los tokens
ALGORITHM = os.getenv("ALGORITHM") # -> traemos el algoritmo usado para generarlos
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")) # -> el tiempo de expiracion de los tokens
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")) # -> el tiempo de expiracion del refresh


# --- Inicialización ---
# -> Creamos un contexto de hashing para contraseñas. 
#    Usamos el algoritmo bcrypt, y con "bcrypt__rounds=12" ajustamos el *work factor* 
#    (la cantidad de iteraciones que bcrypt ejecuta internamente para aumentar la seguridad).
pwd_context = CryptContext(schemes=["bcrypt"], bcrypt__rounds=12)

# -> Dependencia de seguridad que extrae automáticamente el token JWT del header "Authorization: Bearer <token>".
#    "tokenUrl='login'" sirve principalmente para la documentación de Swagger, indicando dónde se obtiene el token.
#    "auto_error=False" hace que no se lance automáticamente un error 401 si no hay token,
#    sino que retorne None, permitiendo manejar la respuesta.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", auto_error=False)

# utilizamos los loggers para mostrar informacion
logging.basicConfig(level=logging.INFO) #-> mostrara información a nivel de INFO o superior
logger = logging.getLogger(__name__) #-> usando como nombre el modulo actual


# --- Funciones de Utilidad de Tokens ---

#-> definimos la función para crear los tokens, "data", los datos que estara dentro del token, 
#   "expires_delta" indica el tiempo que durara el token antes de expirar
def create_access_token(data: dict, expires_delta: timedelta = None): 
    #-> Creamos una copia de "data", para luego agregar mas claves
    to_encode = data.copy()

    if expires_delta: #-> si el valor del tiempo existe
        # definimos una variable
        expire = datetime.now(timezone.utc) + expires_delta #-> obtenemos la fecha y hora actual y sumamos el valor de timedelta
    else:
        # si el valor es None, o no existe, le pasamos un valor manual de 15 minutos
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    # a la copia que guradmos le actualizamos la siguiente información
    to_encode.update({
        "exp": expire, # -> (Expirtion )el tiempo de expiración del token (que entiende JWT)
        "type": "access", # -> el tipo de token en este caso "access"
        "iat": datetime.now(timezone.utc), # -> (Issued At - fecha de emisión) la fecha y hora de hoy en el que se genero 
        "jti": str(uuid.uuid4()) # -> (JWT ID) el identificador unico del token, para poder usarlos si es nesesario en listas negras (revocaciónn)
    })
    # retornmos el diccionario con la data "to_encode",y firmamos con la llave "SECRET_KEY", y el algoritmo a usar para el token "algorithm"
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) 


# -- Funcion que usamos para refrescar los tokens ---
def create_refresh_token(data: dict): #-> Entra como parametro la data que vamos a refrecar
    # -> Se calcula el tiempo de expiración sumando la fecha y hora actual más los días configurados en .env
    # (REFRESH_TOKEN_EXPIRE_DAYS). Este será el límite hasta el cual el refresh token es válido.
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS) 
    #-> Creamos una copia de "data", para luego agregar mas claves
    to_encode = data.copy()
    # a la copia que guradmos le actualizamos la siguiente información
    to_encode.update({
        "exp": expire, # -> (Expirtion )el tiempo de expiración del token (que entiende JWT)
        "type": "refresh", # -> el tipo de token en este caso "refresh"
        "iat": datetime.now(timezone.utc), # -> (Issued At - fecha de emisión) la fecha y hora de hoy en el que se refresco 
        "jti": str(uuid.uuid4()) # (JWT ID) el identificador unico del token
    })
    # -> retormos el token firmado, con la informacion y con el algoritmo implementeado
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# --- Funcion para verificar los tokens ---

#-> se le pasa como parametro, el token, sesion a la base de datos, 
# el parámetro expected_type define si estamos verificando un access token o un refresh token, 
# esto evita que un refresh token se use directamente para acceder.
def verify_token(token: str, db: Session, expected_type: str = "access"):

    # -> Se define una excepción estándar que 
    # será reutilizada en cualquier error de validación, 
    # de modo que siempre devolvemos un error 401 con el mismo formato.
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido o expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # si no llega ningun token devolvemos el error
    if not token:
        raise credentials_exception
    
    try:
        # Cuando decodificamos con jwt.decode, la librería valida automáticamente 
        # si el token está firmado correctamente y si ha expirado (campo exp).
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # en una variable, guardamos el tipo de token trayendolo del "type" que viene en el "payload" 
        token_type = payload.get("type")
        # el "jti" como identificador tambien lo traemos
        jti = payload.get("jti")

        # si el tipo de token obtenido es diferente al que recibe la funcion o no trae su identificador unico, lanzamos error
        if token_type != expected_type or not jti:
            raise credentials_exception

        # La verificación en la tabla TokenBlacklist asegura que tokens previamente invalidados 
        # (por logout, expiracion) no puedan volver a usarse, incluso si todavía no han expirado.
        token_in_db = db.query(TokenBlacklist).filter(TokenBlacklist.jti == jti).first()

        # si el token esta en el blacklist de la base de datos devolvemos un error
        if token_in_db:
            raise credentials_exception
        
        # al completar la operacion retornamos el "payload" del token verificado
        return payload
    except JWTError:
        # si se capturo algun error lo interrumpimos la operación 
        raise credentials_exception


# --- Dependencia de Usuario Actual ---

# -> Definimos una función asincronica, que recibe como parametros, el token con Depends(oauth2_scheme) extrae automáticamente el token del 
# header Authorization: Bearer <token> en la petición, y la sesión a la base de datos
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # si no llega el token, manejamos manualmente
    if not token:
        return None # Permite rutas con usuarios opcionales, es decir que no requieran autenticación
    try:
        #-> llamamos a la función que verifica el token, le pasmos el token, la sesión, y el tipo de token
        payload = verify_token(token, db, expected_type="access")
        #-> en esta variaable traemos el dato del email, del sub, es donde guardamos el identificador
        #  pricipal del usuario que es el correo del usuario (Estandar de JWT)
        user_email: str = payload.get("sub")
        #-> si no hay email para ese usuarios, devolvemos que el contenido del token es invalido
        if user_email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Contenido invalido del token")
        
        #-> en una variable hacemos la consulta a la base de datos verificando que el email exista
        user = db.query(Usuarios).filter(Usuarios.correo == user_email).first()
        #-> si la variable llega vacia lanzamos un error
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado")
        #-> si la operacion sale bien, retornamos la información del usuario
        return user
    # si ocurre aluna excepción, la volvemos a lanzar para que fastapi la maneje y retorne una respuesta adecuada
    except HTTPException:
        raise

    """
    En resumen, esta función valida el token recibido, obtiene el 
    usuario asociado desde la base de datos y lo retorna. 
    Si el token es inválido, está vacío o el usuario no existe, lanza un error 401.
    """

def cleanup_expired_tokens():
    """Elimina tokens caducados de la tabla TokenBlacklist."""
    db = Session(bind=crear)
    try:
        now = datetime.now(timezone.utc)
        expired_tokens = db.query(TokenBlacklist).filter(TokenBlacklist.expires_at < now).all()
        
        for token in expired_tokens:
            db.delete(token)
            print(f"🗑️ Token expirado eliminado: {token.jti}")
        
        db.commit()
    except Exception as e:
        print(f"❌ Error eliminando tokens caducados: {e}")
        db.rollback()
    finally:
        db.close()

