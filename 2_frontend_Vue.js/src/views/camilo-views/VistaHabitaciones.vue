<template>
  <LayoutAuthenticated>
    <div class="container mx-auto p-6">
      <h1 class="text-2xl font-bold mb-6">Lista de Habitaciones</h1>

      <!-- Contenedor para alinear el input y el botón -->
      <div class="flex items-center mb-4 space-x-4">
        <!-- Botón para crear una nueva habitación -->
        <button
          @click="mostrarModalCrear"
          class="bg-green-500 text-white px-4 py-2 rounded-md shadow-sm hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
        >
          Crear Habitación
        </button>
        <!-- Campo de búsqueda con placeholder -->
        <div class="w-full">
          <label for="numero_habitacion" class="block text-sm font-medium overflow-auto w-full">Buscar habitación</label>
          <input
            id="numero_habitacion"
            v-model="buscarHabitacion"
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


      <!-- Tabla de habitacion -->
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
            <tr v-for="habitaciones in habitacion" :key="habitaciones.id_habitacion">
              <td class="border-b-0 lg:w-6 before:hidden"></td>
              <td data-label="ID HABITACION">{{ habitaciones.id_habitacion }}</td>
              <td data-label="NUMERO HABITACION">{{ habitaciones.numero_habitacion }}</td>
              <td data-label="ESTADO">{{ habitaciones.estado }}</td>
              <td data-label="PISO">{{ habitaciones.piso }}</td>
              <td class="before:hidden lg:w-1 whitespace-nowrap">
                <BaseButtons  no-wrap>
                  <!-- Botón de Detalles (color amarillo) -->
                  <BaseButton
                    @click="verDetalles(habitaciones)"
                    :icon="mdiEye"
                    small
                    color="warning"
                  />

                  <!-- Botón de Editar (color verde con el ícono de editar) -->
                  <BaseButton
                    @click="editarHabitacion(habitaciones)"
                    :icon="mdiNoteEdit"
                    small
                    color="success"
                  />

                  <!-- Botón de Eliminar (color rojo) -->
                  <BaseButton
                    @click="confirmarEliminacion(habitaciones.id_habitacion)"
                    :icon="mdiTrashCan"
                    small
                    color="danger"
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
          <br>
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
import { ref, onMounted } from 'vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import RoomModal from '@/components/juanca_components/RoomModal.vue';
import RoomDetailsModal from '@/components/juanca_components/RoomDetailsModal.vue';
import CardBoxModal from '@/components/CardBoxModal.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import { mdiEye, mdiTrashCan,mdiNoteEdit } from '@mdi/js';
import { obtenerHabitacionesPaginadas, eliminarHabitacion} from '@/services/juanca_service/habitacionService';

const habitacion = ref([]);
const showModal = ref(false);
const buscarHabitacion = ref('');
const showDetailsModal = ref(false);
const showConfirmModal = ref(false);
const habitacionSeleccionada = ref({});
const habitacionDetalles = ref({});
const habitacionAEliminar = ref(null);
const totalPaginas = ref(0); // Cambiado a ref
const currentPage = ref(1); // Cambiado a ref

const obtenerHabitaciones = async (page = 1) => {
  try {
    const response = await obtenerHabitacionesPaginadas(page, 10);
    console.log("Respuesta de la API:", response); // Para ver la respuesta completa
    habitacion.value = response.habitacion; // Cambia aquí
    totalPaginas.value = response.total_paginas; // Cambia aquí
  } catch (error) {
    console.error("Error al obtener las habitacion:", error.message);
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
  // Llamar la función de API para guardar o actualizar habitación
  obtenerHabitaciones();
  cerrarModal();
};

const cerrarModal = () => {
  showModal.value = false;
  habitacionSeleccionada.value = {};
};

onMounted(() => {
  obtenerHabitaciones();
});
</script>
