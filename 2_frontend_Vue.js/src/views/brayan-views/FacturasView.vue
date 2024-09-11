<template>
  <LayoutAuthenticated>
    <SectionMain class="bg-blue-100 rounded-lg p-4">
      <h1 class="text-black font-bold mb-8">Historial de Facturas</h1>
      <div class="grid grid-cols-5 gap-2 py-2">
        <input type="search" placeholder="Buscar factura por ID" class="rounded rounded-lg">
        <button type="button" class="bg-blue-800 rounded rounded-lg text-white">Buscar</button>
      </div>

      <div class="overflow-auto" style="max-height: 500px;">
        <table class="min-w-full bg-white border border-gray-300">
          <thead>
            <tr>
              <th class="border-b px-1 py-2">ID Facturación</th>
              <th class="border-b px-4 py-2">ID Check-in</th>
              <th class="border-b px-10 py-2">Subtotal</th>
              <th class="border-b px-10 py-2">Impuestos</th>
              <th class="border-b px-10 py-2">Total</th>
              <th class="border-b px-1 py-2">Total Precio Productos</th>
              <th class="border-b px-6 py-2">Método de Pago</th>
              <th class="border-b px-6 py-2">Estado</th>
              <th class="border-b px-10 py-2">Fecha Salida</th>
              <th class="border-b px-4 py-2">ID Reserva</th>
              <th class="border-b px-4 py-2">Medio Llegada</th>
              <th class="border-b px-4 py-2">Llegada Situación</th>
              <th class="border-b px-4 py-2">Equipaje</th>
              <th class="border-b px-4 py-2">Fecha Reserva</th>
              <th class="border-b px-4 py-2">Empresa</th>
              <th class="border-b px-4 py-2">Valor Depósito</th>
              <th class="border-b px-4 py-2">Forma de Pago</th>
              <th class="border-b px-4 py-2">Nombre Completo</th>
              <th class="border-b px-4 py-2">Número Documento</th>
              <th class="border-b px-4 py-2">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="body in datos_quemados" :key="body.id_facturacion">
              <td class="border-b px-4 py-2">{{ body.id_facturacion }}</td>
              <td class="border-b px-4 py-2">{{ body.id_check_in }}</td>
              <td class="border-b px-4 py-2">{{ body.subtotal }}</td>
              <td class="border-b px-4 py-2">{{ body.impuestos }}</td>
              <td class="border-b px-4 py-2">{{ body.total }}</td>
              <td class="border-b px-4 py-2">{{ body.total_precio_productos }}</td>
              <td class="border-b px-4 py-2">{{ body.metodo_pago }}</td>
              <td class="border-b px-4 py-2">{{ body.estado }}</td>
              <td class="border-b px-4 py-2">{{ body.fecha_salida }}</td>
              <td class="border-b px-4 py-2">{{ body.id_reserva }}</td>
              <td class="border-b px-4 py-2">{{ body.medio_llegada }}</td>
              <td class="border-b px-4 py-2">{{ body.llegada_situacion }}</td>
              <td class="border-b px-4 py-2">{{ body.equipaje }}</td>
              <td class="border-b px-4 py-2">{{ body.fecha_reserva }}</td>
              <td class="border-b px-4 py-2">{{ body.empresa }}</td>
              <td class="border-b px-4 py-2">{{ body.valor_deposito }}</td>
              <td class="border-b px-4 py-2">{{ body.forma_pago }}</td>
              <td class="border-b px-4 py-2">{{ body.nombre_completo }}</td>
              <td class="border-b px-4 py-2">{{ body.numero_documento }}</td>
              <td class="px-6 py-4 text-center">
                <a href="#" @click.prevent="openAgregarProductosModal(body)" class="font-medium text-violet-600 hover:underline mr-3">Agregar Productos</a>
                <a href="#" @click.prevent="openListaProductosModal(body)" class="font-medium text-cyan-600 hover:underline mr-3">Ver Productos</a>
                <a href="#" @click.prevent="openEditModal(body)" class="font-medium text-blue-600 hover:underline mr-3">Editar</a>
                <a href="#" @click.prevent="openDeleteModal(body)" class="font-medium text-red-600 hover:underline">Eliminar</a>
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
import { ref } from 'vue';
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import FacturaEditarView from './FacturaEditarView.vue';
import FacturaEliminarView from './FacturaEliminarView.vue';
import FacturaProductoLista from './FacturaProductoLista.vue';
import FacturaProductoAgregar from './FacturaProductoAgregar.vue';

