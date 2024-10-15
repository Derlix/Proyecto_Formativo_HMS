<template>
  <div
    v-if="visible"
    class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white"
  >
    <div
      class="bg-white dark:bg-gray-800 p-4 sm:p-6 md:p-8 rounded-lg shadow-lg max-w-lg md:max-w-2xl w-full relative"
    >
      <!-- Botón de cerrar -->
      <button @click="close" class="absolute top-4 right-4 text-gray-600 dark:text-gray-300">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>

      <h2
        class="text-xl md:text-2xl mb-4 md:mb-6 font-semibold text-gray-900 dark:text-white text-center"
      >
        Movimiento de pasajeros - Check-In
      </h2>

      <!-- Step 1: Factura List -->
      <div v-if="currentStep === 1">
        <div class="flex items-center border rounded-lg shadow-sm mb-4">
          <input
            type="text"
            placeholder="Buscar pasajero por documento"
            class="search-input flex-grow px-3 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:text-white dark:bg-gray-700"
            v-model="searchDocumento"
          />
        </div>

        <div class="overflow-x-auto bg-gray-50 dark:bg-gray-800 rounded-lg shadow-md p-4 max-h-64">
          <table class="min-w-full bg-white dark:bg-gray-700 border-gray-300 text-xs md:text-sm">
            <thead>
              <tr class="bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-200">
                <th class="px-2 py-2">Nombre Completo</th>
                <th class="px-2 py-2">Documento</th>
                <th class="px-2 py-2">Valor Depositado</th>
                <th class="px-2 py-2">Empresa</th>
                <th class="px-2 py-2">Habitación</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="reserva in filteredReservas"
                :key="reserva.id_reserva"
                class="hover:bg-gray-100 dark:hover:bg-gray-600"
              >
                <td class="border px-2 py-2 dark:text-white">
                  {{ reserva.huesped.nombre_completo }}
                </td>
                <td class="border px-2 py-2 dark:text-white">
                  {{ reserva.huesped.numero_documento }}
                </td>
                <td class="border px-2 py-2 dark:text-white">
                  {{ reserva.reserva.valor_deposito }}
                </td>
                <td class="border px-2 py-2 dark:text-white">{{ reserva.reserva.empresa }}</td>
                <td class="border px-2 py-2 dark:text-white">
                  <div class="flex items-center justify-between">
                    <span>{{ reserva.habitacion.numero_habitacion }}</span>
                    <input
                      type="radio"
                      :value="reserva.id_reserva"
                      v-model="seleccionaridReservaSeleccionada"
                      @change="seleccionaridReserva(reserva.id_reserva)"
                      class="ml-2"
                    />
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Step 2: Datos de Check-In -->
      <div v-if="currentStep === 2">
        <div class="overflow-x-auto bg-gray-50 dark:bg-gray-800 rounded-lg shadow-md p-4 max-h-64">
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
              >Medio de llegada</label
            >
            <select
              v-model="medioLlegada"
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
              required
            >
              <option value="AEREO">Aéreo</option>
              <option value="TERRESTRE">Terrestre</option>
            </select>
          </div>

          <div class="mt-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
              >Situación de llegada</label
            >
            <select
              v-model="situacionLlegada"
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
              required
            >
              <option value="CON RESERVA">Con Reserva</option>
              <option value="SIN RESERVA">Sin Reserva</option>
            </select>
          </div>

          <div class="mt-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
              >Equipaje</label
            >
            <select
              v-model="equipaje"
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
              required
            >
              <option value="SI">Sí</option>
              <option value="NO">No</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Botones de navegación -->
      <div class="flex justify-between mt-4">
        <button
          v-if="currentStep > 1"
          @click="previousStep"
          class="bg-gray-300 text-gray-700 px-4 py-2 rounded-lg"
        >
          Anterior
        </button>
        <button
          v-if="currentStep < 2"
          @click="nextStep"
          class="bg-blue-600 text-white px-4 py-2 rounded-lg"
          :disabled="!seleccionaridReservaSeleccionada"
        >
          Siguiente
        </button>
      </div>

      <!-- Botón de confirmar Check-In -->
      <button
        v-if="currentStep === 2"
        @click="confirmarCheckin"
        class="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg w-full sm:w-auto"
      >
        Confirmar Check-In
      </button>
    </div>
  </div>

  <!-- Modal de éxito -->
  <ModalAlert
    :visible="showSuccess"
    titulo="Éxito"
    descripcion="Check-In realizado con éxito."
    :textBoton="'Cerrar'"
    color="text-green-400"
    @close="closeSuccess"
  />

  <!-- Modal de error -->
  <ModalAlert
    :visible="showError"
    titulo="Error"
    descripcion="Hubo un problema al procesar el Check-In. Intenta nuevamente."
    :textBoton="'Cerrar'"
    color="text-red-600"
    @close="closeError"
  />
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { obtenertodasReservasHabitacion } from '@/services/reservaHabitacionService'
import { crearCheckin } from '@/services/checkinService'
import ModalAlert from './ModalAlert.vue'

const props = defineProps({
  visible: {
    type: Boolean,
    required: true
  }
})

const showSuccess = ref(false)
const showError = ref(false)
const reservas = ref([])
const seleccionaridReservaSeleccionada = ref(null)
const searchDocumento = ref('')
const currentStep = ref(1)
const medioLlegada = ref('')
const situacionLlegada = ref('')
const equipaje = ref('')
const emit = defineEmits(['close'])

const filteredReservas = computed(() => {
  return reservas.value.filter(
    (reserva) =>
      reserva.huesped.numero_documento.includes(searchDocumento.value)
  )
})

const close = () => {
  emit('close')
}

const nextStep = () => {
  if (currentStep.value < 2) {
    currentStep.value++
  }
}

const previousStep = () => {
  if (currentStep.value > 1) {
    currentStep.value--
  }
}

const seleccionaridReserva = (id) => {
  seleccionaridReservaSeleccionada.value = id
}

const confirmarCheckin = async () => {
  try {
    const checkinData = {
      id_reserva: seleccionaridReservaSeleccionada.value, // Debe ser un número válido
      medio_llegada: medioLlegada.value, // Debe ser un valor permitido
      llegada_situacion: situacionLlegada.value, // Debe ser un valor permitido
      equipaje: equipaje.value // Debe ser un valor permitido
    };
    
    console.log('Datos de check-in que se envían:', checkinData); // Para depuración

    await crearCheckin(
      checkinData.id_reserva,
      checkinData.medio_llegada,
      checkinData.llegada_situacion,
      checkinData.equipaje
    );
    
    showSuccess.value = true;
  } catch (error) {
    console.error('Error al crear Check-In:', error);
    if (error.data) {
      console.error('Detalles del error:', error.data);
    } else {
      console.error('Error sin respuesta del servidor:', error.message);
    }
    showError.value = true;
  }
};



const closeSuccess = () => {
  showSuccess.value = false
  close() 
  resetForm()
}

const closeError = () => {
  showError.value = false
  resetForm()
}

const resetForm = () => {
  seleccionaridReservaSeleccionada.value = null
  searchDocumento.value = ''
  medioLlegada.value = 'AEREO'
  situacionLlegada.value = 'CON RESERVA'
  equipaje.value = 'SI'
  currentStep.value = 1 // Regresar al primer paso
}

onMounted(() => {
  fetchReservas()
})

const fetchReservas = async () => {
  try {
    const response = await obtenertodasReservasHabitacion()
    reservas.value = response.data
  } catch (error) {
    console.error('Error al obtener reservas:', error)
  }
}
</script>

