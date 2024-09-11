import api from './api';


const createHotel = async (nombre,ubicacion,direccion,telefono) => {
      try {
        // Realizar una solicitud POST a la API para crear un nuevo hotel
       
        const response = await api.post('/hoteles/hoteles/create/', {
            nombre: nombre,
            ubicacion: ubicacion,
            direccion: direccion,
            telefono: telefono
          }
        
        );
        
        // Manejo de la respuesta (puedes ajustar según tus necesidades)
        console.log('Hotel creado con éxito:', response.data);
    
        // Retorna los datos del hotel creado o cualquier respuesta necesaria
        return response;
      } catch (error) {
        // Manejo de errores
        console.error('Error al crear el hotel:', error.response ? error.response.data : error.message);
        throw error; // Lanza el error para que el llamador lo maneje
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

    export const updateUser = async (nombre,ubicacion,direccion,telefono) => {
      try {
        const response = await api.put(`/users/update/?user_id=${userId}`, {
          nombre: nombre,
          ubicacion: ubicacion,
          direccion: direccion,
          telefono: telefono
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
    
    // Función para eliminar un usuario
    export const deleteHotel = async (hotelId) => {
      try {
        const response = await api.delete(`/hoteles/hoteles/delete/${hotelId}`, {
          headers: {
         'Content-Type': 'application/json'
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
    