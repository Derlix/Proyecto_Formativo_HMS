import api from '@/services/api';

// Obtener todas las facturas
export const getAllFacturas = async () => {
    try {
      const response = await api.get('/facturacion/get_all_facturas', {
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