<script setup>
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionMain from '@/components/SectionMain.vue';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import CardBoxWidget from '@/components/CardBoxWidget.vue'

import { mdiBallotOutline } from '@mdi/js';
import {
    mdiBroom,
    mdiBed,
    mdiFileDocument,
    mdiBedEmpty,
    mdiWrenchClock,
    mdiBedClock,
    mdiCashLock,
    mdiCashCheck
} from '@mdi/js'

</script>

<template>
    <LayoutAuthenticated>
        <SectionMain>

            <TitleIconOnly :icon="mdiBallotOutline" title="Jefe Recepcionista Home" />

            <div class="text-center">
                <h1 class="text-2xl">Estado de Habitaciones</h1>
            </div>

            <div class="grid grid-cols-1 gap-4   lg:grid-cols-3 mt-4 text-white">
                <CardBoxWidget :number="50" label="Habitaciones totales" :icon="mdiBed" :cardColor="'bg-sky-500'"/>
                <CardBoxWidget :number="50" label="Habitaciones disponibles" :icon="mdiBedEmpty" :cardColor="'bg-green-500'"/>
                <CardBoxWidget :number="50" label="Habitaciones ocupadas" :icon="mdiBedClock" :cardColor="'bg-pink-600'"/>
            </div>

            <div class="grid grid-cols-1 gap-4   lg:grid-cols-2 mb-6 mt-4 text-white">
                <CardBoxWidget :number="50" label="Habitaciones en limpieza" :icon="mdiBroom" :cardColor="'bg-amber-500'" />
                <CardBoxWidget :number="50" label="Habitaciones en mantenimiento" :icon="mdiWrenchClock" :cardColor="'bg-rose-700'" />
            </div>

            <div class="color2 p-8 rounded-lg shadow-lg text-center text-gray-200 mt-8">
                <h1 class="text-2xl font-bold mb-6">Registrar entrada y salida</h1>
                <div class="grid grid-cols-2 gap-4">
                    <button class="bg-sky-950 py-2 px-4 rounded">Registrar entrada</button>
                    <button class="bg-sky-950 py-2 px-4 rounded">Registrar salida</button>
                </div>  
            </div>

            <div class="text-center mt-6">
                <h1 class="text-2xl">Transacciones</h1>
            </div>

            <div class="grid grid-cols-1 gap-4 lg:grid-cols-2 mt-4 text-white">
                <CardBoxWidget :number="50" label="Pagos recibidos" :icon="mdiBed" :cardColor="'bg-emerald-500'" />
                <CardBoxWidget :number="50" label="Depositos recibidos" :icon="mdiBedEmpty" :cardColor="'bg-emerald-500'" />
            </div>

            <div class="text-center mt-6">
                <h1 class="text-2xl">Facturación</h1>
            </div>

            <div class="grid grid-cols-1 gap-4 lg:grid-cols-2 mt-4 text-white">
                <CardBoxWidget :number="50" label="Facturas emitidas" :icon="mdiFileDocument" :cardColor="'bg-neutral-500'" />
                <CardBoxWidget :number="50" label="Facturas en proceso" :icon="mdiFileDocument" :cardColor="'bg-neutral-500'" />
            </div>

            <div class="text-center mt-6">
                <h1 class="text-2xl">Caja</h1>
            </div>

            <div class="grid grid-cols-1 gap-4   lg:grid-cols-2 mt-4 text-white">
                <CardBoxWidget :number="50" label="Dinero inicial" :icon="mdiCashCheck" :cardColor="'bg-sky-500'" />
                <CardBoxWidget :number="50" label="Dinero final" :icon="mdiCashLock" :cardColor="'bg-sky-500'" />
            </div>

        </SectionMain>
    </LayoutAuthenticated>
</template>