    import api from './api';

export const getReportByPage = async (page = 1, pageSize = 10) => {
    try {
        const response = await api.get(`/informesAmaLlaves/reports-by-page/?page=${page}&page_size=${pageSize}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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

export const createReport = async (ama_de_llaves_clave, ama_de_llaves_numero_de_personas, estado_reportado, causa, id_habitacion, id_reserva) => {
    try{
        const response = await api.post(`/informesAmaLlaves/create/report`, {
            ama_de_llaves_clave: ama_de_llaves_clave,
            ama_de_llaves_numero_de_personas: ama_de_llaves_numero_de_personas,
            estado_reportado: estado_reportado,
            causa: causa,
            id_habitacion: id_habitacion,
            id_reserva: id_reserva
        },{
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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
}

export const deleteReport = async (id_informe) => {
    try{
        const response = await api.delete(`/informesAmaLlaves/delete/${id_informe}`, {
            headers: {
              'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
            }
        });
        return response;
    } catch (error){
        if (error.response) {
            throw error;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
}

export const getRoomByNameAndId = async () => {
    try {
      const response = await api.get('/habitacion/get_all_rooms_by_name');
      return response.data;
    } catch (error) {
      if (error.response) {
        throw error.response;
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  }

export const getReservaAndHabitacion = async () => {
    try {
      const response = await api.get('/informesAmaLlaves/get_reserva_by_id');
      return response.data;
    } catch (error) {
      if (error.response) {
        throw error.response;
      } else {
        throw new Error('Error de red o de servidor');
      }
    }
  }