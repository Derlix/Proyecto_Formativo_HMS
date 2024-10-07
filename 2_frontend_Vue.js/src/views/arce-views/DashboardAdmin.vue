<script setup>
import { ref, reactive, onMounted } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionMain from '@/components/SectionMain.vue';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import CardBoxWidget from '@/components/CardBoxWidget.vue'
import SectionTitle from '@/components/SectionTitle.vue';
import ModalRegistrarEntrada from '@/components/ModalRegistrarEntrada.vue'
import ModalRegistrarSalida from '@/components/ModalRegistrarSalida.vue'
import { mdiBallotOutline, mdiBroom, mdiBed, mdiFileDocument, mdiBedEmpty, mdiWrenchClock, mdiBedClock, mdiCashLock, mdiCashCheck } from '@mdi/js';
import { obtenerTodasHabitaciones } from '@/services/habitacionService';

const showModal = ref(false)
const showModalSalidas = ref(false)

const habitaciones = reactive({
    totales: 0,
    disponibles: 0,
    ocupadas: 0,
    limpieza: 0,
    mantenimiento: 0,
});

const fetchHabitaciones = async () => {
    try {
        const response = await obtenerTodasHabitaciones();
        const data = response.data;
        
        habitaciones.totales = data.length;
        habitaciones.disponibles = data.filter(habitacion => habitacion.estado === 'ACTIVO').length;
        habitaciones.ocupadas = data.filter(habitacion => habitacion.estado === 'INACTIVO').length;
        habitaciones.limpieza = data.filter(habitacion => habitacion.estado === 'OPERACION').length;
        habitaciones.mantenimiento = data.filter(habitacion => habitacion.estado === 'MANTENIMIENTO').length;
    } catch (error) {
        console.error('Error al cargar habitaciones:', error);
    }
};

onMounted(() => {
    fetchHabitaciones();
});

</script>

<template>
    <LayoutAuthenticated>
        <SectionMain>
            <TitleIconOnly :icon="mdiBallotOutline" title="Jefe Recepcionista Home" />
            <SectionTitle>Estado de habitaciones</SectionTitle>

            <div class="grid grid-cols-1 gap-6 lg:grid-cols-3 mt-4 text-white">
                <CardBoxWidget :number="habitaciones.totales" label="Habitaciones totales" :icon="mdiBed" :cardColor="'bg-sky-500'" />
                <CardBoxWidget :number="habitaciones.disponibles" label="Habitaciones disponibles" :icon="mdiBedEmpty" :cardColor="'bg-green-500'" />
                <CardBoxWidget :number="habitaciones.ocupadas" label="Habitaciones ocupadas" :icon="mdiBedClock" :cardColor="'bg-pink-600'" />
            </div>

            <div class="grid grid-cols-1 gap-6 lg:grid-cols-2 mb-6 mt-4 text-white">
                <CardBoxWidget :number="habitaciones.limpieza" label="Habitaciones en limpieza" :icon="mdiBroom" :cardColor="'bg-amber-500'" />
                <CardBoxWidget :number="habitaciones.mantenimiento" label="Habitaciones en mantenimiento" :icon="mdiWrenchClock" :cardColor="'bg-rose-700'" />
            </div>

            <CardBox class="shadow-md">
                <SectionTitle>Registro entrada y salida</SectionTitle>
                <div class="grid grid-cols-2 gap-6">
                    <button @click="showModal = true" class="bg-blue-600 h-12 rounded-lg my-6 font-bold hover:bg-blue-900 text-white">Registrar entrada</button>
                    <button @click="showModalSalidas = true" class="bg-blue-600 h-12 rounded-lg my-6 font-bold hover:bg-blue-900 text-white">Registrar salida</button>
                    <ModalRegistrarEntrada :visible="showModal" @close="showModal = false" />
                    <ModalRegistrarSalida :visible="showModalSalidas" @close="showModalSalidas = false"/>
                </div>
            </CardBox>

            <SectionTitle first>Transacciones</SectionTitle>
            <div class="grid grid-cols-1 gap-4 lg:grid-cols-2 mt-4 text-white">
                <CardBoxWidget :number="50" label="Pagos recibidos" :icon="mdiBed" :cardColor="'bg-emerald-500'" />
                <CardBoxWidget :number="50" label="Depositos recibidos" :icon="mdiBedEmpty" :cardColor="'bg-emerald-500'" />
            </div>

            <SectionTitle first>Facturación</SectionTitle>
            <div class="grid grid-cols-1 gap-4 lg:grid-cols-2 mt-4 text-white">
                <CardBoxWidget :number="50" label="Facturas emitidas" :icon="mdiFileDocument" :cardColor="'bg-neutral-500'" />
                <CardBoxWidget :number="50" label="Facturas en proceso" :icon="mdiFileDocument" :cardColor="'bg-neutral-500'" />
            </div>

            <SectionTitle first>Caja</SectionTitle>
            <div class="grid grid-cols-1 gap-4 lg:grid-cols-2 mt-4 text-white">
                <CardBoxWidget :number="50" label="Dinero inicial" :icon="mdiCashCheck" :cardColor="'bg-sky-500'" />
                <CardBoxWidget :number="50" label="Dinero final" :icon="mdiCashLock" :cardColor="'bg-sky-500'" />
            </div>
        </SectionMain>
    </LayoutAuthenticated>
</template>
