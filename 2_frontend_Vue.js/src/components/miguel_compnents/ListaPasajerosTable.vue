<script setup>
import { ref, onMounted } from 'vue'
import { mdiEye } from '@mdi/js'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import { getListaPasajerosBypage } from '@/services/listapasajerosService'
import CardBoxModal from '../CardBoxModal.vue'
import NotificationBar from '../alejo_components/NotificationBar.vue'

const currentPage = ref(1)
const TotalPages = ref(0)
const allHuespedes = ref([])
const filteredHuespedes = ref([])
const buscarHuesped = ref('')
const activarvisibleModal = ref(false)
const currentHuesped = ref({})
const isAlertVisible = ref(false)
const modalMessage = ref('')
const colorAlert = ref('')

const fetchHuespedesByPage = async () => {
  try {
    const response = await getListaPasajerosBypage(currentPage.value)
    if (response.data && response.data.movimientos) {
      TotalPages.value = response.data.total_pages
      allHuespedes.value = response.data.movimientos
      console.log("Huéspedes cargados:", allHuespedes.value); 
      filteredHuespedes.value = allHuespedes.value
    } else {
      TotalPages.value = 0
      allHuespedes.value = []
      filteredHuespedes.value = []
    }
  } catch (error) {
    modalMessage.value = 'Error al encontrar pasajeros'
    isAlertVisible.value = true
    colorAlert.value = 'danger'
  }
}

const filterHuespedes = () => {
  if (buscarHuesped.value === '') {
    filteredHuespedes.value = [...allHuespedes.value]; // Restablece la lista si no hay búsqueda
  } else {
    const query = buscarHuesped.value.toLowerCase();

    const filterResult = allHuespedes.value.filter(movimiento => {
      const numeroDocumento = movimiento.huesped.numero_documento || ''; 
      return numeroDocumento.toLowerCase().includes(query);
    });

    if (filterResult.length === 0) {
      modalMessage.value = 'Pasajero no encontrado';
      isAlertVisible.value = true;
      colorAlert.value = 'danger';
      filteredHuespedes.value = []; // Limpia la lista si no se encuentra
      setTimeout(() => {
        isAlertVisible.value = false;
      }, 2000);
    } else {
      filteredHuespedes.value = filterResult;
    }
    console.log("Huéspedes filtrados:", filteredHuespedes.value);
  }
}


const handlePageClick = (page) => {
  currentPage.value = page
  fetchHuespedesByPage()
}

const openVisibleModal = (huesped) => {
  currentHuesped.value = huesped
  activarvisibleModal.value = true
}

onMounted(() => {
  fetchHuespedesByPage()
})
</script>


<template>
  <NotificationBar
    v-if="isAlertVisible"
    :color="colorAlert"
    :description="modalMessage"
    :visible="isModalVisible"
  />
  <!-- MODAL DE VISUALIZACION -->
  <CardBoxModal v-model="activarvisibleModal" title="Visualizar Datos">
    <form>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
        <div class="mb-4">
          <label
            for="huespedNombre_completo"
            class="block text-gray-700 font-medium dark:text-white"
            >Nombre completo</label
          >
          <input
            disabled
            type="text"
            id="huespedNombre_completo"
            class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.nombre_completo"
          />
        </div>
        <div class="mb-4">
          <label for="huespedTipo_documento" class="block text-gray-700 font-medium dark:text-white"
            >Tipo documento</label
          >
          <input
            disabled
            type="text"
            id="huespedTipo_documento"
            class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.tipo_documento"
          />
        </div>
        <div class="mb-4">
          <label
            for="huespedNumero_documento"
            class="block text-gray-700 font-medium dark:text-white"
            >Número documento</label
          >
          <input
            disabled
            type="text"
            id="huespedNumero_documento"
            class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.numero_documento"
          />
        </div>
        <div class="mb-4">
          <label
            for="huespedFecha_expedicion"
            class="block text-gray-700 font-medium dark:text-white"
            >Fecha expedición</label
          >
          <input
            disabled
            type="date"
            id="huespedFecha_expedicion"
            class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.fecha_expedicion"
          />
        </div>
        <div class="mb-4">
          <label for="huespedEmail" class="block text-gray-700 font-medium dark:text-white"
            >Email</label
          >
          <input
            disabled
            type="email"
            id="huespedEmail"
            class="mt-1 block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.email"
          />
        </div>
        <div class="mb-4">
          <label for="huespedTelefono" class="block text-gray-700 font-medium dark:text-white"
            >Teléfono</label
          >
          <input
            disabled
            type="text"
            id="huespedTelefono"
            class="mt-1 block w-full border-gray-300 rounded-md dark:text-white dark:border-gray-600 shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.telefono"
          />
        </div>
        <div class="mb-4">
          <label for="huespedOcupacion" class="block text-gray-700 font-medium dark:text-white"
            >Ocupación</label
          >
          <input
            disabled
            type="text"
            id="huespedOcupacion"
            class="mt-1 block w-full border-gray-300 rounded-md dark:text-white dark:border-gray-600 shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentHuesped.ocupacion"
          />
        </div>
        <div class="mb-4">
          <label for="huespedDireccion" class="block text-gray-700 font-medium dark:text-white"
            >Dirección</label
          >
          <input
            disabled
            type="text"
            id="huespedDireccion"
            class="mt-1 block w-full border-gray-300 rounded-md dark:text-white dark:bg-gray-700 dark:border-gray-600 shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
            v-model="currentHuesped.direccion"
          />
        </div>
      </div>
    </form>
  </CardBoxModal>

  <div class="mb-6 max-w-md mx-left">
    <div class=" flex items-center border rounded-lg shadow-sm">
      <input
        type="text"
        placeholder="Buscar pasajero por documento"
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
        <th>Fecha de entrada</th>
        <th>Fecha de salida</th>
        <th>Documento</th>
        <th>Expedido N.</th>
        <th>Registro N.</th>
        <th>Profesion</th>
        <th />
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="movimiento in filteredHuespedes"
        :key="`${movimiento.huesped.id_huesped}-${movimiento.reserva_habitacion.id_reserva}`"
      >
        <td>{{ movimiento.huesped.nombre_completo }}</td>
        <td>{{ movimiento.reserva_habitacion.fecha_entrada }}</td>
        <td>{{ movimiento.reserva_habitacion.fecha_salida_propuesta }}</td>
        <td>{{ movimiento.huesped.numero_documento }}</td>
        <td>{{ movimiento.huesped.fecha_expedicion }}</td>
        <td>{{ movimiento.reserva_habitacion.id_reserva }}</td>
        <td>{{ movimiento.huesped.ocupacion }}</td>
        <td>
          <BaseButton
            color="info"
            :icon="mdiEye"
            small
            @click="openVisibleModal(movimiento.huesped)"
          />
        </td>
      </tr>
    </tbody>
  </table>

  <BaseLevel>
    <BaseButtons>
      <BaseButton
        v-for="page in TotalPages"
        :key="page"
        :active="page === currentPage"
        :label="page"
        @click="handlePageClick(page)"
      />
    </BaseButtons>
    <small>Página {{ currentPage }} de {{ TotalPages }}</small>
  </BaseLevel>
</template>
