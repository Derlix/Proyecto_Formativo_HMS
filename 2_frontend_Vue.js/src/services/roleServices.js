import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

export const getAllRoles = async () => {
  try {
    const response = await api.get('/role/get-all/');
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};