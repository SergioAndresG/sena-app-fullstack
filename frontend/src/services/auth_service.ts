import axios, { AxiosInstance } from 'axios';

/**
 * Configuración base 
 * Estas constantes defienen la comunicación con el backend y el almacenamineto local
 */
const API_BASE_URL = 'http://localhost:8000'; // URL base de la api
const TOKEN_KEY = 'access_token'; // la variable y nombre que tendra el token, en localStorage
const USER_KEY = 'user'; // Clave para guardar datos del usuario en el localStorage


/**
 * Interfaz que tendra el token JWT
 */
interface JWTPayload {
  exp: number; // Timestamp de expiración
  type: string; // Tipo de token: "access", "refresh"
  [key: string]: any; // Permite mas campos personalizados
}

/**
 * Interfaz del usuario
 */
interface User {
  id: string;
  nombre: string;
  apellidos: string;
  correo: string;
  rol: string;
}

/**
 * SERVICIO DE AUTENTICACIÓN
 * 
 * ARQUITECTURA DE TOKENS:
 * 
 * 1. ACCESS TOKEN (corta duración: 1-60 min)
 *    - Se guarda en localStorage
 *    - Se envía en header Authorization: Bearer <token>
 *    - Se usa para autenticar cada request a la API
 *    - Cuando expira, se renueva automáticamente con el refresh token
 * 
 * 2. REFRESH TOKEN (larga duración: 7-30 días)
 *    - Se guarda en cookie HttpOnly (solo el servidor puede accederla)
 *    - JavaScript NO puede leerla (document.cookie no la muestra)
 *    - El navegador la envía automáticamente en cada request
 *    - Se usa ÚNICAMENTE para renovar el access token
 * 
 * FLUJO DE AUTENTICACIÓN:
 * 
 * LOGIN:
 *   Usuario → Credenciales → Backend
 *   Backend → Access Token (localStorage) + Refresh Token (cookie HttpOnly)
 * 
 * REQUEST NORMAL:
 *   Frontend → Request + Access Token → Backend
 *   Backend → Response
 * 
 * TOKEN EXPIRADO:
 *   Frontend → Request + Access Token expirado → Backend
 *   Backend → 401 Unauthorized
 *   Interceptor detecta 401 → POST /refresh (con cookie automática)
 *   Backend verifica cookie → Nuevo Access Token
 *   Interceptor reintenta request original con nuevo token → Success
 */



// Servicio de autenticación
class AuthService {
  private api: AxiosInstance; // Instancia de axios configurada para la API

  constructor() {
    // CONFIGURACIÓN GLOBAL: Todas las request de axios configurada para la API
    // esto es importante para que las cookies se envien automaticamente
    axios.defaults.withCredentials = true;
    
    // Crear una instancia personalizada
    this.api = axios.create({
      baseURL: API_BASE_URL,
      withCredentials: true, // enviar las cookies en cada request
      timeout: 10000, // TImeout de 10segundos
      headers: {
        'Content-Type': 'application/json', // formato json
      },
    });

    // configurar los interceptores (middelware) para manejar requests y responses
    this.setupInterceptors();
  }

