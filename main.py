from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from connection import base, crear
from ENDPOINTS.fichas import router_tokens
from ENDPOINTS.formatos import router_format
from ENDPOINTS.aprendices import router_aprendices
from ENDPOINTS.login import router_login
from ENDPOINTS.usuarios import router_usuarios


from FUNCIONES.FUNCIONES_FICHAS.delete_fichas import clean_old_db_tokens, cleanup_old_db_records
from FUNCIONES.FUNCIONES_TOKENS.tokens_service import cleanup_expired_tokens
from MODELS.a_usuarios import Usuarios
from MODELS.archivo_excel import ArchivoExcel


from MIDELWARE.security_middleware import SecurityMiddleware

# --- Imports para el Scheduler ---
import os
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI(title="SENA - Procesador de Fichas")

# --- Lógica del Scheduler para Limpieza de Archivos ---
REPORTS_DIR = "archivos_exportados"
scheduler = BackgroundScheduler(daemon=True)

def cleanup_old_reports():
    """Elimina los archivos de reporte con más de 30 días de antigüedad."""
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(days=30)
    
    if not os.path.exists(REPORTS_DIR):
        return

    for root, dirs, files in os.walk(REPORTS_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_modified_time < cutoff:
                    os.remove(file_path)
                    print(f"Eliminado archivo antiguo: {file_path}")
            except Exception as e:
                print(f"Error eliminando {file_path}: {e}")

@app.on_event("startup")
def start_scheduler():
    """Inicia el scheduler y añade la tarea de limpieza."""
    # Se ejecuta todos los días a las 00:00
    scheduler.add_job(cleanup_old_reports, 'cron', hour=0, minute=0)
    scheduler.add_job(cleanup_old_db_records, 'cron', hour=0, minute=0)  
    scheduler.add_job(clean_old_db_tokens, 'cron', hour=0, minute=0)
    scheduler.add_job(cleanup_expired_tokens, 'cron', hour=0, minute=0)

    scheduler.start()

@app.on_event("shutdown")
def shutdown_scheduler():
    """Detiene el scheduler al apagar la aplicación."""
    scheduler.shutdown()
    print("Scheduler detenido.")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # URLs de Vue
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_tokens)
app.include_router(router_format)
app.include_router(router_aprendices)
app.include_router(router_login)
app.include_router(router_usuarios)


# Agregar middleware de seguridad
app.add_middleware(SecurityMiddleware, max_requests_per_minute=100)


base.metadata.create_all(bind=crear)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)