<script setup>
import { ref } from 'vue';
import SectionMain from '@/components/SectionMain.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import FacturaEditarView from './FacturaEditarView.vue';
import FacturaEliminarView from './FacturaEliminarView.vue';

// Datos simulados, normalmente esto vendría de una API o un store
const datos_quemados = ref([
  {
    id_facturacion: 1,
    id_check_in: 101,
    subtotal: 100,
    impuestos: 21,
    total: 121,
    total_precio_productos: 80,
    metodo_pago: 'Tarjeta',
    estado: 'Pagado',
    fecha_salida: '2024-09-01',
    id_reserva: 201,
    medio_llegada: 'Avión',
    llegada_situacion: 'A tiempo',
    equipaje: 'Sí',
    fecha_reserva: '2024-08-30',
    empresa: 'Ejemplo S.A.',
    valor_deposito: 50,
    forma_pago: 'Transferencia',
    nombre_completo: 'Juan Pérez',
    numero_documento: '12345678A'
  },
  {
    id_facturacion: 2,
    id_check_in: 102,
    subtotal: 150,
    impuestos: 31.5,
    total: 181.5,
    total_precio_productos: 120,
    metodo_pago: 'Efectivo',
    estado: 'Pendiente',
    fecha_salida: '2024-09-02',
    id_reserva: 202,
    medio_llegada: 'Tren',
    llegada_situacion: 'Retrasado',
    equipaje: 'No',
    fecha_reserva: '2024-08-31',
    empresa: 'Hotel Lux',
    valor_deposito: 75,
    forma_pago: 'Efectivo',
    nombre_completo: 'Ana Gómez',
    numero_documento: '23456789B'
  },
  {
    id_facturacion: 3,
    id_check_in: 103,
    subtotal: 200,
    impuestos: 42,
    total: 242,
    total_precio_productos: 160,
    metodo_pago: 'Tarjeta',
    estado: 'Pagado',
    fecha_salida: '2024-09-03',
    id_reserva: 203,
    medio_llegada: 'Bus',
    llegada_situacion: 'A tiempo',
    equipaje: 'Sí',
    fecha_reserva: '2024-09-01',
    empresa: 'Grand Hotel',
    valor_deposito: 100,
    forma_pago: 'Tarjeta',
    nombre_completo: 'Carlos Martínez',
    numero_documento: '34567890C'
  },
  {
    id_facturacion: 4,
    id_check_in: 104,
    subtotal: 180,
    impuestos: 37.8,
    total: 217.8,
    total_precio_productos: 140,
    metodo_pago: 'Transferencia',
    estado: 'Pagado',
    fecha_salida: '2024-09-04',
    id_reserva: 204,
    medio_llegada: 'Avión',
    llegada_situacion: 'A tiempo',
    equipaje: 'Sí',
    fecha_reserva: '2024-09-02',
    empresa: 'Ocean View',
    valor_deposito: 90,
    forma_pago: 'Transferencia',
    nombre_completo: 'Marta Ruiz',
    numero_documento: '45678901D'
  },
  {
    id_facturacion: 5,
    id_check_in: 105,
    subtotal: 130,
    impuestos: 27.3,
    total: 157.3,
    total_precio_productos: 110,
    metodo_pago: 'Efectivo',
    estado: 'Pendiente',
    fecha_salida: '2024-09-05',
    id_reserva: 205,
    medio_llegada: 'Tren',
    llegada_situacion: 'A tiempo',
    equipaje: 'No',
    fecha_reserva: '2024-09-03',
    empresa: 'City Hotel',
    valor_deposito: 65,
    forma_pago: 'Efectivo',
    nombre_completo: 'Luis Fernández',
    numero_documento: '56789012E'
  },
  {
    id_facturacion: 2111,
    id_check_in: 3453,
    subtotal: 2233,
    impuestos: 1113.2,
    total: 266.2,
    total_precio_productos: 180,
    metodo_pago: 'Tarjeta',
    estado: 'Pagado',
    fecha_salida: '2024-09-06',
    id_reserva: 206,
    medio_llegada: 'Bus',
    llegada_situacion: 'Retrasado',
    equipaje: 'Sí',
    fecha_reserva: '2024-09-04',
    empresa: 'Skyline Hotel',
    valor_deposito: 110,
    forma_pago: 'Tarjeta',
    nombre_completo: 'Sofía López',
    numero_documento: '67890123F'
  },
  {
    id_facturacion: 5,
    id_check_in: 343,
    subtotal: 235425,
    impuestos: 32434.2,
    total: 266.2,
    total_precio_productos: 180,
    metodo_pago: 'Tarjeta',
    estado: 'Pagado',
    fecha_salida: '2024-09-06',
    id_reserva: 206,
    medio_llegada: 'Bus',
    llegada_situacion: 'Retrasado',
    equipaje: 'Sí',
    fecha_reserva: '2024-09-04',
    empresa: 'Skyline Hotel',
    valor_deposito: 110,
    forma_pago: 'Tarjeta',
    nombre_completo: 'Sofía López',
    numero_documento: '67890123F'
  },
  {
    id_facturacion: 32,
    id_check_in: 234,
    subtotal: 2342,
    impuestos: 46.2,
    total: 266.2,
    total_precio_productos: 180,
    metodo_pago: 'Tarjeta',
    estado: 'Pagado',
    fecha_salida: '2024-09-06',
    id_reserva: 206,
    medio_llegada: 'Bus',
    llegada_situacion: 'Retrasado',
    equipaje: 'Sí',
    fecha_reserva: '2024-09-04',
    empresa: 'Skyline Hotel',
    valor_deposito: 110,
    forma_pago: 'Tarjeta',
    nombre_completo: 'Sofía López',
    numero_documento: '67890123F'
  },
  {
    id_facturacion: 44,
    id_check_in: 34,
    subtotal: 4434,
    impuestos: 4634.2,
    total: 2646.2,
    total_precio_productos: 180,
    metodo_pago: 'Tarjeta',
    estado: 'Pagado',
    fecha_salida: '2024-09-06',
    id_reserva: 206,
    medio_llegada: 'Bus',
    llegada_situacion: 'Retrasado',
    equipaje: 'Sí',
    fecha_reserva: '2024-09-04',
    empresa: 'Skyline Hotel',
    valor_deposito: 110,
    forma_pago: 'Tarjeta',
    nombre_completo: 'Sofía López',
    numero_documento: '67890123F'
  }
]);


