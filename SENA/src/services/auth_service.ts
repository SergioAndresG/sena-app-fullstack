import axios from 'axios'

const API_BASE_URL = 'http://127.0.0.1:8000'

export const authService = {
  // Configurar el token en axios
  setAuthToken(token: string) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
  },
  
  // Verificar si el token es válido
  isTokenValid(): boolean {
    const token = localStorage.getItem('access_token')
    if (!token) return false
    
    try {
      const payload = JSON.parse(atob(token.split('.')[1]))
      const currentTime = Date.now() / 1000
      return payload.exp > currentTime
    } catch {
      return false
    }
  },
  
  // Obtener datos del usuario desde localStorage
  getCurrentUserFromStorage() {
    try {
      const userStr = localStorage.getItem('user')
      return userStr ? JSON.parse(userStr) : null
    } catch {
      return null
    }
  },
  
  // Obtener datos frescos del usuario desde el servidor
  async getCurrentUserFromServer() {
    try {
      const token = localStorage.getItem('access_token')
      if (!token) throw new Error('No token found')
      
      this.setAuthToken(token)
      
      const response = await axios.get(`${API_BASE_URL}/me/`)
      return response.data
    } catch (error) {
      console.error('Error al obtener usuario del servidor:', error)
      throw error
    }
  },
  
  // Logout
  logout() {
    localStorage.removeItem('access_token')
    localStorage.removeItem('user')
    delete axios.defaults.headers.common['Authorization']
  }
}