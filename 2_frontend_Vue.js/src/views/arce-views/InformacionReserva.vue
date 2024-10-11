<script setup>
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import SectionMain from '@/components/SectionMain.vue';
import { mdiBallotOutline } from '@mdi/js';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import SectionTitle from '@/components/SectionTitle.vue';
import CardBox from '@/components/CardBox.vue';
import { reactive, onMounted } from 'vue';
import { getReservaById } from '@/services/arce_service/reservasService';
import { obtenerHabitacionPorId } from '@/services/juanca_service/habitacionService';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const error = reactive({
    message: null
});

const dataReserva = reactive({
    nombre: "",
    email: "",
    telefono: "",
    ocupacion: "",
    direccion: "",
    tipo_documento: "",
    numero_documento: "",
    fecha_expedicion: "",
    fecha_reserva: "",
    empresa: "",
    valor_deposito: 0,
    forma_pago: "",
    estado_reserva: ""
});

const dataHabitacion = reactive({
    numero: "",
    estado: "",
    piso: 0,
    precio_fijo: "",
    tipo: "",
    caracteristica: "",
    adicional: "",
});


const fetchHabitacion = async () => {
    try {
        const habitacionId = 4;
        const response = await obtenerHabitacionPorId(habitacionId);
        error.message = null;

        const habitacion = response.data;
        const categoria = response.data.categoria;
        const caracteristica = response.data.caracteristicas;

        dataHabitacion.numero = habitacion.numero_habitacion
        dataHabitacion.estado = habitacion.estado
        dataHabitacion.piso = habitacion.piso
        dataHabitacion.precio_fijo = categoria.precio_fijo
        dataHabitacion.tipo = categoria.tipo_habitacion
        dataHabitacion.caracteristica = caracteristica.nombre_caracteristicas
        dataHabitacion.adicional = caracteristica.adicional

    } catch (err) {
        error.message = err.response ? err.response.data : 'Error de red o de servidor';
    }
}

const fetchDataReserva = async () => {
    try {
        const reservaId = route.params.id;
        const response = await getReservaById(reservaId);

        error.message = null;
        const huesped = response.huesped;

        dataReserva.nombre = huesped.nombre_completo;
        dataReserva.email = huesped.email;
        dataReserva.telefono = huesped.telefono;
        dataReserva.ocupacion = huesped.ocupacion;
        dataReserva.direccion = huesped.direccion;
        dataReserva.tipo_documento = huesped.tipo_documento;
        dataReserva.numero_documento = huesped.numero_documento;
        dataReserva.fecha_expedicion = huesped.fecha_expedicion;
        dataReserva.fecha_reserva = response.fecha_reserva;
        dataReserva.empresa = response.empresa;
        dataReserva.valor_deposito = Number(response.valor_deposito);
        dataReserva.forma_pago = response.forma_pago;
        dataReserva.estado_reserva = response.estado_reserva;

    } catch (err) {
        error.message = err.response ? err.response.data : 'Error de red o de servidor';
        Object.assign(dataReserva, {
            nombre: "",
            email: "",
            telefono: "",
            ocupacion: "",
            direccion: "",
            tipo_documento: "",
            numero_documento: "",
            fecha_expedicion: "",
            fecha_reserva: "",
            empresa: "",
            valor_deposito: 0,
            forma_pago: "",
            estado_reserva: ""
        });
    }
};

const goToReservas = () => {
    router.push({ name: 'reservas' });
}

onMounted(() => {
    fetchHabitacion()
    fetchDataReserva();
});
</script>