  /**
   * interceptores de axios:
   * estos interceptores son middleware que procesan  requests/responses antes/despues de enviarlos
   */
  private setupInterceptors(): void {
    /**
     * REQUEST INTERCEPTOR
     * Se ejecuta antes de enviar cada request
     * Proposito: Añadir el access token al header de Authorization
     */
    this.api.interceptors.request.use(
      (config) => {
        const token = this.getToken();
        if (token) {
          // Añadir el token al header: Authorization: Bearer <token>
          config.headers['Authorization'] = `Bearer ${token}`;
        }
        config.withCredentials = true; // Aseguramos que se envia las cookies
        
        // DEBUG: Verificar cookies antes de cada request (Solo en desarrollo)
        console.log(`📤 REQUEST to ${config.url}`);
        console.log(`🍪 Cookies disponibles:`, document.cookie);
        
        return config;
      },
      (error) => Promise.reject(error)
    );

    /**
     * RESPONSE INTERCEPTOR
     * Se ejecuta DESPUES de recibir cada response  (o error)
     * Proposito Manejar automaticamente  al revocacionde tokens cunado expiran
     */
    this.api.interceptors.response.use(
      (response) => { // Si la response es exitosa, pasarla sin cambios
        console.log(`📥 RESPONSE ${response.status} from ${response.config.url}`);
        return response;
      },
      async (error) => {
        const originalRequest = error.config;
        // Si recibimos 401 (Unauthorized) y no hemos intentado refresh antes
        if (error.response?.status === 401 && !originalRequest._retry) {
          originalRequest._retry = true; // marcar para no tener
          
          try {
            // logs para depuración
            console.log('🔄 Token expirado, intentando refresh...');
            // Intentar renovar el token usando el refresh token (cookie HttpOnly)
            const newToken = await this.refreshToken();
            // logs para depuración
            console.log('✅ Token refreshed exitosamente');
            // Actualizar si elrequest original viene con eñtoken
            originalRequest.headers['Authorization'] = `Bearer ${newToken}`;
            // reintentar el request original con el nuevi token
            return this.api(originalRequest);
          } catch (refreshError) {
            console.log('❌ Error en refresh, limpiando auth...');
            // si el refresh falla limpiar autenticacion y rechazar
            this.clearAuth();
            return Promise.reject(refreshError);
          }
        }
        
        return Promise.reject(error);
      }
    );
  }

  private getToken(): string | null {
    return localStorage.getItem(TOKEN_KEY);
  }

  setTokens(token: string): void {
    localStorage.setItem(TOKEN_KEY, token);
    console.log('🔐 Access token guardado');
  }

    /**
   * VALIDACION DE TOKENS
   * Decodifica el JWT y verifica si ha expirado los JWT  y verifica si ha expirado
   * los JWT tienen 3 partes separadas por puntos: header.payload.signature
   * el payload esta codificado en base 64 y contiene exp (expiración)
   * 
   */

  isTokenValid(): boolean {
    const token = this.getToken();
    if (!token) return false;
    
    try {
      // Decodificar la segunda parte del JWT (payload)
      const payload: JWTPayload = JSON.parse(atob(token.split('.')[1])); // Tiempo actual en segundos  
      const currentTime = Math.floor(Date.now() / 1000); 
      // comparar tiempo actual con tiempo de expiración 
      const isValid = payload.exp > currentTime;
      // log si el token es valido y cuando expira
      console.log(`🔍 Token válido: ${isValid}, expira: ${new Date(payload.exp * 1000)}`);
      return isValid;
    } catch {
      return false; // Si falla la decodificacion el token es valido
    }
  }

  /**
   * RENOVACIÓN DE TOKEN (REFRESH)
   * 
   * IMPORTANTE: No intentamos verificar si existe la cookie refresh_token con JavaScript
   * porque es HttpOnly (invisible para JS). Simplemente hacemos el request y:
   * 
   * - Si la cookie existe y es válida → Backend devuelve nuevo access token
   * - Si la cookie no existe o es inválida → Backend devuelve 401
   * 
   * El navegador envía automáticamente la cookie HttpOnly, no necesitamos hacer nada.
   */

  private async refreshToken(): Promise<string> {
    try {
      console.log('🔄 Intentando refresh token...');
      console.log('ℹ️ Nota: Las cookies HttpOnly no son visibles en document.cookie');
      
      // post a /refresh - la cookie refresh_token se envia automaticamente
      const response = await axios.post(`${API_BASE_URL}/refresh`, {}, {
        withCredentials: true, // Asegurar que se envien cookies
        headers: {
          'Content-Type': 'application/json',
        }
      });

      // se guarda la respuesta en una variable
      const newAccessToken = response.data.access_token;
      
      if (!newAccessToken) {
        throw new Error('No se recibió access_token en la respuesta');
      }

      // Guardar el nuevo access token
      this.setTokens(newAccessToken);
      console.log('✅ Refresh completado exitosamente');
      return newAccessToken;
    } catch (error: any) {
      // log de error (quitar en produccion)
      console.error('❌ Error en refresh:', {
        status: error.response?.status,
        data: error.response?.data,
        message: error.message
      });
      // si falla el refresh, propagar el error para que el interceptor limpie la auth
      throw error;
    }
  }

