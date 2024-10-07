import api from "@/api";

export const getReservaByHuespedDocument = async (numero_documento) => {
    try {
        const response = await api.get(`/reservas/reservas/huesped/${encodeURIComponent(numero_documento)}`, {
            headers: {
                'Content-Type': 'application/json', // Incluido por consistencia
                'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Cambiado para usar el token desde localStorage
            }
        });
        return response; // Retornamos la respuesta completa
    } catch (error) {
        if (error.response) {
            throw error.response; // Devuelve el error original de la API
        } else {
            throw new Error('Error de red o de servidor'); // Manejar errores de red
        }
    }
};
