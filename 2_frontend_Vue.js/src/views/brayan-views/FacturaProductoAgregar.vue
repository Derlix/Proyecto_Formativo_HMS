<template>
    <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
      <div class="bg-white p-6 rounded-lg shadow-lg w-1/3">
        <h2 class="text-xl font-bold mt-4 mb-1 ">Agregar Producto a la Factura</h2>
        <form @submit.prevent="updateFactura">
          <div class="mb-4">
            <label class="block text-gray-700">ID facturacion</label>
            <input  type="number" class="w-full border border-gray-300 rounded px-3 py-2" />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700">ID producto</label>
            <input  type="number" class="w-full border border-gray-300 rounded px-3 py-2" />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700">Cantidad</label>
            <input  type="number" class="w-full border border-gray-300 rounded px-3 py-2" />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700">Fecha </label>
            <input  type="date" class="w-full border border-gray-300 rounded px-3 py-2" />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700">Precio U</label>
            <input  type="text" class="w-full border border-gray-300 rounded px-3 py-2" />
          </div>
          
          
          <div class="flex justify-end">
            <button type="button" @click="cancelEdit" class="bg-gray-500 text-white px-4 py-2 rounded mr-2">Cancelar</button>
            <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">Guardar</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps, defineEmits } from 'vue';
  import axios from 'axios';
  
  const props = defineProps({
    factura: Object,
  });
  
  const emit = defineEmits(['update', 'close']);
  
  const updateFactura = async () => {
    try {
      await axios.put(`/api/facturacion/${props.factura.id_facturacion}`, props.factura);
      emit('update');
      emit('close');
    } catch (error) {
      console.error("Error al actualizar la factura:", error);
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
  
  input {
    background-color: #ffffff; /* Fondo blanco para inputs */
    color: #333333; /* Texto negro para inputs */
  }
  
  
  h2 {
    background-color: #ffffff; /* Fondo blanco para inputs */
    color: #333333; /* Texto negro para inputs */
  }
  </style>
  