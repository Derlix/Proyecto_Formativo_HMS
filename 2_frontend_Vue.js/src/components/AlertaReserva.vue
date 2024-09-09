<template>
  <div
    v-if="mostrarModal"
    class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50"
  >
    <div class="max-w-xl w-full p-8 bg-blue-50 shadow-lg rounded-lg relative">
      <!-- Botón de cierre en la esquina superior derecha -->
      <button @click="cerrarModal" class="absolute top-4 right-4 text-gray-500 hover:text-gray-700">
        &times;
      </button>

      <!-- Texto explicativo -->
      <p class="text-lg font-semibold text-center text-gray-900 mb-2">
        ¿Qué tipo de huésped deseas cargar?
      </p>
      <p class="text-sm text-center text-gray-600 mb-8">
        Carga un nuevo huésped o busca entre tus contactos a uno recurrente
      </p>

      <!-- Botones de opciones -->
      <div class="flex justify-center space-x-4">
        <button
          @click="seleccionarNuevoHuesped"
          class="bg-blue-800 text-white py-2 px-6 rounded-md hover:bg-blue-900 transition"
        >
          Huésped nuevo
        </button>
        <button
          @click="showModal = true"
          class="bg-gray-300 text-gray-700 py-2 px-6 rounded-md hover:bg-gray-400 transition"
        >
          Huésped existente
        </button>

        <ModalRegistrarReserva :visible="showModal" @close="showModal = false" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'
import ModalRegistrarReserva from './ModalRegistrarReserva.vue'



const props = defineProps({
  mostrarModal: Boolean
})

const emit = defineEmits(['cerrar'])

function cerrarModal() {
  emit('cerrar')
}

function seleccionarNuevoHuesped() {
  console.log('Seleccionar huésped nuevo')
}

function seleccionarHuespedExistente() {
  console.log('Seleccionar huésped existente')
}
</script>
