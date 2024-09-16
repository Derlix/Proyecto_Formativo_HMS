<script setup>
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import productsTable from '@/components/nico_components/productsTable.vue';

// const createProducto = async () => {
//     try {
//         await createProduct(currentProduct.value.nombre_producto, currentProduct.value.descripcion, currentProduct.value.precio_actual);
//         alert('Producto creado exitosamente');
//         fechtProducts();
//         closeModal();
//     } catch (error) {
//         alert('Error al insertar producto: ', error);
//     }
// };

</script>


<template>
    <LayoutAuthenticated>
        <SectionMain class="bg-blue-100 rounded-lg dark:bg-slate-700">
            <h1 class="text-black text-lg font-bold mb-8 dark:text-white">Administrador de productos</h1>
            <div class="grid grid-cols-4 gap-2">
                <button class="bg-blue-800 rounded-lg text-white hover:bg-blue-600">Crear Producto</button>
                <span></span>
                <div class="grid grid-cols-5 col-span-2">
                    <input type="search" placeholder="Buscar Producto" class="rounded-l-md col-span-4 text-black">
                    <button class="bg-blue-800 p-1 text-white rounded-r-md hover:text-black focus:outline-none">
                        <i class="mdi mdi-magnify text-xl"></i>
                    </button>
                </div>
            </div>
            <productsTable/>
        </SectionMain>
    </LayoutAuthenticated>
</template>
