import api from '../api';

// Función para crear una nueva habitación
export const crearHabitacion = async (estado, piso, numero_habitacion, id_categoria_habitacion) => {
  try {
    const response = await api.post('/habitacion/create_room', {
      estado,
      piso,
      numero_habitacion,
      id_categoria_habitacion,
      id_usuario: "string",
    }, {
      headers: {
        'Content-Type': 'application/json',
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

// Función para obtener todas las habitaciones
export const obtenerTodasHabitaciones = async () => {
  try {
    const response = await api.get('/habitacion/get_all_rooms', {
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

// Función para obtener una habitación por su ID
export const obtenerHabitacionPorId = async (id_habitacion) => {
  try {
    const response = await api.get(`/habitacion/get_room_by_id/${id_habitacion}`, {
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

// Función para obtener habitaciones paginadas
export const obtenerHabitacionesPaginadas = async (page = 1, pageSize = 10) => {
  try {
    const response = await api.get(`/habitacion/paginated-habitaciones-detalles/?page=${page}&page_size=${pageSize}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response.data;
  } catch (error) {
    if (error.response) {
      console.error('Error de la API:', error.response.data);
      throw new Error(error.response.data.detail || 'Error al procesar la solicitud');
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};

// Función para actualizar una habitación existente (PUT)
export const actualizarHabitacion = async (id_habitacion, estado, piso, numero_habitacion, id_categoria_habitacion) => {
  try {
    console.log("Datos enviados:", {
      estado,
      piso,
      numero_habitacion,
      id_categoria_habitacion,
      id_usuario: "string"
    });

    const response = await api.put(`/habitacion/update_room_by_id/${id_habitacion}`, {

      estado,
      piso,
      numero_habitacion,
      id_categoria_habitacion,
      id_usuario: "string"
    }, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response;
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

// Función para eliminar una habitación
export const eliminarHabitacion = async (id_habitacion) => {
  try {
    const response = await api.delete(`/habitacion/delete_room_by_id/${id_habitacion}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      }
    });
    return response;
  } catch (error) {
    if (error.response) {
      // Imprime información detallada del error
      console.error('Error status:', error.response.status);
      console.error('Error data:', error.response.data);
      console.error('Error headers:', error.response.headers);
      throw error; // Lanza el error para que lo maneje el store
    } else {
      console.error('Error de red o de servidor:', error.message);
      throw new Error('Error de red o de servidor');
    }
  }
};
