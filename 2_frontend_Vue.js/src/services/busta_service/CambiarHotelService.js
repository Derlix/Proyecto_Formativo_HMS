import api from '../api';

export const updateIdHotel = async (NuevoIdHotel) => {
  try {
    const response = await api.put(`/usuarios/cambiar-hotel/`, {
      id_hotel: NuevoIdHotel,
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
