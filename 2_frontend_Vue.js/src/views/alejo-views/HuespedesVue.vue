<script setup>
import { ref, onMounted } from 'vue'; // Importar las funciones reactivas y del ciclo de vida
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import {
  getHuespedByPage,
  deleteHuesped,
  updateHuesped,
  getHuespedByDocument
} from '@/services/huespedService';

// Define las propiedades reactivas
const huespedes = ref([]);
const currentHuesped = ref({});
const currentPage = ref(1);
const totalPages = ref(0);
const isEditMode = ref(false);
const visible = ref(false);
const buscarHuesped = ref('');
// const imageFile = ref('');
// const imagePreview = ref('');

// Obtiene los huéspedes de la página actual
const fetchHuespedes = async () => {
  try {
    const response = await getHuespedByPage(currentPage.value);
    huespedes.value = response.data.huespedes;
    totalPages.value = response.data.total_pages;
  } catch (error) {
    alert(error.response?.data?.detail || 'Error al obtener los huéspedes');
  }
};

// Busca un huésped por documento
const HuespedByDocument = async () => {
  try {
    const response = await getHuespedByDocument(buscarHuesped.value);
    if (response.data.huesped) {
      currentHuesped.value = response.data.huesped;
      huespedes.value = [currentHuesped.value];
    } else {
      huespedes.value = [];
      alert('No se encontró ningún huésped con el documento proporcionado.');
    }
  } catch (error) {
    alert(error.response?.data?.detail || 'Error al buscar por documento');
  }
};

// Navega a la siguiente página
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
    fetchHuespedes();
  }
};

// Navega a la página anterior
const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    fetchHuespedes();
  }
};

// Formatea una fecha para mostrarla de manera legible
const formatDate = (dateString) => {
  const options = {
    year: 'numeric',
    month: 'numeric',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  };
  return new Date(dateString).toLocaleDateString('es-ES', options);
};

// Elimina un huésped
const deleteHuespedMethod = async (id_huesped) => {
  if (confirm('¿Estás seguro de que deseas eliminar este huésped?')) {
    try {
      await deleteHuesped(id_huesped);
      alert('Huésped eliminado exitosamente');
      fetchHuespedes();
    } catch (error) {
      alert(error.data.detail);
    }
  }
};

// Abre el modal para editar un huésped
const openEditModal = (action, huesped = {}) => {
  
  isEditMode.value = true;
  if (action === 'update') {
    isEditMode.value = true;
    // isDelete.value = false;
    // descripcion.value = 'Actualizar Producto';
    // textBoton.value = 'Actualizar';
    currentHuesped.value = { ...huesped };
  } else if (action === 'delete') {
    isEditMode.value = false;
    // isDelete.value = true;
    // descripcion.value = 'Eliminar Producto';
    // textBoton.value = 'Eliminar';
    currentHuesped.value = { ...huesped };
  }
  visible.value = true;

  
  // Es posible que necesites ajustar cómo mostrar el modal si usas una biblioteca específica
};

const closeModal = () => {
  visible.value = false;
};

// Actualiza un huésped
const update_Huesped = async () => {
  try {
    await updateHuesped(
      currentHuesped.value.id_huesped,
      currentHuesped.value.nombre_completo,
      currentHuesped.value.tipo_documento,
      currentHuesped.value.numero_documento,
      currentHuesped.value.fecha_expedicion,
      currentHuesped.value.email,
      currentHuesped.value.telefono,
      currentHuesped.value.ocupacion,
      currentHuesped.value.direccion
    );
    alert('Huésped actualizado exitosamente');
    fetchHuespedes();
    closeModal();
  } catch (error) {
    alert(error.data.detail);
  }
};

// Llama a fetchHuespedes cuando el componente esté montado
onMounted(() => {
  fetchHuespedes();
});
</script>


