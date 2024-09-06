<!-- EditarProductoModal.vue -->
<template>
    <div class="modal-overlay">
      <div class="modal-content">
        <h1 class="text-black font-bold mb-8">Editar Producto</h1>
        <form @submit.prevent="submitEdits">
          <div class="mb-4">
            <label for="cantidad" class="block text-sm font-medium text-gray-700">Cantidad</label>
            <input
              type="number"
              id="cantidad"
              v-model="formData.cantidad"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm"
              required
            />
          </div>
          <div class="mb-4">
            <label for="precio_unitario" class="block text-sm font-medium text-gray-700">Precio Unitario</label>
            <input
              type="number"
              id="precio_unitario"
              v-model="formData.precio_unitario"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm"
              required
            />
          </div>
          <div class="mb-4">
            <label for="fecha" class="block text-sm font-medium text-gray-700">Fecha</label>
            <input
              type="date"
              id="fecha"
              v-model="formData.fecha"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm"
              required
            />
          </div>
          <div class="flex justify-end space-x-4">
            <button @click="closeModal" type="button" class="bg-red-600 text-white p-2 rounded">Cancelar</button>
            <button type="submit" class="bg-blue-600 text-white p-2 rounded">Guardar</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps, defineEmits } from 'vue';
  
  const props = defineProps({
    producto: Object
  });
  
  const emit = defineEmits(['close', 'save']);
  
  const formData = ref({
    cantidad: props.producto.cantidad,
    precio_unitario: props.producto.precio_unitario,
    fecha: props.producto.fecha || new Date().toISOString().substr(0, 10) // Usa la fecha actual si no hay
  });
  
  const closeModal = () => {
    emit('close');
  };
  
  const submitEdits = () => {
    emit('save', formData.value);
    closeModal();
  };
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    width: 90%;
    max-width: 600px;
  }
  </style>
  