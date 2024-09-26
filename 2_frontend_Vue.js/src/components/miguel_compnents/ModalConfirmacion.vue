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

      <div v-if="paso === 1" class="grid grid-cols-2 gap-4">
        <!-- Controles para adultos y niños -->
        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Adultos</label>
          <div class="flex items-center">
            <button
              @click="disminuirAdultos"
              class="bg-gray-300 dark:bg-gray-700 text-gray-700 dark:text-white px-2 py-1 rounded-l"
            >
              -
            </button>
            <input
              type="number"
              v-model="adultos"
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-r bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
              readonly
            />
            <button
              @click="aumentarAdultos"
              class="bg-gray-300 dark:bg-gray-700 text-gray-700 dark:text-white px-2 py-1 rounded-r"
            >
              +
            </button>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Niños</label>
          <div class="flex items-center">
            <button
              @click="disminuirNinos"
              class="bg-gray-300 dark:bg-gray-700 text-gray-700 dark:text-white px-2 py-1 rounded-l"
            >
              -
            </button>
            <input
              type="number"
              v-model="ninos"
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-r bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
              readonly
            />
            <button
              @click="aumentarNinos"
              class="bg-gray-300 dark:bg-gray-700 text-gray-700 dark:text-white px-2 py-1 rounded-r"
            >
              +
            </button>
          </div>
        </div>

        <!-- Campos para tarifa, impuestos, fechas y estadía -->
        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Tarifa</label>
          <input
            type="text"
            v-model="tarifa"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Impuestos</label
          >
          <input
            type="text"
            v-model="impuestos"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Llegada</label>
          <input
            type="date"
            v-model="llegadaDia"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Salida</label>
          <input
            type="date"
            v-model="salidaDia"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>

        <div class="col-span-2">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Estadía</label>
          <input
            type="text"
            v-model="estadia"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>
      </div>
      <div
        v-else-if="paso === 2"
        class="overflow-x-auto bg-gray-50 dark:bg-gray-800 rounded-lg shadow-md p-4 max-h-64"
      >
        <table class="min-w-full bg-white dark:bg-gray-700 border border-gray-300">
          <thead>
            <tr class="bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-200">
              <th class="px-4 py-2">Habitación</th>
              <th class="px-4 py-2">Categoría</th>
              <th class="px-4 py-2">Piso</th>
              <th class="px-4 py-2">Precio</th>
              <th class="px-4 py-2">Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="  habitacion in habitaciones.filter((h) => h.estado === 'ACTIVO')"
              :key="habitacion.id_habitacion"
              class="hover:bg-gray-100 dark:hover:bg-gray-600"
            >
            <TableCheckboxCell v-if="checkable" @checked="checked($event, client)" />
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.numero_habitacion }}</td>
              <td class="border px-4 py-2 dark:text-white">
                {{ habitacion.id_categoria_habitacion }}
              </td>
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.piso }}</td>
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.precio_actual }}</td>
              <td class="border px-4 py-2">
                <input type="checkbox">
              </td>
            </tr>
          </tbody>
        </table>
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
import { ref, onMounted } from 'vue'
import { obtenerTodasHabitaciones } from '@/services/habitacionService'

const props = defineProps({
  visible: Boolean,
  huesped: Object
})

const emit = defineEmits(['close', 'confirm'])

const paso = ref(1)
const adultos = ref(0)
const ninos = ref(0)
const tarifa = ref('')
const impuestos = ref('')
const llegadaDia = ref('')
const salidaDia = ref('')
const estadia = ref('')
const habitaciones = ref([])

const cerrarModal = () => {
  emit('close')
}

// Navegar entre pasos
const siguiente = () => {
  if (paso.value < 2) {
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

// Ajustar la cantidad de adultos y niños
const aumentarAdultos = () => {
  adultos.value++
}

const disminuirAdultos = () => {
  if (adultos.value > 0) {
    adultos.value--
  }
}

const aumentarNinos = () => {
  ninos.value++
}

const disminuirNinos = () => {
  if (ninos.value > 0) {
    ninos.value--
  }
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

const checked = (isChecked, client) => {
  if (isChecked) {
    checkedRows.value.push(client)
  } else {
    checkedRows.value = remove(checkedRows.value, (row) => row.id === client.id)
  }
}

onMounted(() => {
  cargarHabitaciones()
})
</script>
