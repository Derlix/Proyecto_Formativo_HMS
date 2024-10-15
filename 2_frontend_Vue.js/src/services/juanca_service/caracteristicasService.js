import api from '../api'; // Asegúrate de que este path sea correcto

// Función para obtener todas las características
export const obtenerTodasCaracteristicas = async () => {
  try {
    const response = await api.post('caracteristicas/get-all-features/', {}, {
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

// Función para obtener todas las habitaciones por nombre
export const obtenerHabitacionesPorNombre = async (nombreHabitacion) => {
  try {
    const response = await api.get(`/habitacion/get_all_rooms_by_name/?room_name=${encodeURIComponent(nombreHabitacion)}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response.data; // Retorna los datos de la respuesta
  } catch (error) {
    console.error('Error al obtener las habitaciones por nombre:', error);
    throw error; // Propaga el error para que se maneje en el componente
  }
};

// Función para crear una nueva característica
export const crearCaracteristica = async (nombreCaracteristica, adicional) => {
  try {
    const response = await api.post('caracteristicas/feature-create', {
      nombre_caracteristicas: nombreCaracteristica,
      adicional: adicional,
    }, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response.data; // Retorna los datos de la respuesta
  } catch (error) {
    console.error('Error al crear la característica:', error);
    throw error;
  }
};

// Función para crear una relación entre habitación y característica
export const crearRelacionHabitacionCaracteristica = async (idHabitacion, idCaracteristica) => {
  try {
    const response = await api.post('habitacion-carac/create', {
      id_habitacion: idHabitacion,
      id_caracteristica: idCaracteristica,
    }, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response.data; // Retorna los datos de la respuesta
  } catch (error) {
    console.error('Error al crear la relación entre habitación y característica:', error);
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
