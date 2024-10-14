import api from '../api';

export const obtener_anticipos = async () => {
    try {
        const response = await api.get('/avances/advances/get-all-advances', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });
        console.log(response.data);
        return response.data;
    } catch (error) {
        if (error.response) {
            throw error.response;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};


export const actualizar_anticipo = async (advance_id, data) => {
    try {
        const response = await api.put(`/avances/advances/update-advance/${advance_id}`, data, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });
        return response.data;
    } catch (error) {
        if (error.response) {
            throw error.response;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};

export const eliminar_anticipo = async (advance_id) => {
    try {
        const response = await api.delete(`/avances/advances/delete-advance/${advance_id}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });
        return response.data;
    } catch (error) {
        if (error.response) {
            throw error.response;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};

export const crear_anticipo = async (data) => {
    try {
        const response = await api.post('/avances/advances/create-advance', data, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });
        return response.data;
    } catch (error) {
        if (error.response) {
            throw error.response;
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};


