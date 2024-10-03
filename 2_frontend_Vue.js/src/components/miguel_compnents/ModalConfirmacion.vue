<template>
  <div
    v-if="visible"
    class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
  >
    <div
      class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-2xl w-full relative transition-all"
    >
      <h1 class="text-xl font-semibold mb-4 text-center text-gray-900 dark:text-white">
        Formulario crear reserva
      </h1>

      <div class="flex justify-center mb-6">
        <span class="text-gray-700 dark:text-gray-300 mx-2">Reserva para:</span>
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
            placeholder="Ingrese el nombre de la empresa"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Numero de adultos</label
          >
          <input
            type="number"
            v-model="num_adultos"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            placeholder="Ingrese el numero de adultos"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Numero de niños</label
          >
          <input
            type="number"
            v-model="num_niños"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            placeholder="Ingrese el numero de niños"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Fecha de llegada</label
          >
          <input
            type="date"
            v-model="fecha_llegada"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Fecha de salida</label
          >
          <input
            type="date"
            v-model="fecha_salida"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Depósito</label>
          <input
            type="number"
            v-model="deposito"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            placeholder="Ingrese el monto del depósito"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Forma de Pago</label
          >
          <select
            v-model="forma_pago"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          >
            <option value="">Seleccione una opción</option>
            <option value="EFECTIVO">Efectivo</option>
            <option value="DEBITO">Débito</option>
            <option value="CREDITO">Crédito</option>
          </select>
        </div>
      </div>

      <div
        v-if="paso === 2"
        class="overflow-x-auto bg-gray-50 dark:bg-gray-800 rounded-lg shadow-md p-4 max-h-64"
      >
        <table class="min-w-full bg-white dark:bg-gray-700 border-gray-300">
          <thead>
            <tr class="bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-200">
              <th class="px-4 py-2">ID Reserva</th>
              <th class="px-4 py-2">Fecha de Reserva</th>
              <!-- <th class="px-4 py-2">Fecha de Llegada</th>
              <th class="px-4 py-2">Fecha de Salida</th> -->
              <th class="px-4 py-2">Estado</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="reserva in reservas"
              :key="reserva.id_reserva"
              class="hover:bg-gray-100 dark:hover:bg-gray-600"
            >
              <td class="border px-4 py-2 dark:text-white">{{ reserva.id_reserva }}</td>
              <td class="border px-4 py-2 dark:text-white">{{ reserva.fecha_reserva }}</td>
              <!-- <td class="border px-4 py-2 dark:text-white">{{ reserva.fecha_llegada }}</td>
              <td class="border px-4 py-2 dark:text-white">{{ reserva.fecha_salida }}</td> -->
              <td class="border px-4 py-2 dark:text-white">{{ reserva.estado_reserva }}</td>
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

      <div
        v-else-if="paso === 3"
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
                <input
                  type="checkbox"
                  :value="habitacion.id_habitacion"
                  v-model="habitacionSeleccionada"
                  @change="seleccionarHabitacion(habitacion.id_habitacion)"
                />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- Alerta de éxito -->
      <div
        v-if="showSuccessAlert"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white"
      >
        <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-sm w-full relative">
          <button
            @click="closeAlert"
            class="absolute top-2 right-2 text-gray-600 dark:text-gray-300"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
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
          <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            Reserva realizada con éxito
          </h3>
          <p>La reserva se ha completado correctamente.</p>
          <button
            @click="closeAlert"
            class="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg w-full"
          >
            Cerrar
          </button>
        </div>
      </div>

      <!-- Alerta de error -->
      <div
        v-if="showError"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white"
      >
        <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-sm w-full relative">
          <button
            @click="closeError"
            class="absolute top-2 right-2 text-gray-600 dark:text-gray-300"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
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
          <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            Error al realizar la reserva
          </h3>
          <p>Hubo un problema al procesar la reserva. Intenta nuevamente.</p>
          <button
            @click="closeError"
            class="mt-4 bg-red-600 text-white px-4 py-2 rounded-lg w-full"
          >
            Cerrar
          </button>
        </div>
      </div>

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
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { obtenerTodasHabitaciones } from '@/services/habitacionService'
import { crearReserva } from '@/services/reservaService'
import { crearReservaHabitacion } from '@/services/reservaHabitacionService'
import { obtenerReservasPorHuesped } from '@/services/reservaService'

const props = defineProps({
  visible: Boolean, // Prop que controla la visibilidad del modal
  huesped: Object
})

const emit = defineEmits(['close', 'confirm'])
const reservas = ref([])
const paso = ref(1)
const fecha_reserva = ref('')
const fecha_llegada = ref('')
const fecha_salida = ref('')
const num_adultos = ref('')
const num_niños = ref('')
const empresa = ref('')
const habitaciones = ref([])
const deposito = ref('')
const forma_pago = ref('')
const habitacionSeleccionada = ref(null)
const seleccionaridReservaSeleccionada = ref(null)
const showSuccessAlert = ref(false) // Estado para mostrar la alerta

