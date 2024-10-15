<script setup>
import { ref, onMounted} from 'vue';
import { getAllHistorialReservas, getHistorialReservasByPage} from '@/services/busta_service/HistorialReservasService';
import { getHuespedByDocument } from '@/services/huespedService';
import NotificationBar from '@/components/alejo_components/NotificationBar.vue'; 
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import { mdiChartTimelineVariant } from '@mdi/js';
import BaseLevel from '@/components/BaseLevel.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import BaseButton from '@/components/BaseButton.vue';
const reservas = ref([]);
const isHuespedModalVisible = ref(false);
const selectedHuesped = ref(null);
const TotalPages = ref(0);
const currentPage = ref(1);
const modalMessage = ref('');
const isAlertVisible = ref(false);
const colorAlert = ref('');

// const fetchReservas = async () => {
//   try {
//     const data = await getAllHistorialReservas();
//     reservas.value = data.reverse(); // Invertir el orden para mostrar del último al primero
//   } catch (error) {
//     console.error('Error al obtener el historial de reservas:', error);
//     alert('Ocurrió un error al obtener el historial de reservas.');
//   }
// };

const fetchPageReservas = async () => {
  try {
    const response = await getHistorialReservasByPage(currentPage.value);
    TotalPages.value = response.data.total_paginas;
    reservas.value = response.data.reservas; // Invertir el orden para mostrar del último al primero
    
  } catch (error) {
    console.error('Error al obtener el historial de reservas:', error);
    showAlert('Ocurrió un error al obtener el historial de reservas.', 'danger');

  }
};

const showAlert = (message, color) => {
  modalMessage.value = message;
  colorAlert.value = color;
  isAlertVisible.value = true;
  setTimeout(() => {
    isAlertVisible.value = false;
  }, 3000);
};

const openHuespedModal = async (numero_documento) => {
  try {
    const data = await getHuespedByDocument(numero_documento);
    selectedHuesped.value = data.data; // Asegúrate de que esto sea correcto según la respuesta de la API
    isHuespedModalVisible.value = true;
  } catch (error) {
    console.error('Error al obtener el huésped:', error);
    
    showAlert('Ocurrió un error al obtener los datos del huésped', 'danger');
  }
};



onMounted(() => {
  fetchPageReservas();
});
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <TitleIconOnly :icon="mdiChartTimelineVariant" title="Historial de reservas" />
    </SectionMain>

    <SectionMain>
      <NotificationBar
    v-if="isAlertVisible"
    :color="colorAlert"
    :description="modalMessage"
    :visible="isModalVisible"
  />
      <table class="">
        <thead>
          <tr class="">
            <th class="">ID Reserva</th>
            <th class="">Check In</th>
            <th class="">Check Out</th>
            <th class="">Huésped</th>
            <th class="">Cédula</th>
            <th class="">Total</th>
            <th class="">Estado</th>
            <th class="">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="reserva in reservas" :key="reserva.id_reserva" class="">
            <td>{{ reserva.id_reserva }}</td>
            <td>{{ reserva.fecha_reserva }}</td>
            <td>{{ reserva.fecha_reserva }}</td>
            <td>{{ reserva.huesped.nombre_completo }}</td>
            <td>{{ reserva.huesped.numero_documento }}</td>
            <td>{{ reserva.valor_deposito }}</td>
            <td>
              <span :class="{
                'inline-block px-3 py-1 text-xs font-semibold text-green-700 bg-green-200 rounded-full dark:text-green-100 dark:bg-green-600': reserva.estado_reserva === 'ACTIVO',
                'inline-block px-3 py-1 text-xs font-semibold text-red-700 bg-red-200 rounded-full dark:text-red-100 dark:bg-red-600': reserva.estado_reserva !== 'ACTIVO'
              }">
                {{ reserva.estado_reserva }}
              </span>
            </td>
            <td class="">
              <button @click="openHuespedModal(reserva.huesped.numero_documento)" class="bg-blue-500 text-white px-2 py-1 rounded">Ver Huésped</button>
            </td>
          </tr>
        </tbody>
      </table>
      
      <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800">
    <BaseLevel>
      <BaseButtons>
        <BaseButton
          v-for="page in TotalPages"
          :key="page"
          :active="page === currentPage"
          :label="page"
          :color="page === currentPage ? 'lightDark' : 'whiteDark'"
          small
          @click="currentPage = page; fetchPageReservas()"
        />
      </BaseButtons>
      <small>Página {{ currentPage }} de {{ TotalPages }}</small>
    </BaseLevel>
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
