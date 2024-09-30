<script setup>
import { ref, onMounted } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import CardBox from '@/components/CardBox.vue'
import ModalRegistrarEntrada from '@/components/ModalRegistrarEntrada.vue'
import ModalRegistrarSalida from '@/components/ModalRegistrarSalida.vue'
import CardBoxWidget from '@/components/CardBoxWidget.vue'
import SectionMain from '@/components/SectionMain.vue'
import TitleIconOnly from '@/components/TitleIconOnly.vue'
import SectionTitle from '@/components/SectionTitle.vue'
import {
  mdiBed,
  mdiCheckCircleOutline,
  mdiSprayBottle,
  mdiMinusCircle,
  mdiBallotOutline,
  mdiTools,
} from '@mdi/js'
import { obtenerTodasHabitacion } from '@/services/habitacionService'

const showModal = ref(false)
const showModalSalidas = ref(false)
const totalHabitaciones = ref(0)
const habitacionesActivas = ref(0)
const habitacionesMantenimiento = ref(0)
const habitacionesOcupadas = ref(0)
const habitacionesOperacion = ref(0)

const fetchHabitaciones = async () => {
  try {
    const habitaciones = await obtenerTodasHabitacion()
    totalHabitaciones.value = habitaciones.length
    habitacionesActivas.value = habitaciones.filter(h => h.estado === 'ACTIVO').length
    habitacionesMantenimiento.value = habitaciones.filter(h => h.estado === 'MANTENIMIENTO').length
    habitacionesOcupadas.value = habitaciones.filter(h => h.estado === 'INACTIVO').length
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
    <sectionMain>
      <TitleIconOnly :icon="mdiBallotOutline" title="Transpaso cuenta" />

        <div class="grid grid-cols-1 gap-6 lg:grid-cols-3 mt-6">
          <CardBoxWidget
            :number="totalHabitaciones"
            label="Habitaciones totales"
            :icon="mdiBed"
            :cardColor="'bg-blue-950'"
            :color="'text-white'"
          />
          <CardBoxWidget
            :number="habitacionesActivas"
            label="Habitaciones disponibles"
            :icon="mdiCheckCircleOutline"
            :cardColor="'bg-green-400'"
            :color="'text-white'"
          />
          <CardBoxWidget
            :number="habitacionesMantenimiento"
            label="Habitaciones en limpieza"
            :icon="mdiSprayBottle"
            :cardColor="'bg-sky-400'"
            :color="'text-white'"
          />
          <CardBoxWidget
            :number="habitacionesOcupadas"
            label="Habitaciones ocupadas"
            :icon="mdiMinusCircle"
            :cardColor="'bg-red-700'"
            :color="'text-white'"
          />
          <CardBoxWidget
            :number="habitacionesOperacion"
            label="Habitaciones en operación"
            :icon="mdiTools"
            :cardColor="'bg-orange-600'"
            :color="'text-white'"
          />
        </div>

        <SectionTitle first>Entradas y salidas</SectionTitle>

        <div class="grid grid-cols-1 gap-6 lg:grid-cols-2">
          <CardBox class="shadow-md">  
            <h1 class="text-center m-4 font-medium text-xl">Registrar entradas y salidas de huéspedes</h1>
            <div class="grid grid-cols-1 gap-3 w-full lg:grid-cols-2">
              <button @click="showModal = true" class="bg-blue-600 h-12 rounded-lg my-6 font-bold hover:bg-blue-900 text-white">Registrar Entrada</button>
              <button @click="showModalSalidas = true" class="bg-blue-600 h-12 text-white rounded-lg my-6 font-bold hover:bg-blue-900">Registrar Salida</button>

              <!-- Mostrar modal de registrar entrada -->
              <ModalRegistrarEntrada :visible="showModal" @close="showModal = false" />

              <!-- Modal para registrar salida -->
              <ModalRegistrarSalida :visible="showModalSalidas" @close="showModalSalidas = false"/>
            </div>

          </CardBox>
          <CardBox class="shadow-md">  
            <h1 class="text-center m-4 font-medium text-xl">Movimientos de pasajeros correspondientes</h1>
            <div class="grid grid-cols-1 gap-3 w-full lg:grid-cols-1">
              <button @click="showModal = true" class="bg-blue-500 h-12 rounded-lg m-6 font-bold hover:bg-blue-900 text-white">Registrar Entrada</button>
            </div>
          </CardBox>
        </div>
    </sectionMain>
  </LayoutAuthenticated>
</template>

