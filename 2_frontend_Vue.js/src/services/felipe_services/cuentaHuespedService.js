import api from '@/services/api';
export const createCuentaHuesped = async (cuentaHuespedData) => {
  try {
    const response = await api.post('/create_cuenta_huesped', cuentaHuespedData);
    return response.data;
  } catch (error) {
    console.error('Error al crear la cuenta de huésped:', error);
    throw error.response.data.detail;
  }
};

export const getCuentaHuespedByIdCuenta = async (idCuenta) => {
      try {
        const response = await api.get(`/get-cuenta-huesped-by-id_cuenta`, {
          params: { id_cuenta: idCuenta }
        });
        return response.data;
      } catch (error) {
        console.error('Error al obtener la cuenta de huésped:', error);
        throw error.response.data.detail;
      }
    };
    
    export const getCuentaHuespedByIdReserva = async (idReserva) => {
      try {
        const response = await api.get(`/cuenta-huesped/get-cuenta-huesped-by-id_reserva/?id_reserva=${idReserva}`);
        return response;
      } catch (error) {
        console.error('Error al obtener la cuenta de huésped por ID de reserva:', error);
        throw error.response.data.detail;
      }
    };
    
    export const getCuentaHuespedByIdHuesped = async (idHuesped) => {
      try {
        const response = await api.get(`/cuenta-huesped/get-cuenta-huesped-by-id_huesped/?id_huesped=${idHuesped}`);
        return response;
      } catch (error) {
        console.error('Error al obtener la cuenta de huésped por ID de huésped:', error);
        throw error.response.data.detail;
      }
    };
    
    export const getAllCuentasHuespedes = async () => {
      try {
        const response = await api.get(`/get-all-cuentas-huespedes`);
        return response.data;
      } catch (error) {
        console.error('Error al obtener todas las cuentas de huéspedes:', error);
        throw error.response.data.detail;
      }
    };
    
    export const updateCuentaHuesped = async (idCuenta, cuentaHuespedData) => {
      try {
        const response = await api.put('/update-cuenta_huesped', { id_cuenta: idCuenta, ...cuentaHuespedData });
        return response.data;
      } catch (error) {
        console.error('Error al actualizar la cuenta de huésped:', error);
        throw error.response.data.detail;
      }
    };

    export const getCuentasHuespedesByPage = async (page = 1, pageSize = 10) => {
      try {
        const response = await api.get('/cuenta_huespedes-by-page', {
          params: { page, page_size: pageSize }
        });
        return response;
      } catch (error) {
        console.error('Error al obtener las cuentas de huéspedes paginadas:', error);
        throw error.response.data.detail;
      }
    };
    
    export const deleteCuentaHuesped = async (idCuenta) => {
      try {
        const response = await api.delete(`/delete-cuenta_huesped/${idCuenta}`);
        return response.data;
      } catch (error) {
        console.error('Error al eliminar la cuenta de huésped:', error);
        throw error.response.data.detail;
      }
    };
    