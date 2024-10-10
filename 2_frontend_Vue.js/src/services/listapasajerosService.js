import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

export const getAllPasajeros = async () => {
    try {
      const response = await api.get('/movimiento_pasajeros/get_all_movimientos_pasajeros');
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  };

// Función para obtener todos los usuarios con paginación
export const getListaPasajerosBypage = async (page = 1, pageSize = 10) => {
  try {
    const response = await api.get(`/movimiento_pasajeros/get_all_movimientos_pasajeros_paginated?page=${page}&page_size=${pageSize}`);
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};




