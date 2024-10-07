<script setup>
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import SectionMain from '@/components/SectionMain.vue';
import { mdiBallotOutline } from '@mdi/js';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import SectionTitle from '@/components/SectionTitle.vue';
import CardBox from '@/components/CardBox.vue';
import { reactive, onMounted } from 'vue';
import { getHuespedByDocument } from '@/services/huespedService';

const numeroDocumento = '1012345678'; // Cédula fija

const infoHuesped = reactive({
    nombre: "",
    email: "",
    telefono: "",
    ocupacion: ""
});

const error = reactive({
    message: null
});

const fetchHuesped = async () => {
    try {
        const response = await getHuespedByDocument(numeroDocumento);
        error.message = null; // Limpiar el error si la llamada fue exitosa

        // Asignar los datos necesarios a infoHuesped
        infoHuesped.nombre = response.data.nombre_completo; 
        infoHuesped.email = response.data.email;
        infoHuesped.telefono = response.data.telefono;
        infoHuesped.ocupacion = response.data.ocupacion;
    } catch (err) {
        error.message = err.response ? err.response.data : 'Error de red o de servidor';
        // Limpiar los datos del huésped si hay un error
        infoHuesped.nombre = "";
        infoHuesped.email = "";
        infoHuesped.telefono = "";
        infoHuesped.ocupacion = "";
    }
};

// Llamar a la función al montar el componente
onMounted(() => {
    fetchHuesped();
});

const infoReserva = reactive({
    tipo: "Suite",
    habitacion: "101",
    cantidad: 2,
    cambio: "No",
    comprovante: "comprovante_12345.pdf",
});

const infoCheck = reactive({
    llegada: "2024-10-01",
    salida: "2024-10-05",
});

const infoDinero = reactive({
    adelanto: "$150.00",
    medio: "Tarjeta de Crédito",
});
</script>

<template>
    <LayoutAuthenticated>
        <SectionMain>
            <TitleIconOnly :icon="mdiBallotOutline" title="Información reserva" />

            <div class="flex flex-col sm:flex-row justify-end mb-4">
                <button class="bg-blue-600 h-12 rounded-lg my-2 font-bold hover:bg-blue-900 text-white py-2 px-4 mx-1">Factura temporal</button>
                <button class="bg-blue-600 h-12 rounded-lg my-2 font-bold hover:bg-blue-900 text-white py-2 px-4 mx-1">Crear check-out</button>
                <button class="bg-blue-600 h-12 rounded-lg my-2 font-bold hover:bg-blue-900 text-white py-2 px-4 mx-1">Complementada con éxito</button>
            </div>

            <CardBox class="shadow-md mb-4">
                <SectionTitle>Información de huésped</SectionTitle>
                <div class="flex flex-col mb-4 px-6 py-4">
                    <div class="flex flex-col sm:flex-row sm:justify-between">
                        <div class="flex-1 mb-4 sm:mb-0">
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Nombre:</p>
                                <p class="text-base">{{ infoHuesped.nombre }}</p>
                            </div>
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Email:</p>
                                <p class="text-base">{{ infoHuesped.email }}</p>
                            </div>
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Teléfono:</p>
                                <p class="text-base">{{ infoHuesped.telefono }}</p>
                            </div>
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Ocupación:</p>
                                <p class="text-base">{{ infoHuesped.ocupacion }}</p>
                            </div>
                        </div>
                        <div class="flex-1 ml-6">
                            <div class="font-bold text-xl mb-2">Observaciones</div>
                            <textarea class="w-full h-24 p-2 border rounded text-black"></textarea>
                        </div>
                    </div>
                </div>
            </CardBox>

            <div class="flex flex-col sm:flex-row mt-6">
                <CardBox class="shadow-md w-full sm:w-1/2 mb-4 sm:mb-0">
                    <SectionTitle>Información de reserva</SectionTitle>
                    <div class="m-6 space-y-6">
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
                </CardBox>

                <div class="w-full sm:w-1/2 sm:ml-6">
                    <CardBox class="shadow-md mb-4">
                        <SectionTitle>Check-in y check-out</SectionTitle>
                        <div class="flex flex-col sm:flex-row mb-4 px-6 py-4">
                            <div class="flex-1 mb-2 sm:mb-0 flex justify-between">
                                <p class="text-base">Llegada:</p>
                                <p class="text-base">{{ infoCheck.llegada }}</p>
                            </div>
                            <div class="flex-1 flex justify-between">
                                <p class="text-base">Salida:</p>
                                <p class="text-base">{{ infoCheck.salida }}</p>
                            </div>
                        </div>
                    </CardBox>

                    <CardBox class="shadow-md">
                        <SectionTitle>Información de dinero</SectionTitle>
                        <div class="flex flex-col mb-4 px-6 py-4">
                            <div class="flex justify-between mb-2">
                                <p class="text-base">Adelanto:</p>
                                <p class="text-base">{{ infoDinero.adelanto }}</p>
                            </div>
                            <div class="flex justify-between">
                                <p class="text-base">Medio de pago:</p>
                                <p class="text-base">{{ infoDinero.medio }}</p>
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
