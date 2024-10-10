<script setup>
  import { ref, onMounted } from 'vue'
import { mdiEye, mdiTrashCan } from '@mdi/js'
import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import { getHuespedByPage, deleteHuesped, updateHuesped, getAllHuespedes } from '@/services/huespedService';
import NotificationBar from '@/components/alejo_components/NotificationBar.vue'

defineProps({
  checkable: Boolean
})

const huespedes = ref([]);
const allhuespedes = ref([]);
const originalHuespedes = ref([]);
const buscarHuesped = ref(''); 
const currentHuesped = ref({});
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

const fetchAllHuespedes = async () => {
  try {
    const response = await getAllHuespedes();
    allhuespedes.value = response.data;
    console.log('all huespedes:',allhuespedes.value);
  } catch (error) {
    alert(error.response?.data?.detail || 'Error al obtener los huéspedes');
  }
}; 
fetchAllHuespedes();



const fetchHuespedesByPage = async () => {
  try {
    const response = await getHuespedByPage(currentPage.value);
    
    const activos = response.data.huespedes.filter(huesped => huesped.huesped_estado === true);
    huespedes.value = activos;
    originalHuespedes.value = activos;
    console.log(huespedes.value);
    console.log('Total de huéspedes activos:', activos.length);
    TotalPages.value = response.data.total_pages;
  } catch (error) {
    alert(error.response?.data?.detail || 'Error al obtener los huéspedes');
  }
}; 

    // Filtra las categorías según la búsqueda
const filterHuespedes = () => {
  if (buscarHuesped.value === '') {
    fetchHuespedesByPage();
  }else {
    console.log(buscarHuesped.value);
    const query = buscarHuesped.value.toLowerCase();
    huespedes.value = [...originalHuespedes.value];   
    huespedes.value.forEach(huesped => {
      if(huesped.huesped_estado){
        const filterResult = allhuespedes.value.filter(huesped =>
        huesped.numero_documento && 
        huesped.numero_documento.toLowerCase().includes(query)
        );
        if(filterResult.length === 0){
          modalMessage.value = 'Huésped no encontrado';
          isAlertVisible.value = true;
          colorAlert.value = 'danger';
          activarModalEdit.value = false;
          setTimeout(() => {
          isAlertVisible.value = false;
          }, 2000);
          huespedes.value = [];
        }else {
          huespedes.value = filterResult;
          
        }
      }
    });
    console.log("huespedes filtrados", huespedes.value);
    

   
  }
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

    await fetchHuespedesByPage();
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

    await fetchHuespedesByPage(); // Actualiza la lista de huéspedes
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
  fetchHuespedesByPage();
});

</script>

<template>
  <NotificationBar
  v-if="isAlertVisible"
  :color="colorAlert" 
  :description="modalMessage"
  :visible="isModalVisible"
  />


  <CardBoxModal v-model="activarModalEdit" title="Editar huésped"  buttonLabel="Guardar cambios" has-cancel @cancel="cancelEdit"
  @confirm="update_Huesped " >
    <form @submit.prevent="update_Huesped()">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
        <!-- Primer par de campos -->
        <div class="mb-4">
          <label for="huespedNombre_completo" class="block text-gray-700  font-medium dark:text-white">Nombre completo</label>
          <input
            type="text"
            id="huespedNombre_completo"
            class="mt-1 block w-full border-gray-300 rounded-md shado dark:text-white dark:border-gray-600 rounded-mdw-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.nombre_completo"
            required
          />
        </div>
        <div class="mb-4">
          <label for="huespedTipo_documento" class="block text-gray-700  font-medium dark:text-white">Tipo documento</label>
          <input
            type="text"
            id="huespedTipo_documento"
            class="mt-1 block w-full border-gray-300 rounded-md shad dark:text-white dark:border-gray-600 rounded-mdow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.tipo_documento"
            required
          />
        </div>
        <!-- Segundo par de campos -->
        <div class="mb-4">
          <label for="huespedNumero_documento" class="block text-gray-700  font-medium dark:text-white">Número documento</label>
          <input
            type="text"
            id="huespedNumero_documento"
            class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 rounded-md-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            
            required
          />
        </div>
        <div class="mb-4">
          <label for="huespedFecha_expedicion" class="block text-gray-700  font-medium dark:text-white">Fecha expedición</label>
          <input
            type="date"
            id="huespedFecha_expedicion"
            class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 rounded-md-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.fecha_expedicion"
            required
          />
        </div>
        <!-- Tercer par de campos -->
        <div class="mb-4">
          <label for="huespedEmail" class="block text-gray-700 font-medium dark:text-white">Email</label>
          <input
            type="email"
            id="huespedEmail"
            class="mt-1 block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.email"
            required
          />
        </div>
        <div class="mb-4">
          <label for="huespedTelefono" class="block text-gray-700  font-medium dark:text-white">Teléfono</label>
          <input
            type="text"
            id="huespedTelefono"
            class="mt-1 block w-full border-gray-300 rounded-md dark:text-white dark:border-gray-600 shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.telefono"
            required
          />
        </div>
        <!-- Último par de campos -->
        <div class="mb-4">
          <label for="huespedOcupacion" class="block text-gray-700  font-medium dark:text-white">Ocupación</label>
          <input
            type="text"
            id="huespedOcupacion"
            class="mt-1 block w-full border-gray-300 rounded-md dark:text-white dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.ocupacion"
            required
          />
        </div>
        <div class="mb-4">
          <label for="huespedDireccion" class="block text-gray-700  font-medium dark:text-white">Dirección</label>
          <input
            type="text"
            id="huespedDireccion"
            class="mt-1 block w-full border-gray-300 rounded-md dark:text-white dark:bg-gray-700  dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
            v-model="currentHuesped.direccion"
            required
          />
        </div>
      </div>

    </form>
  </CardBoxModal >

  <CardBoxModal v-model="activarModalDelete.visible"  v-if="activarModalDelete.huesped" title="Eliminar huésped" buttonLabel="Eliminar" button="danger" has-cancel @confirm="confirmDelete"
  @cancel="cancelDelete" >
    <p class="text-xl">Esta seguro de eliminar a: </p>
    <b>{{ activarModalDelete.huesped.nombre_completo }}</b><br>
    <small>{{ activarModalDelete.huesped.tipo_documento }}: {{ activarModalDelete.huesped.numero_documento }}</small>
  </CardBoxModal>

  <div class="mb-6 max-w-md mx-left">
    <div class=" flex items-center border rounded-lg shadow-sm">
      <input
        type="text"
        placeholder="Buscar huésped por documento"
        class="search-input flex-grow px-4 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:text-white dark:bg-gray-700 " 
        v-model="buscarHuesped"
        @input="filterHuespedes"
      />

    </div>
  </div>

  <table>
    <thead>
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
        <th />
      </tr>
    </thead>
    <tbody>
      <tr v-for="huesped in huespedes" :key="huesped.id_huesped">
        
        
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
            @click="currentPage = page; fetchHuespedesByPage()"
            />
        </BaseButtons>
        <small>Página {{ currentPage }} de {{ TotalPages }}</small>
    </BaseLevel>
    </div>
 


</template>
