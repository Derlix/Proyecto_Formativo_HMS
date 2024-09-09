<template>
    <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
      <div class="bg-white p-6 rounded-lg shadow-lg w-4/5 max-w-4xl">
        <h1 class="text-xl font-bold mb-4">Historial de Productos de la Factura</h1>
        <div class="overflow-auto" style="max-height: 500px;">
          <table class="min-w-full bg-white border border-gray-300">
            <thead>
              <tr>
                <th class="border-b px-1 py-2">ID Facturación</th>
                <th class="border-b px-1 py-2">ID Factura Producto</th>
                <th class="border-b px-5 py-2">ID Producto</th>
                <th class="border-b px-3 py-2">Cantidad</th>
                <th class="border-b px-4 py-2">Precio U</th>
                <th class="border-b px-8 py-2">Nombre</th>
                <th class="border-b px-8 py-2">Descripción</th>
                <th class="border-b px-4 py-2">Precio Actual</th>
                <th class="border-b px-4 py-2">Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="producto in datos_productos" :key="producto.id_factura_producto">
                <td class="border-b px-4 py-2">{{ producto.id_facturacion }}</td>
                <td class="border-b px-4 py-2">{{ producto.id_factura_producto }}</td>
                <td class="border-b px-4 py-2">{{ producto.id_producto }}</td>
                <td class="border-b px-4 py-2">{{ producto.cantidad }}</td>
                <td class="border-b px-4 py-2">{{ producto.precio_unitario }}</td>
                <td class="border-b px-4 py-2">{{ producto.nombre }}</td>
                <td class="border-b px-4 py-2">{{ producto.descripcion }}</td>
                <td class="border-b px-4 py-2">{{ producto.precio_actual }}</td>
                <td class="border-b px-4 py-2">
                  <a href="#" @click.prevent="openEditModal(producto)" class="font-medium text-blue-600 hover:underline mr-3">Editar</a>
                  <a href="#"  @click.prevent="openDeleteModal(producto)" class="font-medium text-red-600 hover:underline">Eliminar</a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="flex justify-end mt-4">
          <button @click="$emit('close')" class="bg-gray-500 text-white px-4 py-2 rounded mr-2">Cerrar</button>
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
  </template>
  
  <script setup>
  import { ref, watch } from 'vue';
  import ProductoFacturaEditar from './ProductoFacturaEditar.vue';
  import ProductoFacturaEliminar from './ProductoFacturaEliminar.vue';
  
  // Props y datos
  const props = defineProps({
    factura: Object,
  });
  
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
  
  // Watch prop changes
  watch(() => props.factura, (newFactura) => {
    datos_productos.value = newFactura.datos_productos || [];
  });
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
    font-size: small;
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
    color: #000000;
  }
  </style>
  