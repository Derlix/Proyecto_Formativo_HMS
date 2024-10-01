import api from '@/services/api';

export const createHotel = async (nombre, ubicacion, direccion, telefono) => {
  try {
    const payload = {
      nombre,
      ubicacion,
      direccion,
      telefono,
    };

    const response = await api.post('/hoteles/hoteles/create/', payload, {
      headers: {
        'Content-Type': 'application/json',
      },
    });

    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};
    export const getHotels = async () => {
      try {
        const response = await api.get('/hoteles/hoteles/get_all/', {
        }, {
          headers: {
            'Content-Type': 'application/json',
             
          }
        });
        return response;
      } catch (error) {
        if (error.response) {
          throw error; // Lanza el error para que lo maneje el store
        } else {
          throw new Error('Error de red o de servidor'); // Manejar errores de red
        }
      }
    };
    export const getHotelsByPage = async (page = 1, pageSize = 5) => {
      try {
        const response = await api.get(`/hoteles/hoteles-by-page/?page=${page}&page_size=${pageSize}`);
        return response;
      } catch (error) {
        if (error.response) {
          throw error.response; // Devuelve el error original de la API
        } else {
          throw new Error('Error de red o de servidor');
        }
      }
    };

    export const updateHotel = async (hotel_id,nombre,ubicacion,direccion,telefono) => {
      try {
        const response = await api.put(`/hoteles/hoteles/update/?hotel_id=${hotel_id}`, {
          nombre: nombre,
          ubicacion: ubicacion,
          direccion: direccion,
          telefono: telefono
        });
        return response;
      } catch (error) {
        if (error.response) {
          throw error.response; // Devuelve el error original de la API
        } else {
          throw new Error('Error de red o de servidor'); // Manejar errores de red
        }
      }
    };
    
    
    // Función para eliminar un usuario

    export const deleteHotel = async (id_hotel) => {
      try {
        const response = await api.delete(`/hoteles/hoteles/delete/${id_hotel}`);
        return response;
      } catch (error) {
        if (error.response) {
          throw error.response; // Devuelve el error original de la API
        } else {
          throw new Error('Error de red o de servidor'); // Manejar errores de red
        }
      }
    };

    export const getHotelById = async (id_hotel) => {
      try {
        const response = await api.get(`/hoteles/hoteles/get_hotel_by_id/?id_hotel=${id_hotel}`);
        return response;
      } catch (error) {
        if (error.response) {
          throw error.response; // Devuelve el error original de la API
        } else {
          throw new Error('Error de red o de servidor'); // Manejar errores de red
        }
      }
    };
    
    