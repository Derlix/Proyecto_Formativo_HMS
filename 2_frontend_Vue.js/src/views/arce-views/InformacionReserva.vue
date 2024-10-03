<script setup>
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionMain from '@/components/SectionMain.vue';
import { mdiBallotOutline } from '@mdi/js';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import SectionTitle from '@/components/SectionTitle.vue';
import CardBox from '@/components/CardBox.vue';
import { reactive } from 'vue';
import { info_habitaciones } from '@/services/arce_service/informePasajeroService';

const infoHuesped = reactive({
    nombre: "María Pérez",
    email: "maria.perez@example.com",
    telefono: "5551234567",
    ocupacion: "Ingeniera"
})

const infoReserva = reactive({
    tipo: "Suite",
    habitacion: "101",
    cantidad: 2,
    cambio: "No",
    comprovante: "comprovante_12345.pdf",
})

const infoCheck = reactive({
    llegada: "2024-10-01",
    salida: "2024-10-05",
})

const infoDinero = reactive({
    adelanto: "$150.00",
    medio: "Tarjeta de Crédito",
})

// Función p

</script>

<template>
    <LayoutAuthenticated>
        <SectionMain>
            <TitleIconOnly :icon="mdiBallotOutline" title="Información reserva" />

            <div class="flex justify-end">
                <button
                    class="bg-blue-600 h-12 rounded-lg my-6 font-bold hover:bg-blue-900 text-white py-2 px-4 m-1">Factura
                    temporal</button>
                <button
                    class="bg-blue-600 h-12 rounded-lg my-6 font-bold hover:bg-blue-900 text-white py-2 px-4 m-1">Crear
                    check-out</button>
                <button
                    class="bg-blue-600 h-12 rounded-lg my-6 font-bold hover:bg-blue-900 text-white py-2 px-4 m-1">Complementada
                    con éxito</button>
            </div>

            <CardBox class="shadow-md">
                <SectionTitle>Información de huesped</SectionTitle>

                <div class="flex flex-wrap mb-4 px-6 py-4">
                    <div class="flex flex-row w-full items-center justify-between">
                        <p class="text-base">Nombre: {{ infoHuesped.nombre }}</p>
                        <p class="text-base">Email: {{ infoHuesped.email }}</p>
                        <p class="text-base">Teléfono: {{ infoHuesped.telefono }}</p>
                        <p class="text-base">Ocupación: {{ infoHuesped.ocupacion }}</p>
                    </div>
                </div>

                <div class="px-6 py-4">
                    <div class="font-bold text-xl mb-2">Observaciones</div>
                    <textarea class="w-1/2 h-24 p-2 border rounded text-black"></textarea>
                </div>
            </CardBox>

            <div class="flex mt-6">
                <CardBox class="shadow-md w-1/2">
                    <SectionTitle>Información de reserva</SectionTitle>

                    <div class="m-6">
                        <div class="space-y-6">
                            <div class="flex justify-between">
                                <p class="text-lg">Tipo de habitación:</p>
                                <p class="text-base">{{ infoReserva.tipo }}</p>
                            </div>

                            <div class="flex justify-between">
                                <p class="text-lg">Habitación:</p>
                                <p class="text-base">{{ infoReserva.habitacion }}</p>
                            </div>

                            <div class="flex justify-between">
                                <p class="text-lg">Cantidad de Personas:</p>
                                <p class="text-base">{{ infoReserva.cantidad }}</p>
                            </div>

                            <div class="flex justify-between">
                                <p class="text-lg">Cambio de Reserva:</p>
                                <p class="text-base">{{ infoReserva.cambio }}</p>
                            </div>

                            <div class="flex justify-between">
                                <p class="text-lg">Comprobante de Reserva:</p>
                                <p class="text-base">{{ infoReserva.comprovante }}</p>
                            </div>
                        </div>

                    </div>
                </CardBox>

                <div class="w-1/2 ml-6">

                    <CardBox class="shadow-md">
                        <SectionTitle>Check-in y check-out</SectionTitle>
                        <div class="flex flex-wrap mb-4 px-6 py-4">
                            <div class="flex flex-row w-full items-center justify-between">
                                <p class=" text-base">Llegada:{{ infoCheck.llegada }}</p>
                                <p class=" text-base">Salida: {{ infoCheck.salida }}</p>
                            </div>
                        </div>
                    </CardBox>

                    <CardBox class="shadow-md mt-6">
                        <SectionTitle>Información de dinero</SectionTitle>

                        <div class="flex flex-wrap mb-4 px-6 py-4">
                            <div class="flex flex-row w-full items-center justify-between">
                                <p class=" text-base">Adelanto: {{ infoDinero.adelanto }}</p>
                                <p class=" text-base">Medio de pago: {{ infoDinero.medio }}</p>
                            </div>
                        </div>
                    </CardBox>
                </div>
            </div>

            <div class="flex justify-end mt-5">
                <button class="bg-green-500 text-white py-2 px-4 rounded m-1">¿Necesitas ayuda?</button>
            </div>

        </SectionMain>
    </LayoutAuthenticated>
</template>