// Datos simulados
const datos_quemados = ref([
  {
    id_facturacion: 1,
    id_check_in: 'CI001',
    subtotal: 100.0,
    impuestos: 20.0,
    total: 120.0,
    total_precio_productos: 90.0,
    metodo_pago: 'Tarjeta de Crédito',
    estado: 'Pagado',
    fecha_salida: '2024-09-01',
    id_reserva: 'R001',
    medio_llegada: 'Avión',
    llegada_situacion: 'A tiempo',
    equipaje: '1 maleta',
    fecha_reserva: '2024-08-01',
    empresa: 'Hotel XYZ',
    valor_deposito: 50.0,
    forma_pago: 'Transferencia',
    nombre_completo: 'Juan Pérez',
    numero_documento: '12345678'
  },
  {
    id_facturacion: 2,
    id_check_in: 'CI002',
    subtotal: 150.0,
    impuestos: 30.0,
    total: 180.0,
    total_precio_productos: 140.0,
    metodo_pago: 'Efectivo',
    estado: 'Pendiente',
    fecha_salida: '2024-09-05',
    id_reserva: 'R002',
    medio_llegada: 'Bus',
    llegada_situacion: 'Retrasado',
    equipaje: '2 maletas',
    fecha_reserva: '2024-08-15',
    empresa: 'Hotel ABC',
    valor_deposito: 70.0,
    forma_pago: 'Efectivo',
    nombre_completo: 'Ana Gómez',
    numero_documento: '87654321'
  },
  
  {
    id_facturacion: 3,
    id_check_in: 'CI003',
    subtotal: 200.0,
    impuestos: 40.0,
    total: 240.0,
    total_precio_productos: 190.0,
    metodo_pago: 'Tarjeta de Débito',
    estado: 'Pagado',
    fecha_salida: '2024-09-10',
    id_reserva: 'R003',
    medio_llegada: 'Taxi',
    llegada_situacion: 'A tiempo',
    equipaje: '1 maleta',
    fecha_reserva: '2024-08-20',
    empresa: 'Hotel DEF',
    valor_deposito: 100.0,
    forma_pago: 'Tarjeta de Débito',
    nombre_completo: 'Carlos Ruiz',
    numero_documento: '11223344'
  },
  {
    id_facturacion: 4,
    id_check_in: 'CI004',
    subtotal: 250.0,
    impuestos: 50.0,
    total: 300.0,
    total_precio_productos: 240.0,
    metodo_pago: 'Transferencia',
    estado: 'Pagado',
    fecha_salida: '2024-09-15',
    id_reserva: 'R004',
    medio_llegada: 'Avión',
    llegada_situacion: 'A tiempo',
    equipaje: '3 maletas',
    fecha_reserva: '2024-08-25',
    empresa: 'Hotel GHI',
    valor_deposito: 120.0,
    forma_pago: 'Transferencia',
    nombre_completo: 'Laura Martínez',
    numero_documento: '55667788'
  },
  {
    id_facturacion: 5,
    id_check_in: 'CI002',
    subtotal: 150.0,
    impuestos: 30.0,
    total: 180.0,
    total_precio_productos: 140.0,
    metodo_pago: 'Efectivo',
    estado: 'Pendiente',
    fecha_salida: '2024-09-05',
    id_reserva: 'R002',
    medio_llegada: 'Bus',
    llegada_situacion: 'Retrasado',
    equipaje: '2 maletas',
    fecha_reserva: '2024-08-15',
    empresa: 'Hotel ABC',
    valor_deposito: 70.0,
    forma_pago: 'Efectivo',
    nombre_completo: 'Ana Gómez',
    numero_documento: '87654321'
  }
  ,
  {
    id_facturacion: 5,
    id_check_in: 'CI002',
    subtotal: 150.0,
    impuestos: 30.0,
    total: 180.0,
    total_precio_productos: 140.0,
    metodo_pago: 'Efectivo',
    estado: 'Pendiente',
    fecha_salida: '2024-09-05',
    id_reserva: 'R002',
    medio_llegada: 'Bus',
    llegada_situacion: 'Retrasado',
    equipaje: '2 maletas',
    fecha_reserva: '2024-08-15',
    empresa: 'Hotel ABC',
    valor_deposito: 70.0,
    forma_pago: 'Efectivo',
    nombre_completo: 'Ana Gómez',
    numero_documento: '87654321'
  },
  {
    id_facturacion: 5,
    id_check_in: 'CI002',
    subtotal: 150.0,
    impuestos: 30.0,
    total: 180.0,
    total_precio_productos: 140.0,
    metodo_pago: 'Efectivo',
    estado: 'Pendiente',
    fecha_salida: '2024-09-05',
    id_reserva: 'R002',
    medio_llegada: 'Bus',
    llegada_situacion: 'Retrasado',
    equipaje: '2 maletas',
    fecha_reserva: '2024-08-15',
    empresa: 'Hotel ABC',
    valor_deposito: 70.0,
    forma_pago: 'Efectivo',
    nombre_completo: 'Ana Gómez',
    numero_documento: '87654321'
  },
  {
    id_facturacion: 5,
    id_check_in: 'CI002',
    subtotal: 150.0,
    impuestos: 30.0,
    total: 180.0,
    total_precio_productos: 140.0,
    metodo_pago: 'Efectivo',
    estado: 'Pendiente',
    fecha_salida: '2024-09-05',
    id_reserva: 'R002',
    medio_llegada: 'Bus',
    llegada_situacion: 'Retrasado',
    equipaje: '2 maletas',
    fecha_reserva: '2024-08-15',
    empresa: 'Hotel ABC',
    valor_deposito: 70.0,
    forma_pago: 'Efectivo',
    nombre_completo: 'Ana Gómez',
    numero_documento: '87654321'
  }
  
]);

