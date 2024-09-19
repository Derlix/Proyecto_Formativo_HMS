<script setup>
import { ref, onMounted } from 'vue'
import { mdiFileEdit, mdiTrashCan } from '@mdi/js'
import CardBoxModal from '@/components/CardBoxModal.vue'
import ModalAlert from '../ModalAlert.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import { getProductsByPage, deleteProduct, updateProduct } from '@/services/productService';

defineProps({
  checkable: Boolean
});

const productos = ref([]);
const currentProduct = ref({});
const TotalPages = ref(0);
const isEditMode = ref(false);
const activarModalEdit = ref(false);
const currentPage = ref(1);
const isModalVisible = ref(false);
const modalMessage = ref('');

const activarModalDelete = ref({
  visible: false,
  huesped: null
});

const fechtProducts = async () => {
  try {
    const response = await getProductsByPage(currentPage.value);
    productos.value = response.data.productos;
    TotalPages.value = response.data.total_pages;
  } catch (error) {
    alert('Error al obtener productos: ', error);
  }
};

const openEditModal = (producto = {}) => {
  isEditMode.value = true;
  currentProduct.value = { ...producto };
  activarModalEdit.value = true;
};

const update_Product = async () => {
  try {
    await updateProduct(
      currentProduct.value.id_producto,
      currentProduct.value.nombre_producto,
      currentProduct.value.descripcion,
      currentProduct.value.precio_actual
    );
    alert('Producto actualizado exitosamente');
    fechtProducts();
  } catch (error) {
    alert(error.data.detail);
  }
};

const openDeleteModal = (producto) => {
  activarModalDelete.value = {
    visible: true,
    producto: producto
  };
};

const confirmDelete = async () => {
  const producTem = activarModalDelete.value.producto;

  try {
    await deleteProduct(producTem.id_producto);
    alert('Producto Eliminado Con Exito');
    fechtProducts();
    activarModalDelete.value.visible = false;
  } catch (error) {
    console.error('Error al eliminar el Producto:', error);
    alert('Hubo un problema al intentar eliminar el producto.');
  }
};

const cancelDelete = () => {
  activarModalDelete.value.visible = false;
};

onMounted(() => {
  fechtProducts();
});
</script>

<template>
  <CardBoxModal v-model="activarModalEdit" title="Editar Producto">
    <form @submit.prevent="update_Product()">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="mb-4">
          <label for="nombre" class="block text-gray-700 font-medium">Nombre:</label>
          <input type="text" id="nombre" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm" v-model="currentProduct.nombre_producto" required/>
        </div>
        <div class="mb-4">
          <label for="precio" class="block text-gray-700 font-medium">Precio:</label>
          <input type="text" id="precio" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm" v-model="currentProduct.precio_actual" required/>
        </div>
        <div class="mb-4">
          <label for="descripcion" class="block text-gray-700 font-medium">Descripcion:</label>
          <input type="text" id="descripcion" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm" v-model="currentProduct.descripcion" required/>
        </div>
      </div>
      <div class="mt-2">
        <BaseButton type="submit" label="Guardar cambios" color="info" small/>
      </div>
    </form>
  </CardBoxModal>

  <CardBoxModal v-model="activarModalDelete.visible" v-if="activarModalDelete.producto" title="Eliminar Producto" buttonLabel="Eliminar" button="danger" has-cancel @confirm="confirmDelete" @cancel="cancelDelete">
    <p class="text-xl">¿Está seguro de eliminar el producto?</p>
    <li><b>{{ activarModalDelete.producto.nombre_producto }}</b></li>
    <li><b>{{ activarModalDelete.producto.descripcion }}</b></li>
    <li><b>{{ activarModalDelete.producto.precio_actual }}</b></li>
  </CardBoxModal>

  <table>
    <thead>
      <tr>
        <th v-if="checkable"/>
        <th/>
        <th>Nombre</th>
        <th>Descripcion</th>
        <th>Precio</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="producto in productos" :key="producto.id_producto">
        <td class="border-b-0 lg:w-6 before:hidden"></td>
        <td data-label="Nombre: ">{{ producto.nombre_producto }}</td>
        <td data-label="Descripcion: ">{{ producto.descripcion }}</td>
        <td data-label="Precio: ">{{ producto.precio_actual }}</td>
        <td class="before:hidden lg:w-1 whitespace-nowrap">
          <BaseButtons type="justify-start lg:justify-end" no-wrap>
            <BaseButton color="info" :icon="mdiFileEdit" small @click="openEditModal(producto)"/>
            <BaseButton color="danger" :icon="mdiTrashCan" small @click="openDeleteModal(producto)"/>
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
            @click="currentPage = page; fechtProducts()"
            />
        </BaseButtons>
        <small>Página {{ currentPage }} de {{ TotalPages }}</small>
    </BaseLevel>
    </div>

  <ModalAlert v-if="isModalVisible" :descripcion="modalMessage" textBoton="Cerrar" :visible="isModalVisible" @close="handleClose"/>
</template>
