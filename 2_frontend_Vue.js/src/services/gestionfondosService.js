import api from './api';


export const createFondo = async (id_usuario, dinero_incial, dinero_final, fecha_fin) => {
  try {
    const response = await api.post('/Manejo-dinero/create', { // Updated endpoint
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
    // Corrected query parameter formatting
    const response = await api.get(`/Manejo-dinero/all-manejo-caja-paginated/?page=${page}&page_size=${pageSize}`);
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

export const updateFondo = async (id_manejo_caja, dinero_inicial, dinero_final, fecha_fin) => {
  try {
    const response = await api.put(`/Manejo-dinero/update-manejo-caja-by-id${id_manejo_caja}`, {
        dinero_inicial: dinero_inicial,
        dinero_final: dinero_final,
        fecha_fin: fecha_fin,
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

export const deleteFondo = async (id_manejo_caja) => {
  try {
      const response = await api.delete(`/Manejo-dinero/delete-manejo-caja-by-id${id_manejo_caja}`, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
          }
      });
      return response;
  } catch (error) {
      if (error.response) {
          throw error; // Lanza el error para que lo maneje el store
      } else {
          throw new Error('Error de red o de servidor'); // Manejar errores de red
      }
  }
};

export const getFondoById = async (id_manejo_caja) => {
  try {
    const response = await api.get(`/Manejo-dinero/get-manejo-caja-by-id${id_manejo_caja}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response.data; // Devuelve solo los datos de respuesta
  } catch (error) {
    if (error.response) {
      console.error('Detalles del error al obtener el fondo por ID:', error.response.data); // Mostrar detalles del error
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};


