<template>
  <div
    v-if="visible"
    class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
  >
    <div
      class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-2xl w-full relative transition-all"
    >
      <button
        @click="cerrarModal"
        class="absolute top-4 right-4 text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300"
      >
        &times;
      </button>

      <h1 class="text-xl font-semibold mb-4 text-center text-gray-900 dark:text-white">
        Formulario crear reserva
      </h1>

      <div class="flex justify-center mb-6">
        <span class="text-gray-700 dark:text-gray-300 mx-2">Reserva para: </span>
        <p class="text-gray-900 dark:text-gray-100">{{ huesped.nombre_completo }}</p>
      </div>

      <!-- Paso 1 - Datos de la reserva -->
      <div v-if="paso === 1" class="grid grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Fecha de Reserva</label
          >
          <input
            type="date"
            v-model="fecha_reserva"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Empresa</label>
          <input
            type="text"
            v-model="empresa"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>
      </div>

      <!-- Paso 2 - Selección de habitación -->
      <div
        v-else-if="paso === 2"
        class="overflow-x-auto bg-gray-50 dark:bg-gray-800 rounded-lg shadow-md p-4 max-h-64"
      >
        <table class="min-w-full bg-white dark:bg-gray-700 border-gray-300">
          <thead>
            <tr class="bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-200">
              <th class="px-4 py-2">Habitación</th>
              <th class="px-4 py-2">Características</th>
              <th class="px-4 py-2">Piso</th>
              <th class="px-4 py-2">Precio</th>
              <th class="px-4 py-2">Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="habitacion in habitaciones.filter((h) => h.estado === 'ACTIVO')"
              :key="habitacion.id_habitacion"
              class="hover:bg-gray-100 dark:hover:bg-gray-600"
            >
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.numero_habitacion }}</td>
              <td class="border px-4 py-2 dark:text-white">
                {{ habitacion.caracteristicas.nombre_caracteristicas }}
              </td>
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.piso }}</td>
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.precio_actual }}</td>
              <td class="border px-4 py-2 flex justify-center items-center">
                <input type="checkbox" />
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-else-if="paso === 3" class="space-y-4">
        <h2 class="text-lg font-semibold text-gray-900 dark:text-gray-200">
          Seleccione un método de pago
        </h2>

        <div class="flex items-center space-x-4">
          <!-- Campo para agregar depósito -->
          <div class="flex-1">
            <label class="text-sm font-medium text-gray-700 dark:text-gray-300">Depósito</label>
            <input
              type="number"
              v-model="deposito"
              class="p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
              placeholder="Ingrese el monto del depósito"
            />
          </div>

          <!-- Campo para seleccionar la forma de pago -->
          <div class="flex-1">
            <label class="text-sm font-medium text-gray-700 dark:text-gray-300"
              >Forma de pago</label
            >
            <select
              v-model="forma_pago"
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            >
              <option value="">Seleccione una opción</option>
              <option value="EFECTIVO">Efectivo</option>
              <option value="DEBITO">Débito</option>
              <option value="CREDITO">Crédito</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Botones de navegación entre pasos -->
      <div class="flex justify-between mt-6">
        <button
          v-if="paso > 1"
          @click="atras"
          class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-200 font-semibold py-2 px-4 rounded-md hover:bg-gray-400 dark:hover:bg-gray-500 transition"
        >
          Atrás
        </button>
        <button
          @click="siguiente"
          class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition"
        >
          Siguiente
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { obtenerTodasHabitaciones } from '@/services/habitacionService'

const props = defineProps({
  visible: Boolean,
  huesped: Object
})

const emit = defineEmits(['close', 'confirm'])

const paso = ref(1)
const fecha_reserva = ref('')
const empresa = ref('')
const habitaciones = ref([])

const deposito = ref('')
const pagar_total = ref(false)
const concepto = ref('')

const cerrarModal = () => {
  emit('close')
}

// Navegar entre pasos
const siguiente = () => {
  if (paso.value < 3) {
    paso.value++
  } else {
    confirmarReserva()
  }
}

const atras = () => {
  if (paso.value > 1) {
    paso.value--
  }
}

const confirmarReserva = () => {
  cerrarModal()
}

const cargarHabitaciones = async () => {
  try {
    const response = await obtenerTodasHabitaciones()
    habitaciones.value = response.data
    console.log(habitaciones.value)
  } catch (error) {
    console.error('Error al cargar las habitaciones:', error)
  }
}

onMounted(() => {
  cargarHabitaciones()
})
</script>
