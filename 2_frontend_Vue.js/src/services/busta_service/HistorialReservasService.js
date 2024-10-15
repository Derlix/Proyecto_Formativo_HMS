import api from '@/services/api';

// Obtener todo el historial de reservas
export const getAllHistorialReservas = async () => {
    try {
        const response = await api.get('/reservas/get_all', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`, // Incluye el token de autenticación
            },
        });
        return response.data; // Devuelve los datos de la respuesta
    } catch (error) {
        if (error.response) {
            throw error; // Lanza el error para que lo maneje el componente que lo llame
        } else {
            throw new Error('Error de red o de servidor'); // Manejar errores de red
        }
    }
};

export const getHistorialReservasByPage = async (page, pageSize = 10) => {
    try {
      const response = await api.get(`/reservas/paginadas/huesped?page=${page}&page_size=${pageSize}`);
      return response;
    } catch (error) {
      console.error('Error al obtener el historial de reservas paginadas:', error);
      throw error.response.data.detail;
    }
  };