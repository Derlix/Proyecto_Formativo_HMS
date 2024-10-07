import api from "./api";

export const createProduct = async (nombre, descripcion, precio) => {
    try {
        const response = await api.post(`/producto/create`, {
            nombre_producto: nombre,
            descripcion: descripcion,
            precio_actual: precio
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

export const updateProduct = async (productoId, nombre, descripcion, precio) => {
    try {
        const response = await api.put(`/producto/update/?product_id=${productoId}`, {
            nombre_producto: nombre,
            descripcion: descripcion,
            precio_actual: precio
        }, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
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

export const deleteProduct = async (idProducto) => {
    try {
        const response = await api.delete(`/producto/delete/${idProducto}`, {
            headers: {
              'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Incluye el token de autenticación
            }
        });
        return response;
    } catch (error) {
        if (error.response) {
            throw error; // Lanza el error para que lo maneje el store
        } else {
            throw new Error('Error de red o de servidor'); // Manejar errores de red
        }
    }
}

export const getProductsByPage = async(page = 1, pageSize = 10) => {
    try {
        const response = await api.get(`/producto/products-by-page/?page=${page}&page_size=${pageSize}`, {
            headers: {
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