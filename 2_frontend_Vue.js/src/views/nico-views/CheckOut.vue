<script setup>
import SectionMain from '@/components/SectionMain.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
        <div>
            <h1 class="bg-blue-400 p-5 text-white font-semibold rounded-t-lg border-2 border-black border-b-0">Check-Out</h1>
            <div class="border-2 border-black pb-4 pl-4 dark:text-white">
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Nombre:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="text" placeholder="Juan">
                    <h2 class="text-start dark:text-white">Seguro:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="number" placeholder="$25.000">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">llegada:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="date">
                    <h2 class="text-start dark:text-white">Anticipo:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="number" placeholder="$5.000">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Salida:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="date">
                    <h2 class="text-start dark:text-white">Miscelaneos:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="number" placeholder="12%">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Registro N°:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="number" placeholder="4233">
                    <h2 class="text-start dark:text-white">Transferencia Debito:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="text" placeholder="Si">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Habitacion N°:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="number" placeholder="104">
                    <h2 class="text-start dark:text-white">Total Debitos:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="number" placeholder="3">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Precio por noche:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="number" placeholder="$40.000">
                    <h2 class="text-start dark:text-white">Particular:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="text" placeholder="No">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Noches de estadia:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="number" placeholder="5">
                    <h2 class="text-start dark:text-white">Transferencia Credito:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="text" placeholder="No">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Impuestos:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="number" placeholder="12%">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Tipo de habitacion:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="text" placeholder="VIP">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Acompañantes:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="number" placeholder="5">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Deposito:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="number" placeholder="50.000">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Tarjeta Credito:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="text" placeholder="No">
                </div>
                <div class="grid grid-cols-4 font-medium p-2 gap-3 text-black">
                    <h2 class="text-start dark:text-white">Total Credito:</h2>
                    <input class="border-none bg-gray-300 rounded-2xl text-center h-7 w-48" type="text" placeholder="No">
                </div>
            </div>
            <div class="grid grid-cols-2 p-5 text-black font-bold">
                <h2 class="dark:text-white">TOTAL A PAGAR:</h2>
                <span class="text-end dark:text-white">12.900.000</span>
                <h2 class="mt-5 dark:text-white">Metodos de pago:</h2>
            </div>
            <div class="grid grid-cols-3 font-medium gap-48 text-center px-10">
                <button class="bg-blue-950 text-white rounded-xl h-10">Efectivo</button>
                <button class="bg-blue-950 text-white rounded-xl h-10">Tarjeta</button>
                <button class="bg-blue-950 text-white rounded-xl h-10">Transferencia</button>
            </div>
            <div class="flex justify-center mt-5">
                <button class="bg-blue-400 text-white rounded-xl h-10 w-52">Generar Factura</button>
            </div>
        </div>
    </SectionMain>
  </LayoutAuthenticated>
</template>
