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

// Genera el resumen de habitaciones activas y total por piso
const generarResumen = () => {
    resumenPorPiso.value = Object.entries(habitacionesPorPiso.value).map(([piso, habitaciones]) => {
        const habitacionesActivas = habitaciones.filter(h => h.estado === 'ACTIVO');
        const totalMonto = habitacionesActivas.reduce((sum, habitacion) => sum + habitacion.precio_actual, 0);
        
        return {
            piso,
            totalHabitacionesActivas: habitacionesActivas.length,
            montoTotal: totalMonto
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
            <TitleIconOnly :icon="mdiBallotOutline" title="Informe Pasajeros" />

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
                                class=""
                            >
                                <td class="py-3 px-6 text-left whitespace-nowrap" data-label="Habitación">{{ habitacion.numero_habitacion }}</td>
                                <td class="py-3 px-6 text-left" data-label="Categoría">{{ habitacion.categoria.tipo_habitacion }}</td>
                                <td class="py-3 px-6 text-left" data-label="Estado">{{ habitacion.estado }}</td>
                                <td class="py-3 px-6 text-left" data-label="Precio">$ {{ habitacion.precio_actual }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <BaseDivider/>

            <SectionTitle>Recopilación de habitaciones activas</SectionTitle>

            <div class="overflow-x-auto">
                <table class="min-w-full rounded-lg shadow-md lg:table mt-4">
                    <thead>
                        <tr class="text-sm leading-normal">
                            <th class="py-3 px-6 text-left">Piso</th>
                            <th class="py-3 px-6 text-left">Habitaciones Activas</th>
                            <th class="py-3 px-6 text-left">Monto Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr 
                            v-for="resumen in resumenPorPiso" 
                            :key="resumen.piso" 
                            class=""
                        >
                            <td class="py-3 px-6 text-left" data-label="Piso">{{ resumen.piso }}</td>
                            <td class="py-3 px-6 text-left" data-label="Habitaciones Activas">{{ resumen.totalHabitacionesActivas }}</td>
                            <td class="py-3 px-6 text-left" data-label="Monto Total">$ {{ resumen.montoTotal.toFixed(2) }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </SectionMain>
    </LayoutAuthenticated>
</template>
