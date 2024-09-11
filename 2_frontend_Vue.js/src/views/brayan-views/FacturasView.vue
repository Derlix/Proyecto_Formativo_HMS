<template>
  <LayoutAuthenticated>
    <SectionMain class="bg-blue-200 rounded-lg p-6">
      <h1 class="text-2xl font-bold text-gray-800 mb-8">Historial de Facturas</h1>
      <div class="grid grid-cols-1 md:grid-cols-5 gap-4 py-4">
        <input
          type="search"
          placeholder="Buscar factura por ID"
          class="rounded-lg border border-gray-300 p-2"
        />
        <button
          type="button"
          class="bg-blue-800 rounded-lg text-white p-2 hover:bg-blue-700 transition"
        >
          Buscar
        </button>
      </div>
      <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-6 max-w-8xl mx-auto ">
        <table class="min-w-full text-sm text-left divide-y divide-gray-200 dark:divide-gray-600" style="table-layout: auto;">

          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400 ">
            <tr>
              <th class=" px-2 py-3 w-28">ID Facturación</th>
              <th class="  px-2 py-7 w-28">ID Check-in</th>
              <th class="px-4 py-3 w-28">Subtotal</th>
              <th class="px-4 py-3 w-28">Impuestos</th>
              <th class="px-4 py-3 w-28">Total</th>
              <th class="px-4 py-3 w-32">Total Precio Productos</th>
              <th class=" px-4 py-3 w-44">Método de Pago</th>
              <th class="px-4 py-3 w-28">Estado</th>
              <th class="px-4 py-3 w-32">Fecha Salida</th>
              <th class="px-2 py-3 w-28">ID Reserva</th>
              <th class="px-2 py-3 w-32">Medio Llegada</th>
              <th class="px-2 py-3 w-24">Llegada Situación</th>
              <th class="px-2 py-3 w-28">Equipaje</th>
              <th class="px-2 py-3 w-28">Fecha Reserva</th>
              <th class="px-2 py-3 w-32">Empresa</th>
              <th class="px-2 py-3 w-28">Valor Depósito</th>
              <th class="px-2 py-3 w-28">Forma de Pago</th>
              <th class="px-2 py-3 w-36">Nombre</th>
              <th class="px-2 py-3 w-32">N° Documento</th>
              <th class="px-4 py-3 w-64">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(factura, index) in facturas" :key="factura.id_facturacion"
                :class="{'bg-gray-100 dark:bg-gray-900': index % 2 === 0, 'bg-white dark:bg-gray-800': index % 2 !== 0}">
              <td class="px-2 py-2 dark:text-white">{{ factura.id_facturacion }}</td>
              <td class="px-2 py-2 dark:text-white">{{ factura.check_in.id_check_in }}</td>
              <td class="px-4 py-2 dark:text-white">{{ factura.subtotal }}</td>
              <td class="px-4 py-2 dark:text-white">{{ factura.impuestos }}</td>
              <td class="px-4 py-2 dark:text-white">{{ factura.total }}</td>
              <td class="px-4 py-2 dark:text-white">{{ factura.total_precio_productos }}</td>
              <td class="px-4 py-2 dark:text-white">{{ factura.metodo_pago }}</td>
              <td class="px-4 py-2 dark:text-white">{{ factura.estado }}</td>
              <td class="px-4 py-2 dark:text-white">{{ factura.fecha_salida }}</td>
              <td class="px-2 py-2 dark:text-white">{{ factura.reserva.id_reserva }}</td>
              <td class="px-2 py-2 dark:text-white">{{ factura.check_in.medio_llegada }}</td>
              <td class="px-2 py-2 dark:text-white">{{ factura.check_in.llegada_situacion }}</td>
              <td class="px-2 py-2 dark:text-white">{{ factura.check_in.equipaje }}</td>
              <td class="px-2 py-2 dark:text-white">{{ factura.reserva.fecha_reserva }}</td>
              <td class="px-2 py-2 dark:text-white">{{ factura.reserva.empresa }}</td>
              <td class="px-2 py-2 dark:text-white">{{ factura.reserva.valor_deposito }}</td>
              <td class="px-2 py-2 dark:text-white">{{ factura.reserva.forma_pago }}</td>
              <td class="px-2 py-2 dark:text-white">{{ factura.huesped.nombre_completo }}</td>
              <td class="px-2 py-2 dark:text-white">{{ factura.huesped.numero_documento }}</td>
              <td class="px-2 py-2 w-64">
                <div class="flex justify-center space-x-2">
                  <a
                    href="#"
                    @click.prevent="openAgregarProductosModal(factura)"
                    class="text-violet-600 hover:underline dark:text-violet-400 btn btn-primary"
                  >
                    Agregar Productos
                  </a>
                  <a
                    href="#"
                    @click.prevent="openListaProductosModal(factura)"
                    class="text-cyan-600 hover:underline dark:text-cyan-400"
                  >
                    Ver Productos
                  </a>
                  <a
                    href="#"
                    @click.prevent="openEditModal(factura)"
                    class="text-blue-600 hover:underline dark:text-blue-400"
                  >
                    Editar
                  </a>
                  <a
                    href="#"
                    @click.prevent="openDeleteModal(factura)"
                    class="text-red-600 hover:underline dark:text-red-400"
                  >
                    Eliminar
                  </a>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Modal de edición -->
      <FacturaEditarView
        v-if="showEditModal"
        :factura="selectedFactura"
        @update="handleUpdate"
        @close="closeEditModal"
      />

      <!-- Modal de Eliminación -->
      <FacturaEliminarView
        v-if="showDeleteModal"
        :factura="selectedFactura"
        @update="handleDelete"
        @close="closeDeleteModal"
      />

      <!-- Modal de Productos -->
      <FacturaProductoLista
        v-if="showlistaProductosModal"
        :factura="selectedFactura"
        @close="closeProductosModal"
      />

      <!-- Modal de Agregar Productos -->
      <FacturaProductoAgregar
        v-if="agregarProductosModal"
        :factura="selectedFactura"
        @close="closeAgregarProductosModal"
      />
    </SectionMain>
  </LayoutAuthenticated>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import FacturaEditarView from './FacturaEditarView.vue';
