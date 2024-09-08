<template>
    <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
      <div class="bg-white p-6 rounded-lg shadow-lg w-1/3">
        <h2 class="text-xl font-bold mt-4 mb-1">Eliminar Factura</h2>
        <p class="mb-4">¿Está seguro que desea eliminar la factura con el ID {{ factura.id_facturacion }}?</p>
        <div class="flex justify-end">
          <button type="button" @click="cancelEdit" class="bg-gray-500 text-white px-4 py-2 rounded mr-2">Cancelar</button>
          <button type="button" @click="confirmDelete" class="bg-red-500 text-white px-4 py-2 rounded">Eliminar</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue';
  import axios from 'axios';
  
  const props = defineProps({
    factura: Object,
  });
  
  const emit = defineEmits(['delete', 'close']);
  
  const confirmDelete = async () => {
    try {
      await axios.delete(`/api/facturacion/${props.factura.id_facturacion}`);
      emit('delete');
      emit('close');
    } catch (error) {
      console.error("Error al eliminar la factura:", error);
    }
  };
  
  const cancelEdit = () => {
    emit('close');
  };
  </script>
  
  <style scoped>
  /* Estilos para el modal */
  .fixed {
    position: fixed;
  }
  .bg-opacity-50 {
    background-color: rgba(0, 0, 0, 0.5);
  }
  </style>
  