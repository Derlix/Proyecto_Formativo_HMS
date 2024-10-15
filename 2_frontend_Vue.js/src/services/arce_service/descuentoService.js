import api from '../api';

// Función para obtener todos los descuentos
export const info_descuentos = async () => {
    try {
        const response = await api.get('/descuento/descuentos/get-all-discounts', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error al obtener descuentos:', error.response?.data || error);
        throw error.response || new Error('Error de red o de servidor');
    }
};

// Función para crear un descuento
export const crear_descuento = async (descuento) => {
    try {
        const response = await api.post('/descuento/descuentos/create-discount', descuento, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                'Content-Type': 'application/json'
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error al crear descuento:', error.response?.data || error);
        throw error.response || new Error('Error de red o de servidor');
    }
};

// Función para actualizar un descuento
export const actualizar_descuento = async (discountId, descuento) => {
    try {
        const response = await api.put(`/descuento/descuentos/update-discount/${discountId}`, descuento, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                'Content-Type': 'application/json'
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error al actualizar descuento:', error.response?.data || error);
        throw error.response || new Error('Error de red o de servidor');
    }
};

// Función para eliminar un descuento
export const eliminar_descuento = async (discountId) => {
    try {
        const response = await api.delete(`/descuento/descuentos/delete-discount/${discountId}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error al eliminar descuento:', error.response?.data || error);
        throw error.response || new Error('Error de red o de servidor');
    }
};

// Función para autorizar un descuento
export const autorizar_descuento = async (discountId, quien_autorizo) => {
    try {
        const response = await api.post(`/descuento/descuentos/authorize-discount/${discountId}`, {
            quien_autorizo,
            autorizado: 1
        }, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                'Content-Type': 'application/json'
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error al autorizar descuento:', error.response?.data || error);
        throw error.response || new Error('Error de red o de servidor');
    }
};
