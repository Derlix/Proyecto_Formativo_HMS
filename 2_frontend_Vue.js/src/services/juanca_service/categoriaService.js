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


// Función para crear una nueva categoría de habitación
export const crearCategoria = async (precio_fijo, tipo_habitacion, id_hotel) => {
  try {
    const response = await api.post('categoria-habitacion/create', {
      precio_fijo,       // Precio fijo de la categoría
      tipo_habitacion,   // Tipo de habitación
      id_hotel           // ID del hotel
    }, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
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


// Función para actualizar una categoría
export const actualizarCategoria = async (id_categoria_habitacion, tipo_habitacion, precio_fijo, id_hotel) => {
  try {
    // Usar el ID directamente en la URL y eliminar params
    const response = await api.put(`categoria-habitacion/update_categoria_habitacion/`, {
      precio_fijo,
      tipo_habitacion,
      id_hotel
    }, {
      params: {
        id_categoria_habitacion // Enviar el ID de la categoría como parámetro de consulta
      },
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
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



// Función para eliminar una categoría
export const eliminarCategoria = async (id_categoria_habitacion) => {
  try {
    const response = await api.delete(`/categorias/${id_categoria_habitacion}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
      }
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

// Función para obtener categorías paginadas
export const obtenerCategoriasPaginadas = async (pagina = 1, pageSize = 10) => {
  try {
    const response = await api.get(`/categoria-habitacion/categorie-by-page/`, {
      params: {
        page: pagina,
        page_size: pageSize
      }
    });
    console.log(response)
    return response; // Ajusta según la estructura de tu API
  } catch (error) {
    if (error.response) {
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