const seleccionarHabitacion = (id_habitacion) => {
  habitacionSeleccionada.value = id_habitacion
  console.log('Habitación seleccionada:', habitacionSeleccionada.value)
}

const seleccionaridReserva = (id_reserva) => {
  seleccionaridReservaSeleccionada.value = id_reserva
  console.log('ID Reserva seleccionada:', seleccionaridReservaSeleccionada.value)
}

// Función para cargar las reservas por número de documento
const cargarReservasDelHuesped = async () => {
  try {
    const response = await obtenerReservasPorHuesped(props.huesped.numero_documento)
    reservas.value = response.data // Asigna las reservas obtenidas
    console.log('Reservas del huésped:', reservas.value) // Imprime las reservas en la consola
  } catch (error) {
    console.error('Error al obtener reservas:', error) // Imprime el error si falla la petición
  }
}

// Cargar las reservas cuando se monte el componente
onMounted(() => {
  if (props.huesped && props.huesped.numero_documento) {
    cargarReservasDelHuesped()
  }
})

// Vigila el paso actual para cargar reservas si es necesario
watch(paso, (nuevoPaso) => {
  if (nuevoPaso === 2) {
    cargarReservasDelHuesped()
  }
})

// Método para cerrar la alerta
const closeAlert = () => {
  showSuccessAlert.value = false // Cerrar la alerta
  closeModal()
}

// Método para finalizar el paso 3
const finalizarPaso3 = async () => {
  if (!habitacionSeleccionada.value) {
    console.error('Por favor, selecciona una habitación antes de continuar.')
    return
  }

  await confirmarReservaHabitacion() // Llama a la función para confirmar la reserva de habitación

  showSuccessAlert.value = true
}


// Método para avanzar en los pasos
const siguiente = async () => {
  if (paso.value === 1) {
    await confirmarReserva()
  } else if (paso.value === 3) {
    await finalizarPaso3() // Llama a la función que finaliza el paso 3
  }

  if (paso.value < 4) {
    paso.value++
  }
}

const atras = () => {
  if (paso.value > 1) {
    paso.value--
  }
}

// Confirmar la reserva
const confirmarReserva = async () => {
  try {
    const response = await crearReserva(
      fecha_reserva.value,
      empresa.value,
      parseFloat(deposito.value),
      forma_pago.value,
      'ACTIVO',
      props.huesped.id_huesped
    )

    console.log('Reserva creada exitosamente:', response.data)
  } catch (error) {
    console.error('Error al crear la reserva:', error.response ? error.response.data : error)
  }
}

// Confirmar la reserva de habitación
const confirmarReservaHabitacion = async () => {
  try {
    const response = await crearReservaHabitacion(
      seleccionaridReservaSeleccionada.value, // ID de la reserva creada
      habitacionSeleccionada.value,
      num_adultos.value,
      num_niños.value,
      fecha_llegada.value,
      fecha_salida.value
    )
    console.log('Habitación reservada exitosamente:', response.data)
  } catch (error) {
    console.error(
      'Error al crear la reserva de la habitación:',
      error.response ? error.response.data : error
    )
  }
}

// Cargar las habitaciones
const cargarHabitaciones = async () => {
  try {
    const response = await obtenerTodasHabitaciones()
    habitaciones.value = response.data
  } catch (error) {
    console.error('Error al cargar las habitaciones:', error)
  }
}

// Manejo de los modales y el historial de navegación
const modalStack = ref([]) // Pila de modales abiertos

const handlePopState = () => {
  if (modalStack.value.length > 0) {
    modalStack.value.pop() // Elimina el último modal del historial
    if (modalStack.value.length === 0) {
      emit('close') // Cierra el modal si no hay más en la pila
    }
  }
}

const openModal = () => {
  modalStack.value.push('reservaModal') // Añade el modal al historial
  window.history.pushState({}, '', '') // Añade un nuevo estado al historial
}

const closeModal = () => {
  emit('close')
  modalStack.value = [] // Limpia la pila de modales
}

onMounted(() => {
  window.addEventListener('popstate', handlePopState) // Escucha el evento "popstate"
  if (props.visible) {
    openModal() // Abre el modal al montar si está visible
  }
})

watch(
  () => props.visible,
  (newValue) => {
    if (newValue) {
      openModal()
    }
  }
)

onUnmounted(() => {
  window.removeEventListener('popstate', handlePopState) // Elimina el listener al desmontar
  modalStack.value = [] // Limpia la pila de modales al desmontar
})

cargarHabitaciones()
</script>
