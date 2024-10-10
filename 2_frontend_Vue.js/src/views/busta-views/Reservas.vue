<script setup>
import { ref, onMounted } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import AlertaCrearReserva from '@/components/miguel_compnents/AlertaCrearReserva.vue'
import { obtenerTodasHabitaciones } from '@/services/habitacionService'
import ModalCambiarHabitacion from '@/components/alejo_components/ModalCambiarHabitacion.vue'
import Calendario from '@/components/arias_components/Calendario.vue'
import ModalTarjetaReserva from '@/components/alejo_components/ModalTarjetaReserva.vue'
const showModalCambiarHabitacion = ref(false)
const showModalCrearReserva = ref(false)
const showModalTarjetaReserva = ref(false)
const habitaciones = ref([])

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

<template>
  <LayoutAuthenticated>
    <div class="px-3 py-4">
      <h2 class="text-xl font-bold text-gray-900 dark:text-gray-100">Operador De Reservas</h2>

      <div class="flex justify-center space-x-4 py-4">
        <button
          @click="showModalCrearReserva = true"
          class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition"
        >
          Crear reserva
        </button>
        
        <AlertaCrearReserva :mostrarModal="showModalCrearReserva" @cerrar="showModalCrearReserva = false" />
    
        <button
          @click="showModalCambiarHabitacion = true"
          class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition"
        >
          Cambiar habitación
        </button>
        
        <ModalCambiarHabitacion :isVisible="showModalCambiarHabitacion" @close="showModalCambiarHabitacion = false" />

        <button
          class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition"
        >
          Cambiar reserva
        </button>

        <button
          class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition"
        >
          Registrar comprobante de descuento
        </button>

        <button
          @click="showModalTarjetaReserva = true"
          class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition"
        >
          Tarjeta Reserva
        </button>
        <ModalTarjetaReserva :isVisible="showModalTarjetaReserva"  title="" @close="showModalTarjetaReserva = false"  />
      </div>

      <Calendario />

      <div class="overflow-x-auto">
        <table class="table-auto w-full border-collapse text-left">
          <thead class="bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-100">
            <tr>
              <th class="px-4 py-2">Habitación</th>
              <th class="px-4 py-2">caracteristicas</th>
              <th class="px-4 py-2">Piso</th>
              <th class="px-4 py-2">Estado</th>
              <th class="px-4 py-2">Precio</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="habitacion in habitaciones"
              :key="habitacion.id_habitacion"
              class="bg-white dark:bg-gray-800 border-b dark:border-gray-700"
            >
              <td class="px-4 py-2">{{ habitacion.numero_habitacion }}</td>
              <td class="px-4 py-2">{{ habitacion.caracteristicas.nombre_caracteristicas }}</td>
              <td class="px-4 py-2">{{ habitacion.piso }}</td>
              <td class="px-4 py-2">
                <span
                  class="inline-block px-3 py-1 text-xs font-semibold rounded-full"
                  :class="{
                    'bg-green-100 text-green-700 dark:bg-green-800 dark:text-green-100':
                      habitacion.estado === 'ACTIVO',
                    'bg-yellow-100 text-yellow-700 dark:bg-yellow-800 dark:text-yellow-100':
                      habitacion.estado === 'MANTENIMIENTO',
                    'bg-red-100 text-red-700 dark:bg-red-800 dark:text-red-100':
                      habitacion.estado === 'INACTIVO'
                  }"
                >
                  {{ habitacion.estado }}
                </span>
              </td>
              <td class="px-4 py-2">{{ habitacion.precio_actual | currency }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </LayoutAuthenticated>
</template>
