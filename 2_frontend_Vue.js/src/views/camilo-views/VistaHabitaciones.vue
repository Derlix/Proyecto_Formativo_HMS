<template>
  <LayoutAuthenticated>
    <div class="container mx-auto p-6">
      <h1 class="text-2xl font-bold mb-6">Lista de Habitaciones</h1>

      <!-- Contenedor para alinear el input y el botón -->
      <div class="flex items-center mb-4 space-x-4">
        <!-- Botón para crear una nueva habitación -->
        <button
          @click="mostrarModalCrear"
          class="bg-green-700 text-white px-4 py-2 rounded-md shadow-sm hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
        >
          Crear Habitación
        </button>
        <!-- Campo de búsqueda con placeholder -->
        <div class="w-full">
          <label for="numero_habitacion" class="block text-sm font-medium overflow-auto w-full">Buscar habitación</label>
          <input
            id="numero_habitacion"
            v-model="buscarHabitacion"
            @input="buscarHabitacionPorNumero"
            type="text"
            placeholder="Ingrese el número de habitación"
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          />
        </div>
      </div>

      <!-- Modal para crear/editar una habitación -->
      <RoomModal
        :visible="showModal"
        :habitacion="habitacionSeleccionada"
        @close="cerrarModal"
        @save="guardarHabitacion"
      />

      <!-- Modal para mostrar detalles de la habitación -->
      <RoomDetailsModal
        :visible="showDetailsModal"
        :habitacion="habitacionDetalles"
        @close="showDetailsModal = false"
      />

      <!-- Modal para confirmar eliminación -->
      <CardBoxModal
        :modelValue="showConfirmModal"
        title="Confirmar Eliminación"
        button-label="Eliminar"
        hasCancel
        @confirm="eliminarHabitacionConfirmada"
        @cancel="showConfirmModal = false"
      >
        <p>¿Estás seguro de que deseas eliminar esta habitación?</p>
      </CardBoxModal>

      <!-- Modal para asignar características -->
      <AsignarCaracteristicasModal
        :visible="showCaracteristicasModal"
        :habitacion="habitacionSeleccionada"
        @close="showCaracteristicasModal = false"
        @asignacionExitosa="handleAsignacionExitosa"
      />


      <!-- Tabla de habitaciones -->
      <div class="w-full overflow-auto mb-4">
        <table>
          <thead>
            <tr>
              <th />
              <th>ID</th>
              <th>Núm Habitación</th>
              <th>Estado</th>
              <th>Piso</th>
              <th>Acciones</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr v-for="habitacion in habitacionesFiltradas" :key="habitacion.id_habitacion">
              <td class="border-b-0 lg:w-6 before:hidden"></td>
              <td data-label="ID HABITACION">{{ habitacion.id_habitacion }}</td>
              <td data-label="NUMERO HABITACION">{{ habitacion.numero_habitacion }}</td>
              <td data-label="ESTADO">{{ habitacion.estado }}</td>
              <td data-label="PISO">{{ habitacion.piso }}</td>
              <td class="before:hidden lg:w-1 whitespace-nowrap">
                <BaseButtons no-wrap>
                  <!-- Botón de Detalles -->
                  <BaseButton
                    @click="verDetalles(habitacion)"
                    :icon="mdiEye"
                    small
                    color="warning"
                  />
                  <!-- Botón de Editar -->
                  <BaseButton
                    @click="editarHabitacion(habitacion)"
                    :icon="mdiNoteEdit"
                    small
                    color="success"
                  />
                  <!-- Botón de Eliminar -->
                  <BaseButton
                    @click="confirmarEliminacion(habitacion.id_habitacion)"
                    :icon="mdiTrashCan"
                    small
                    color="danger"
                  />
                  <!-- Botón de Asignar Características -->
                  <BaseButton
                    @click="AsignarCaracteristicas(habitacion)"
                    :icon="mdiPlus"
                    small
                    color="primary"
                  />
                </BaseButtons>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800 relative" style="overflow-x: auto; white-space: nowrap;">
        <BaseLevel>
          <small>Página {{ currentPage }} de {{ totalPaginas }}</small>
          <br />
          <BaseButtons style="display: inline-flex; overflow-x: auto; flex-wrap: nowrap;">
            <BaseButton
              v-for="page in totalPaginas"
              :key="page"
              :active="page === currentPage"
              :label="page"
              :color="page === currentPage ? 'lightDark' : 'whiteDark'"
              small
              @click="currentPage = page; obtenerHabitaciones(currentPage)"
            />
          </BaseButtons>
        </BaseLevel>
      </div>
    </div>
  </LayoutAuthenticated>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import RoomModal from '@/components/juanca_components/RoomModal.vue';
