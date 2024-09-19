<script setup>
import { ref, onMounted } from 'vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import { obtenerTodasHabitaciones } from '@/services/juanca_service/habitacionService';
import SectionMain from '@/components/SectionMain.vue';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import { mdiBallotOutline} from '@mdi/js'


const habitaciones = ref([]);

const obtenerHabitaciones = async () => {
    try {
        const response = await obtenerTodasHabitaciones();
        habitaciones.value = response.data;
    } catch (error) {
        console.error("Error al obtener las habitaciones:", error.message);
    }
};

onMounted(() => {
    obtenerHabitaciones();
});


</script>

<template>
    <LayoutAuthenticated>
        <SectionMain>
            <TitleIconOnly :icon="mdiBallotOutline" title="Informe Pasajeros"/>
                <table
                    class="min-w-full bg-white border border-gray-200 rounded-lg shadow-md overflow-hidden block lg:table">
                    <thead>
                        <tr class="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
                            <th class="py-3 px-6 text-left">Número</th>
                            <th class="py-3 px-6 text-left">Piso</th>
                            <th class="py-3 px-6 text-left">Categoría</th>
                            <th class="py-3 px-6 text-left">Estado</th>
                            <th class="py-3 px-6 text-left">Precio</th>
                            <th class="py-3 px-6 text-center">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="habitacion in habitaciones" :key="habitacion.id_habitacion"
                            class="border-b border-gray-200 hover:bg-gray-100">
                            <td class="py-3 px-6 text-left whitespace-nowrap">{{ habitacion.numero_habitacion }}</td>
                            <td class="py-3 px-6 text-left">{{ habitacion.piso }}</td>
                            <td class="py-3 px-6 text-left">{{ habitacion.id_categoria_habitacion }}</td>
                            <td class="py-3 px-6 text-left">{{ habitacion.estado }}</td>
                            <td class="py-3 px-6 text-left">{{ habitacion.precio_actual }}</td>
                        </tr>
                    </tbody>
                </table>
        </SectionMain>
    </LayoutAuthenticated>
</template>