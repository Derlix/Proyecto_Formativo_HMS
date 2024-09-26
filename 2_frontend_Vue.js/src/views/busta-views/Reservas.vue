<script setup>
import { ref, onMounted } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import AlertaCrearReserva from '@/components/miguel_compnents/AlertaCrearReserva.vue'
import { obtenerTodasHabitaciones } from '@/services/habitacionService';


const showModal = ref(false)
const habitaciones = ref([]) 

const cargarHabitaciones = async () => {
  try {
    const response = await obtenerTodasHabitaciones() 
    habitaciones.value = response.data 
    console.log(habitaciones.value)
  } catch (error) {
    console.error("Error al cargar las habitaciones:", error)
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
        <button @click="showModal = true" class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition">
          Crear reserva
        </button>
        
        <AlertaCrearReserva :mostrarModal="showModal" @cerrar="showModal = false" />
    
        <button class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition">
          Cambiar habitación
        </button>
    
        <button class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition">
          Cambiar reserva
        </button>
    
        <button class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition">
          Registrar comprobante de descuento
        </button>
      </div>

      <div class="overflow-x-auto">
        <table class="table-auto w-full border-collapse text-left">
          <thead class="bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-100">
            <tr>
              <th class="px-4 py-2">Habitación</th>
              <th class="px-4 py-2">Tipo</th>
              <th class="px-4 py-2">Piso</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="habitacion in habitaciones" :key="habitacion.id_habitacion" class="bg-white dark:bg-gray-800">
              <td class="px-4 py-2">{{ habitacion.numero_habitacion }}</td>
              <td class="px-4 py-2">{{ habitacion.id_categoria_habitacion }}</td>
              <td class="px-4 py-2">{{ habitacion.piso }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </LayoutAuthenticated>
</template>