import api from '../api';

// Función para crear una nueva habitación
export const crearHabitacion = async (estado, piso, numero_habitacion, id_categoria_habitacion, id_usuario) => {
  try {
    console.log(estado, piso, numero_habitacion, id_categoria_habitacion, id_usuario);
    const response = await api.post('/habitacion/create_room', {
      estado,
      piso,
      numero_habitacion,
      id_categoria_habitacion,
      id_usuario,
    }, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      }
    });

    return response.data;
  } catch (error) {
    if (error.response) {
      throw error.response;
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
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      }
    });
    return response.data;
  } catch (error) {
    if (error.response?.status === 404) {
      return [];
    } else {
      throw error;
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
    return response;
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

export const verificarNumeroHabitacion = async (numero_habitacion, id_habitacion = null) => {
  try {
    const habitaciones = await obtenerTodasHabitaciones();

    const habitacionExiste = habitaciones.some(h =>
      h.numero_habitacion === numero_habitacion &&
      h.id_habitacion !== id_habitacion
    );

    return habitacionExiste;
  } catch (error) {
    console.error('Error al verificar el número de habitación:', error);
    throw new Error('No se pudo verificar el número de habitación.');
  }
};

export const obtenerHabitacionPorNumero = async (numeroHabitacion) => {
  console.log("Buscando habitación con número:", numeroHabitacion);
  try {
    const response = await api.get(`/habitacion/get_room_by_numero/${encodeURIComponent(numeroHabitacion)}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
    });
    return response.data; // Retorna los datos de la respuesta
  } catch (error) {
    console.error('Error al obtener la habitación por número:', error);
    throw error; // Propaga el error para que se maneje en el componente
  }
};
