import axios from 'axios';

// Obtener datos de IP con ip-api.com
export const getIpLocation = async () => {
    try {
        // Realizar petición GET a la API de ip-api.com
        const response = await axios.get('http://ip-api.com/json', {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
        });
        // Retornar datos de la respuesta
        return response.data;
    } catch (error) {
        // Manejar error de la petición
        if (error.response) {
            throw error;
        } else {
            throw new Error('Network or server error');
        }
    }
};
