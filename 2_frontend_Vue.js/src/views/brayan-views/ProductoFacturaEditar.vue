<template>
  <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
    <div class="bg-blue-200 p-6 rounded-lg shadow-lg w-1/3">
      <h2 class="text-xl font-bold text-gray-800 mt-4 mb-1">Editar Producto</h2>
      <form @submit.prevent="submitEdits">
        <div class="mb-4">
          <label for="cantidad" class="block text-gray-700">Cantidad</label>
          <input
            type="number"
            id="cantidad"
            v-model="formData.cantidad"
            class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500"
            required
          />
        </div>
        <div class="mb-4">
          <label for="precio_unitario" class="block text-gray-700">Precio Unitario</label>
          <input
            type="number"
            id="precio_unitario"
            v-model="formData.precio_unitario"
            class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500"
            required
          />
        </div>
        <div class="mb-4">
          <label for="fecha" class="block text-gray-700">Fecha</label>
          <input
            type="date"
            id="fecha"
            v-model="formData.fecha"
            class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500"
            required
          />
        </div>
        <div class="flex justify-end">
          <button @click="closeModal" type="button" class="bg-gray-500 text-white px-4 py-2 rounded mr-2 hover:bg-gray-600 transition">
            Cancelar
          </button>
          <button type="submit" class="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
            Guardar
          </button>
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

.fixed {
  position: absolute;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

input {
  color: #333333; /* Texto negro */
}

button {
  transition: background-color 0.3s;
}


h2 {
  color: #2d3748; /* Gris oscuro */
}
</style>
