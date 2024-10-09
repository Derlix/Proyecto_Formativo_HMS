import api from '../api';

// Función para obtener todos los descuentos
export const info_descuentos = async () => {
    try {
        const response = await api.get('/descuento/descuentos/get-all-discounts', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
            }
        });
        console.log(response.data)
        return response.data; // Asegúrate de devolver solo los datos
    } catch (error) {
        if (error.response) {
            throw error.response; // Devuelve el error original de la API
        } else {
            throw new Error('Error de red o de servidor');
        }
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
        return response.data; // Retorna el descuento creado
    } catch (error) {
        console.error('Error al crear descuento:', error); // Agrega un registro de error
        if (error.response) {
            throw error.response; // Devuelve el error original de la API
        } else {
            throw new Error('Error de red o de servidor');
        }
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
        return response.data; // Retorna la respuesta de la actualización
    } catch (error) {
        if (error.response) {
            throw error.response; // Devuelve el error original de la API
        } else {
            throw new Error('Error de red o de servidor');
        }
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
        return response.data; // Retorna la respuesta de la eliminación
    } catch (error) {
        if (error.response) {
            throw error.response; // Devuelve el error original de la API
        } else {
            throw new Error('Error de red o de servidor');
        }
    }
};

