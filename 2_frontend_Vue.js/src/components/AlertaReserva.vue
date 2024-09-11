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
        ¿Qué tipo de huesped deseas cargar?
      </p>
      <p class="text-sm text-center text-gray-600 mb-8">
        Carga un nuevo huesped o busca entre tus contactos a uno recurrente
      </p>

      <!-- Botones de opciones -->
      <div class="flex justify-center space-x-4">
        <button
          @click="seleccionarNuevoHuesped"
          class="bg-blue-800 text-white py-2 px-6 rounded-md hover:bg-blue-900 transition"
        >
          huesped nuevo
        </button>
        <button
          @click="abrirHuespedExistente"
          class="bg-gray-300 text-gray-700 py-2 px-6 rounded-md hover:bg-gray-400 transition"
        >
          huesped existente
        </button>
      </div>
    </div>
    <!-- Mostrar modal de huesped existente -->
    <ModalHuespedExistente :visible="mostrarHuespedExistente" @close="mostrarHuespedExistente = false" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ModalHuespedExistente from '@/components/ModalHuespedExistente.vue'

const props = defineProps({
  mostrarModal: Boolean
})

const emit = defineEmits(['cerrar'])

const mostrarHuespedExistente = ref(false)

function cerrarModal() {
  emit('cerrar')
}

function seleccionarNuevoHuesped() {
  console.log('Seleccionar huesped nuevo')
}

function abrirHuespedExistente() {
  mostrarHuespedExistente.value = true

}
</script>
