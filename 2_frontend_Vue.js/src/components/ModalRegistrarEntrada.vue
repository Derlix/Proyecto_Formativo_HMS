<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white">
    <div class="bg-white dark:bg-gray-800 p-8 sm:p-12 rounded-lg shadow-lg max-w-2xl w-full relative">
      <!-- Botón de cerrar -->
      <button @click="close" class="absolute top-4 right-4 text-gray-600 dark:text-gray-300">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <h2 class="text-2xl mb-6 font-semibold text-gray-900 dark:text-white">Movimiento de pasajeros - ENTRADA</h2>

      <div class="grid grid-cols-2 gap-4 mb-5">
        <div>
          <label for="documento" class="block mb-1 text-sm font-medium">Documento</label>
          <input
            type="text"
            id="documento"
            v-model="documento"
            @blur="buscarReserva"
            class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
          >
        </div>
        <div>
          <label for="nombre" class="block mb-1 text-sm font-medium">Nombre Completo</label>
          <input
            type="text"
            id="nombre"
            v-model="nombre"
            :disabled="!reservaEncontrada"
            class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
          >
        </div>
        <div>
          <label for="habitacion" class="block mb-1 text-sm font-medium">Habitación</label>
          <input
            type="text"
            id="habitacion"
            v-model="numeroHabitacion"
            :disabled="!reservaEncontrada"
            class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
          >
        </div>
        <!-- Medio de llegada select -->
        <div>
          <label for="medioLlegada" class="block mb-1 text-sm font-medium">Medio de Llegada</label>
          <select
            id="medioLlegada"
            v-model="medioLlegada"
            class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
          >
            <option value="AEREO">AÉREO</option>
            <option value="TERRESTRE">TERRESTRE</option>
          </select>
        </div>
        <!-- Situación de llegada select -->
        <div>
          <label for="situacionLlegada" class="block mb-1 text-sm font-medium">Situación de Llegada</label>
          <select
            id="situacionLlegada"
            v-model="situacionLlegada"
            class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
          >
            <option value="CON RESERVA">CON RESERVA</option>
            <option value="SIN RESERVA">SIN RESERVA</option>
          </select>
        </div>
        <!-- Equipaje select -->
        <div>
          <label for="equipaje" class="block mb-1 text-sm font-medium">Equipaje</label>
          <select
            id="equipaje"
            v-model="equipaje"
            class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
          >
            <option value="SI">SI</option>
            <option value="NO">NO</option>
          </select>
        </div>
      </div>

      <button @click="confirmarCheckin" :disabled="!reservaEncontrada" class="bg-blue-600 text-white px-6 py-3 rounded w-full">
        Confirmar
      </button>
    </div>
  </div>

  <!-- Alerta de éxito -->
  <div v-if="showSuccess" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white">
    <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-sm w-full relative">
      <button @click="closeSuccess" class="absolute top-2 right-2 text-gray-600 dark:text-gray-300">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
      <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">Check-in realizado con éxito</h3>
      <p>El check-in se ha completado correctamente.</p>
      <button @click="closeSuccess" class="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg w-full">
        Cerrar
      </button>
    </div>
  </div>

  <!-- Alerta de error -->
  <div v-if="showError" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white">
    <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-sm w-full relative">
      <button @click="closeError" class="absolute top-2 right-2 text-gray-600 dark:text-gray-300">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
      <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">Error al realizar el check-in</h3>
      <p>Hubo un problema al procesar el check-in. Intenta nuevamente.</p>
      <button @click="closeError" class="mt-4 bg-red-600 text-white px-4 py-2 rounded-lg w-full">
        Cerrar
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { obtenertodasReservasHabitacion } from '@/services/reservaHabitacionService'
import { crearCheckin } from '@/services/checkinService'

const props = defineProps({
  visible: {
    type: Boolean,
    required: true
  }
})


const showSuccess = ref(false)
const showError = ref(false)
const documento = ref('')
const nombre = ref('')
const numeroHabitacion = ref('')
const medioLlegada = ref('AEREO') 
const situacionLlegada = ref('CON RESERVA') 
const equipaje = ref('SI') 
const reservaEncontrada = ref(false)
const idReserva = ref(null) 

const emit = defineEmits(['close'])

const closeSuccess = () => {
  showSuccess.value = false
  emit('close') 
}

const closeError = () => {
  showError.value = false
  emit('close') 
}

const buscarReserva = async () => {
  try {
    const response = await obtenertodasReservasHabitacion()
    if (response.data && response.data.length) {
      const reserva = response.data.find(r => r.huesped.numero_documento === documento.value)

      if (reserva) {
        reservaEncontrada.value = true
        nombre.value = reserva.huesped.nombre_completo
        numeroHabitacion.value = reserva.habitacion.numero_habitacion
        idReserva.value = reserva.id_reserva // Guarda el ID de la reserva
      } else {
        resetFields()
      }
    } else {
      resetFields()
    }
  } catch (error) {
    console.error('Error al buscar la reserva:', error)
    resetFields()
  }
}

const confirmarCheckin = async () => {
  if (!idReserva.value) {
    console.error('No se encontró ninguna reserva asociada al documento.')
    return
  }

  try {
    const response = await crearCheckin(
      idReserva.value,   
      medioLlegada.value, 
      situacionLlegada.value, 
      equipaje.value
    )
    showSuccess.value = true 
  } catch (error) {
    showError.value = true 
  }
}

const resetFields = () => {
  reservaEncontrada.value = false
  nombre.value = ''
  numeroHabitacion.value = ''
  idReserva.value = null
  medioLlegada.value = 'AEREO'
  situacionLlegada.value = 'CON_RESERVA'
  equipaje.value = 'SI'
}


const close = () => {
  emit('close')
}
</script>
