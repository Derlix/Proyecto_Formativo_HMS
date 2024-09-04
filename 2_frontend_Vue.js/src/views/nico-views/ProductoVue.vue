<script setup>
import SectionMain from '@/components/SectionMain.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain class="bg-blue-100 rounded-lg">
        <h1 class="text-black font-bold mb-8">Administrador de productos</h1>
        <div class="grid grid-cols-5 gap-2">
            <h2 class="mt-2 dark:text-black">Productos</h2>
            <button type="button" class="bg-blue-800 rounded-lg text-white">Crear Productos</button>
            <input type="search" placeholder="Search Product" class="rounded-lg">
            <button type="button" class="bg-blue-800 rounded-lg text-white">Buscar</button>
            <div class="flex justify-end">
                <span class="mt-2 dark:text-black">Mostrar por : {{ selected }}</span>
                <select v-model="selected">
                <option disabled value=""></option>
                <option>5</option>
                <option>10</option>
                <option>15</option>
                </select>
            </div>
        </div>
        <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-6">
            <table class="w-full text-sm text-left rtl:text-right text-black font-medium dark:text-gray-100">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3">
                            ID
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Nombre Producto
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Descripcion
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Precio
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Acciones
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                        <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1003
                        </th>
                        <td class="px-6 py-4">
                            Jabón
                        </td>
                        <td class="px-6 py-4">
                            Jabón para el lava manos
                        </td>
                        <td class="px-6 py-4">
                            $4.000
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-900 hover:underline mr-3">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-900 hover:underline">Eliminar</a>
                        </td>
                    </tr>
                    <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                        <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1004
                        </th>
                        <td class="px-6 py-4">
                            Crema dental
                        </td>
                        <td class="px-6 py-4">
                            Crema de dientes Luminous White
                        </td>
                        <td class="px-6 py-4">
                            $10.000
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-3">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">Eliminar</a>
                        </td>
                    </tr>
                    <tr class="bg-white dark:bg-gray-800">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1008
                        </th>
                        <td class="px-6 py-4">
                            Toallas
                        </td>
                        <td class="px-6 py-4">
                            Toallas de baño
                        </td>
                        <td class="px-6 py-4">
                            $9.000
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-900 hover:underline mr-3">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-900 hover:underline">Eliminar</a>
                        </td>
                    </tr>
                    <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1004
                        </th>
                        <td class="px-6 py-4">
                            Crema dental
                        </td>
                        <td class="px-6 py-4">
                            Crema de dientes Luminous White
                        </td>
                        <td class="px-6 py-4">
                            $10.000
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-3">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">Eliminar</a>
                        </td>
                    </tr>
                    <tr class="bg-white dark:bg-gray-800">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1008
                        </th>
                        <td class="px-6 py-4">
                            Toallas
                        </td>
                        <td class="px-6 py-4">
                            Toallas de baño
                        </td>
                        <td class="px-6 py-4">
                            $9.000
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-900 hover:underline mr-3">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-900 hover:underline">Eliminar</a>
                        </td>
                    </tr>
                    <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1004
                        </th>
                        <td class="px-6 py-4">
                            Crema dental
                        </td>
                        <td class="px-6 py-4">
                            Crema de dientes Luminous White
                        </td>
                        <td class="px-6 py-4">
                            $10.000
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-3">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">Eliminar</a>
                        </td>
                    </tr>
                    <tr class="bg-white dark:bg-gray-800">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1008
                        </th>
                        <td class="px-6 py-4">
                            Toallas
                        </td>
                        <td class="px-6 py-4">
                            Toallas de baño
                        </td>
                        <td class="px-6 py-4">
                            $9.000
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-900 hover:underline mr-3">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-900 hover:underline">Eliminar</a>
                        </td>
                    </tr>
                    <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1004
                        </th>
                        <td class="px-6 py-4">
                            Crema dental
                        </td>
                        <td class="px-6 py-4">
                            Crema de dientes Luminous White
                        </td>
                        <td class="px-6 py-4">
                            $10.000
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-3">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">Eliminar</a>
                        </td>
                    </tr>
                    <tr class="bg-white dark:bg-gray-800">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1008
                        </th>
                        <td class="px-6 py-4">
                            Toallas
                        </td>
                        <td class="px-6 py-4">
                            Toallas de baño
                        </td>
                        <td class="px-6 py-4">
                            $9.000
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-900 hover:underline mr-3">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-900 hover:underline">Eliminar</a>
                        </td>
                    </tr>
                    <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1004
                        </th>
                        <td class="px-6 py-4">
                            Crema dental
                        </td>
                        <td class="px-6 py-4">
                            Crema de dientes Luminous White
                        </td>
                        <td class="px-6 py-4">
                            $10.000
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-3">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">Eliminar</a>
                        </td>
                    </tr>
                    <tr class="bg-white dark:bg-gray-800">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1008
                        </th>
                        <td class="px-6 py-4">
                            Toallas
                        </td>
                        <td class="px-6 py-4">
                            Toallas de baño
                        </td>
                        <td class="px-6 py-4">
                            $9.000
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-900 hover:underline mr-3">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-900 hover:underline">Eliminar</a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

    </SectionMain>
  </LayoutAuthenticated>
</template>
