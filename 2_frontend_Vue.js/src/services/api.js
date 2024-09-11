import axios from 'axios';
import router from '@/router'; // Importa directamente el router

// Crear una instancia de Axios
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL, // Usar la URL de la API desde el archivo .env
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }
});

// Interceptor para manejar errores
api.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error.response && error.response.status === 401 && error.response.data.detail === "Invalid token") {
      // Redirigir a la página de login
      router.push('/'); // Reemplaza '/' con la ruta a la que deseas redirigir
    }
    return Promise.reject(error);
  }
);

export default api;
