import api from '@/services/api';
import axios from 'axios';


// Obtener todas las facturas
export const getAllFacturas = async () => {
    try {
      const response = await api.get('/facturacion/get_all_facturas', {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('access_token')}`, // Incluye el token de autenticación
        },
      });
      return response.data; // Devuelve los datos de la respuesta
    } catch (error) {
      if (error.response) {
        throw error; // Lanza el error para que lo maneje el componente que lo llame
      } else {
        throw new Error('Error de red o de servidor'); // Manejar errores de red
      }
    }
  };



  
  export const updateFacturaService = async (id_facturacion, subtotal, impuestos, total, total_precio_productos, metodo_pago, estado, fecha_salida) => {
    try {
      const response = await api.put(`/facturacion/update_factura/${id_facturacion}`, {
        subtotal,
        impuestos,
        total,
        total_precio_productos,
        metodo_pago,
        estado,
        fecha_salida
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


  
export const deleteFactura = async (id_facturacion) => {
  try {
      const response = await api.delete(`/facturacion/delete_factura/${id_facturacion}`, {
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
  
export const getFacturaByPage = async (page = 1, page_size = 10) => {
  try {
    const response = await api.get(`/facturacion/get_all_facturas_paginated?page=${page}&page_size=${page_size}`);
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};



export const getFacturaByid = async (id_facturacion) => {
  try {
    const response = await api.get(`/facturacion/get_factura_by_id/?id_facturacion=${encodeURIComponent(id_facturacion)}`);
    return response;
  } catch (error) {
    if (error.response) {
      throw error.response; // Devuelve el error original de la API
    } else {
      throw new Error('Error de red o de servidor'); // Manejar errores de red
    }
  }
};
