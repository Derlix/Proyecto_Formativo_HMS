import api from './api'; 


export const createFondo = async (id_usuario, dinero_incial, dinero_final, fecha_fin) => {
    try {
      const response = await api.post('/Manejo-dinero/', {
        id_usuario,
        dinero_incial,
        dinero_final,
        fecha_fin,
      });
  
      console.log('Respuesta de la API:', response); // Para depurar
      return response.data; // Devolver solo los datos de respuesta
    } catch (error) {
      if (error.response) {
        console.error('Detalles del error:', error.response.data); // Mostrar detalles del error
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  };


export const obtenerFondosPaginados = async (page = 1, pageSize = 10) => {
  try {
    // Realiza la solicitud a la API con los parámetros de paginación
    const response = await api.get(`/Manejo-dinero/all/?page=${page}&page_size=${pageSize}`);

    return response.data; // Devuelve solo los datos de respuesta
  } catch (error) {
    if (error.response) {
      console.error('Detalles del error al obtener fondos:', error.response.data); // Mostrar detalles del error
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};