const showEditModal = ref(false);
const showDeleteModal = ref(false);
const showlistaProductosModal = ref(false);
const agregarProductosModal = ref(false);
const selectedFactura = ref(null);

const openEditModal = (factura) => {
  selectedFactura.value = factura;
  showEditModal.value = true;
};

const closeEditModal = () => {
  showEditModal.value = false;
};

const openDeleteModal = (factura) => {
  selectedFactura.value = factura;
  showDeleteModal.value = true;
};

const closeDeleteModal = () => {
  showDeleteModal.value = false;
};

const openListaProductosModal = (factura) => {
  selectedFactura.value = factura;
  showlistaProductosModal.value = true;
};

const closeProductosModal = () => {
  showlistaProductosModal.value = false;
};

const openAgregarProductosModal = (factura) => {
  selectedFactura.value = factura;
  agregarProductosModal.value = true;
};

const closeAgregarProductosModal = () => {
  agregarProductosModal.value = false;
};

const handleUpdate = (updatedFactura) => {
  // Logic to update factura in the list
};

const handleDelete = (factura) => {
  // Logic to delete factura from the list
};
</script>
<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  background-color: #ffffff; /* Fondo blanco para toda la tabla */
  color: #000000; /* Texto negro */
}

th, td {
  text-align: left;
  white-space: nowrap;
  border: 1px solid #000000; /* Bordes negros */
}

th {
  background-color: #f0f0f0; /* Fondo gris claro para las cabeceras */
}

tbody tr:nth-child(even) {
  background-color: #f9f9f9; /* Fondo gris claro para filas alternadas */
}

tbody tr:nth-child(odd) {
  background-color: #ffffff; /* Fondo blanco para filas alternadas */
}

h1 {
  font-size: 1.5rem;
}
</style>