import FacturaEliminarView from './FacturaEliminarView.vue';
import FacturaProductoLista from './FacturaProductoLista.vue';
import FacturaProductoAgregar from './FacturaProductoAgregar.vue';
import axios from 'axios';


// import { getFacturasByPage } from "@/services_brayan/FacturaService";

const facturas = ref([]);

// Importar el servicio para obtener  facturas
import { getAllFacturas } from "@/services/brayan_service/FacturacionService";

const fetchFacturas = async () => {
  try {
    const response = await getAllFacturas(); 
    facturas.value = response; 
  } catch (error) {
    console.error('Error al obtener facturas:', error.message);
    if (error.response) {
      console.error('Error en la respuesta:', error.response);
    }
  }
};

onMounted(() => {
  fetchFacturas();
});


const showEditModal = ref(false);
const showDeleteModal = ref(false);
const showlistaProductosModal = ref(false);
const agregarProductosModal = ref(false);
const selectedFactura = ref(null);

function openAgregarProductosModal(factura) {
  selectedFactura.value = factura;
  agregarProductosModal.value = true;
}

function openListaProductosModal(factura) {
  selectedFactura.value = factura;
  showlistaProductosModal.value = true;
}

function openEditModal(factura) {
  selectedFactura.value = factura;
  showEditModal.value = true;
}

function openDeleteModal(factura) {
  selectedFactura.value = factura;
  showDeleteModal.value = true;
}

function closeEditModal() {
  showEditModal.value = false;
}

function closeDeleteModal() {
  showDeleteModal.value = false;
}

function closeProductosModal() {
  showlistaProductosModal.value = false;
}

function closeAgregarProductosModal() {
  agregarProductosModal.value = false;
}

function handleUpdate() {
  // Lógica para actualizar la factura
  closeEditModal();
}

function handleDelete() {
  // Lógica para eliminar la factura
  closeDeleteModal();
}
</script>

<style scoped>
  table {
    table-layout: fixed; /* Hace que el width se respete */
    width: 100%; /* Asegura que la tabla use todo el ancho disponible */
  }
  th, td {
    white-space: nowrap; /* Evita que el contenido se rompa en múltiples líneas */
  }
  
</style>