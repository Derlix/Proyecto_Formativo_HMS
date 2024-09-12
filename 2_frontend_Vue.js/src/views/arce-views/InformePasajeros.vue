<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';

// Variables reactivas para almacenar los datos de las habitaciones y el token de acceso
const habitaciones = ref([]);
const accessToken = ref('');

// Función para obtener el token de acceso
const obtenerToken = async () => {
    try {
        const response = await axios.post('https://api-hotel-suqt.onrender.com/login/token', {
            username: 'admin@gmail.com',
            password: '12345'
        }, {
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        });
        accessToken.value = response.data.access_token;
        obtenerHabitaciones();
    } catch (error) {
        console.error('Error al obtener el token:', error.message);
    }
};

// Función para obtener las habitaciones usando el token de acceso
const obtenerHabitaciones = async () => {
    try {
        const response = await axios.get('https://api-hotel-suqt.onrender.com/habitacion/', {
            headers: { 'Authorization': `Bearer ${accessToken.value}` }
        });
        habitaciones.value = response.data;
    } catch (error) {
        console.error('Error al obtener las habitaciones:', error.message);
    }
};

// Agrupar habitaciones por piso
const habitacionesPorPiso = computed(() => {
    return habitaciones.value.reduce((acc, habitacion) => {
        if (!acc[habitacion.piso]) {
            acc[habitacion.piso] = [];
        }
        acc[habitacion.piso].push(habitacion);
        return acc;
    }, {});
});

// Calcular datos para la tabla de recopilación
const recopilacionDatos = computed(() => {
    return Object.entries(habitacionesPorPiso.value).map(([piso, habitacionesPiso]) => {
        return {
            piso: piso,
            cantidadHabitaciones: habitacionesPiso.length,
            habitaciones: habitacionesPiso
        };
    });
});

// Al montar el componente, obtenemos el token y las habitaciones
onMounted(() => {
    obtenerToken();
});
</script>

<template>
    <LayoutAuthenticated>
        <div class="p-5 flex flex-col items-center">
            <h1 class="text-3xl font-bold mb-5 text-center">Habitaciones Disponibles</h1>
            
            <!-- Lista de tarjetas por piso -->
            <div class="w-full max-w-4xl mb-10">
                <div v-for="(habitacionesPiso, piso) in habitacionesPorPiso" :key="piso" class="mb-8">
                    <div class="bg-white border border-gray-300 rounded-md shadow-sm p-4">
                        <h2 class="text-xl font-bold mb-4 text-center">Piso {{ piso }}</h2>
                        <table class="w-full border border-gray-300">
                            <thead>
                                <tr>
                                    <th class="border px-4 py-2">Número</th>
                                    <th class="border px-4 py-2">Precio Actual</th>
                                    <th class="border px-4 py-2">Estado</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="habitacion in habitacionesPiso" :key="habitacion.id_habitacion" class="border-b">
                                    <td class="px-4 py-2">{{ habitacion.numero_habitacion }}</td>
                                    <td class="px-4 py-2">{{ habitacion.precio_actual }}</td>
                                    <td class="px-4 py-2">{{ habitacion.estado }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- Tabla de recopilación -->
            <div class="w-full max-w-4xl">
                <table class="w-full border border-gray-300 bg-white">
                    <thead>
                        <tr>
                            <td colspan="3" class="text-center py-2 text-lg font-bold">Tabla de Recopilación</td>
                        </tr>
                        <tr>
                            <th class="border px-4 py-2">Piso</th>
                            <th class="border px-4 py-2">Número de Habitaciones</th>
                            <th class="border px-4 py-2">Habitaciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="dato in recopilacionDatos" :key="dato.piso" class="border-b">
                            <td class="px-4 py-2">{{ dato.piso }}</td>
                            <td class="px-4 py-2">{{ dato.cantidadHabitaciones }}</td>
                            <td class="px-4 py-2">
                                <ul>
                                    <li v-for="habitacion in dato.habitaciones" :key="habitacion.id_habitacion">
                                        {{ habitacion.numero_habitacion }}
                                    </li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </LayoutAuthenticated>
</template>

<style scoped>
body {
    background-color: #edf8ff;
}

.table-header {
    background-color: #5589b9;
    color: white;
}

.table-column-header {
    background-color: #d9d9d9;
}

.card {
    min-width: 300px;
}
</style>
