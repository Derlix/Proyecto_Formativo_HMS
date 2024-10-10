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

const obtenerCategoriaPorNombre = async (nombreCategoria) => {
  try {
    const response = await fetch(`https://api-hotel-suqt.onrender.com/categoria-habitacion/get_room_categorie_name/?p_category_name=${encodeURIComponent(nombreCategoria)}`);
    const data = await response.json();

    if (data && data.length > 0) {
      return data[0].id_categoria_habitacion; // Ajusta esto según la estructura de tu respuesta
    } else {
      throw new Error('Categoría no encontrada');
    }
  } catch (error) {
    console.error('Error al obtener la categoría:', error);
  }
};
