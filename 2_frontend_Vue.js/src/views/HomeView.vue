<script setup>
import { ref } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import CardBox from '@/components/CardBox.vue'
import ModalRegistrarEntrada from '@/components/ModalRegistrarEntrada.vue'
import ModalRegistrarSalida from '@/components/ModalRegistrarSalida.vue'
import CardBoxWidget from '@/components/CardBoxWidget.vue'
import {
  mdiBed,
  mdiCheckCircleOutline,
  mdiSprayBottle,
  mdiMinusCircle,
  mdiTools,
} from '@mdi/js'

const showModal = ref(false)
const showModalSalidas = ref(false)
</script>



<template>
  <LayoutAuthenticated>
    <sectionMain>
        <h1 class="font-bold">Estado Actual De las Habitaciones</h1>

        <div class="grid grid-cols-1 gap-12 lg:grid-cols-3 mb-6 mt-4">
          <CardBoxWidget
            :number="50"
            label="Habitaciones totales"
            :icon="mdiBed"
            :cardColor="'bg-blue-950'"
            :color="'text-white'"
          />
          <CardBoxWidget
            :number="24"
            label="Habitaciones disponibles"
            :icon="mdiCheckCircleOutline"
            :cardColor="'bg-green-400'"
            :color="'text-white'"
          />
          <CardBoxWidget
            :number="8"
            label="Habitaciones en limpieza"
            :icon="mdiSprayBottle"
            :cardColor="'bg-blue-600'"
            :color="'text-white'"
          />
          <CardBoxWidget
            :number="7"
            label="Habitaciones ocupadas"
            :icon="mdiMinusCircle"
            :cardColor="'bg-red-700'"
            :color="'text-white'"
          />
          <CardBoxWidget
            :number="2"
            label="Habitaciones en operación"
            :icon="mdiTools"
            :cardColor="'bg-orange-600'"
            :color="'text-white'"
          />
        </div>

        <h1 class="font-bold">Operadores de entradas y salidas</h1>
        <div class="grid grid-cols-1 gap-16 lg:grid-cols-2 mt-4">
          <CardBox :color="'bg-blue-600'" :rounded="'rounded-lg'">  
            <h1 class="text-center m-4 font-medium text-xl text-white">Registrar entradas y salidas de huéspedes</h1>
            <div class="grid grid-cols-1 gap-3 w-full lg:grid-cols-2">
              <button @click="showModal = true" class="bg-blue-950 h-12 rounded-lg my-6 font-bold hover:bg-blue-900 text-white">Registrar Entrada</button>
              <button @click="showModalSalidas = true" class="bg-blue-300 h-12 rounded-lg my-6 text-black font-bold border-2 border-blue-950 hover:bg-blue-100">Registrar Salida</button>

              <!-- Mostrar modal de registrar entrada -->
              <ModalRegistrarEntrada :visible="showModal" @close="showModal = false" />

              <!-- Modal para registrar salida -->
              <ModalRegistrarSalida :visible="showModalSalidas" @close="showModalSalidas = false"/>
            </div>
          </CardBox>
          <CardBox :color="'bg-blue-600'" :rounded="'rounded-lg'">  
            <h1 class="text-center m-4 font-medium text-xl text-white">Movimientos de pasajeros correspondientes</h1>
            <div class="grid grid-cols-1 gap-3 w-full lg:grid-cols-1">
              <button @click="showModal = true" class="bg-blue-950 h-12 rounded-lg m-6 font-bold hover:bg-blue-900 text-white">Registrar Entrada</button>
            </div>
          </CardBox>
        </div>
    </sectionMain>
  </LayoutAuthenticated>
</template>

