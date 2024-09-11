<template>
  <div
    v-if="visible"
    class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50"
  >
    <div class="max-w-3xl w-full p-8 bg-white shadow-lg rounded-lg relative">
      <!-- Botón de cierre en la esquina superior derecha -->
      <button @click="cerrarModal" class="absolute top-4 right-4 text-gray-500 hover:text-gray-700">
        &times;
      </button>

      <h1 class="text-lg font-bold mb-4 text-center">Seleccionar Huesped Existente</h1>

      <!-- Formulario para ingresar documento -->
      <div class="mb-6">
        <label for="documento" class="block text-sm font-medium text-gray-700 mb-2">
          Ingresar Documento:
        </label>
        <input
          v-model="documento"
          type="text"
          id="documento"
          class="block w-full border rounded-md p-2"
          placeholder="Ingrese el documento del huésped"
          @input="buscarHuesped"
        />
      </div>

      <!-- Mostrar datos del huésped -->
      <div v-if="huesped" class="bg-gray-100 p-4 rounded-md border border-gray-300">
        <p><strong>Nombre Completo:</strong> {{ huesped.nombre_completo }}</p>
        <p><strong>Numero Documento:</strong> {{ huesped.numero_documento }}</p>
        <p><strong>Telefono:</strong> {{ huesped.telefono }}</p>
        <p><strong>Email:</strong> {{ huesped.email }}</p>
        <p><strong>Ocupacion:</strong> {{ huesped.ocupacion }}</p>
        <p><strong>Direccion:</strong> {{ huesped.direccion }}</p>
      </div>

      <!-- Botones para cerrar y seleccionar huésped -->
      <div class="flex justify-between mt-6">
        <button
          @click="cerrarModal"
          class="bg-gray-300 text-gray-700 font-semibold py-2 px-4 rounded-md hover:bg-gray-400 transition"
        >
          Cerrar
        </button>

        <button
          @click="confirmarSeleccion"
          :disabled="!huesped"
          class="bg-blue-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 transition"
          :class="{ 'opacity-50 cursor-not-allowed': !huesped }"
        >
          Confirmar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { getHuespedByDocument } from '@/services/huespedService'

const props = defineProps({
  visible: Boolean
})

const emit = defineEmits(['close'])

const mostrarModal = ref(false)
const documento = ref('')
const huesped = ref(null)

watch(
  () => props.visible,
  (newValue) => {
    mostrarModal.value = newValue
  }
)

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
    if (response && response.data) {
      huesped.value = response.data
    } else {
      huesped.value = null
    }
  } catch (error) {
    console.error('Error al encontrar huesped:', error)
    huesped.value = null
  }
}

function confirmarSeleccion() {
  cerrarModal()
}
</script>
