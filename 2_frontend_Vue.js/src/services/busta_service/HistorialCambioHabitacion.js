import api from '@/services/api';

export const getHistorialCambioHabitacionesByPage = async (page, pageSize = 10) => {
    try {
        const response = await api.get(`/historial-cambio-habitaciones/historial-cambios-habitaciones/paginadas?page=${page}&page_size=${pageSize}`);
        return response;
    } catch (error) {
        console.error('Error al obtener el historial de cambio de habitaciones paginadas:', error);
        throw error.response.data.detail;
    }
};
