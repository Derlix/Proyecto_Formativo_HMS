<template>
  <LayoutAuthenticated>
    <div class="caracteristicas-habitacion container mx-auto p-4">
      <h1 class="text-2xl font-semibold text-center mb-6 text-black">Gestión de Características</h1>

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

      <!-- Modal para crear/editar una característica -->
      <CrearCaracteristica
        :visible="showModal"
        :categoria="caracteristicaSeleccionada"
        @close="cerrarModal"
        @save="guardarCaracteristica"
        @characteristicCreated="mostrarAlerta('Característica creada exitosamente', 'success')"
        @characteristicUpdated="mostrarAlerta('Característica editada con éxito', 'success')"
      />

      <!-- Modal para confirmar eliminación -->
      <CardBoxModal
        :modelValue="showConfirmModal"
        title="Confirmar Eliminación"
        button-label="Eliminar"
        hasCancel
        @confirm="eliminarCaracteristicaService"
        @cancel="showConfirmModal = false"
      >
        <p>¿Estás seguro de que deseas eliminar esta característica?</p>
      </CardBoxModal>

      <!-- Tabla de características -->
      <div v-if="caracteristicas.length" class="w-full overflow-auto mb-4">
        <table>
          <thead>
            <tr>
              <th class="text-black">Nombre</th>
              <th class="text-black">Precio adicional</th>
              <th class="text-black">Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in caracteristicas" :key="item.id_caracteristica">
              <td class="text-black">{{ item.nombre_caracteristicas }}</td>
              <td class="text-black">{{ item.adicional }}</td>
              <td>
                <BaseButtons no-wrap>
                  <!-- Botón para editar -->
                  <BaseButton
                    @click="editarCaracteristica(item)"
                    :icon="mdiNoteEdit"
                    small
                    color="success"
                  />
                  <!-- Botón para eliminar -->
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

      <!-- Paginador -->
      <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800 relative" style="overflow-x: auto; white-space: nowrap;">
        <BaseLevel>
          <small>Página {{ currentPage }} de {{ totalPaginas }}</small>
          <BaseButtons style="display: inline-flex; overflow-x: auto; flex-wrap: nowrap;">
            <BaseButton
              v-for="page in totalPaginas"
              :key="page"
              :active="page === currentPage"
              :label="page"
              :color="page === currentPage ? 'lightDark' : 'whiteDark'"
              small
              @click="changePage(page)"
            />
          </BaseButtons>
        </BaseLevel>
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
import { obtenerCaracteristicasPaginadas, eliminarCaracteristica } from '@/services/juanca_service/caracteristicasService';
import { mdiTrashCan, mdiNoteEdit } from '@mdi/js';
import CardBoxModal from '@/components/CardBoxModal.vue';

export default {
  components: {
    LayoutAuthenticated,
    CrearCaracteristica,
    BaseButtons,
    BaseButton,
    NotificationBar,
    CardBoxModal,
  },
  setup() {
    const caracteristicas = ref([]);
    const showModal = ref(false);
    const showConfirmModal = ref(false);
    const caracteristicaSeleccionada = ref(null);
    const idCaracteristicaAEliminar = ref(null);
    const isAlertVisible = ref(false);
    const modalMessage = ref('');
    const colorAlert = ref('');
    const totalPaginas = ref(1);
    const currentPage = ref(1);

    const fetchCaracteristicas = async (page = 1) => {
      try {
        const response = await obtenerCaracteristicasPaginadas(page, 10);
        if (response && response.caracteristicas && Array.isArray(response.caracteristicas)) {
          caracteristicas.value = response.caracteristicas;
          totalPaginas.value = response.total_pages || 1;
        } else {
          console.error('Error: La respuesta del API no tiene el formato esperado.');
          caracteristicas.value = [];
        }
      } catch (error) {
        console.error('Error al obtener las características:', error);
      }
    };

    const confirmarEliminacion = (id) => {
      idCaracteristicaAEliminar.value = id;
      showConfirmModal.value = true;
    };

    const eliminarCaracteristicaService = async () => {
      try {
        await eliminarCaracteristica(idCaracteristicaAEliminar.value);
        await fetchCaracteristicas(currentPage.value);
        mostrarAlerta('Característica eliminada con éxito.', 'success');
      } catch (error) {
        console.error('Error al eliminar la característica:', error);
        mostrarAlerta('Las características que están en uso no se pueden eliminar.', 'danger');
      } finally {
        showConfirmModal.value = false;
      }
    };

    const mostrarModalCrear = () => {
      caracteristicaSeleccionada.value = null;
      showModal.value = true;
    };

    const cerrarModal = () => {
      showModal.value = false;
    };

    const guardarCaracteristica = async () => {
      await fetchCaracteristicas(currentPage.value);
      cerrarModal();
    };

    const editarCaracteristica = (item) => {
      caracteristicaSeleccionada.value = { ...item };
      showModal.value = true;
    };


    const changePage = (page) => {
      currentPage.value = page;
      fetchCaracteristicas(page);
    };

    const mostrarAlerta = (message, color) => {
      isAlertVisible.value = true;
      colorAlert.value = color;
      modalMessage.value = message;
      setTimeout(() => {
        isAlertVisible.value = false;
      }, 3000);
    };

    onMounted(() => {
      fetchCaracteristicas();
    });

    return {
      caracteristicas,
      showModal,
      showConfirmModal,
      confirmarEliminacion,
      eliminarCaracteristicaService,
      mostrarModalCrear,
      cerrarModal,
      guardarCaracteristica,
      isAlertVisible,
      modalMessage,
      colorAlert,
      totalPaginas,
      currentPage,
      changePage,
      editarCaracteristica,
      mdiTrashCan,
      mdiNoteEdit,
    };
  },
};
</script>
