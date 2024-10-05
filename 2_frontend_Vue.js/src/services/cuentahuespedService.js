import api from './api'; 



export const obtenerTodasCuentasHuesped = async () => {
    try {
      const response = await api.get('/cuenta-huesped/get-all-cuentas-huespedes/');
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  };


  