<script setup>
import SectionMain from '@/components/SectionMain.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain class="bg-blue-100 rounded-lg">
        <div>
            <h1 class="text-black text-xl font-bold mb-4">Trasunto Movimiento Cuenta Huesped</h1>
            <div>
                <label for="" class=" text-gray-900">Factura</label><br>
                <input type="search" class="mt-2 w-64 rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="id">
            </div>

            <h1 class="my-4 text-xl font-semibold">Habitacion</h1>
            <div class="grid grid-cols-4 gap-6">
                <div>
                    <label for="" class=" text-gray-900">Salida</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Check In</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Personas</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Nombre</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
            </div>

            <h1 class="my-4 text-xl font-semibold">Balance Inicial</h1>
            <div class="grid grid-cols-4 gap-6">
                <div>
                    <label for="" class=" text-gray-900">Debito</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Credito</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
            </div>

            <h1 class="my-4 text-xl font-semibold">Debitos</h1>
            <div class="grid grid-cols-7 gap-4">
                <div class="col-span-2">
                    <label for="" class=" text-gray-900">Habitacion</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Impuesto</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Seguro</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div class="text-center">
                    <button class="text-white font-semibold bg-blue-700 px-3 py-2 text-sm rounded-lg">Agregar Productos</button>
                </div>
                <div>
                    <label for="" class=" text-gray-900">Anticipo</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Trans. Debito</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
            </div>

            <div class="grid grid-cols-7 gap-4">
                <div class="col-span-1"></div>
                <div class="col-span-1"></div>
                <div class="col-span-1"></div>
                <div class="col-span-1"></div>
                <div class="col-span-1"><button class="text-white font-semibold mt-3 bg-blue-700 px-3 py-2 text-sm rounded-lg">Ver Productos Agregados</button></div>
                <div class="col-span-1 text-center mt-2">Total: </div>
                <div>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
            </div>

            <h1 class="my-4 text-xl font-semibold">Creditos</h1>
            <div class="grid grid-cols-7 gap-4">
                <div class="col-span-2">
                    <label for="" class=" text-gray-900">Efectivo</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Descuento</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Deposito</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">T.credito</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Particular</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Trans. credito</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
            </div>

            <h1 class="my-4 text-xl font-semibold">Balance Final</h1>
            <div class="grid grid-cols-4 gap-6">
                <div>
                    <label for="" class=" text-gray-900">Debito</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
                <div>
                    <label for="" class=" text-gray-900">Credito</label><br>
                    <input type="search" class="mb-4 w-full rounded-md border-0 py-1.5 pl-7 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
            </div>
            <div class="text-center">
                <button class="m-2 bg-green-600 text-white px-3 py-2 rounded-lg font-bold">Confirmar</button>
                <button class="m-2 bg-red-600 text-white px-3 py-2 rounded-lg font-bold">Cancelar</button>
            </div>
        </div>
    </SectionMain>
  </LayoutAuthenticated>
</template>