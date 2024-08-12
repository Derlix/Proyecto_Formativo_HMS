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
  mdiChartPie
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
    <sectionMain>
      <SectionTitleLineWithButton :icon="mdiChartTimelineVariant" title="Informe ama de llaves"></SectionTitleLineWithButton>
    </sectionMain>
    <SectionMain>
        <table class="table-auto w-full border-collapse border border-gray-300 dark:border-gray-600">
          <thead>
            <tr class="bg-gray-200 dark:bg-gray-800">
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">HABITACION</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2" colspan="2">INFORME AMA DE LLAVES</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2" colspan="2">RACK HABITACIONES</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">CAUSA</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">FECHA</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">HORA</th>
            </tr>
            <tr class="bg-gray-200 dark:bg-gray-800">
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2"></th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Clave</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Personas</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Situación</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Personas</th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2"></th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2"></th>
              <th class="border border-gray-300 dark:border-gray-600 px-4 py-2"></th>
            </tr>
          </thead>
          <tbody>
            <tr class="bg-white dark:bg-gray-900">
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">1010</td>
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">A1</td>
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">3</td>
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Ocupada</td>
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">3</td>
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Revisión</td>
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">10/08/2024</td>
              <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">14:30</td>
            </tr>
          </tbody>
        </table>
    </SectionMain>
  </LayoutAuthenticated>
</template>
