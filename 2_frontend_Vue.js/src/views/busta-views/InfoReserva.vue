<script setup>
import { computed, ref, onMounted } from 'vue'
import { useMainStore } from '@/stores/main'
import {
  mdiAccountMultiple,
  mdiCartOutline,
  mdiChartTimelineVariant,
  mdiMonitorCellphone,
  mdiReload,
  mdiGithub,
  mdiInformation,
  mdiChartPie,
  mdiCircle
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
import BaseIcon from '@/components/BaseIcon.vue'

const chartData = ref(null)

const fillChartData = () => {
  chartData.value = chartConfig.sampleChartData()
}

onMounted(() => {
  fillChartData()
})

const mainStore = useMainStore()

const clientBarItems = computed(() => mainStore.clients.slice(0, 4))

const transactionBarItems = computed(() => mainStore.history)
</script>

<template>
  <LayoutAuthenticated>
    <div>
      <div class="flex justify-end items-center space-x-2 px-4">
        <button class="bg-[#1B324F] hover:bg-[#315889] text-white font-bold py-2 px-4 rounded">
          Factura temporal
        </button>
        <button class="bg-[#1B324F] hover:bg-[#315889] text-white font-bold py-2 px-4 rounded">
          Crear Check out
        </button>
        <div class="text-green-500 font-bold py-2 px-4 rounded">
          Completada con éxito <BaseIcon :path="mdiCircle" />
        </div>
      </div>
    </div>
    <div class="px-4">
      <h3 class="text-xl font-bold">Reserva N°: <span>04487</span></h3>

      <!-- Información de Huésped -->
      <h2 class="py-3">Información de Huésped</h2>
      <div class="mt-3">
        <table class="table-auto w-full border-collapse border border-gray-300 dark:border-gray-600">
          <thead>
            <tr class="bg-gray-200 dark:bg-gray-800">
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Reservado por</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Email</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Teléfono</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Ocupación</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Observaciones</th>
            </tr>
          </thead>
          <tbody>
            <tr class="bg-white dark:bg-gray-900">
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Juan Pérez</td>
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">juan.perez@example.com</td>
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">123-456-7890</td>
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Ingeniero</td>
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Sin observaciones</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Información de Reserva -->
      <div class="mt-3">
        <div class="">
          <h2 class="mb-4">Información de Reserva</h2>
          <table class="table-auto w-full border-collapse border border-gray-300 dark:border-gray-600">
            <thead>
              <tr class="bg-gray-200 dark:bg-gray-800">
                <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Tipo de Habitación</th>
                <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Habitación</th>
                <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Cantidad de Personas</th>
                <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Cambio de Reserva</th>
                <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Comprobante de Reserva</th>
              </tr>
            </thead>
            <tbody>
              <tr class="bg-white dark:bg-gray-900">
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Sencilla</td>
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">1010</td>
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">3</td>
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Sin cambios</td>
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">No registrado</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Información de Check-in y Check-out -->
      <div class="mt-3">
        <div class="">
          <h2 class="mb-4">Información de Check-in y Check-out</h2>
          <table class="table-auto w-full border-collapse border border-gray-300 dark:border-gray-600 mb-6">
            <thead>
              <tr class="bg-gray-200 dark:bg-gray-800">
                <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Llegada</th>
                <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Salida</th>
              </tr>
            </thead>
            <tbody>
              <tr class="bg-white dark:bg-gray-900">
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">25/10/2194</td>
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">25/11/2194</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Información de Dinero -->
      <div class="mt-3 mb-3">
        <div class="">
          <h2 class="mb-4">Información de Dinero</h2>
          <table class="table-auto w-full border-collapse border border-gray-300 dark:border-gray-600">
            <thead>
              <tr class="bg-gray-200 dark:bg-gray-800">
                <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Tipo</th>
                <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Monto</th>
                <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Medio de Pago</th>
              </tr>
            </thead>
            <tbody>
              <tr class="bg-white dark:bg-gray-900">
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Adelanto</td>
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">$3000</td>
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Efectivo</td>
              </tr>
              <tr class="bg-white dark:bg-gray-900">
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Pago Total</td>
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">$10000</td>
                <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Tarjeta de Crédito</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </LayoutAuthenticated>
</template>
