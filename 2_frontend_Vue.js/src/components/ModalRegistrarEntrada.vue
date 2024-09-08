<template>
    <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 text-black">
      <div class="bg-blue-100 p-16 rounded-lg shadow-lg max-w-2xl w-full relative">
        <!-- Botón de cerrar (ícono de cerrar en la esquina superior derecha) -->
        <button @click="close" class="absolute top-4 right-4 text-black hover:text-red-500">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
  
        <h2 class="text-2xl mb-6">Movimiento de pasajeros - ENTRADA</h2>
  
        <div class="grid grid-cols-2 gap-4 mb-5">
          <div>
            <label for="document" class="block mb-1">Documento</label>
            <input type="text" id="document" class="w-full rounded-lg p-2">
          </div>
          <div>
            <label for="nombre" class="block mb-1">Nombre Completo</label>
            <input type="text" id="nombre" class="w-full rounded-lg p-2">
          </div>
          <div>
            <label for="habitacion" class="block mb-1">Habitación</label>
            <input type="text" id="habitacion" class="w-full rounded-lg p-2">
          </div>
          <div>
            <label for="procedencia" class="block mb-1">Procedencia</label>
            <input type="text" id="procedencia" class="w-full rounded-lg p-2">
          </div>
        </div>
  
        <div class="mb-4">
          <label for="observaciones" class="block mb-1">Observaciones:</label>
          <textarea id="observaciones" rows="4" class="w-full rounded-lg p-2"></textarea>
        </div>
  
        <div class="mb-4">
          <label for="elaborado" class="block mb-1">Elaborado por:</label>
          <input type="text" id="elaborado" class="w-full rounded-lg p-2">
        </div>
  
        <button @click="close" class="bg-green-600 text-white px-6 py-3 rounded w-full hover:bg-green-700">
          Confirmar
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    visible: {
      type: Boolean,
      required: true
    }
  })
  
  const emit = defineEmits(['close'])
  
  const close = () => {
    emit('close')
  }
  </script>
  