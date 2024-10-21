import api from '../api'; // Asegúrate de que este path sea correcto

// Función para obtener todas las características
export const obtenerTodasCaracteristicas = async () => {
  try {
    const response = await api.get('caracteristicas/get-all-features/', {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response.data; // Retorna los datos de la respuesta
  } catch (error) {
    console.error('Error al obtener las características:', error);
    throw error;
  }
};

// Función para obtener características con paginación
export const obtenerCaracteristicasPaginadas = async (page = 1, pageSize = 10) => {
  try {
    const response = await api.get(`caracteristicas/feature-by-page/?page=${page}&page_size=${pageSize}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response.data; // Retorna los datos de la respuesta
  } catch (error) {
    console.error('Error al obtener las características:', error);
    throw error;
  }
};

// Función para editar una característica
export const actualizarCaracteristica = async (caracteristica_id, nombre_caracteristica, adicional) => {
  try {
    console.log("Datos enviados:", {
      nombre_caracteristica,
      adicional,
    });

    const response = await api.put(`caracteristicas/update_feature/?caracteristica_id=${caracteristica_id}`, {
      nombre_caracteristica,  // Asegúrate de que este sea el nombre del campo correcto
      adicional,              // Asegúrate de que este sea el nombre del campo correcto
    }, {
      headers: {
        'Content-Type': 'application/json', // Asegura que el Content-Type sea JSON
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`, // Incluye el token de autenticación
      }
    });

    return response.data; // Devuelve los datos de la respuesta en caso de éxito
  } catch (error) {
    if (error.response) {
      // Muestra los detalles de error específicos si están disponibles
      console.error('Error de la API:', error.response.data);
      throw new Error(error.response.data.detail || 'Error al procesar la solicitud');
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};



// Función para crear una nueva característica
export const crearCaracteristica = async (nombreCaracteristica, adicional) => {
  try {
    const response = await api.post('caracteristicas/feature-create', {
      nombre_caracteristicas: nombreCaracteristica,  // Correct field name
      adicional: adicional  // Correct field name
    }, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      }
    });
    return response.data; // Return the API response
  } catch (error) {
    console.error('Error al crear la característica:', error);
    throw error;
  }
};


// Función para crear una relación entre habitación y característica
export const crearRelacionHabitacionCaracteristica = async (idHabitacion, idCaracteristica) => {
  try {
    const response = await api.post(
      'habitacion-carac/create', // Asegúrate de que la ruta sea la correcta
      {
        id_habitacion: idHabitacion,
        id_caracteristica: idCaracteristica,
      },
      {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
        }
      }
    );
    return response.data; // Retorna los datos de la respuesta si es necesario
  } catch (error) {
    console.error('Error al crear la relación habitación-característica:', error);
    throw error;
  }
};

// Función para editar la relación entre habitación y característica
export const actualizarRelacionHabitacionCaracteristica = async (id_habitacion, id_caracteristica, id_usuario) => {
  try {
    const response = await api.put(`/habitacion-carac/${id_habitacion}/${id_caracteristica}`, {
      id_habitacion,
      id_caracteristica,
      id_usuario // Asegúrate de que este campo sea necesario y lo que deseas enviar
    }, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response.data; // Retorna los datos de la respuesta
  } catch (error) {
    if (error.response) {
      // Muestra los detalles de error específicos si están disponibles
      console.error('Error de la API:', error.response.data);
      throw new Error(error.response.data.detail || 'Error al procesar la solicitud');
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para eliminar la relación entre habitación y característica
export const eliminarRelacionHabitacionCaracteristica = async (id_habitacion, id_caracteristica) => {
  try {
    const response = await api.delete(`/habitacion-carac/${id_habitacion}/${id_caracteristica}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response.data; // Retorna los datos de la respuesta
  } catch (error) {
    if (error.response) {
      // Muestra los detalles de error específicos si están disponibles
      console.error('Error de la API:', error.response.data);
      throw new Error(error.response.data.detail || 'Error al procesar la solicitud');
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para eliminar una característica por ID
export const eliminarCaracteristica = async (idCaracteristica) => {
  try {
    const response = await api.delete(`caracteristicas/feature-delete/${idCaracteristica}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response.data; // Retorna los datos de la respuesta
  } catch (error) {
    console.error('Error al eliminar la característica:', error);
    throw error;
  }
};
