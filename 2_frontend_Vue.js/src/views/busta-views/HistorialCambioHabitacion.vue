<script setup>
import { ref, onMounted } from 'vue';
import { getHistorialCambioHabitacionesByPage } from '@/services/busta_service/HistorialCambioHabitacion';
import NotificationBar from '@/components/alejo_components/NotificationBar.vue'; 
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import { mdiChartTimelineVariant } from '@mdi/js';
import BaseLevel from '@/components/BaseLevel.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import BaseButton from '@/components/BaseButton.vue';

const historialCambioHabitaciones = ref([]); // Cambiar a historialCambioHabitaciones
const TotalPages = ref(0);
const currentPage = ref(1);
const modalMessage = ref('');
const isAlertVisible = ref(false);
const colorAlert = ref('');
    
const fetchPageHistorialCambioHabitacion = async () => {
  try {
    const response = await getHistorialCambioHabitacionesByPage(currentPage.value);
    TotalPages.value = response.data.total_paginas;
    historialCambioHabitaciones.value = response.data.historial_cambio_habitaciones; // Actualizado
  } catch (error) {
    console.error('Error al obtener el historial de cambio de habitaciones:', error);
    showAlert('Ocurrió un error al obtener el historial de cambio de habitaciones.', 'danger');
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

onMounted(() => {
  fetchPageHistorialCambioHabitacion();
});
</script>


<template>
    <LayoutAuthenticated>
      <SectionMain>
        <TitleIconOnly :icon="mdiChartTimelineVariant" title="Historial de cambio de habitaciones" />
      </SectionMain>
  
      <SectionMain>
        <NotificationBar
          v-if="isAlertVisible"
          :color="colorAlert"
          :description="modalMessage"
          :visible="isAlertVisible"
        />
        <div class="max-h-96 overflow-y-auto ">
            <table class="min-w-full table-auto">
              <thead>
                <tr>
                  <th class="px-4 py-2">ID Historial</th>
                  <th class="px-4 py-2">Fecha Cambio</th>
                  <th class="px-4 py-2">Huésped</th>
                  <th class="px-4 py-2">Documento</th>
                  <th class="px-4 py-2">Correo</th>
                  <th class="px-4 py-2">Motivo cambio</th>
                  <th class="px-4 py-2">Habitación Anterior</th>
                  <th class="px-4 py-2">Habitación Nueva</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="historial in historialCambioHabitaciones" :key="historial.id_historial">
                  <td class="border px-4 py-2">{{ historial.id_historial }}</td>
                  <td class="border px-4 py-2">{{ historial.fecha_cambio }}</td>
                  <td class="border px-4 py-2">{{ historial.huesped.nombre_completo }}</td>
                  <td class="border px-4 py-2">{{ historial.huesped.numero_documento }}</td>
                  <td class="border px-4 py-2">{{ historial.huesped.email }}</td>
                  <td class="border px-4 py-2">{{ historial.motivo_cambio }}</td>
                  <td class="border px-4 py-2">{{ historial.habitacion_anterior }} ({{ historial.tipo_habitacion_anterior }})</td>
                  <td class="border px-4 py-2">{{ historial.habitacion_nueva }} ({{ historial.tipo_habitacion_nueva }})</td>
                </tr>
              </tbody>
            </table>
        </div>
  
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
                @click="currentPage = page; fetchPageHistorialCambioHabitacion()"
              />
            </BaseButtons>
            <small>Página {{ currentPage }} de {{ TotalPages }}</small>
          </BaseLevel>
        </div>
      </SectionMain>
    </LayoutAuthenticated>
  </template>
  