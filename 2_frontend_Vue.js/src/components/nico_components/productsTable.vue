<script setup>
import { ref, onMounted } from 'vue';
import { mdiEye, mdiTrashCan } from '@mdi/js';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import SectionMain from '@/components/SectionMain.vue';
import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue';
import NotificationBar from '@/components/alejo_components/NotificationBar.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseLevel from '@/components/BaseLevel.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import { createProduct, getProductsByPage, updateProduct, deleteProduct } from '@/services/productService';

const productos = ref([]);
const currentProduct = ref({});
const TotalPages = ref(0);
const currentPage = ref(1);

const isEditMode = ref(false);  
const isAlertVisible = ref(false);
const colorAlert = ref('');
const modalMessage = ref('');

const isModalVisible = ref(false);
const activarModalDelete = ref({
    visible: false,
    producto: null
});

const fetchProducts = async () => {
    try {
        const response = await getProductsByPage(currentPage.value);
        productos.value = response.data.productos;
        TotalPages.value = response.data.total_pages;
    } catch (error) {
        modalMessage.value = 'Error al obtener productos';
        colorAlert.value = 'danger';
        isAlertVisible.value = true;
        setTimeout(() => { isAlertVisible.value = false; }, 3000);
    }
};

const openCreateModal = () => {
    isEditMode.value = false;
    currentProduct.value = { nombre_producto: '', descripcion: '', precio_actual: '' };
    isModalVisible.value = true;
};

const openEditModal = (producto) => {
    isEditMode.value = true;
    currentProduct.value = { ...producto };
    isModalVisible.value = true;
};

const closeModal = () => {
    isModalVisible.value = false;
};

const saveProduct = async () => {
    try {
        if (isEditMode.value) {
            await updateProduct(currentProduct.value.id_producto, currentProduct.value.nombre_producto, currentProduct.value.descripcion, currentProduct.value.precio_actual);
            modalMessage.value = "Producto actualizado con éxito";
        } else {
            await createProduct(currentProduct.value.nombre_producto, currentProduct.value.descripcion, currentProduct.value.precio_actual);
            modalMessage.value = "Producto creado con éxito";
        }  
        colorAlert.value = 'success';
        isAlertVisible.value = true;
        closeModal();
        fetchProducts();
        
        setTimeout(() => { isAlertVisible.value = false; }, 3000);
    } catch (error) {
        modalMessage.value = 'Error al guardar el producto';
        colorAlert.value = 'danger';
        setTimeout(() => { isAlertVisible.value = false; }, 3000);
        isAlertVisible.value = true;
    }
};

const openDeleteModal = (producto) => {
    activarModalDelete.value = { visible: true, producto };
};

const confirmDelete = async () => {
    try {
        await deleteProduct(activarModalDelete.value.producto.id_producto);
        modalMessage.value = "Producto eliminado con éxito";
        colorAlert.value = 'success';
        isAlertVisible.value = true;
        activarModalDelete.value.visible = false;
        fetchProducts();
        setTimeout(() => { isAlertVisible.value = false; }, 3000);
    } catch (error) {
        modalMessage.value = 'Error al eliminar el producto';
        setTimeout(() => { isAlertVisible.value = false; }, 3000);
        colorAlert.value = 'danger';
        isAlertVisible.value = true;
    }
};

const cancelDelete = () => {
    activarModalDelete.value.visible = false;
};

onMounted(() => {
    fetchProducts();
});
</script>

<template>
    <LayoutAuthenticated>
        <SectionMain>
            <h1 class="text-black dark:text-white text-2xl font-bold mb-8">Gestión de Productos</h1>
            <NotificationBar v-if="isAlertVisible" :color="colorAlert" :description="modalMessage" />
            <BaseButton @click="openCreateModal" color="info" label="Agregar Producto" class="mb-4" />

            <table>
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Descripción</th>
                        <th>Precio</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="producto in productos" :key="producto.id_producto">
                        <td>{{ producto.nombre_producto }}</td>
                        <td>{{ producto.descripcion }}</td>
                        <td>{{ producto.precio_actual }}</td>
                        <td>
                            <BaseButtons type="justify-start lg:justify-end" no-wrap>
                                <BaseButton color="info" :icon="mdiEye" small @click="openEditModal(producto)" />
                                <BaseButton color="danger" :icon="mdiTrashCan" small @click="openDeleteModal(producto)" />
                            </BaseButtons>
                        </td>
                    </tr>
                </tbody>
            </table>

            <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800">
                <BaseLevel>
                    <BaseButtons>
                        <BaseButton v-for="page in TotalPages" :key="page" :active="page === currentPage" :label="page" :color="page === currentPage ? 'lightDark' : 'whiteDark'" small @click="() => { currentPage = page; fetchProducts(); }" />
                    </BaseButtons>
                    <small>Página {{ currentPage }} de {{ TotalPages }}</small>
                </BaseLevel>
            </div>
        </SectionMain>
    </LayoutAuthenticated>

    <CardBoxModal class="dark:text-white" v-model="isModalVisible" :title="isEditMode ? 'Editar Producto' : 'Crear Producto'" :buttonLabel="isEditMode ? 'Guardar Cambios' : 'Crear Producto'" has-cancel @confirm="saveProduct" @cancel="closeModal">
        <form @submit.prevent="saveProduct">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="mb-4">
                    <label for="nombre" class="block text-gray-700 font-medium dark:text-white">Nombre:</label>
                    <input type="text" id="nombre" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700 dark:text-white" v-model="currentProduct.nombre_producto" required />
                </div>
                <div class="mb-4">
                    <label for="precio" class="block text-gray-700 font-medium dark:text-white">Precio:</label>
                    <input type="number" id="precio" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700 dark:text-white" v-model="currentProduct.precio_actual" min="1" required />
                </div>
                <div class="mb-4">
                    <label for="descripcion" class="block text-gray-700 font-medium dark:text-white">Descripción:</label>
                    <input type="text" id="descripcion" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700 dark:text-white" v-model="currentProduct.descripcion" required />
                </div>
            </div>
        </form>
    </CardBoxModal>

    <CardBoxModal class="dark:text-white" v-model="activarModalDelete.visible" title="Eliminar Producto" buttonLabel="Eliminar" button="danger" has-cancel @confirm="confirmDelete" @cancel="cancelDelete">
        <p class="text-xl">¿Está seguro de eliminar el producto?</p>
        <ul>
            <li><b>Nombre:</b> {{ activarModalDelete.producto?.nombre_producto }}</li>
            <li><b>Descripción:</b> {{ activarModalDelete.producto?.descripcion }}</li>
            <li><b>Precio:</b> {{ activarModalDelete.producto?.precio_actual }}</li>
        </ul>
    </CardBoxModal>
</template>
