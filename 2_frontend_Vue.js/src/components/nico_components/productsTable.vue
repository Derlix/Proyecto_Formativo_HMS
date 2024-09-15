<script setup>
import { ref } from 'vue'
import CardBoxModal from '@/components/CardBoxModal.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import { getProductsByPage, createProduct, updateProduct, deleteProduct } from '@/services/productService'
import { mdiBookEdit, mdiTrashCan } from '@mdi/js'

const productos = ref([]);
const currentProduct = ref({});
const currentPage = ref(1);
const TotalPages = ref(0);
const isEditMode = ref(false);
const activarModal = ref(false);
const descripcion = ref('');

const fechtProducts = async () => {
    try {
        const response = await getProductsByPage(currentPage.value);
        productos.value = response.data.productos;
        TotalPages.value = response.data.total_pages;
    } catch (error) {
        alert('Error al obtener productos: ', error);
    }
};

const updateProducto = async () => {
    try {
        await updateProduct(currentProduct.value.id_producto, currentProduct.value.nombre_producto, currentProduct.value.descripcion, currentProduct.value.precio_actual);
        alert('Producto actualizado exitosamente');
        fechtProducts();
        closeModal();
    } catch (error) {
        alert('Error al actualizar producto: ', error);
    }
};

// const eliminarProducto = async (id_producto) => {
//     if (confirm('¿Estás seguro de que deseas eliminar este producto?')) {
//         try {
//             await deleteProduct(id_producto);
//             alert('Producto eliminado exitosamente');
//             fechtProducts(); // Refresca la lista de productos después de eliminar
//         } catch (error) {
//             alert('Error al eliminar el producto:', error);
//         }
//     }
// };

const openModal = (action, producto = {}) => {
    if (action === 'update') {
        isEditMode.value = true;
        descripcion.value = 'Actualizar Producto';
        currentProduct.value = { ...producto };
    } else if (action === 'delete') {
        isEditMode.value = false;
        deleteProduct()
        descripcion.value = 'Eliminar Producto';
        CardBoxModal.buttonLabel = "Eliminar";
        currentProduct.value = { ...producto };
    }
};

const closeModal = () => {
    activarModal.value = false;
};

fechtProducts();
</script>

<template>
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
                        <BaseButton color="danger" :icon="mdiTrashCan" small @click="openModal('delete', producto)" />
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

    <!-- Modal para crear/actualizar/eliminar producto -->
    <CardBoxModal v-model="activarModal" :title="descripcion">
        <form @submit.prevent="isEditMode ? updateProducto() : createProducto()">
            <div class="grid grid-cols-2 gap-3">
                <div class="mb-4">
                    <label for="nombre" class="block text-gray-700 dark:text-white">Nombre del producto</label>
                    <input v-model="currentProduct.nombre_producto" type="text" id="nombre" class="w-full px-3 py-2 border rounded dark:text-black dark:bg-gray-400" required />
                </div>
                <div class="mb-4">
                    <label for="precio" class="block text-gray-700 dark:text-white">Precio</label>
                    <input v-model="currentProduct.precio_actual" type="number" id="precio" class="w-full px-3 py-2 border rounded dark:text-black dark:bg-gray-400" required />
                </div>
            </div>
            <div>
                <label for="descripcion" class="block text-gray-700 dark:text-white">Descripción</label>
                <input v-model="currentProduct.descripcion" type="text" id="descripcion" class="w-full px-3 py-2 border rounded dark:text-black dark:bg-gray-400" required />
            </div>
        </form>
    </CardBoxModal>
</template>
