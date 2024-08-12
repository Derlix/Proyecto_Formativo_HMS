<script setup>
import { computed, ref, onMounted } from 'vue'
import { useMainStore } from '@/stores/main'
import {
  mdiAccountMultiple,
  mdiCartOutline,
  mdiChartTimelineVariant,
  mdiMonitorCellphone,
  mdiReload,
  mdiBed,
  mdiCloseCircle,
  mdiSprayBottle,
  mdiTools,
  mdiMinusCircle,
  mdiBroom,
  mdiChartPie,
  mdiCheckCircleOutline,
  mdiAlertCircleOutline
} from '@mdi/js'
import * as chartConfig from '@/components/Charts/chart.config.js'
import LineChart from '@/components/Charts/LineChart.vue'
import SectionMain from '@/components/SectionMain.vue'
import CardBoxWidget from '@/components/CardBoxWidget.vue'
import CardBox from '@/components/CardBox.vue'
import TableSampleClients from '@/components/TableSampleClients.vue'
import NotificationBar from '@/components/NotificationBar.vue'
import BaseButton from '@/components/BaseButton.vue'
import CardBoxTransaction from '@/components/CardBoxTransaction.vue'
import CardBoxClient from '@/components/CardBoxClient.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import SectionBannerStarOnGitHub from '@/components/SectionBannerStarOnGitHub.vue'
import Modal from '@/components/Modal.vue'

const fillChartData = () => {
  chartData.value = chartConfig.sampleChartData()
}

onMounted(() => {
  fillChartData()
})

const mainStore = useMainStore()

const clientBarItems = computed(() => mainStore.clients.slice(0, 4))

const transactionBarItems = computed(() => mainStore.history)

const showModal = ref(false)

const chartData = ref(null)
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
          />
          <CardBoxWidget
            :number="24"
            label="Habitaciones disponibles"
            :icon="mdiCheckCircleOutline"
            :cardColor="'bg-green-400'"
          />
          <CardBoxWidget
            :number="8"
            label="Habitaciones en limpieza"
            :icon="mdiSprayBottle"
            :cardColor="'bg-blue-600'"
          />
          <CardBoxWidget
            :number="7"
            label="Habitaciones ocupadas"
            :icon="mdiMinusCircle"
            :cardColor="'bg-red-700'"
          />
          <CardBoxWidget
            :number="2"
            label="Habitaciones en operación"
            :icon="mdiTools"
            :cardColor="'bg-orange-600'"
          />
        </div>

        <h1 class="font-bold">Operadores de entradas y salidas</h1>
        <div class="grid grid-cols-1 gap-16 lg:grid-cols-2 mt-4">
          <CardBox :color="'bg-blue-600'" :rounded="'rounded-lg'">
            <h1 class="text-center m-4 font-medium text-xl">Registrar entradas y salidas de huéspedes</h1>
            <div class="grid grid-cols-1 gap-3 w-full lg:grid-cols-2">
              <button @click="showModal = true" class="bg-blue-950 h-12 rounded-lg my-6 font-bold hover:bg-blue-900 text-white">Registrar Entrada</button>
              <button @click="showModal = true" class="bg-blue-300 h-12 rounded-lg my-6 text-black font-bold border-2 border-blue-950 hover:bg-blue-100">Registrar Salida</button>

              <Modal :visible="showModal" @close="showModal = false" />
            </div>
          </CardBox>
          <CardBox :color="'bg-blue-600'" :rounded="'rounded-lg'">
            <h1 class="text-center m-4 font-medium text-xl">Movimientos de pasajeros correspondientes</h1>
            <div class="grid grid-cols-1 gap-3 w-full lg:grid-cols-1">
              <button @click="showModal = true" class="bg-blue-950 h-12 rounded-lg m-6 font-bold hover:bg-blue-900 text-white">Registrar Entrada</button>
            </div>
          </CardBox>
        </div>
    </sectionMain>
  </LayoutAuthenticated>
</template>
