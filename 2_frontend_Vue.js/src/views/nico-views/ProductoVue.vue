<script setup>
import { ref } from 'vue'
import SectionMain from '@/components/SectionMain.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import ModalProducto from '@/components/ModalProducto.vue';

const crearProducto = ref(false)
const editarProducto = ref(false)
const eliminarProducto = ref(false)
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain class="bg-blue-100 rounded-lg">
        <h1 class="text-black font-bold mb-8">Administrador de productos</h1>
        <div class="grid grid-cols-4 gap-2">
            <button @click="crearProducto = true" class="bg-blue-800 rounded-lg text-white">Crear Productos</button>
            <span></span>
            <div class="grid grid-cols-5 col-span-2">
                <input type="search" placeholder="Search Product" class=" rounded-l-md col-span-4">
                <button class="bg-blue-800 p-1 text-white rounded-r-md hover:text-black focus:outline-none">
                    <i class="mdi mdi-magnify text-xl"></i>
                </button>
            </div>

        </div>
        <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-6">
            <table class="w-full text-sm text-center rtl:text-right text-black font-medium dark:text-gray-100">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th>ID</th>
                        <th>Nombre Producto</th>
                        <th>Descripcion</th>
                        <th>Precio</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>123</td>
                        <td>Frutas</td>
                        <td>Manzanas, peras, uvas</td>
                        <td>35.000</td>
                        <td class="text-center">
                            <button @click="editarProducto = true" class="text-green-500 rounded-md hover:text-black focus:outline-none">
                                <i class="mdi mdi-square-edit-outline text-2xl"></i>
                            </button>
                            <button @click="eliminarProducto = true" class="text-red-500 rounded-md hover:text-black focus:outline-none">
                                <i class="mdi mdi-trash-can text-2xl"></i>
                            </button>
                        </td>
                    </tr>
                    <tr>
                        <td>144</td>
                        <td>Verduras</td>
                        <td>papa, cebolla, tomate</td>
                        <td>50.000</td>
                        <td class="text-center">
                            <button @click="editarProducto = true" class="text-green-500 rounded-md hover:text-black focus:outline-none">
                                <i class="mdi mdi-square-edit-outline text-2xl"></i>
                            </button>
                            <button @click="eliminarProducto = true" class="text-red-500 rounded-md hover:text-black focus:outline-none">
                                <i class="mdi mdi-trash-can text-2xl"></i>
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <ModalProducto
        descripcion="Crear Producto"
        textBoton="Crear Producto"
        :visible="crearProducto" 
        @close="crearProducto = false" />

        <ModalProducto
        descripcion="Actualizar Producto"
        textBoton="Actualizar Producto"
        :visible="editarProducto" 
        @close="editarProducto = false" />

        <ModalProducto
        descripcion="Eliminar Producto"
        textBoton="Eliminar Producto"
        :visible="eliminarProducto" 
        @close="eliminarProducto = false" />

    </SectionMain>
  </LayoutAuthenticated>
</template>