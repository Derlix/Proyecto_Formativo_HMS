<script setup>
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
</script>

<template>
    <LayoutAuthenticated>
        <div class="m-10">

            <h2 class="text-2xl font-bold mb-4">Información de Reserva</h2>
            <div class="flex justify-end">
                    <button class="bg-gray-500 text-white py-2 px-4 rounded m-1">Factura temporal</button>
                    <button class="bg-gray-500 text-white py-2 px-4 rounded m-1">Crear check-out</button>
                    <button class="bg-green-500 text-white py-2 px-4 rounded m-1">Complementada con éxito</button>
            </div>

            <div class="rounded overflow-hidden shadow-lg mt-5">
                <div class="">
                    <div class="font-bold text-white mb-2 color2 px-6 py-4">Información de huesped</div>

                    <div class="flex flex-wrap mb-4 px-6 py-4">
                        <div class="flex flex-row w-full items-center justify-between">
                            <p class="text-gray-700 text-base">Reservado por: Juan Arias</p>
                            <p class="text-gray-700 text-base">Email: juan@gmail.com</p>
                            <p class="text-gray-700 text-base">Telefono: 1231231230</p>
                            <p class="text-gray-700 text-base">Ocupacion: Docente</p>
                        </div>
                    </div>

                    <div class="px-6 py-4">
                        <div class="font-bold text-xl mb-2">Observaciones</div>
                        <textarea class="w-1/2 h-24 p-2 border rounded"></textarea>
                    </div>
                </div>
            </div>

            <div class="rounded overflow-hidden shadow-lg mt-5">
                <div class="">
                    <div class="font-bold text-white mb-2 color2 px-6 py-4">Información de reserva</div>
                    <div class="flex flex-wrap mb-4 px-6 py-4">
                        <div class="flex flex-row w-full items-center justify-between">
                            <p class="text-gray-700 text-base">Tipo de habitación: Sencilla</p>
                            <p class="text-gray-700 text-base">Habitación: 1010</p>
                            <p class="text-gray-700 text-base">Cantidad Personas: 3</p>
                            <p class="text-gray-700 text-base">Cambio reserva: Sin cambios</p>
                            <p class="text-gray-700 text-base">Comprovante de reserva: No registrado</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="flex space-x-4">
                <div class="rounded overflow-hidden shadow-lg mt-5 flex-1">
                    <div>
                        <div class="font-bold text-white mb-2 color2 px-6 py-4">Check-in y check-out</div>
                        <div class="flex flex-wrap mb-4 px-6 py-4">
                            <div class="flex flex-row w-full items-center justify-between">
                                <p class="text-gray-700 text-base">Llegada: 20/05/07</p>
                                <p class="text-gray-700 text-base">Salida: 25/05/07</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="rounded overflow-hidden shadow-lg mt-5 flex-1">
                    <div>
                        <div class="font-bold text-white mb-2 color2 px-6 py-4">Información de dinero</div>
                        <div class="flex flex-wrap mb-4 px-6 py-4">
                            <div class="flex flex-row w-full items-center justify-between">
                                <p class="text-gray-700 text-base">Adelanto: $500000</p>
                                <p class="text-gray-700 text-base">Medio de pago: Efectivo</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="flex justify-end mt-5">
                    <button class="bg-green-500 text-white py-2 px-4 rounded m-1">¿Necesitas ayuda?</button>
            </div>


        </div>
    </LayoutAuthenticated>
</template>


<style scoped>
.color1 {
    background-color: #EFF8FF;
}

.color2 {
    background-color: #6287B4;
}
</style>