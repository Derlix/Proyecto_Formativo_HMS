<script setup>
import { computed, ref, onMounted } from 'vue'
import { useMainStore } from '@/stores/main'
import {
  mdiChartTimelineVariant,
} from '@mdi/js'
import * as chartConfig from '@/components/Charts/chart.config.js'
import SectionMain from '@/components/SectionMain.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'

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
      <SectionTitleLineWithButton :icon="mdiChartTimelineVariant" title="Historial de Reservas"></SectionTitleLineWithButton>
    </sectionMain>

    <sectionMain>

      <table class="table-auto w-full border-collapse border border-gray-300 dark:border-gray-600">
        <thead>
          <tr class="bg-gray-200 dark:bg-gray-800">
            <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">ID Reserva</th>
            <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Check In</th>
            <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Check Out</th>
            <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Huésped</th>
            <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Cédula</th>
            <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Total</th>
            <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Estado</th>
          </tr>
        </thead>
        <tbody>
          <tr class="bg-white dark:bg-gray-900">
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">565</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">2024-02-03</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">2024-02-06</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Adolfo Gomez</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">103242390</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">$50,000</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">
              <span
                class="inline-block px-3 py-1 text-xs font-semibold text-green-700 bg-green-200 rounded-full dark:text-green-100 dark:bg-green-600">
                Activo
              </span>
            </td>
          </tr>
          <tr class="bg-white dark:bg-gray-900">
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">205</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">2024-02-05</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">2024-02-09</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">Juan Gomez</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">1022000</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">$80,000</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">
              <span
                class="inline-block px-3 py-1 text-xs font-semibold text-green-700 bg-green-200 rounded-full dark:text-green-100 dark:bg-green-600">
                Activo
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </sectionMain>
  </LayoutAuthenticated>
</template>
