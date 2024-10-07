import api from '../api';

export const creaateUser = async (nombre_completo, email, id_hotel, passhash) => {
  try {
    const response = await api.post('/login/register', {
      nombre_completo,
      email,
      usuario_rol: 'string',
      img_profile: 'string',
      id_hotel,
      passhash,
    });
    return response;
  } catch (error) {
    if (error.response) {
      console.error('Error en la respuesta de la API:', error.response.data);
      throw error.response;
    } else {
      console.error('Error de red o servidor:', error.message);
      throw new Error('Error de red o de servidor');
    }
  }
};