import RoomDetailsModal from '@/components/juanca_components/RoomDetailsModal.vue';
import CardBoxModal from '@/components/CardBoxModal.vue';
import AsignarCaracteristicasModal from '@/components/juanca_components/AsignarCaracteristicasModal.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import { mdiEye, mdiTrashCan, mdiNoteEdit, mdiPlus } from '@mdi/js';
import { obtenerHabitacionesPaginadas, eliminarHabitacion, obtenerHabitacionPorNumero } from '@/services/juanca_service/habitacionService';

const habitacion = ref([]);
const showModal = ref(false);
const buscarHabitacion = ref('');
const showDetailsModal = ref(false);
const showConfirmModal = ref(false);
const showCaracteristicasModal = ref(false);
const habitacionSeleccionada = ref({});
const habitacionDetalles = ref({});
const habitacionAEliminar = ref(null);
const totalPaginas = ref(0);
const currentPage = ref(1);

const habitacionesFiltradas = computed(() => {
  return habitacion.value.filter(h =>
    h.numero_habitacion.toString().includes(buscarHabitacion.value)
  );
});

const obtenerHabitaciones = async (page = 1) => {
  try {
    const response = await obtenerHabitacionesPaginadas(page, 10);
    habitacion.value = response.habitacion;
    totalPaginas.value = response.total_paginas;
  } catch (error) {
    console.error("Error al obtener las habitaciones:", error.message);
  }
};

const buscarHabitacionPorNumero = async () => {
  const numeroHabitacion = buscarHabitacion.value.trim();

  if (numeroHabitacion) {
    try {
      const response = await obtenerHabitacionPorNumero(numeroHabitacion);
      if (response && response.habitacion && response.habitacion.length > 0) {
        habitacion.value = [response.habitacion[0]];
        currentPage.value = 1;
        obtenerHabitaciones(1);
      } else {
        habitacion.value = [];
      }
    } catch (error) {
      console.error('Error al obtener la habitación:', error.message);
      habitacion.value = [];
    }
  } else {
    obtenerHabitaciones();
  }
};

const verDetalles = (habitacion) => {
  habitacionDetalles.value = habitacion;
  showDetailsModal.value = true;
};

const eliminarHabitacionConfirmada = async () => {
  try {
    await eliminarHabitacion(habitacionAEliminar.value);
    showConfirmModal.value = false;
    habitacionAEliminar.value = null;
    obtenerHabitaciones();
  } catch (error) {
    console.error("Error al eliminar la habitación:", error.message);
  }
};

const confirmarEliminacion = (id_habitacion) => {
  habitacionAEliminar.value = id_habitacion;
  showConfirmModal.value = true;
};

const editarHabitacion = (habitacion) => {
  habitacionSeleccionada.value = habitacion;
  showModal.value = true;
};

const mostrarModalCrear = () => {
  habitacionSeleccionada.value = {
    id_habitacion: null,
    numero_habitacion: '',
    piso: '',
    id_categoria_habitacion: '',
    estado: '',
    precio_actual: '',
    caracteristicas: {},
  };
  showModal.value = true;
};

const guardarHabitacion = () => {
  obtenerHabitaciones();
  cerrarModal();
};

const cerrarModal = () => {
  showModal.value = false;
  habitacionSeleccionada.value = {};
};

const AsignarCaracteristicas = (habitacion) => {
  habitacionSeleccionada.value = habitacion;
  showCaracteristicasModal.value = true;
};

const handleAsignacionExitosa = async () => {
  alert('Características asignadas exitosamente.');
  showCaracteristicasModal.value = false;
  await obtenerHabitaciones();
};

onMounted(() => {
  obtenerHabitaciones(currentPage.value);
});
</script>
