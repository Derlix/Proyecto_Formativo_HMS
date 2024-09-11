<template>
  <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
    <div class="bg-blue-200 p-6 rounded-lg shadow-lg w-1/3">
      <h2 class="text-xl font-bold text-gray-800 mt-4 mb-1">Agregar Producto a la Factura</h2>
      <form @submit.prevent="updateFactura">
        <div class="mb-4">
          <label class="block text-gray-700">ID facturacion</label>
          <input type="number" class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">ID producto</label>
          <input type="number" class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Cantidad</label>
          <input type="number" class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Fecha</label>
          <input type="date" class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Precio U</label>
          <input type="text" class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" />
        </div>
        <div class="flex justify-end">
          <button type="button" @click="cancelEdit" class="bg-gray-500 text-white px-4 py-2 rounded mr-2 hover:bg-gray-600 transition">Cancelar</button>
          <button type="submit" class="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-700 transition">Guardar</button>
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

.fixed {
  position: absolute;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

input {

  color: #333333;
}

button {
  transition: background-color 0.3s;
}



h2 {
  color: #2d3748; 
}
</style>