<template>
    <LayoutAuthenticated>
        <SectionMain>
            <TitleIconOnly :icon="mdiBallotOutline" title="Información reserva" />

            <div class="flex justify-between items-center mb-4">
                <button @click="goToReservas" class="bg-blue-600 h-12 rounded-lg font-bold hover:bg-blue-900 text-white transition duration-300 ease-in-out py-2 px-6 shadow-lg transform hover:scale-105">Regresar</button>
                <div class="flex space-x-4">
                    <button class="bg-blue-600 h-12 rounded-lg font-bold hover:bg-blue-900 text-white transition duration-300 ease-in-out py-2 px-6 shadow-lg transform hover:scale-105">Factura temporal</button>
                    <button class="bg-blue-600 h-12 rounded-lg font-bold hover:bg-blue-900 text-white transition duration-300 ease-in-out py-2 px-6 shadow-lg transform hover:scale-105">Crear check-out</button>
                    <button class="bg-blue-600 h-12 rounded-lg font-bold hover:bg-blue-900 text-white transition duration-300 ease-in-out py-2 px-6 shadow-lg transform hover:scale-105">Complementada con éxito</button>
                </div>
            </div>

            <div class="flex flex-col sm:flex-row mt-6 gap-6">

                <CardBox class="shadow-md w-full sm:w-1/2">
                    <SectionTitle>Información de huésped</SectionTitle>
                    <div class="flex flex-col mb-4 px-6 py-4">
                        <div class="flex flex-col">
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Nombre:</p>
                                <p class="text-base">{{ dataReserva.nombre }}</p>
                            </div>
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Tipo documento:</p>
                                <p class="text-base">{{ dataReserva.tipo_documento }}</p>
                            </div>
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Número documento:</p>
                                <p class="text-base">{{ dataReserva.numero_documento }}</p>
                            </div>
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Fecha expedición:</p>
                                <p class="text-base">{{ dataReserva.fecha_expedicion }}</p>
                            </div>
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Email:</p>
                                <p class="text-base">{{ dataReserva.email }}</p>
                            </div>
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Teléfono:</p>
                                <p class="text-base">{{ dataReserva.telefono }}</p>
                            </div>
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Ocupación:</p>
                                <p class="text-base">{{ dataReserva.ocupacion }}</p>
                            </div>
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Dirección:</p>
                                <p class="text-base">{{ dataReserva.direccion }}</p>
                            </div>
                        </div>
                    </div>
                </CardBox>

                <CardBox class="shadow-md w-full sm:w-1/2 mb-4 sm:mb-0">
                    <SectionTitle>Información de reserva</SectionTitle>
                    <div class="m-6 space-y-6">
                        <div class="flex justify-between">
                            <p class="text-lg">Fecha:</p>
                            <p class="text-base">{{ dataReserva.fecha_reserva }}</p>
                        </div>
                        <div class="flex justify-between">
                            <p class="text-lg">Empresa:</p>
                            <p class="text-base">{{ dataReserva.empresa }}</p>
                        </div>
                        <div class="flex justify-between">
                            <p class="text-lg">Depósito:</p>
                            <p class="text-base">{{ dataReserva.valor_deposito }}</p>
                        </div>
                        <div class="flex justify-between">
                            <p class="text-lg">Forma de pago:</p>
                            <p class="text-base">{{ dataReserva.forma_pago }}</p>
                        </div>
                        <div class="flex justify-between">
                            <p class="text-lg">Estado:</p>
                            <p class="text-base">{{ dataReserva.estado_reserva }}</p>
                        </div>
                    </div>
                </CardBox>
            </div>

            <div class="flex flex-col sm:flex-row mt-6 gap-6">
                <CardBox class="shadow-md w-full sm:w-1/2 mb-4 sm:mb-0">
                    <SectionTitle>Información de habitación</SectionTitle>
                    <div class="flex flex-col mb-4 px-6 py-4">
                        <div class="flex justify-between mb-2">
                            <p class="text-base">Número:</p>
                            <p class="text-base">{{ dataHabitacion.numero }}</p>
                        </div>
                        <div class="flex justify-between mb-2">
                            <p class="text-base">Estado:</p>
                            <p class="text-base">{{ dataHabitacion.estado }}</p>
                        </div>
                        <div class="flex justify-between mb-2">
                            <p class="text-base">Piso:</p>
                            <p class="text-base">{{ dataHabitacion.piso }}</p>
                        </div>
                        <div class="flex justify-between mb-2">
                            <p class="text-base">Precio fijo:</p>
                            <p class="text-base">{{ dataHabitacion.precio_fijo }}</p>
                        </div>
                        <div class="flex justify-between mb-2">
                            <p class="text-base">Tipo:</p>
                            <p class="text-base">{{ dataHabitacion.tipo }}</p>
                        </div>
                        <div class="flex justify-between mb-2">
                            <p class="text-base">Características:</p>
                            <p class="text-base">{{ dataHabitacion.caracteristica }}</p>
                        </div>
                        <div class="flex justify-between mb-2">
                            <p class="text-base">Adicional:</p>
                            <p class="text-base">{{ dataHabitacion.adicional }}</p>
                        </div>
                    </div>
                </CardBox>
            </div>

            <div class="flex justify-end mt-5">
                <button class="bg-green-500 text-white py-2 px-4 rounded m-1">¿Necesitas ayuda?</button>
            </div>
        </SectionMain>
    </LayoutAuthenticated>
</template>
