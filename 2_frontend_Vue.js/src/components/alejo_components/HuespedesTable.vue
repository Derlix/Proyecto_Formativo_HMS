<script setup>
import { ref, onMounted } from 'vue'
import { mdiEye, mdiTrashCan } from '@mdi/js'
import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue'
import ModalAlert from '../ModalAlert.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import { getHuespedByPage, deleteHuesped, updateHuesped, getHuespedByDocument} from '@/services/huespedService';
import NotificationBar from '@/components/alejo_components/NotificationBar.vue'

defineProps({
  checkable: Boolean
})

const huespedes = ref([]);
const currentHuesped = ref({});
const buscarHuesped = ref('');
const TotalPages = ref(0);
const currentPage = ref(1);
const isEditMode = ref(false);
const activarModalEdit = ref(false);
const isModalVisible = ref(false);
const isAlertVisible = ref(false);
const colorAlert = ref('');
const modalMessage = ref('');
const activarModalDelete = ref({
  visible: false,
  huesped: null
});






const fetchHuespedes = async () => {
  try {
    const response = await getHuespedByPage(currentPage.value);

    const activos = response.data.huespedes.filter(huesped => huesped.huesped_estado === true);

    huespedes.value = activos;

    TotalPages.value = response.data.total_pages;
  } catch (error) {
    alert(error.response?.data?.detail || 'Error al obtener los huéspedes');
  }
};



async function buscar_Huesped() {
  if (buscarHuesped.value.trim() === '') {
    fetchHuespedes();
  } else {
    // Buscar un huésped específico
    try {
      const response = await getHuespedByDocument(buscarHuesped.value);
      if (response && response.data) {
        currentHuesped.value = response.data;
        if (currentHuesped.value.huesped_estado){
          huespedes.value = [currentHuesped.value]; 
        }else {
          modalMessage.value = 'El huésped ha sido eliminado';
          isModalVisible.value = true;
        }
      }else {
        huespedes.value = []; // No se encontró el huésped
        currentHuesped.value = null;
        modalMessage.value = 'El huésped no existe';
        isModalVisible.value = true;
      }
    } catch (error) {
      console.error('Error al encontrar huésped:', error);
      huespedes.value = [];
      currentHuesped.value = null;
      
    }
  }
};

const handleClose = () => {
  isModalVisible.value = false;
  buscarHuesped.value = "";
};



const openEditModal = (huesped = {}) => {
  isEditMode.value = true;
  currentHuesped.value = { ...huesped };
  activarModalEdit.value = true;
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
    modalMessage.value = 'Huésped actualizado exitosamente';
    isAlertVisible.value = true;
    colorAlert.value = 'success';
    activarModalEdit.value = false;

    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
    //cierra el modal en tres segundos

    await fetchHuespedes();
  } catch (error) {
    modalMessage.value = error.data.detail;
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    activarModalEdit.value = false;

    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);

  }
};


const cancelEdit = () => {
  activarModalEdit.value = false;
  // Solo cierra el modal
};



// Método para abrir el modal
const openDeleteModal = (huesped) => {
  activarModalDelete.value = {
    visible: true,
    huesped: huesped
    
  };
};


// Método para confirmar la eliminación
const confirmDelete = async () => {
  const huespedTemp = activarModalDelete.value.huesped;
  if (!huespedTemp) return;

  try {
    await deleteHuesped(huespedTemp.id_huesped);
    modalMessage.value = 'Huésped eliminado exitosamente';
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);

    await fetchHuespedes(); // Actualiza la lista de huéspedes
    activarModalDelete.value.visible = false; 
  } catch (error) {
    modalMessage.value = error.data.detail;
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    activarModalDelete.value.visible = false; 

  }
};

// Método para cancelar la eliminación
const cancelDelete = () => {
  activarModalDelete.value.visible = false; // Solo cierra el modal
};



const formatDate = (dateString) => {
  const options = {
    year: 'numeric',
    month: 'numeric',
    day: 'numeric',
    timeZone: 'UTC'
  };
  return new Date(dateString).toLocaleDateString('es-ES', options);
};


