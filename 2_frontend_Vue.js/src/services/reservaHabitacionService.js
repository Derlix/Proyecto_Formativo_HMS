import api from './api'; 

export const crearReservaHabitacion = async (id_reserva, id_habitacion, num_adultos, num_niños, fecha_entrada, fecha_salida_propuesta) => {
  try {
    const response = await api.post('/Reserva-habitacion/crear-reserva', {
      id_reserva: id_reserva,
      id_habitacion: id_habitacion,
      num_adultos: num_adultos,
      num_niños: num_niños,
      motivo_cambio: "String",
      fecha_entrada: fecha_entrada,
      fecha_salida_propuesta: fecha_salida_propuesta, // Este campo está correcto
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

  export const obtenerReservasHabitacionPorPagina = async (page = 1, pageSize = 10) => {
    try {
      const response = await api.get(`/Reserva-habitacion/reservas-habitacion-por-pagina/${page}&page_size=${pageSize}`);
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  };
  




  export const actualizarReservaHabitacion = async (id_reserva, old_id_habitacion, reserva_habitacion) => {
    try {
      const response = await api.put(`/Reserva-habitacion/update/?id_reserva=${id_reserva}&old_id_habitacion=${old_id_habitacion}`, {
        id_reserva: reserva_habitacion.id_reserva,
        id_habitacion: reserva_habitacion.id_habitacion, // Mantenemos el id_habitacion del objeto
        num_adultos: reserva_habitacion.num_adultos,
        num_niños: reserva_habitacion.num_niños,
        //motivo_cambio: reserva_habitacion.motivo_cambio,
        fecha_entrada: reserva_habitacion.fecha_entrada,
        fecha_salida_propuesta: reserva_habitacion.fecha_salida_propuesta,
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

  export const deleteReservaHabitacion = async (id_reserva) => {
    try {
      const response = await api.delete(`/Reserva-habitacion/delete/${id_reserva}`, {
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
  
  export const obtenertodasReservasHabitacion = async () => {
    try {
      const response = await api.get('/Reserva-habitacion/get_all');
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  };