<template>
  <LayoutAuthenticated>
    <SectionMain class="bg-blue-100 rounded-lg">
      <h1 class="text-black font-bold mb-8">Historial Huespedes</h1>
      <div class="mb-6">
        <div class="flex items-center border rounded-lg shadow-sm">
          <input
            type="search"
            id="documentoBuscar"
            placeholder="Buscar huesped por documento"
            class="flex-grow px-4 py-2 border-gray-300 rounded-l-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
            v-model="buscarHuesped"
          />
          <button
            class="bg-blue-800 p-2 text-white rounded-r-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
            @click="HuespedByDocument"
          >
            <i class="mdi mdi-magnify text-xl"></i>
          </button>
        </div>
      </div>
     
      <div>
        <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-6">
          <table class="w-full text-sm text-center rtl:text-right text-black font-medium dark:text-gray-100">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
              <tr>
                <th>Nombre completo</th>
                <th>Tipo documento</th>
                <th>Número documento</th>
                <th>Fecha expedición</th>
                <th>Email</th>
                <th>Teléfono</th>
                <th>Ocupación</th>
                <th>Dirección</th>
                <th>Estado</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="huesped in huespedes" :key="huesped.id_huespede">
                <td>{{ huesped.nombre_completo }}</td>
                <td>{{ huesped.tipo_documento }}</td>
                <td>{{ huesped.numero_documento }}</td>
                <td>{{ formatDate(huesped.fecha_expedicion) }}</td>
                <td>{{ huesped.email }}</td>
                <td>{{ huesped.telefono }}</td>
                <td>{{ huesped.ocupacion }}</td>
                <td>{{ huesped.direccion }}</td>
                <td>{{ huesped.huesped_estado ? 'Activo' : 'Inactivo' }}</td>
                <td>
                  <button
                    @click="openEditModal('update', huesped)"
                    class="text-green-500 rounded-md hover:text-black focus:outline-none"
                  >
                    <i class="mdi mdi-square-edit-outline text-2xl"></i>
                  </button>
                  <button
                    @click="deleteHuespedMethod(huesped.id_huespede)"
                    class="text-red-500 rounded-md hover:text-black focus:outline-none"
                  >
                    <i class="mdi mdi-trash-can text-2xl"></i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      

      <!-- Controles de paginación -->
      <div class="pagination-controls">
        <!-- Botón para la página anterior, con click llama a la función prevPage  -->
        <button class="btn btn-primary m-3" @click="prevPage" :disabled="currentPage === 1">
          Anterior
        </button>
        <!-- Muestra la página actual y total de páginas -->
        <span>Página {{ currentPage }} de {{ totalPages }}</span>
        <!-- Botón para la página siguiente,  con click llama a la función nextPage -->
        <button
          class="btn btn-primary m-3"
          @click="nextPage"
          :disabled="currentPage === totalPages"
        >
          Siguiente
        </button>
      </div>

    
      <!-- Modal para editar usuario -->
      <div
        v-if="visible"
        id="userModal"
        tabindex="-1"
        aria-labelledby="userModalLabel"
        class="fixed inset-0 z-50 bg-gray-900 bg-opacity-50 flex items-center justify-center"
      
      >
        <div class="flex items-center justify-center min-h-screen p-4">
          <div class="bg-white rounded-lg shadow-lg w-full max-w-4xl">
            <div class="flex justify-between items-center p-4 border-b border-gray-200">
              <!-- Título para editar usuario -->
              <h5 id="userModalLabel" class="text-lg font-semibold">Editar Huesped</h5>
              <button
                type="button"
                class="text-gray-400 hover:text-gray-600"
                @click="closeModal"
                aria-label="Close"
              >
                <svg
                  class="w-6 h-6"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M6 18L18 6M6 6l12 12"
                  ></path>
                </svg>
              </button>
            </div>
            <div class="p-4">
              <form @submit.prevent="update_Huesped()">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <!-- Primer par de campos -->
                  <div class="mb-4">
                    <label for="huespedNombre_completo" class="block text-gray-700 font-medium">Nombre completo</label>
                    <input
                      type="text"
                      id="huespedNombre_completo"
                      class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                      v-model="currentHuesped.nombre_completo"
                      required
                    />
                  </div>
                  <div class="mb-4">
                    <label for="huespedTipo_documento" class="block text-gray-700 font-medium">Tipo documento</label>
                    <input
                      type="text"
                      id="huespedTipo_documento"
                      class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                      v-model="currentHuesped.tipo_documento"
                      required
                    />
                  </div>
                  <!-- Segundo par de campos -->
                  <div class="mb-4">
                    <label for="huespedNumero_documento" class="block text-gray-700 font-medium">Número documento</label>
                    <input
                      type="text"
                      id="huespedNumero_documento"
                      class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                      v-model="currentHuesped.numero_documento"
                      required
                    />
                  </div>
                  <div class="mb-4">
                    <label for="huespedFecha_expedicion" class="block text-gray-700 font-medium">Fecha expedición</label>
                    <input
                      type="text"
                      id="huespedFecha_expedicion"
                      class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                      v-model="currentHuesped.fecha_expedicion"
                      required
                    />
                  </div>
                  <!-- Tercer par de campos -->
                  <div class="mb-4">
                    <label for="huespedEmail" class="block text-gray-700 font-medium">Email</label>
                    <input
                      type="text"
                      id="huespedEmail"
                      class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                      v-model="currentHuesped.email"
                      required
                    />
                  </div>
                  <div class="mb-4">
                    <label for="huespedTelefono" class="block text-gray-700 font-medium">Teléfono</label>
                    <input
                      type="text"
                      id="huespedTelefono"
                      class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                      v-model="currentHuesped.telefono"
                      required
                    />
                  </div>
                  <!-- Último par de campos -->
                  <div class="mb-4">
                    <label for="huespedOcupacion" class="block text-gray-700 font-medium">Ocupación</label>
                    <input
                      type="text"
                      id="huespedOcupacion"
                      class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                      v-model="currentHuesped.ocupacion"
                      required
                    />
                  </div>
                  <div class="mb-4">
                    <label for="huespedDireccion" class="block text-gray-700 font-medium">Dirección</label>
                    <input
                      type="text"
                      id="huespedDireccion"
                      class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                      v-model="currentHuesped.direccion"
                      required
                    />
                  </div>
                </div>
            
                <!-- Botón de enviar (guardar cambios) -->
                <div class="mt-4">
                  <button
                    type="submit"
                    class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-white bg-blue-500 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                    >
                    Guardar Cambios
                  </button>
                </div>
              </form>
            </div>
            
          </div>
        </div>
      </div>

      <!-- <ModalHuesped
        descripcion="Editar Huesped"
        textBoton="Editar Huesped"
        :visible="editarHuesped" 
        @close="editarHuesped = false" />

        <ModalHuesped
        descripcion="Eliminar Huesped"
        textBoton="Eliminar Huesped"
        :visible="eliminarHuesped" 
        @close="eliminarHuesped = false" /> -->
    </SectionMain>
  </LayoutAuthenticated>
</template>

