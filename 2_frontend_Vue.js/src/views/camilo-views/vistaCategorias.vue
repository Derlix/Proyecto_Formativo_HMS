<template>
  <LayoutAuthenticated>
    <div class="categorias container mx-auto p-4">
      <h1 class="text-2xl font-semibold text-center mb-6 text-black dark:text-white">Gestión de Categorías</h1>

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
          Crear Categoría
        </button>

        <router-link
          to="/habitaciones"
          class="bg-blue-700 text-white px-4 py-2 rounded-md shadow-sm hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
        >
          Volver
        </router-link>
      </div>

      <!-- Modal para crear o editar una categoría -->
      <CrearCategoria
        :visible="showModalCrear"
        :categoria="categoriaSeleccionada"
        @close="cerrarModal"
        @save="handleCategoriaCreada"
      />

      <!-- Modal para confirmar eliminación -->
      <CardBoxModal
        :modelValue="showConfirmModal"
        title="Confirmar Eliminación"
        button-label="Eliminar"
        hasCancel
        @confirm="eliminarCategoriaService"
        @cancel="showConfirmModal = false"
      >
        <p>¿Estás seguro de que deseas eliminar esta categoría?</p>
      </CardBoxModal>

      <!-- Tabla de categorías -->
      <div v-if="categorias.length" class="w-full overflow-auto mb-4">
        <table>
          <thead>
            <tr>
              <th class="text-black dark:text-white">Tipo de Habitación</th> <!-- Columna para Tipo de Habitación -->
              <th class="text-black dark:text-white">Precio Fijo</th> <!-- Columna para Precio Fijo -->
              <th class="text-black dark:text-white">Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in categorias" :key="item.id_categoria">
              <td class="text-black px-4 py-2 border-b-2 text-sm dark:text-white">{{ item.tipo_habitacion }}</td> <!-- Mostrar Tipo de Habitación -->
              <td class="text-black px-4 py-2 border-b-2 text-sm dark:text-white">{{ formatCurrency(item.precio_fijo) }}</td> <!-- Mostrar Precio Fijo -->
              <td>
                <BaseButtons no-wrap>
                  <!-- Botón para editar -->
                  <BaseButton
                    @click="editarCategoria(item)"
                    :icon="mdiNoteEdit"
                    small
                    color="success"
                  />
                  <!-- Botón para eliminar -->
                  <!-- <BaseButton
                    @click="confirmarEliminacion(item.id_categoria)"
                    :icon="mdiTrashCan"
                    small
                    color="danger"
                  /> -->
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
import CrearCategoria from '@/components/juanca_components/categorias.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import BaseButton from '@/components/BaseButton.vue';
import NotificationBar from '@/components/alejo_components/NotificationBar.vue';
import { obtenerCategoriasPaginadas, eliminarCategoria } from '@/services/juanca_service/categoriaService';
import { mdiTrashCan, mdiNoteEdit } from '@mdi/js';
import CardBoxModal from '@/components/CardBoxModal.vue';

export default {
  components: {
    LayoutAuthenticated,
    CrearCategoria,
    BaseButtons,
    BaseButton,
    NotificationBar,
    CardBoxModal,
  },
  setup() {
    const categorias = ref([]);
    const showModalCrear = ref(false);
    const showConfirmModal = ref(false);
    const categoriaSeleccionada = ref({});
    const idCategoriaAEliminar = ref(null);
    const isAlertVisible = ref(false);
    const modalMessage = ref('');
    const colorAlert = ref('');
    const totalPaginas = ref(1);
    const currentPage = ref(1);

    const fetchCategorias = async (page = 1) => {
      try {
        const response = await obtenerCategoriasPaginadas(page, 10);
        const { data } = response;
        if (data && data.categories && Array.isArray(data.categories)) {
          categorias.value = data.categories;
          totalPaginas.value = data.total_pages || 1;
        } else {
          categorias.value = [];
        }
      } catch (error) {
        console.error('Error al obtener las categorías:', error);
      }
    };

    const confirmarEliminacion = (id) => {
      idCategoriaAEliminar.value = id;
      showConfirmModal.value = true;
    };

    const eliminarCategoriaService = async () => {
      try {
        await eliminarCategoria(idCategoriaAEliminar.value);
        await fetchCategorias(currentPage.value);
        mostrarAlerta('Categoría eliminada con éxito.', 'success');
      } catch (error) {
        mostrarAlerta('La categoría no se puede eliminar porque está en uso.', 'danger');
      } finally {
        showConfirmModal.value = false;
      }
    };

    const mostrarModalCrear = () => {
      categoriaSeleccionada.value = null;
      showModalCrear.value = true;
    };

    const cerrarModal = () => {
      showModalCrear.value = false;
    };

    const handleCategoriaCreada = async () => {
      await fetchCategorias(currentPage.value);
      cerrarModal();
    };

    const editarCategoria = (item) => {
      if (!item.id_categoria_habitacion) {
        console.error('Error: La categoría seleccionada no tiene un ID válido.');
        return;
      }

      categoriaSeleccionada.value = { ...item };
      showModalCrear.value = true;
    };

    const changePage = (page) => {
      currentPage.value = page;
      fetchCategorias(page);
    };


    const formatCurrency = (value) => {
      return new Intl.NumberFormat('es-CO', {
          style: 'currency',
          currency: 'COP',
          minimumFractionDigits: 0,
      }).format(value);
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
      fetchCategorias();
    });

    return {
      categorias,
      showModalCrear,
      showConfirmModal,
      confirmarEliminacion,
      eliminarCategoriaService,
      mostrarModalCrear,
      cerrarModal,
      handleCategoriaCreada,
      isAlertVisible,
      modalMessage,
      colorAlert,
      totalPaginas,
      currentPage,
      changePage,
      formatCurrency,
      editarCategoria,
      categoriaSeleccionada,
      mdiTrashCan,
      mdiNoteEdit,
    };
  },
};
</script>
