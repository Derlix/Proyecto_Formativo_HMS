<script setup>
import { ref, onMounted } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import CardBox from '@/components/CardBox.vue'
import ModalRegistrarEntrada from '@/components/ModalRegistrarEntrada.vue'
import ModalRegistrarSalida from '@/components/ModalRegistrarSalida.vue'
import CardBoxWidget from '@/components/CardBoxWidget.vue'
import SectionMain from '@/components/SectionMain.vue'
import TitleIconOnly from '@/components/TitleIconOnly.vue'
import {
  mdiBed,
  mdiSprayBottle,
  mdiMinusCircle,
  mdiBallotOutline,
  mdiTools,
mdiDoorClosed,
mdiDoorOpen,
} from '@mdi/js'
import { obtenerTodasHabitacion } from '@/services/habitacionService'

const showModal = ref(false)
const showModalSalidas = ref(false)
const totalHabitaciones = ref(0)
const habitacionesActivas = ref(0)
const habitacionesMantenimiento = ref(0)
const habitacionesOcupadas = ref(0)
const habitacionesOperacion = ref(0)
const habitacionesInactivas = ref(0)

const fetchHabitaciones = async () => {
  try {
    const habitaciones = await obtenerTodasHabitacion()
    totalHabitaciones.value = habitaciones.length
    habitacionesActivas.value = habitaciones.filter(h => h.estado === 'ACTIVO').length
    habitacionesMantenimiento.value = habitaciones.filter(h => h.estado === 'MANTENIMIENTO').length
    habitacionesOcupadas.value = habitaciones.filter(h => h.estado === 'OCUPADO').length
    habitacionesInactivas.value = habitaciones.filter(h => h.estado === 'INACTIVO').length
    habitacionesOperacion.value = habitaciones.filter(h => h.estado === 'OPERACION').length


  } catch (error) {
    console.error('Error al obtener habitaciones:', error)
  }
}

onMounted(() => {
  fetchHabitaciones()
})
</script>



<template>
    <LayoutAuthenticated>
      <SectionMain>
        <TitleIconOnly :icon="mdiBallotOutline" title="Estado de habitaciones" />
  
        <!-- Estadísticas de habitaciones -->
        <div class="grid grid-cols-1 gap-6 lg:grid-cols-3 mt-6">
          <CardBoxWidget
            :number="totalHabitaciones"
            label="Habitaciones totales"
            :icon="mdiBed"
            :cardColor="'bg-gray-800 dark:bg-gray-400'"
            :color="'text-gray-100 dark:text-gray-900'"
          />
          <CardBoxWidget
            :number="habitacionesActivas"
            label="Habitaciones disponibles"
            :icon="mdiDoorOpen"
            :cardColor="'bg-green-400 dark:bg-green-500'"
            :color="'text-gray-100 dark:text-gray-900'"
          />
          <CardBoxWidget
            :number="habitacionesMantenimiento"
            label="Habitaciones en limpieza"
            :icon="mdiSprayBottle"
            :cardColor="'bg-blue-400 dark:bg-blue-600'"
            :color="'text-gray-100 dark:text-gray-900'"
          />
          <CardBoxWidget
            :number="habitacionesOcupadas"
            label="Habitaciones ocupadas"
            :icon="mdiDoorClosed"
            :cardColor="'bg-yellow-400 dark:bg-yellow-600'"
            :color="'text-gray-100 dark:text-gray-900'"
          />
          <CardBoxWidget
            :number="habitacionesOperacion"
            label="Habitaciones en operación"
            :icon="mdiTools"
            :cardColor="'bg-orange-400 dark:bg-orange-600'"
            :color="'text-gray-100 dark:text-gray-900'"
          />
          <CardBoxWidget
            :number="habitacionesInactivas"
            label="Habitaciones inactivas"
            :icon="mdiMinusCircle"
            :cardColor="'bg-red-400 dark:bg-red-600'"
            :color="'text-gray-100 dark:text-gray-900'"
          />
        </div>
  
  
      <!-- Check-In / Check-Out -->
      <div class="grid grid-cols-1 gap-6 lg:grid-cols-1 mt-6">
        <CardBox class="shadow-lg bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-200 rounded-lg p-6 transition-all duration-300 ease-in-out">
          <h1 class="text-center font-medium text-xl mb-6">Check-In - Check-Out</h1>
          <div class="grid grid-cols-1 gap-4 lg:grid-cols-2">
            <button
              @click="showModal = true"
              class="bg-blue-600 hover:bg-blue-700 text-white h-12 rounded-lg font-bold transition duration-300 ease-in-out shadow-md transform hover:scale-105">
              Registrar Check-In
            </button>
            <button
              @click="showModalSalidas = true"
              class="bg-blue-600 hover:bg-blue-700  text-white h-12 rounded-lg font-bold transition duration-300 ease-in-out shadow-md transform hover:scale-105">
              Registrar Check-Out
            </button>
            <ModalRegistrarEntrada :visible="showModal" @close="showModal = false" />
            <ModalRegistrarSalida :visible="showModalSalidas" @close="showModalSalidas = false" />
          </div>
        </CardBox>
      </div>
    </SectionMain>
  </LayoutAuthenticated>
</template>