import api from "../api";

export const getReservaById = async (id_reserva) => {
    try {
        const response = await api.get(`/reservas/reservas/${id_reserva}`, {
            headers: {
                'Content-Type': 'application/json', // Incluido por consistencia
                'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Token desde localStorage
            }
        });
        return response.data; // Retornamos solo los datos de la respuesta

    } catch (error) {
        if (error.response) {
            throw error.response; // Devuelve el error original de la API
        } else {
            throw new Error('Error de red o de servidor'); // Manejar errores de red
        }
    }
};
