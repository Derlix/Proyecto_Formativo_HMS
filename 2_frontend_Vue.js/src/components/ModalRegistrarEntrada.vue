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

      <!-- Step 1: Reservation List -->
      <div v-if="currentStep === 1">
        <div class="overflow-x-auto bg-gray-50 dark:bg-gray-800 rounded-lg shadow-md p-4 max-h-64">
          <table class="min-w-full bg-white dark:bg-gray-700 border-gray-300">
            <thead>
              <tr class="bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-200">
                <th class="px-4 py-2">Nombre Completo</th>
                <th class="px-4 py-2">Fecha de Reserva</th>
                <th class="px-4 py-2">Habitación</th>
                <th class="px-4 py-2">Estado Habitación</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="reserva in reservas"
                :key="reserva.id_reserva"
                class="hover:bg-gray-100 dark:hover:bg-gray-600"
              >
                <td class="border px-4 py-2 dark:text-white">{{ reserva.huesped.nombre_completo }}</td>
                <td class="border px-4 py-2 dark:text-white">{{ reserva.fecha_entrada }}</td>
                <td class="border px-4 py-2 dark:text-white">{{ reserva.habitacion.numero_habitacion }}</td>
                <td class="border px-4 py-2 dark:text-white">{{ reserva.habitacion.estado }}</td>
                <td class="border px-4 py-2 flex justify-center items-center">
                  <input
                    type="checkbox"
                    :value="reserva.id_reserva"
                    v-model="seleccionaridReservaSeleccionada"
                    @change="seleccionaridReserva(reserva.id_reserva)"
                  />
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <button @click="nextStep" class="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg">Siguiente</button>
      </div>

      <!-- Step 2: Arrival Situation -->
      <div v-else-if="currentStep === 2">
        <div class="mb-4">
  <label for="llegada" class="block mb-1 text-sm font-medium">Situación de llegada</label>
  <select
    id="llegada"
    v-model="situacionLlegada"
    class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
  >
    <option value="CON RESERVA">Con reserva</option>
    <option value="SIN RESERVA">Sin reserva</option>
  </select>
</div>

<div class="mb-4">
  <label for="mediollegada" class="block mb-1 text-sm font-medium">Medio de llegada</label>
  <select
    id="mediollegada"
    v-model="mediollegada"
    class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
  >
    <option value="AEREO">Aereo</option>
    <option value="TERRESTRE">Terrestre</option>
  </select>
</div>

<div class="mb-4">
  <label for="equipaje" class="block mb-1 text-sm font-medium">Equipaje</label>
  <select
    id="equipaje"
    v-model="equipaje"
    class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
  >
    <option value="SI">Si</option>
    <option value="NO">No</option>
  </select>
</div>

<div class="flex justify-between mt-4">
  
  <button @click="previousStep" class="bg-gray-400 text-white px-4 py-2 rounded-lg">Anterior</button>
  <button @click="confirmarSalida" class="bg-blue-600 text-white px-6 py-3 rounded-lg">Confirmar</button>
</div>
</div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
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
const reservas = ref([]) // Array to store reservations
const seleccionaridReservaSeleccionada = ref([]) // For storing selected reservation IDs
const currentStep = ref(1) // Step control
const situacionLlegada = ref('')
const mediollegada = ref('')
const equipaje = ref('')
const emit = defineEmits(['close'])

const close = () => {
  emit('close')
}

const nextStep = () => {
  currentStep.value = 2
}

const previousStep = () => {
  currentStep.value = 1
}

const fetchReservas = async () => {
  try {
    const response = await obtenertodasReservasHabitacion()
    reservas.value = response.data || []
  } catch (error) {
    console.error('Error al obtener las reservas:', error)
  }
}

const seleccionaridReserva = (id) => {
  if (seleccionaridReservaSeleccionada.value.includes(id)) {
    seleccionaridReservaSeleccionada.value = seleccionaridReservaSeleccionada.value.filter(reservaId => reservaId !== id)
  } else {
    seleccionaridReservaSeleccionada.value.push(id)
  }
}

onMounted(() => {
  fetchReservas() // Fetch reservations on component mount
})
</script>
