// categoriaService.js
import api from '../api';

// Función para obtener todas las categorías de habitación
export const obtenerCategoriasHabitacion = async () => {
  try {
    const response = await api.post('categoria-habitacion/get-all_room_categories/');
    return response.data; // Retorna los datos de la respuesta
  } catch (error) {
    console.error('Error al obtener las categorías de habitación:', error);
    throw error;
  }
};
