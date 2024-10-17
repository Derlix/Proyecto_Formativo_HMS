<script setup>
import { ref, onMounted } from 'vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import AlertaCrearReserva from '@/components/miguel_compnents/AlertaCrearReserva.vue';
import ModalCambiarHabitacion from '@/components/alejo_components/ModalCambiarHabitacion.vue';
import ModalTarjetaReserva from '@/components/alejo_components/ModalTarjetaReserva.vue';
import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue';
import Calendario from '@/components/arias_components/Calendario.vue';
import { obtenerHabitacionesPaginadas } from '@/services/juanca_service/habitacionService.js';
import BaseButtons from '@/components/BaseButtons.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseLevel from '@/components/BaseLevel.vue';

const showModalCambiarHabitacion = ref(false);
const showModalCrearReserva = ref(false);
const showModalTarjetaReserva = ref(false);
const habitaciones = ref([]);
const activarModalCaracteristicas = ref(false);
const habitacionSeleccionada = ref(null);
const TotalPages = ref(0);
const currentPage = ref(1);

const fetchReservas = async () => {
  try {
    const response = await obtenerHabitacionesPaginadas(currentPage.value);
    habitaciones.value = response.data.habitacion;
    TotalPages.value = response.data.total_paginas;

    if (currentPage.value > TotalPages.value) {
        currentPage.value = TotalPages.value;
    }
  } catch (error) {
    alert("Error al cargar las habitaciones")
    console.error('Error al cargar las habitaciones:', error);
  }
};

const calcularPrecioTotal = (habitacion) => {
  let precioTotal = habitacion.categoria?.precio_fijo || 0;

  if (habitacion.caracteristicas?.length > 0) {
    habitacion.caracteristicas.forEach((caracteristica) => {
      precioTotal += caracteristica.adicional || 0;
    });
  }

  return new Intl.NumberFormat('es-CO', {
    style: 'currency',
    currency: 'COP',
    minimumFractionDigits: 0,
  }).format(precioTotal);
};

const verCaracteristicas = (habitacion) => {
  habitacionSeleccionada.value = habitacion;
  activarModalCaracteristicas.value = true;
};

onMounted(() => {
  fetchReservas();
});
</script>

<template>
  <LayoutAuthenticated>
    <div class="px-3 py-4">
      <h2 class="text-xl font-bold text-gray-900 dark:text-gray-100">Operador De Reservas</h2>
      <div class="flex justify-center space-x-4 py-4">
        <button @click="showModalCrearReserva = true" class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition duration-300 ease-in-out py-2 px-6 shadow-lg transform hover:scale-105">
          Crear reserva
        </button>

        
        <AlertaCrearReserva :mostrarModal="showModalCrearReserva" @cerrar="showModalCrearReserva = false" />
        <button @click="showModalCambiarHabitacion = true" class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition duration-300 ease-in-out py-2 px-6 shadow-lg transform hover:scale-105">
          Cambiar habitación
        </button>

        <ModalCambiarHabitacion :isVisible="showModalCambiarHabitacion" @close="showModalCambiarHabitacion = false" />
        <button class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition duration-300 ease-in-out py-2 px-6 shadow-lg transform hover:scale-105">
          Cambiar reserva
        </button>
        

        <button @click="showModalTarjetaReserva = true" class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition duration-300 ease-in-out py-2 px-6 shadow-lg transform hover:scale-105">
          Tarjeta Reserva
        </button>
        <ModalTarjetaReserva :isVisible="showModalTarjetaReserva" @close="showModalTarjetaReserva = false" />
      </div>

      <Calendario />

      <div class="overflow-x-auto">
        <h2 class="text-xl font-bold text-gray-900 dark:text-gray-100 px-2 py-4">Información de habitaciones</h2>
        <table class="table-auto w-full border-collapse text-left">
          <thead class="bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-100">
            <tr>
              <th class="px-4 py-2">Habitación</th>
              <th class="px-4 py-2">Características</th>
              <th class="px-4 py-2">Piso</th>
              <th class="px-4 py-2">Estado</th>
              <th class="px-4 py-2">Precio</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="habitacion in habitaciones" :key="habitacion.id_habitacion" class="bg-white dark:bg-gray-800 border-b dark:border-gray-700">
              <td class="px-4 py-2">{{ habitacion.numero_habitacion }}</td>
              <td class="px-4 py-2">
                <button @click="verCaracteristicas(habitacion)" class="bg-blue-500 text-white px-2 py-1 rounded hover:bg-blue-600 transition">
                  Ver características
                </button>
              </td>
              <td class="px-4 py-2">{{ habitacion.piso }}</td>
              <td class="px-4 py-2">
                <span
                  class="inline-block px-3 py-1 text-xs font-semibold rounded-full"
                  :class="{
                    'bg-green-100 text-green-700 dark:bg-green-800 dark:text-green-100': habitacion.estado === 'ACTIVO',
                    'bg-yellow-100 text-yellow-700 dark:bg-yellow-800 dark:text-yellow-100': habitacion.estado === 'MANTENIMIENTO',
                    'bg-blue-100 text-blue-700 dark:bg-blue-800 dark:text-yellow-100': habitacion.estado === 'OCUPADO',
                    'bg-yellow-200 text-yellow-700 dark:bg-yellow-300 dark:text-black': habitacion.estado === 'OPERACION',
                    'bg-red-100 text-red-700 dark:bg-red-800 dark:text-red-100': habitacion.estado === 'INACTIVO'}">
                  {{ habitacion.estado }}
                </span>
              </td>

              <td class="px-4 py-2">{{ calcularPrecioTotal(habitacion) }}</td>
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
                small @click="() => { currentPage = page; fetchReservas(); }"/>
            </BaseButtons>
            <small>Página {{ currentPage }} de {{ TotalPages }}</small>
        </BaseLevel>
    </div>

      <CardBoxModal v-model="activarModalCaracteristicas" title="Características de la habitación" has-cancel :showPrimaryButton="false" @cancel="activarModalCaracteristicas = false">
        <ul v-if="habitacionSeleccionada?.caracteristicas">
          <li v-for="caracteristica in habitacionSeleccionada.caracteristicas" :key="caracteristica.id_caracteristica">
            {{ caracteristica.nombre_caracteristicas }} (Adicional: {{ caracteristica.adicional }})
          </li>
        </ul>
      </CardBoxModal>

    </div>
  </LayoutAuthenticated>
</template>
