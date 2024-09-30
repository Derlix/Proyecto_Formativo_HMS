import api from './api'; 

export const crearReserva = async (fecha_reserva, empresa, valor_deposito, forma_pago, estado_reserva, id_huesped) => {
  try {
    const response = await api.post('/reservas/Insert_Reserva', {
      fecha_reserva: fecha_reserva,
      empresa: empresa,
      valor_deposito: valor_deposito,
      forma_pago: forma_pago,
      estado_reserva: estado_reserva,
      id_huesped: id_huesped,
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


export const obtenertodasReservas = async () => {
    try {
      const response = await api.get('/reservas/get_all');
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  };


  export const obtenerReservasPorPagina = async (page = 1, pageSize = 10) => {
    try {
      const response = await api.get(`/reservas/reservas/paginadas?page=${page}&page_size=${pageSize}`);
      return response;
    } catch (error) {
      if (error.response) {
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  };
  




  export const actualizarReservas = async (id_reserva, fecha_reserva, empresa, valor_deposito, forma_pago, estado_reserva, id_huesped) => {
    try {
      const response = await api.put(`/reservas/Actualizar_Reserva/${id_reserva}`, {
        fecha_reserva: fecha_reserva,
        empresa: empresa,
        valor_deposito: valor_deposito,
        forma_pago: forma_pago,
        estado_reserva: estado_reserva,
        id_huesped: id_huesped,
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
  

  export const deleteReserva = async (id_reserva) => {
    try {
      const response = await api.delete(`reservas/delete${id_reserva}`, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
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
  


// huespedService.js

export const obtenerReservasPorHuesped = async (numero_documento) => {
  try {
    const response = await api.get(`/reservas/reservas/huesped/${numero_documento}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token si es necesario
      }
    });
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
}

