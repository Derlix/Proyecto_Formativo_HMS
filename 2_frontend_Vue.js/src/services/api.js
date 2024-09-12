import axios from 'axios';
import { useAuthStore } from '@/stores'; // Importa el store de Pinia
import { useSpinnerStore } from '@/stores/spinner'; // Importa el store de Pinia para el spinner
import router from '@/router'; // Importa el router de Vue

// Crear una instancia de Axios
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL, // Usar la URL de la API desde el archivo .env
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }
});

// Interceptor para añadir el token de autorización
api.interceptors.request.use(config => {
    const authStore = useAuthStore(); // Obtener el store de autenticación

    const spinnerStore = useSpinnerStore(); // Obtener el store del spinner
    spinnerStore.showSpinner(); // Mostrar spinner al iniciar la petición

    const token = authStore.accessToken;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`; // Añadir el token a las cabeceras
    }
    return config;
  }, error => {
    return Promise.reject(error);
  });

// Interceptor para manejar respuestas y errores
api.interceptors.response.use(response => {

  const spinnerStore = useSpinnerStore(); // Obtener el store del spinner
  spinnerStore.hideSpinner(); // Ocultar el spinner al recibir la respuesta

  return response;
}, error => {
  const spinnerStore = useSpinnerStore(); // Obtener el store del spinner
  spinnerStore.hideSpinner(); // Ocultar el spinner si hay un error
  
  if (error.response && error.response.status === 401 && error.response.data.detail === 'Invalid token') {
    // Elimina el token y los datos de usuario del store
    const authStore = useAuthStore();
    authStore.logout();
    // Redirigir a la página de login
    router.push('/'); 
  }
  return Promise.reject(error);
});

export default api;