const showEditModal = ref(false);
const showDeleteModal = ref(false);
const selectedFactura = ref(null);

const openEditModal = (factura) => {
  selectedFactura.value = { ...factura }; // Clona el objeto para editar
  showEditModal.value = true;
};

const openDeleteModal = (factura) => {
  selectedFactura.value = { ...factura }; // Clona el objeto para eliminar
  showDeleteModal.value = true;
};

const handleUpdate = () => {
  showEditModal.value = false;
  // Aquí puedes actualizar los datos en el componente si es necesario
};

const handleDelete = () => {
  showDeleteModal.value = false;
  // Aquí puedes eliminar los datos en el componente si es necesario
};

const closeEditModal = () => {
  showEditModal.value = false;
};

const closeDeleteModal = () => {
  showDeleteModal.value = false;
};
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain class="bg-blue-100 rounded-lg p-4">
      <h1 class="text-black font-bold mb-8">Historial de Facturas</h1>
      <div class="grid grid-cols-5 gap-2 py-2">
            
            <input type="search" placeholder="Buscar factura por ID" class="rounded rounded-lg">
            <button type="button" class="bg-blue-800 rounded rounded-lg text-white">Buscar</button>
           
        </div>
      <!-- Contenedor con scroll horizontal y vertical -->
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
    </SectionMain>
  </LayoutAuthenticated>
</template>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  text-align: left;
  white-space: nowrap; 
}

th {
  background-color: #f4f4f4;
}

h1 {
  font-size: 1.5rem;
}
</style>