   /**
   * GESTIÓN DEL USUARIO
   * Métodos para obtener y guardar información del usuario
   */
  
  // Obtener usuario guardado localmente (sin hacer request al servidor)
  getCurrentUserFromStorage(): User | null {
    try {
      const userStr = localStorage.getItem(USER_KEY);
      return userStr ? JSON.parse(userStr) : null;
    } catch {
      return null;
    }
  }

  // Guardar usuario en localStorage
  private setUser(user: User): void {
    localStorage.setItem(USER_KEY, JSON.stringify(user));
  }

  // Obtener usuario actual desde el servidor (hace request con token)
  async getCurrentUserFromServer(): Promise<User> {
    try {
      const response = await this.api.get<User>('/me');
      const userData = response.data;
      
      // Guardar localmente para acceso rápido
      this.setUser(userData);
      
      return userData;
    } catch (error) {
      throw error;
    }
  }

  /**
   * LOGIN
   * 
   * FLUJO:
   * 1. Enviar credenciales al backend
   * 2. Backend valida y devuelve:
   *    - access_token (JSON)
   *    - refresh_token (cookie HttpOnly)
   *    - user (JSON)
   * 3. Guardar access_token en localStorage
   * 4. Guardar user en localStorage
   * 5. La cookie refresh_token se guarda automáticamente en el navegador
   */
  async login(email: string, password: string): Promise<User> {
    try {
      const response = await axios.post(`${API_BASE_URL}/login`, {
        correo: email,
        contraseña: password
      }, {
        withCredentials: true, // CRÍTICO: permite recibir la cookie HttpOnly
        headers: {
          'Content-Type': 'application/json',
        }
      });

      const { access_token, user } = response.data;
      
      if (!access_token || !user) {
        throw new Error('Respuesta de login inválida');
      }

      // Guardar access token y usuario localmente
      this.setTokens(access_token);
      this.setUser(user);
      
      // NOTA: La cookie refresh_token ya está guardada por el navegador
      // No podemos verla con document.cookie porque es HttpOnly
      
      return user;
    } catch (error: any) {
      throw error;
    }
  }

  /**
   * LOGOUT
   * 
   * FLUJO:
   * 1. Notificar al backend (invalida refresh token en blacklist)
   * 2. Limpiar datos locales (access token y usuario)
   * 3. Backend elimina la cookie refresh_token
   */
  async logout(): Promise<void> {
    try {
      await this.api.post('/logout');
    } catch (error) {
      // Incluso si falla el logout en servidor, limpiar localmente
    } finally {
      this.clearAuth();
    }
  }

  /**
   * LIMPIAR AUTENTICACIÓN
   * Elimina toda la información de autenticación del lado del cliente
   */
  private clearAuth(): void {
    localStorage.removeItem(TOKEN_KEY);
    localStorage.removeItem(USER_KEY);
    delete axios.defaults.headers.common['Authorization'];
  }

  /**
   * UTILIDADES
   */
  
  // Verificar si el usuario está autenticado (token válido)
  isAuthenticated(): boolean {
    return this.isTokenValid();
  }

  // Obtener la instancia de axios configurada (para usar en otros servicios)
  getApiInstance(): AxiosInstance {
    return this.api;
  }

  /**
   * DEBUG
   * Método útil para diagnosticar problemas de autenticación
   */
  debugCookieStatus(): void {
    console.log('=== DEBUG COOKIE STATUS ===');
    console.log('URL base:', API_BASE_URL);
    console.log('Dominio actual:', window.location.hostname);
    console.log('Puerto actual:', window.location.port);
    console.log('Cookies visibles en JS:', document.cookie);
    console.log('⚠️ IMPORTANTE: Las cookies HttpOnly NO aparecen en document.cookie');
    console.log('Access token en localStorage:', !!this.getToken());
    console.log('Usuario autenticado:', this.isAuthenticated());
  }
}

// Exportar una instancia única (Singleton)
// Esto asegura que toda la app use la misma instancia del servicio
export const authService = new AuthService();
export { AuthService };