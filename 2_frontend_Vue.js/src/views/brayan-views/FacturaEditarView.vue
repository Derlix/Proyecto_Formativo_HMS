<template>
  <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
    <div class="bg-blue-200 p-6 rounded-lg shadow-lg w-1/3">
      <h2 class="text-xl font-bold text-gray-800 mt-4 mb-1">Editar Factura</h2>
      <form @submit.prevent="updateFactura">
        <div class="mb-4">
          <label class="block text-gray-700">Subtotal</label>
          <input v-model="factura.subtotal" type="number" class="w-full border border-gray-300 rounded px-3 py-2" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Impuestos</label>
          <input v-model="factura.impuestos" type="number" class="w-full border border-gray-300 rounded px-3 py-2" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Total</label>
          <input v-model="factura.total" type="number" class="w-full border border-gray-300 rounded px-3 py-2" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Total Precio Productos</label>
          <input v-model="factura.total_precio_productos" type="number" class="w-full border border-gray-300 rounded px-3 py-2" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Método de Pago</label>
          <input v-model="factura.metodo_pago" type="text" class="w-full border border-gray-300 rounded px-3 py-2" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Estado</label>
          <input v-model="factura.estado" type="text" class="w-full border border-gray-300 rounded px-3 py-2" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Fecha Salida</label>
          <input v-model="factura.fecha_salida" type="date" class="w-full border border-gray-300 rounded px-3 py-2" />
        </div>
        <div class="flex justify-end">
          <button type="button" @click="cancelEdit" class="bg-gray-500 text-white px-4 py-2 rounded mr-2 hover:bg-gray-600 transition">
            Cancelar
          </button>
          <button type="submit" class="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
            Editar
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue';
import axios from 'axios';

import { getAllFacturas, updateFacturaService  } from "@/services/brayan_service/FacturacionService";


const props = defineProps({
  factura: Object,
});

const emit = defineEmits(['update', 'close']);

const updateFactura = async () => {
  try {
    await updateFacturaService(
      props.factura.id_facturacion,
      props.factura.subtotal,
      props.factura.impuestos,
      props.factura.total,
      props.factura.total_precio_productos,
      props.factura.metodo_pago,
      props.factura.estado,
      props.factura.fecha_salida
    ); 
    alert('Factura editada exitosamente');
    emit('update'); 
    emit('close'); 
  } catch (error) {
    alert('Error al actualizar la factura: ' + (error.response?.data?.message || error.message));
  }
};


const cancelEdit = () => {
  emit('close');
};
</script>




<style scoped>
/* Estilos para el modal */
.fixed {
  position: absolute;
}
.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

input{
  
  color: #333333; /* Texto negro */
}

/* Fondo azul y estilo de los botones */
button {
  transition: background-color 0.3s;
}
</style>
