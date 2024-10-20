<template>
  <LayoutAuthenticated>
    <div class="caracteristicas-habitacion container mx-auto p-4">
      <h1 class="text-2xl font-semibold text-center mb-6">Gestión de Características</h1>

      <!-- Alerta de éxito -->
      <NotificationBar
        v-if="isAlertVisible"
        :color="colorAlert"
        :description="modalMessage"
        :visible="isAlertVisible"
      />

      <!-- Botón para abrir el modal de creación -->
      <div class="flex items-center mb-4 space-x-4 px-5">

        <button
          @click="mostrarModalCrear"
          class="bg-green-700 text-white px-4 py-2 rounded-md shadow-sm hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
        >
          Crear Característica
        </button>

        <router-link
          to="/habitaciones"
          class="bg-blue-700 text-white px-4 py-2 rounded-md shadow-sm hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
        >
          Volver
        </router-link>

      </div>



      <!-- Modal para crear una característica -->
      <CrearCaracteristica
        :visible="showModal"
        @close="cerrarModal"
        @save="handleCaracteristicaCreada"
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
        <p>¿Estás seguro de que deseas eliminar esta característica?</p>
      </CardBoxModal>

      <!-- Tabla de características -->
      <div v-if="caracteristicas.length" class="w-full overflow-auto mb-4">
        <table>
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Precio adicional</th>
              <th>Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in caracteristicas" :key="item.id_caracteristica">
              <td>{{ item.nombre_caracteristicas }}</td>
              <td>{{ item.adicional }}</td>
              <td>
                <BaseButtons no-wrap>
                  <BaseButton
                    @click="confirmarEliminacion(item.id_caracteristica)"
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
    </div>
  </LayoutAuthenticated>
</template>

<script>
import { onMounted, ref } from 'vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import CrearCaracteristica from '@/components/juanca_components/CrearCaracteristica.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import BaseButton from '@/components/BaseButton.vue';
import NotificationBar from '@/components/alejo_components/NotificationBar.vue';
import { obtenerTodasCaracteristicas, eliminarCaracteristica } from '@/services/juanca_service/caracteristicasService';
import { mdiTrashCan } from '@mdi/js';
import CardBoxModal from '@/components/CardBoxModal.vue';

export default {
  components: { LayoutAuthenticated, CrearCaracteristica, BaseButtons, BaseButton, NotificationBar, CardBoxModal },
  setup() {
    const caracteristicas = ref([]);
    const showModal = ref(false);
    const showConfirmModal = ref(false);
    const idCaracteristicaAEliminar = ref(null);
    const isAlertVisible = ref(false);
    const modalMessage = ref('');
    const colorAlert = ref('');

    const fetchCaracteristicas = async () => {
      try {
        const response = await obtenerTodasCaracteristicas();
        caracteristicas.value = response;
      } catch (error) {
        console.error('Error al obtener las características:', error);
      }
    };

    const confirmarEliminacion = (id) => {
      idCaracteristicaAEliminar.value = id; // Guarda el ID para usarlo al confirmar
      showConfirmModal.value = true; // Muestra el modal de confirmación
    };

    const eliminarHabitacionConfirmada = async () => {
      try {
        await eliminarCaracteristica(idCaracteristicaAEliminar.value);
        await fetchCaracteristicas(); // Recargar la lista después de eliminar
        mostrarAlerta('Característica eliminada con éxito.', 'success'); // Alerta de éxito
      } catch (error) {
        console.error('Error al eliminar la característica:', error);
        mostrarAlerta('Las características que están en uso no se pueden eliminar.', 'danger');
      } finally {
        showConfirmModal.value = false; // Cierra el modal de confirmación
      }
    };

    const mostrarModalCrear = () => {
      showModal.value = true;
    };

    const cerrarModal = () => {
      showModal.value = false;
    };

    const handleCaracteristicaCreada = async () => {
      await fetchCaracteristicas();
      mostrarAlerta('Característica creada con éxito.', 'success');
      cerrarModal();
    };

    const mostrarAlerta = (message, color) => {
      isAlertVisible.value = true;
      colorAlert.value = color;
      modalMessage.value = message;
      setTimeout(() => {
        isAlertVisible.value = false;
      }, 3000);
    };

    onMounted(fetchCaracteristicas);

    return {
      caracteristicas,
      showModal,
      showConfirmModal,
      fetchCaracteristicas,
      confirmarEliminacion,
      eliminarHabitacionConfirmada,
      mostrarModalCrear,
      cerrarModal,
      handleCaracteristicaCreada,
      isAlertVisible,
      modalMessage,
      colorAlert,
      mdiTrashCan
    };
  }
};
</script>
