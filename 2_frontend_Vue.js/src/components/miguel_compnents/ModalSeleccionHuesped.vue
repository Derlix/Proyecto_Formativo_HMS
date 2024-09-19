<template>
  <div
    v-if="visible"
    class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50"
  >
    <div class="max-w-3xl w-full p-8 bg-white dark:bg-gray-800 shadow-lg rounded-lg relative transition-all">
      <button @click="cerrarModal" class="absolute top-4 right-4 text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300">
        &times;
      </button>

      <h1 class="text-lg font-bold mb-4 text-center text-gray-900 dark:text-white">Seleccionar Huésped Existente</h1>

      <div class="mb-6">
        <label for="documento" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
          Ingresar Documento:
        </label>
        <input
          v-model="documento"
          type="text"
          id="documento"
          class="block w-full border rounded-md p-2 bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white border-gray-300 dark:border-gray-600"
          placeholder="Ingrese el documento del huésped"
          @input="buscarHuesped"
        />
      </div>

      <div v-if="huesped" class="bg-gray-100 dark:bg-gray-700 p-4 rounded-md border border-gray-300 dark:border-gray-600">
        <p class="text-gray-900 dark:text-gray-100"><strong>Nombre Completo:</strong> {{ huesped.nombre_completo }}</p>
        <p class="text-gray-900 dark:text-gray-100"><strong>Número Documento:</strong> {{ huesped.numero_documento }}</p>
        <p class="text-gray-900 dark:text-gray-100"><strong>Teléfono:</strong> {{ huesped.telefono }}</p>
        <p class="text-gray-900 dark:text-gray-100"><strong>Email:</strong> {{ huesped.email }}</p>
        <p class="text-gray-900 dark:text-gray-100"><strong>Ocupación:</strong> {{ huesped.ocupacion }}</p>
        <p class="text-gray-900 dark:text-gray-100"><strong>Dirección:</strong> {{ huesped.direccion }}</p>
      </div>

      <div class="flex justify-between mt-6">
        <button
          @click="cerrarModal"
          class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-200 font-semibold py-2 px-4 rounded-md hover:bg-gray-400 dark:hover:bg-gray-500 transition"
        >
          Cerrar
        </button>
        <button
          @click="confirmarSeleccion"
          :disabled="!huesped"
          class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition"
          :class="{ 'opacity-50 cursor-not-allowed': !huesped }"
        >
          Confirmar
        </button>
      </div>
    </div>

    <ModalConfirmacion
      :visible="mostrarConfirmacion"
      @close="mostrarConfirmacion = false"
      :huesped="huesped"
    />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { getHuespedByDocument } from '@/services/huespedService'
import ModalConfirmacion from './ModalConfirmacion.vue';

const props = defineProps({
  visible: Boolean
})

const emit = defineEmits(['close'])

const documento = ref('')
const huesped = ref(null)
const mostrarConfirmacion = ref(false)

watch(
  () => props.visible,
  (newValue) => {
    if (!newValue) {
      resetState()
    }
  }
)

function resetState() {
  documento.value = ''
  huesped.value = null
}

function cerrarModal() {
  emit('close')
}

async function buscarHuesped() {
  if (documento.value.trim() === '') {
    huesped.value = null
    return
  }

  try {
    const response = await getHuespedByDocument(documento.value)
    huesped.value = response?.data || null
  } catch (error) {
    console.error('Error al encontrar huésped:', error)
    huesped.value = null
  }
}

function confirmarSeleccion() {
  mostrarConfirmacion.value = true
}
</script>
