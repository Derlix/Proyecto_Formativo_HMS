<script setup>
import {
    ref
} from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import CardBoxWidget from '@/components/CardBoxWidget.vue'
import {
    mdiCash,
    mdiTools,
    mdiFileDocument,
    mdiCurrencyUsd,
    mdiInboxArrowDown
} from '@mdi/js'
</script>

<template>
<LayoutAuthenticated>
    <div class="m-10">
        <div class="flex justify-between text-lg font-bold">
            <h1>Dinero inicial: $120000</h1>
            <h1>Dinero final en caja: $180000</h1>
        </div>

        <div class="grid grid-cols-1 gap-4   lg:grid-cols-3 mb-6 mt-4 text-white">
            <CardBoxWidget :number="50" label="Pagos recibidos" :icon="mdiCurrencyUsd" :cardColor="'bg-green-500'" />
            <CardBoxWidget :number="50" label="Depósitos recibidos" :icon="mdiCash" :cardColor="'bg-sky-500'" />
            <CardBoxWidget :number="50" label="Facturas emitidas" :icon="mdiFileDocument" :cardColor="'bg-blue-950'" />
        </div>
        <div class="flex gap-4 text-white">
            <CardBoxWidget class="flex-1" :number="50" label="Facturas en proceso recibidos" :icon="mdiInboxArrowDown" :cardColor="'bg-amber-500'" />
            <CardBoxWidget class="flex-1" :number="50" label="Habitaciones en mantenimiento" :icon="mdiTools" :cardColor="'bg-red-500'" />
        </div>
        <div class="color2 p-8 rounded-lg shadow-lg text-center text-gray-200 w-1/2 mt-8">
            <h1 class="text-2xl font-bold mb-6">Registro Fondos Caja de Recepción</h1>
            <div class="grid grid-cols-2 gap-4">
                <button class="bg-sky-950 py-2 px-4 rounded">Registrar Fondos</button>
                <button class="bg-sky-950 py-2 px-4 rounded">Ver todos los registros</button>
                <button class="bg-sky-950 py-2 px-4 rounded">Modificar Registro</button>
                <button class="bg-sky-950 py-2 px-4 rounded">Eliminar Registro</button>
            </div>
            
        </div>
        <div class="flex justify-end mt-5">
                <button class="bg-green-500 text-white py-2 px-4 rounded m-1">¿Necesitas ayuda?</button>
        </div>
    </div>
</LayoutAuthenticated>
</template>

<style>
.color2 {
    background-color: #6287B4;
}
</style>
