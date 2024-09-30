import api from './api'; 

export const crearCheckin = async (id_reserva, medio_llegada, llegada_situacion, equipaje) => {
  try {
    const response = await api.post('/check-in/create_checkin', {
      id_reserva: id_reserva,
      medio_llegada: medio_llegada,
      llegada_situacion: llegada_situacion,
      equipaje: equipaje,
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


export const obtenertodosCheckin = async () => {
    try {
      const response = await api.get('/check-in/get_checkin');
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  };


