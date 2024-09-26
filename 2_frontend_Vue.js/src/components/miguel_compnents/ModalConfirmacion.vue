<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
    <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-2xl w-full relative transition-all">
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
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Fecha de Reserva</label>
          <input type="date" v-model="fecha_reserva" class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white" />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Empresa</label>
          <input type="text" v-model="empresa" class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white" placeholder="Ingrese el nombre de la empresa" />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Depósito</label>
          <input type="number" v-model="deposito" class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white" placeholder="Ingrese el monto del depósito" />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Forma de Pago</label>
          <select v-model="forma_pago" class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white">
            <option value="">Seleccione una opción</option>
            <option value="EFECTIVO">Efectivo</option>
            <option value="DEBITO">Débito</option>
            <option value="CREDITO">Crédito</option>
          </select>
        </div>
      </div>

      <!-- Paso 2 - Selección de habitación -->
      <div v-else-if="paso === 2" class="overflow-x-auto bg-gray-50 dark:bg-gray-800 rounded-lg shadow-md p-4 max-h-64">
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
            <tr v-for="habitacion in habitaciones.filter((h) => h.estado === 'ACTIVO')" :key="habitacion.id_habitacion" class="hover:bg-gray-100 dark:hover:bg-gray-600">
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.numero_habitacion }}</td>
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.caracteristicas.nombre_caracteristicas }}</td>
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.piso }}</td>
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.precio_actual }}</td>
              <td class="border px-4 py-2 flex justify-center items-center">
                <input type="checkbox" />
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Botones de navegación entre pasos -->
      <div class="flex justify-between mt-6">
        <button v-if="paso > 1" @click="atras" class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-200 font-semibold py-2 px-4 rounded-md hover:bg-gray-400 dark:hover:bg-gray-500 transition">
          Atrás
        </button>
        <button @click="siguiente" class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition">
          Siguiente
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { obtenerTodasHabitaciones } from '@/services/habitacionService'
import { crearReserva } from '@/services/reservaService'


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
const forma_pago = ref('')

const cerrarModal = () => {
  emit('close')
}


const siguiente = async () => {
  if (paso.value === 1) {
    await confirmarReserva(); 
  }
  if (paso.value < 2) {
    paso.value++;
  }
}

const atras = () => {
  if (paso.value > 1) {
    paso.value--;
  }
}

const confirmarReserva = async () => {
  try {
    const response = await crearReserva(
      fecha_reserva.value,
      empresa.value,
      parseFloat(deposito.value), 
      forma_pago.value,
      "ACTIVO", 
      props.huesped.id_huesped 
    );

    console.log('Reserva creada exitosamente:', response.data);
  } catch (error) {
    console.error('Error al crear la reserva:', error);
  }
};


const cargarHabitaciones = async () => {
  try {
    const response = await obtenerTodasHabitaciones()
    habitaciones.value = response.data
  } catch (error) {
    console.error('Error al cargar las habitaciones:', error)
  }
}

onMounted(() => {
  cargarHabitaciones()
})
</script>

