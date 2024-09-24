<script setup>
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import productsTable from '@/components/nico_components/productsTable.vue';
import NotificationBar from '@/components/alejo_components/NotificationBar.vue';
import BaseButton from '@/components/BaseButton.vue';
import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue';
import { createProduct, getProductsByPage } from '@/services/productService';
import { ref } from 'vue';

const productos = ref([]);
const currentProduct = ref({});
const TotalPages = ref(0);
const currentPage = ref(1);
const activarModal = ref(false);
const colorAlert = ref('');
const modalMessage = ref('');
const isAlertVisible = ref(false)

// Función para abrir el modal
const openCreateModal = () => {
  activarModal.value = true;
};

const cancelCreate = () => {
  activarModal.value = false;
  currentProduct.value = '';
}


const closeModal = () => {
  activarModal.value = false;
};

const fechtProducts = async () => {
    try {
        const response = await getProductsByPage(currentPage.value);
        productos.value = response.data.productos;
        TotalPages.value = response.data.total_pages;
        closeModal();
    } catch (error) {
        alert('Error al obtener productos: ', error);
    }
};

const reloadPage = () => {
  window.location.reload();
};

const createProducto = async () => {
  try {
    await createProduct(currentProduct.value.nombre_producto, currentProduct.value.descripcion, currentProduct.value.precio_actual);
    modalMessage.value = "Producto Creado con éxito";
    isAlertVisible.value = true;
    colorAlert.value = 'success';
    
    fechtProducts();
    closeModal();
    
    setTimeout(() => {
        isAlertVisible.value = false;
    }, 3000);
  } catch (error) {
    alert('Error al insertar producto: ', error);
  }
};

const handleSubmit = () => {
  createProducto();
  reloadPage();
};

</script>


<template>
    <CardBoxModal v-model="activarModal" title="Crear Producto" class="dark:text-white" buttonLabel="Crear Producto" has-cancel @cancel="cancelCreate" @confirm="createProducto ">
        <form @submit.prevent="handleSubmit()">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="mb-4">
                    <label for="nombre" class="block text-gray-700 font-medium dark:text-white">Nombre:</label>
                    <input type="text" id="nombre" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" v-model="currentProduct.nombre_producto" required/>
                </div>
                <div class="mb-4">
                    <label for="precio" class="block text-gray-700 font-medium dark:text-white">Precio:</label>
                    <input type="text" id="precio" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" v-model="currentProduct.precio_actual" required/>
                </div>
                <div class="mb-4">
                    <label for="descripcion" class="block text-gray-700 font-medium dark:text-white">Descripcion:</label>
                    <input type="text" id="descripcion" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" v-model="currentProduct.descripcion" required/>
                </div>
            </div>
        </form>
    </CardBoxModal>
    <LayoutAuthenticated>
        <SectionMain class=" rounded-lg">
            <h1 class="text-black dark:text-white text-2xl font-bold mb-8">Historial Productos</h1>
            <NotificationBar
            v-if="isAlertVisible"
            :color="colorAlert" 
            :description="modalMessage"
            :visible="isModalVisible"
            />
            <div>
                <BaseButton @click="openCreateModal" color="info" label="Agregar Producto" class="mb-4" />
            </div>
            <productsTable></productsTable>
        </SectionMain>
    </LayoutAuthenticated>
</template>