onMounted(() => {
  fetchHuespedes();
});

</script>

<template>
  <NotificationBar
  v-if="isAlertVisible"
  :color="colorAlert" 
  :description="modalMessage"
  :visible="isModalVisible"
  />

  <ModalAlert
  v-if="isModalVisible"
  :descripcion="modalMessage"
  textBoton="Cerrar"
  :visible="isModalVisible"
  @close="handleClose"
  />

  <CardBoxModal v-model="activarModalEdit" title="Editar huesped"  buttonLabel="Guardar cambios" has-cancel @cancel="cancelEdit"
  @confirm="update_Huesped " >
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
            type="date"
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
            type="email"
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
      <!-- <div class="mt-4">
        <BaseButton
              type="submit"
              label="Guardar cambios"
              color="info"
              small
            /> 
      </div> -->
    </form>
  </CardBoxModal >

  <CardBoxModal v-model="activarModalDelete.visible"  v-if="activarModalDelete.huesped" title="Eliminar huesped" buttonLabel="Eliminar" button="danger" has-cancel @confirm="confirmDelete"
  @cancel="cancelDelete" >
    <p class="text-xl">Esta seguro de eliminar a: </p>
    <b>{{ activarModalDelete.huesped.nombre_completo }}</b><br>
    <small>{{ activarModalDelete.huesped.tipo_documento }}: {{ activarModalDelete.huesped.numero_documento }}</small>
  </CardBoxModal>

  <div class="mb-6 max-w-md mx-left">
    <div class=" flex items-center border rounded-lg shadow-sm ">
      <input
        type="search"
        id="buscarHuesped"
        placeholder="Buscar huesped por documento"
        class="flex-grow px-4 py-2 border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
        v-model="buscarHuesped"
        @input="buscar_Huesped"
      />
    </div>
  </div>

  <table>
    <thead>
      <tr>
        <th v-if="checkable" />
        <th />
        <th>Nombre completo</th>
        <th>Tipo documento</th>
        <th>Número documento</th>
        <th>Fecha expedición</th>
        <th>Email</th>
        <th>Teléfono</th>
        <th>Ocupación</th>
        <th>Dirección</th>
        <th>Estado</th>
        <th />
      </tr>
    </thead>
    <tbody>
      <tr v-for="huesped in huespedes" :key="huesped.id_huesped">
        
        <td class="border-b-0 lg:w-6 before:hidden">
          
        </td>
        <td data-label="Nombre completo">
          {{ huesped.nombre_completo }}
        </td>
        <td data-label="Tipo documento">
          {{ huesped.tipo_documento }}
        </td>
        <td data-label="Número documento">
          {{ huesped.numero_documento }}
        </td>
        <td data-label="Fecha expedición">
          {{ formatDate(huesped.fecha_expedicion) }}
        </td>
        <td data-label="Email">
          {{ huesped.email }}
        </td>
        <td data-label="Teléfono">
          {{ huesped.telefono }}
        </td>
        <td data-label="Ocupación">
          {{ huesped.ocupacion }}
        </td>
        <td data-label="Dirección">
          {{ huesped.direccion  }}
        </td>
        <td data-label="Estado">
          {{ huesped.huesped_estado ? 'Activo' : 'Inactivo' }}
        </td>
        
        <td class="before:hidden lg:w-1 whitespace-nowrap">
          <BaseButtons type="justify-start lg:justify-end" no-wrap>
            <BaseButton color="info" :icon="mdiEye" small @click="openEditModal(huesped)" />
            <BaseButton color="danger" :icon="mdiTrashCan" small @click="openDeleteModal(huesped)"/>
          </BaseButtons>
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
            @click="currentPage = page; fetchHuespedes()"
            />
        </BaseButtons>
        <small>Página {{ currentPage }} de {{ TotalPages }}</small>
    </BaseLevel>
    </div>
 


</template>
