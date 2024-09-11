<template>
  <LayoutAuthenticated>
    <SectionMain>
     
      <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-75">
        <div class="bg-blue-100 p-6 rounded-lg shadow-lg w-4/5 max-w-4xl">
          <h1 class="text-2xl font-bold text-gray-800 mb-8">Historial de Productos de la Factura</h1>
          
          <div class="relative overflow-x-auto shadow-md sm:rounded-lg max-h-96 overflow-y-auto">
            <table class="min-w-full text-sm text-left divide-y divide-gray-100 bg-blue-50" style="table-layout: auto;">
              <thead class="text-xs text-gray-700 uppercase bg-blue-100 dark:bg-gray-400 dark:text-gray-400">
                <tr>
                  <th class="px-2 py-2">ID Facturación</th>
                  <th class="px-2 py-2">ID Factura Producto</th>
                  <th class="px-4 py-2">ID Producto</th>
                  <th class="px-4 py-2">Cantidad</th>
                  <th class="px-4 py-2">Precio U</th>
                  <th class="px-4 py-2">Nombre</th>
                  <th class="px-4 py-2">Descripción</th>
                  <th class="px-4 py-2">Precio Actual</th>
                  <th class="px-4 py-2">Acciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(producto, index) in datos_productos" :key="producto.id_factura_producto"
                    :class="{'bg-blue-50': index % 2 === 0, 'bg-white': index % 2 !== 0}">
                  <td class="px-2 py-1 dark:text-dark">{{ producto.id_facturacion }}</td>
                  <td class="px-2 py-1 dark:text-dark">{{ producto.id_factura_producto }}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.id_producto }}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.cantidad }}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.precio_unitario }}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.nombre }}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.descripcion }}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.precio_actual }}</td>
                  <td class="px-4 py-1">
                    <div class="flex justify-center space-x-2">
                      <a href="#" @click.prevent="openEditModal(producto)" class="} hover:underline  text-blue-600  dark:text-blue-600 font-bold">Editar</a>
                      <a href="#" @click.prevent="openDeleteModal(producto)" class="}hover:underline  text-red-600  dark:text-red-600 font-bold">Eliminar</a>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="flex justify-end mt-4">
            <button @click="$emit('close')" class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600 transition">Cerrar</button>
          </div>

          <!-- Modal para editar producto -->
          <ProductoFacturaEditar
            v-if="showEditModal"
            :producto="selectedProduct"
            @close="closeEditModal"
            @save="saveProductEdits"
          />

          <!-- Modal para eliminar producto -->
          <ProductoFacturaEliminar
            v-if="showDeleteModal"
            :producto="selectedProduct"
            @close="closeDeleteModal"
            @save="handleDelete"
          />
        </div>
      </div>
    </SectionMain>
  </LayoutAuthenticated>
</template>

<script setup>
import { ref } from 'vue';
import ProductoFacturaEditar from './ProductoFacturaEditar.vue';
import ProductoFacturaEliminar from './ProductoFacturaEliminar.vue';


const datos_productos = ref([
  {
    id_facturacion: 1,
    id_factura_producto: 1,
    id_producto: 'P001',
    cantidad: 2,
    precio_unitario: 10.0,
    nombre: 'Producto A',
    descripcion: 'Descripción del producto A',
    precio_actual: 20.0
  },
  {
    id_facturacion: 1,
    id_factura_producto: 2,
    id_producto: 'P002',
    cantidad: 1,
    precio_unitario: 15.0,
    nombre: 'Producto B',
    descripcion: 'Descripción del producto B',
    precio_actual: 15.0
  }
]);

const showDeleteModal = ref(false);
const showEditModal = ref(false);
const selectedProduct = ref(null);

const openEditModal = (producto) => {
  selectedProduct.value = { ...producto };
  showEditModal.value = true;
};

const openDeleteModal = (producto) => {
  selectedProduct.value = { ...producto };
  showDeleteModal.value = true;
};

const closeEditModal = () => {
  showEditModal.value = false;
};

const closeDeleteModal = () => {
  showDeleteModal.value = false;
};

const saveProductEdits = (updatedProduct) => {
  const index = datos_productos.value.findIndex(p => p.id_factura_producto === updatedProduct.id_factura_producto);
  if (index !== -1) {
    datos_productos.value[index] = { ...datos_productos.value[index], ...updatedProduct };
  }
};

const handleDelete = (factura) => {
  // Logic to delete factura from the list
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  text-align: left;
  white-space: nowrap;
  border: 1px solid #e2e8f0;
  font-size: small;
  color: #000000;
}

th {
  background-color: #e0f2f1; /* Azul claro para las cabeceras */
  color: #000000;
}

tbody tr:nth-child(even) {
  background-color: #e5f6f8; /* Azul claro para filas alternadas */
}

/* Estilo de los botones */
button {
  transition: background-color 0.3s;
}

h1 {
  font-size: 1.5rem;
  color: #00030a;
}

.fixed {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
