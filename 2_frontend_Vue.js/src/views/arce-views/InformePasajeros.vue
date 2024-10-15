<script setup>
import { ref, onMounted } from 'vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import { info_habitaciones } from '@/services/arce_service/informePasajeroService';
import SectionMain from '@/components/SectionMain.vue';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import { mdiBallotOutline } from '@mdi/js';
import SectionTitle from '@/components/SectionTitle.vue';
import BaseDivider from '@/components/BaseDivider.vue';

const habitaciones = ref([]);
const habitacionesPorPiso = ref({});
const resumenPorPiso = ref([]);

// Función para obtener las habitaciones
const obtenerHabitaciones = async () => {
    try {
        const response = await info_habitaciones();
        habitaciones.value = response.data;
        agruparPorPiso();
        generarResumen();
    } catch (error) {
        console.error("Error al obtener las habitaciones:", error.message);
    }
};

// Agrupa habitaciones por piso
const agruparPorPiso = () => {
    habitacionesPorPiso.value = habitaciones.value.reduce((acc, habitacion) => {
        const piso = habitacion.piso;
        if (!acc[piso]) {
            acc[piso] = [];
        }
        acc[piso].push(habitacion);
        return acc;
    }, {});
};

// Genera el resumen de habitaciones activas, inactivas, ocupadas y en mantenimiento por piso
const generarResumen = () => {
    resumenPorPiso.value = Object.entries(habitacionesPorPiso.value).map(([piso, habitaciones]) => {
        const totalActivas = habitaciones.filter(h => h.estado === 'ACTIVO').length;
        const totalInactivas = habitaciones.filter(h => h.estado === 'INACTIVO').length;
        const totalOcupadas = habitaciones.filter(h => h.estado === 'OCUPADO').length;
        const totalMantenimiento = habitaciones.filter(h => h.estado === 'MANTENIMIENTO').length;
        const totalHabitaciones = habitaciones.length; // Total de habitaciones en el piso

        return {
            piso,
            totalHabitaciones,
            totalActivas,
            totalInactivas,
            totalOcupadas,
            totalMantenimiento
        };
    });
};

// Carga las habitaciones al montar el componente
onMounted(() => {
    obtenerHabitaciones();
});
</script>

<template>
    <LayoutAuthenticated>
        <SectionMain>
            <TitleIconOnly :icon="mdiBallotOutline" title="Informe habitaciones" />

            <div v-for="(habitaciones, piso) in habitacionesPorPiso" :key="piso">
                <SectionTitle>Piso {{ piso }}</SectionTitle>
                
                <div class="overflow-x-auto">
                    <table class="min-w-full rounded-lg shadow-md lg:table mt-4">
                        <thead>
                            <tr class="text-sm leading-normal">
                                <th class="py-3 px-6 text-left">Habitación</th>
                                <th class="py-3 px-6 text-left">Categoría</th>
                                <th class="py-3 px-6 text-left">Estado</th>
                                <th class="py-3 px-6 text-left">Precio</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr 
                                v-for="habitacion in habitaciones" 
                                :key="habitacion.id_habitacion"
                            >
                                <td class="py-3 px-6 text-left whitespace-nowrap" data-label="Habitación">{{ habitacion.numero_habitacion }}</td>
                                <td class="py-3 px-6 text-left" data-label="Categoría">{{ habitacion.categoria.tipo_habitacion }}</td>
                                <td class="py-3 px-6 text-left" data-label="Estado">{{ habitacion.estado }}</td>
                                <td class="py-3 px-6 text-left" data-label="Precio">$ {{ habitacion.categoria.precio_fijo }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <BaseDivider/>

            <SectionTitle>Recopilación de habitaciones</SectionTitle>

            <div class="overflow-x-auto">
                <table class="min-w-full rounded-lg shadow-md lg:table mt-4">
                    <thead>
                        <tr class="text-sm leading-normal">
                            <th class="py-3 px-6 text-left">Piso</th>
                            <th class="py-3 px-6 text-left">Total Habitaciones</th>
                            <th class="py-3 px-6 text-left">Habitaciones Activas</th>
                            <th class="py-3 px-6 text-left">Habitaciones Inactivas</th>
                            <th class="py-3 px-6 text-left">Habitaciones Ocupadas</th>
                            <th class="py-3 px-6 text-left">Habitaciones en Mantenimiento</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr 
                            v-for="resumen in resumenPorPiso" 
                            :key="resumen.piso"
                        >
                            <td class="py-3 px-6 text-left" data-label="Piso">{{ resumen.piso }}</td>
                            <td class="py-3 px-6 text-left" data-label="Total Habitaciones">{{ resumen.totalHabitaciones }}</td>
                            <td class="py-3 px-6 text-left" data-label="Habitaciones Activas">{{ resumen.totalActivas }}</td>
                            <td class="py-3 px-6 text-left" data-label="Habitaciones Inactivas">{{ resumen.totalInactivas }}</td>
                            <td class="py-3 px-6 text-left" data-label="Habitaciones Ocupadas">{{ resumen.totalOcupadas }}</td>
                            <td class="py-3 px-6 text-left" data-label="Habitaciones en Mantenimiento">{{ resumen.totalMantenimiento }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </SectionMain>
    </LayoutAuthenticated>
</template>
