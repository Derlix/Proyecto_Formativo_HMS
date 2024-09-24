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
                <tr v-for="(producto, index) in productos" :key="producto.factura_producto.id_factura_producto"
                    :class="{'bg-blue-50': index % 2 === 0, 'bg-white': index % 2 !== 0}">
                  <td class="px-2 py-1 dark:text-dark">{{ props.factura?.id_facturacion }}</td>
                  <td class="px-2 py-1 dark:text-dark">{{ producto.factura_producto.id_factura_producto}}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.factura_producto?.id_producto || 'N/A' }}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.factura_producto?.cantidad || 'N/A' }}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.factura_producto?.precio_unitario || 'N/A' }}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.productos?.nombre_producto || 'N/A' }}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.productos?.descripcion || 'N/A' }}</td>
                  <td class="px-4 py-1 dark:text-dark">{{ producto.productos?.precio_actual || 'N/A' }}</td>
                  <td class="px-4 py-1">
                    <div class="flex justify-center space-x-2">
                      <a href="#" @click.prevent="openEditModal(producto)" class="hover:underline text-blue-600 dark:text-blue-600 font-bold">Editar</a>
                      <a href="#" @click.prevent="openDeleteModal(producto)" class="hover:underline text-red-600 dark:text-red-600 font-bold">Eliminar</a>
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
            @save="handleUpdate"
          />

          <!-- Modal para eliminar producto -->
          <ProductoFacturaEliminar
            v-if="showDeleteModal"
            :producto="selectedProduct"
            @close="closeDeleteModal"
            @delete="handleDelete"
          />

        </div>
      </div>
    </SectionMain>
  </LayoutAuthenticated>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import ProductoFacturaEditar from './ProductoFacturaEditar.vue';
import ProductoFacturaEliminar from './ProductoFacturaEliminar.vue';
import { getProductosFacturaById } from "@/services/brayan_service/FacturaProductoService";


const props = defineProps({
  factura: Object,
});

const productos = ref([]);
const selectedProduct = ref(null);

const fetchProductos = async () => {
  try {
    if (props.factura && props.factura.id_facturacion) {
      const response = await getProductosFacturaById(props.factura.id_facturacion);
      console.log(response); // Verifica la estructura de la respuesta
      if (response && response.productos) {
        productos.value = response.productos; // Asegúrate de asignar la lista de productos
      } else {
        console.error('No se encontraron productos en la respuesta:', response);
      }
    }
  } catch (error) {
    console.error('Error al obtener productos de la factura:', error);
  }
};

watch(() => props.factura, fetchProductos, { immediate: true });






const showDeleteModal = ref(false);
const showEditModal = ref(false);

const openEditModal = (producto) => {
  if (producto && producto.factura_producto) {
    selectedProduct.value = { ...producto };
    showEditModal.value = true;
  } else {
    console.error('Producto no válido:', producto);
  }
};

const openDeleteModal = (producto) => {
  if (producto && producto.factura_producto && producto.factura_producto.id_factura_producto) {
    selectedProduct.value = { ...producto };
    showDeleteModal.value = true;
  } else {
    console.error('Producto no válido:', producto);
  }
};



const closeEditModal = () => {
  showEditModal.value = false;
};

const closeDeleteModal = () => {
  showDeleteModal.value = false;
};


async function handleUpdate() {
  try {
    await fetchProductos(); 
    
    closeEditModal(); 
  } catch (error) {
   
    console.error('Error al actualizar la factura:', error);
  }
}



async function handleDelete() {
  try {
    await fetchProductos();  
    closeDeleteModal();   
  } catch (error) {
    alert('Error al eliminar el producto de la factura:', error);
  }
}


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
