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

export const createReport = async (id_habitacion, estado_reportado) => {
    try{
        const response = await api.post(`/informesAmaLlaves/create/report`, {
            id_habitacion: id_habitacion,
            estado_reportado: estado_reportado
        },{
            headers: {
                'Content-Type': 'application/json',
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

export const updateReport = async (id_informe, id_habitacion, estado_reportado) => {
    try{
        const response = await api.put(`/informesAmaLlaves/update/report/?id_informe=${id_informe}`, {
            id_habitacion: id_habitacion,
            estado_reportado: estado_reportado
        },{
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });
        return response;
    } catch(error) {
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
        throw error.response; // Devuelve el error original de la API
      } else {
        throw new Error('Error de red o de servidor'); // Manejar errores de red
      }
    }
  }