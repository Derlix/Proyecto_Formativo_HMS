<script setup>
import { ref, onMounted } from 'vue';
import { getAllHistorialReservas } from '@/services/busta_service/HistorialReservasService'; // Importar el servicio

import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue';
import { mdiChartTimelineVariant } from '@mdi/js';

const reservas = ref([]); // Variable para almacenar las reservas

const fetchReservas = async () => {
  try {
    const data = await getAllHistorialReservas(); // Llamar al servicio para obtener los datos
    reservas.value = data; // Guardar los datos en la variable
  } catch (error) {
    console.error('Error al obtener el historial de reservas:', error);
    alert('Ocurrió un error al obtener el historial de reservas.');
  }
};

onMounted(() => {
  fetchReservas(); // Llamar a fetchReservas cuando se monte el componente
});
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiChartTimelineVariant" title="Historial de Reservas" />
    </SectionMain>

    <SectionMain>
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
          <tr v-for="reserva in reservas" :key="reserva.id_reserva" class="bg-white dark:bg-gray-900">
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.id_reserva }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.fecha_reserva }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.fecha_reserva }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.huesped.nombre_completo }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.huesped.numero_documento }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.valor_deposito }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">
              <span
                :class="{
                  'inline-block px-3 py-1 text-xs font-semibold text-green-700 bg-green-200 rounded-full dark:text-green-100 dark:bg-green-600': reserva.estado_reserva === 'ACTIVO',
                  'inline-block px-3 py-1 text-xs font-semibold text-red-700 bg-red-200 rounded-full dark:text-red-100 dark:bg-red-600': reserva.estado_reserva !== 'ACTIVO'
                }"
              >
                {{ reserva.estado_reserva }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </SectionMain>
  </LayoutAuthenticated>
</template>
