<script setup>
import { ref, onMounted, computed } from 'vue';
import { getAllHistorialReservas } from '@/services/busta_service/HistorialReservasService';
import { getHuespedByDocument } from '@/services/huespedService';
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import { mdiChartTimelineVariant } from '@mdi/js';

const reservas = ref([]);
const isHuespedModalVisible = ref(false);
const selectedHuesped = ref(null);
const currentPage = ref(1);
const itemsPerPage = ref(5); // Número de reservas por página

const fetchReservas = async () => {
  try {
    const data = await getAllHistorialReservas();
    reservas.value = data.reverse(); // Invertir el orden para mostrar del último al primero
  } catch (error) {
    console.error('Error al obtener el historial de reservas:', error);
    alert('Ocurrió un error al obtener el historial de reservas.');
  }
};

const openHuespedModal = async (numero_documento) => {
  try {
    const data = await getHuespedByDocument(numero_documento);
    selectedHuesped.value = data.data; // Asegúrate de que esto sea correcto según la respuesta de la API
    isHuespedModalVisible.value = true;
  } catch (error) {
    console.error('Error al obtener el huésped:', error);
    alert('Ocurrió un error al obtener los datos del huésped.');
  }
};

const totalPages = computed(() => {
  return Math.ceil(reservas.value.length / itemsPerPage.value);
});

const paginatedReservas = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return reservas.value.slice(start, end);
});

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

onMounted(() => {
  fetchReservas();
});
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <TitleIconOnly :icon="mdiChartTimelineVariant" title="Historial de reservas" />
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
            <th class="border border-gray-300 dark:border-gray-600 px-4 py-2">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="reserva in paginatedReservas" :key="reserva.id_reserva" class="bg-white dark:bg-gray-900">
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.id_reserva }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.fecha_reserva }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.fecha_reserva }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.huesped.nombre_completo }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.huesped.numero_documento }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">{{ reserva.valor_deposito }}</td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">
              <span :class="{
                'inline-block px-3 py-1 text-xs font-semibold text-green-700 bg-green-200 rounded-full dark:text-green-100 dark:bg-green-600': reserva.estado_reserva === 'ACTIVO',
                'inline-block px-3 py-1 text-xs font-semibold text-red-700 bg-red-200 rounded-full dark:text-red-100 dark:bg-red-600': reserva.estado_reserva !== 'ACTIVO'
              }">
                {{ reserva.estado_reserva }}
              </span>
            </td>
            <td class="border border-gray-300 dark:border-gray-600 px-4 py-2">
              <button @click="openHuespedModal(reserva.huesped.numero_documento)" class="bg-blue-500 text-white px-2 py-1 rounded">Ver Huésped</button>
            </td>
          </tr>
        </tbody>
      </table>
      
      <div class="flex justify-between mt-4">
        <button @click="prevPage" :disabled="currentPage === 1" class="bg-gray-300 text-gray-700 px-4 py-2 rounded">Anterior</button>
        <span>Página {{ currentPage }} de {{ totalPages }}</span>
        <button @click="nextPage" :disabled="currentPage === totalPages" class="bg-gray-300 text-gray-700 px-4 py-2 rounded">Siguiente</button>
      </div>
    </SectionMain>

    <!-- Modal para mostrar información del huésped -->
    <div v-if="isHuespedModalVisible" class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-4 w-11/12 max-w-lg">
        <h2 class="text-xl font-bold mb-4">Detalles del Huésped</h2>
        <div v-if="selectedHuesped">
          <p><strong>Nombre Completo:</strong> {{ selectedHuesped.nombre_completo }}</p>
          <p><strong>Tipo de Documento:</strong> {{ selectedHuesped.tipo_documento }}</p>
          <p><strong>Número de Documento:</strong> {{ selectedHuesped.numero_documento }}</p>
          <p><strong>Fecha de Expedición:</strong> {{ selectedHuesped.fecha_expedicion }}</p>
          <p><strong>Email:</strong> {{ selectedHuesped.email }}</p>
          <p><strong>Teléfono:</strong> {{ selectedHuesped.telefono }}</p>
          <p><strong>Ocupación:</strong> {{ selectedHuesped.ocupacion }}</p>
          <p><strong>Dirección:</strong> {{ selectedHuesped.direccion }}</p>
        </div>
        <button @click="isHuespedModalVisible = false" class="mt-4 bg-blue-500 text-white px-4 py-2 rounded">Cerrar</button>
      </div>
    </div>
  </LayoutAuthenticated>
</template>
