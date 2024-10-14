<script setup>
import { ref, onMounted } from 'vue'
import { mdiEye } from '@mdi/js'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import { getListacomprobanteByPage } from '@/services/comprobanteService'
import CardBoxModal from '../CardBoxModal.vue'
import NotificationBar from '../alejo_components/NotificationBar.vue'

const currentPage = ref(1)
const TotalPages = ref(0)
const allcomprobantes = ref([])
const filteredHuespedes = ref([])
const buscarHuesped = ref('')
const activarvisibleModal = ref(false)
const currentHuesped = ref({})
const isAlertVisible = ref(false)
const modalMessage = ref('')
const colorAlert = ref('')

const fetchComprobantes = async () => {
  try {
    const response = await getListacomprobanteByPage(currentPage.value)
    if (response.data && response.data.comprobantes) {
      TotalPages.value = response.data.total_pages
      allcomprobantes.value = response.data.comprobantes
      filteredHuespedes.value = allcomprobantes.value
    } else {
      TotalPages.value = 0
      allcomprobantes.value = []
      filteredHuespedes.value = []
    }
  } catch (error) {
    modalMessage.value = 'Error al encontrar comprobantes'
    isAlertVisible.value = true
    colorAlert.value = 'danger'
  }
}

const filterHuespedes = () => {
  if (buscarHuesped.value === '') {
    filteredHuespedes.value = [...allcomprobantes.value]; // Restablece la lista si no hay búsqueda
  } else {
    const query = buscarHuesped.value.toLowerCase();

    const filterResult = allcomprobantes.value.filter(comprobante => {
      const documento = comprobante.huesped?.numero_documento 
        ? String(comprobante.huesped.numero_documento) // Convertir a string
        : ''; // Manejar el caso en que no exista numero_documento

      return documento.toLowerCase().includes(query);
    });

    if (filterResult.length === 0) {
      modalMessage.value = 'Comprobante no encontrado';
      isAlertVisible.value = true;
      colorAlert.value = 'danger';
      filteredHuespedes.value = []; // Limpia la lista si no se encuentra
      setTimeout(() => {
        isAlertVisible.value = false;
      }, 2000);
    } else {
      filteredHuespedes.value = filterResult;
    }
  }
};


const handlePageClick = (page) => {
  currentPage.value = page
  fetchComprobantes()
}

const openVisibleModal = (huesped) => {
  currentHuesped.value = huesped
  activarvisibleModal.value = true
}

onMounted(() => {
  fetchComprobantes()
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
            >Fecha salida</label
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
        <th>N. documento</th>     
        <th>Huesped N.</th>
        <th>Reserva N.</th>
        <th>Fecha de salida</th>
        <th>Valor de deposito</th>
        <th>Forma de pago</th>
        <th>Usuario</th>
        <th>Usuario N.</th>
        <th />
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="comprobante in filteredHuespedes"
        :key="`${comprobante.huesped.id_huesped}-${comprobante.reserva_habitacion.id_reserva}`"
      >
        <td>{{ comprobante.huesped.nombre_completo }}</td>
        <td>{{ comprobante.huesped.numero_documento }}</td>
        <td>{{ comprobante.huesped.id_huesped }}</td>
        <td>{{ comprobante.reserva.id_reserva }}</td>
        <td>{{ comprobante.reserva_habitacion.fecha_salida_propuesta }}</td>
        <td>{{ comprobante.reserva.valor_deposito }}</td>
        <td>{{ comprobante.reserva.forma_pago }}</td>
        <td>{{ comprobante.usuario.nombre_completo }}</td>
        <td>{{ comprobante.usuario.id_usuario }}</td>
        <td>
          <BaseButton
            color="info"
            :icon="mdiEye"
            small
            @click="openVisibleModal(comprobante.huesped)"
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
