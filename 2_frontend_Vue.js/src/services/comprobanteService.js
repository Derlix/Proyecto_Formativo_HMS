import api from './api'; // Asegúrate de que `api.js` esté configurado adecuadamente

export const getAllcomprobantes = async () => {
    try {
      const response = await api.get('/comprobante_deposito/get_all_comprobantes_depositos');
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
export const getListacomprobanteByPage = async (page = 1, pageSize = 10) => {
  try {
    const response = await api.get(`/comprobante_deposito/get_all_comprobantes_depositos_paginated?page=${page}&page_size=${pageSize}`);
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};




