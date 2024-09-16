<script setup>
import SectionMain from '@/components/SectionMain.vue'
import BaseButtons from '@/components/BaseButtons.vue';
import BaseButton from '@/components/BaseButton.vue';
import { mdiBookEdit, mdiTrashCan } from '@mdi/js'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import { ref } from 'vue';
import { getProductsByPage, createProduct, updateProduct, deleteProduct } from '../../services/productService.js'

const productos = ref([]);
const currentProduct = ref({});
const currentPage = ref(1);
const TotalPages = ref(0);
const isEditMode = ref(false);
const visible = ref(false);
const isDelete = ref(false);
const descripcion = ref('');
const textBoton = ref('');

const fechtProducts = async () => {
  try {
    const response = await getProductsByPage(currentPage.value);
    productos.value = response.data.productos;
    TotalPages.value = response.data.total_pages;
  } catch (error) {
    alert('Error al obtener productos: ', error);
  }
};

const createProducto = async () => {
  try {
    await createProduct(currentProduct.value.nombre, currentProduct.value.descripcion, currentProduct.value.precio);
    alert('Producto creado exitosamente');
    fechtProducts();
    closeModal();
  } catch (error) {
    alert('Error al insertar producto: ', error);
  }
};

const updateProducto = async () => {
  try {
    await updateProduct(currentProduct.value.id_producto, currentProduct.value.nombre, currentProduct.value.descripcion, currentProduct.value.precio);
    alert('Producto actualizado exitosamente');
    fechtProducts();
    closeModal();
  } catch (error) {
    alert('Error al actualizar producto: ', error);
  }
};

const eliminarProducto = async (id_producto) => {
  if (confirm('¿Estás seguro de que deseas eliminar este producto?')) {
    try {
      await deleteProduct(id_producto);
      alert('Producto eliminado exitosamente');
      fechtProducts(); // Refresca la lista de productos después de eliminar
    } catch (error) {
      alert('Error al eliminar el producto:', error);
    }
  }
};

const openModal = (action, producto = {}) => {
  if (action === 'create') {
    isEditMode.value = false;
    isDelete.value = false;
    descripcion.value = 'Crear Producto';
    textBoton.value = 'Crear';
    currentProduct.value = { nombre: '', descripcion: '', precio: '' };
  } else if (action === 'update') {
    isEditMode.value = true;
    isDelete.value = false;
    descripcion.value = 'Actualizar Producto';
    textBoton.value = 'Actualizar';
    currentProduct.value = { ...producto };
  } else if (action === 'delete') {
    isEditMode.value = false;
    isDelete.value = true;
    descripcion.value = 'Eliminar Producto';
    textBoton.value = 'Eliminar';
    currentProduct.value = { ...producto };
  }
  visible.value = true;
};

const closeModal = () => {
  visible.value = false;
};

fechtProducts();
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain class="bg-blue-100 rounded-lg">
        <h1 class="text-black font-bold mb-8">Administrador de productos</h1>
            <div class="grid grid-cols-4 gap-2">
                <button @click="openModal('create')" class="bg-blue-800 rounded-lg text-white">Crear Producto</button>
                <span></span>
                <div class="grid grid-cols-5 col-span-2">
                    <input type="search" placeholder="Buscar Producto" class="rounded-l-md col-span-4">
                    <button class="bg-blue-800 p-1 text-white rounded-r-md hover:text-black focus:outline-none">
                        <i class="mdi mdi-magnify text-xl"></i>
                    </button>
                </div>
            </div>

            <table>
                <thead>
                <tr>
                    <th>Id</th>
                    <th>Nombre</th>
                    <th>Descripcion</th>
                    <th>Precio</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="producto in productos" :key="producto.id_producto">
                    <td>{{ producto.id_producto }}</td>
                    <td>{{ producto.nombre_producto }}</td>
                    <td>{{ producto.descripcion }}</td>
                    <td>{{ producto.precio_actual }}</td>
                    <td class="before:hidden lg:w-1 whitespace-nowrap">
                    <BaseButtons type="justify-start lg:justify-end" no-wrap>
                        <BaseButton color="info" :icon="mdiBookEdit" small @click="openModal('update', producto)" />
                        <BaseButton color="danger" :icon="mdiTrashCan" small @click="eliminarProducto(producto.id_producto)" />
                    </BaseButtons>
                    </td>
                </tr>
            </tbody>
        </table>

      <!-- Paginación -->
      <div class="flex items-center justify-center space-x-4 py-4">
        <button class="bg-blue-500 text-white font-semibold py-2 px-4 rounded hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed" @click="PrevPage" :disabled="currentPage === 1">Anterior</button>
        <span class="text-gray-700 font-medium">Página {{ currentPage }} de {{ TotalPages }}</span>
        <button class="bg-blue-500 text-white font-semibold py-2 px-4 rounded hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed" @click="nextPage" :disabled="currentPage === TotalPages">Siguiente</button>
      </div>

      <!-- Modal de Crear/Actualizar/Eliminar -->
      <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
        <div class="bg-blue-100 p-6 rounded-lg shadow-lg max-w-2xl w-full">
          <p class="text-black mb-4 rounded border-opacity-10 font-bold text-2xl text-center pt-3 pb-2">{{ descripcion }}</p>
          <div class="p-6">
            <form @submit.prevent="isEditMode ? updateProducto() : createProducto()">
              <div class="grid grid-cols-2 gap-3">
                <div class="mb-4">
                  <label for="nombre" class="block text-gray-700">Nombre del producto</label>
                  <input v-model="currentProduct.nombre" :disabled="isDelete" type="text" id="nombre" class="w-full px-3 py-2 border rounded" required />
                </div>
                <div class="mb-4">
                  <label for="precio" class="block text-gray-700">Precio</label>
                  <input v-model="currentProduct.precio" :disabled="isDelete" type="number" step="0.01" id="precio" class="w-full px-3 py-2 border rounded" required />
                </div>
              </div>
              <div class="mb-4">
                <label for="descripcion" class="block text-gray-700">Descripción</label>
                <input v-model="currentProduct.descripcion" :disabled="isDelete" type="text" id="descripcion" class="w-full px-3 py-2 border rounded h-16" required />
              </div>
              <div class="flex justify-center space-x-4">
                <button type="submit" class="bg-green-800 text-white px-4 py-2 rounded">{{ textBoton }}</button>
                <button type="button" class="bg-red-500 text-white px-4 py-2 rounded" @click="closeModal">Cancelar</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </SectionMain>
  </LayoutAuthenticated>
</template>
