<template>
  <div
    v-if="mostrarModal"
    class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
  >
    <div
      class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-2xl w-full relative transition-all"
    >
      <button
        @click="cerrarModal"
        class="absolute top-4 right-4 text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300 z-10"
      >
        &times;
      </button>

      <p class="text-gray-900 dark:text-white text-3xl mb-4 text-center p-4">
        ¿Qué tipo de huésped deseas cargar?
      </p>
      <p class="text-gray-600 dark:text-gray-400 text-center mb-6">
        Carga un nuevo huésped o busca entre tus contactos a uno recurrente
      </p>

      <div class="flex justify-center">
        <button
          @click="abrirModalCrearHuesped"
          class="bg-blue-500 dark:bg-blue-600 text-white px-4 py-2 rounded text-center mt-8 hover:bg-blue-600 dark:hover:bg-blue-700 transition"
        >
          Huésped Nuevo
        </button>
        <button
          @click="abrirHuespedExistente"
          class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-200 px-4 py-2 rounded text-center mt-8 ml-4 hover:bg-gray-400 dark:hover:bg-gray-500 transition"
        >
          Huésped Existente
        </button>
      </div>
    </div>

    <ModalCrearHuesped
      :visible="mostrarModalCrearHuesped"
      @close="cerrarModalCrearHuesped"
    />
    <ModalSeleccionHuesped
      :visible="mostrarHuespedExistente"
      @close="mostrarHuespedExistente = false"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ModalCrearHuesped from './ModalCrearHuesped.vue'
import ModalSeleccionHuesped from './ModalSeleccionHuesped.vue'

const props = defineProps({
  mostrarModal: Boolean
})

const emit = defineEmits(['cerrar'])

const mostrarHuespedExistente = ref(false)
const mostrarModalCrearHuesped = ref(false)

function cerrarModal() {
  emit('cerrar')
}

function abrirModalCrearHuesped() {
  mostrarModalCrearHuesped.value = true
  console.log('Modal de creación de huésped abierto:', mostrarModalCrearHuesped.value)
}

function cerrarModalCrearHuesped() {
  mostrarModalCrearHuesped.value = false
}

function abrirHuespedExistente() {
  mostrarHuespedExistente.value = true
}


</script>
