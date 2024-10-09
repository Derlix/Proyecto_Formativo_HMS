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
