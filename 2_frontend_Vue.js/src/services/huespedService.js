import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

// Función para crear un nuevo usuario
export const createHuesped = async (nombre_completo, tipo_documento, numero_documento, fecha_expedicion, email, telefono, ocupacion, direccion) => {
  try {
    const response = await api.post('/huespedes/create_huesped', {
      nombre_completo,
      tipo_documento,
      numero_documento,
      fecha_expedicion,
      email,
      telefono,
      ocupacion,
      direccion,
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

// Función para obtener un usuario por su email
export const getHuespedByEmail = async (email) => {
  try {
    const response = await api.get(`/huespedes/get-huesped-by-email/?email=${encodeURIComponent(email)}`);
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};


export const getHuespedByDocument = async (numero_documento) => {
    try {
      const response = await api.get(`/huespedes/get-huesped-by-numero_documento/?numero_documento=${encodeURIComponent(numero_documento)}`);
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor'); // Manejar errores de red
      }
    }
  };

export const getAllHuespedes = async () => {
    try {
      const response = await api.get('/huespedes/get-all-huespedes/');
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  };

// Función para obtener todos los usuarios con paginación
export const getHuespedByPage = async (page = 1, pageSize = 10) => {
  try {
    const response = await api.get(`/huespedes/huespedes-by-page/?page=${page}&page_size=${pageSize}`);
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};




// Función para actualizar un usuario
export const updateHuesped = async (HuespedId, nombre_completo, tipo_documento, numero_documento, fecha_expedicion, email, telefono, ocupacion, direccion) => {
  try {
    const response = await api.put(`/huespedes/update-huesped/?id_huesped=${HuespedId}`, {
        nombre_completo: nombre_completo,
        tipo_documento: tipo_documento,
        numero_documento: numero_documento,
        fecha_expedicion: fecha_expedicion,
        mail: email,
        telefono: telefono,
        ocupacion: ocupacion,
        direccion: direccion,
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};


export const deleteHuesped = async (HuespedId) => {
  try {
      const response = await api.put(`/huespedes/delete-huesped/${HuespedId}`, {
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
}
