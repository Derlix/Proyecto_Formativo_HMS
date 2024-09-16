import api from '../api';

// Función para crear una nueva habitación
export const crearHabitacion = async (estado, piso, precio_actual, id_usuario, numero_habitacion, id_categoria_habitacion) => {
  try {
    const response = await api.post('/habitacion/', {
      estado,
      piso,
      precio_actual,
      id_usuario,
      numero_habitacion,
      id_categoria_habitacion,
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
    const response = await api.get('/habitacion/', {
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
    const response = await api.get(`/habitacion/${id_habitacion}`, {
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

// Función para actualizar una habitación existente (PUT)
export const actualizarHabitacion = async (id_habitacion, estado, piso, precio_actual, id_usuario, numero_habitacion, id_categoria_habitacion) => {
  try {
    const response = await api.put(`/habitacion/${id_habitacion}`, {
      estado,
      piso,
      precio_actual,
      id_usuario,
      numero_habitacion,
      id_categoria_habitacion,
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
    const response = await api.delete(`/habitacion/${id_habitacion}`, {
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
