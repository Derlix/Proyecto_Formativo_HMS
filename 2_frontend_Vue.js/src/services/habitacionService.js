import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

// Función para crear un nuevo usuario
export const crearHabitacion = async (estado, piso, precio_actual, id_usuario, numero_habitacion, id_categoria_habitacion) => {
  try {
    const response = await api.post('/habitacion/create', {
      estado: estado,
      piso: piso,
      precio_actual: precio_actual,
      id_usuario: id_usuario,
      numero_habitacion: numero_habitacion,
      id_categoria_habitacion: id_categoria_habitacion,
      ocupacion: ocupacion,
      direccion: direccion,
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

export const obtenerTodasHabitaciones = async () => {
  try {
    const response = await api.get('/habitacion/get_all');
    return response; 
  } catch (error) {
    console.error('Error al obtener habitaciones:', error);
    throw error; // Re-lanza el error para manejarlo en el componente
  }
};

// export const obtenerTodasHabitacion = async (estado, piso, precio_actual, id_usuario, numero_habitacion, id_categoria_habitacion, id_habitacion) => {
//     try {
//       const response = await api.get('/habitacion/get_all', {
//         estado: estado,
//         piso: piso,
//         precio_actual: precio_actual,
//         id_usuario: id_usuario,
//         numero_habitacion: numero_habitacion,
//         id_categoria_habitacion: id_categoria_habitacion,
//         ocupacion: ocupacion,
//         direccion: direccion,
//         id_habitacion: id_habitacion,
//       });
//       return response;
//     } catch (error) {
//       if (error.response) {
//         throw error.response; // Devuelve el error original de la API
//       } else {
//         throw new Error('Error de red o de servidor');
//       }
//     }
//   };

// Función para obtener un usuario por su email
export const ObtenerHabitacionId = async (id_habitacion) => {
  try {
    const response = await api.get(`/habitacion/${encodeURIComponent(id_habitacion)}`);
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};







// Función para actualizar un usuario
export const actualizarHabitacion = async (estado, piso, precio_actual, id_usuario, numero_habitacion, id_categoria_habitacion) => {
  try {
    const response = await api.put(`/huespedes/update-huesped/?id_huesped=${HuespedId}`, {
        estado: estado,
        piso: piso,
        precio_actual: precio_actual,
        id_usuario: id_usuario,
        numero_habitacion: numero_habitacion,
        id_categoria_habitacion: id_categoria_habitacion,
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

// Función para eliminar un usuario
export const eliminarHabitacion = async (id_habitacion) => {
  try {
    const response = await api.delete(`/huespedes/delete-huesped/${id_habitacion}`);
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};
