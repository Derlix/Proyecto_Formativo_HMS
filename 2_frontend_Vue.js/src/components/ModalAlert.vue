<template>
  <div
    v-if="visible"
    class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50 transition-opacity duration-300"
  >
    <div class="bg-white p-8 rounded-lg shadow-xl max-w-lg w-full transform scale-100 hover:scale-105 transition-transform duration-200">
      <p class="text-gray-800 text-lg text-center mb-6 leading-relaxed">{{ descripcion }}</p>
      <div class="flex justify-center space-x-4">
        <button
          class="bg-blue-500 hover:bg-blue-600 text-white font-semibold px-6 py-3 rounded-lg shadow-md transition-colors duration-200 ease-in-out focus:outline-none focus:ring-4 focus:ring-blue-300"
          @click="confirmar"
        >
          {{ textBoton }}
        </button>
        <button
          class="bg-gray-500 hover:bg-gray-600 text-white font-semibold px-6 py-3 rounded-lg shadow-md transition-colors duration-200 ease-in-out focus:outline-none focus:ring-4 focus:ring-gray-300"
          @click="close"
        >
          Cancelar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  descripcion: {
    type: String,
    default: ''
  },
  textBoton: {
    type: String,
    default: ''
  },
  visible: {
    type: Boolean,
    required: true
  }
});

const emit = defineEmits(['close', 'confirm']);

const close = () => {
  emit('close');
};

const confirmar = () => {
  emit('confirm');
};
</script>
