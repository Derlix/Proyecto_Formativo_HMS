import api from '../api';

// Función para obtener todas las habitaciones
export const info_habitaciones = async () => {
    try {
      const response = await api.get('/habitacion/get_all_rooms/', {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
        }
      });
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  };