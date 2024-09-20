import api from '@/services/api';

export const getProductosFacturaById = async (id_facturacion) => {
  try {
    const token = localStorage.getItem('token'); // O sessionStorage.getItem('token')
    
    const response = await api.get(`https://api-hotel-suqt.onrender.com/factura-producto/get_productos_factura_by_id/`, {
      params: { id_facturacion },
      headers: {
        'Authorization': `Bearer ${token}` // Ajusta esto según el esquema de tu API
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error al obtener productos de la factura:', error);
    throw error;
  }
};


export const addProductoToFactura = async (id_facturacion, id_producto, cantidad,fecha,  precio_unitario) => {
    try {
      const response = await api.post('/factura-producto/create_factura_producto', {
        id_facturacion: id_facturacion,
        id_producto: id_producto,
        cantidad: cantidad,
        fecha: fecha,
        precio_unitario: precio_unitario
       
      });
      return response.data;
    } catch (error) {
      console.error('Error al agregar el producto a la factura:', error);
      throw error;
    }
  };

  export const deleteProductoFactura = async (id_factura_producto) => {
    try {
      const response = await api.delete(`/factura-producto/delete_producto_factura/${id_factura_producto}`, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        }
      });
      return response;
    } catch (error) {
      if (error.response) {
        console.error('Error en la respuesta:', error.response.data);
        throw error;
      } else {
        console.error('Error de red o servidor:', error.message);
        throw new Error('Error de red o de servidor');
      }
    }
  };
  



  export const updateProductoFactura = async (id_factura_producto, cantidad, fecha, precio_unitario) => {
    try {
      const response = await api.put(`/factura-producto/update_productos_factura/${id_factura_producto}`, {
        cantidad,
        fecha,
        precio_unitario
        
      }, {
        headers: {
          'Content-Type': 'application/json',
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





  

  //ESTO ES SOLO PARA OBTENER LOS PRODUCTOS Y COLOCAR EL NOMBR EEN EL INPUT DE AGRREGAR PRODUCTO A LA FACVTURA
export const getAllProductosPrueba = async () => {
  try {
    const response = await api.get('/producto/get-all/');
    return response.data; // Asume que la lista de productos está en response.data
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};
  