<script setup>
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
</script>

<template>
    <LayoutAuthenticated>
        <div class="max-w-6xl mx-auto p-6 bg-white shadow-md rounded-lg">
            <h1 class="text-2xl font-bold mb-4">Solicitud de Avance de Efectivo</h1>

            <form @submit.prevent="submitForm">
                <div class="mb-4">
                    <label for="fecha" class="block text-sm font-medium text-gray-700">Fecha:</label>
                    <input type="date" id="fecha" v-model="fecha" class="mt-1 block w-full border rounded-md p-2"
                        required>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                    <div>
                        <label for="habitacion" class="block text-sm font-medium text-gray-700">N. Habitación:</label>
                        <input type="text" id="habitacion" v-model="habitacion"
                            class="mt-1 block w-full border rounded-md p-2" required>
                    </div>
                    <div>
                        <label for="huesped" class="block text-sm font-medium text-gray-700">Huésped:</label>
                        <input type="text" id="huesped" v-model="huesped"
                            class="mt-1 block w-full border rounded-md p-2" required>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                    <div>
                        <label for="tipo_identificacion" class="block text-sm font-medium text-gray-700">Tipo:</label>
                        <select id="tipo_identificacion" v-model="tipoIdentificacion"
                            class="mt-1 block w-full border rounded-md p-2" required>
                            <option value="">Tipo de documento</option>
                            <option value="cedula">Cédula</option>
                            <option value="pasaporte">Pasaporte</option>
                            <option value="ruc">RUC</option>
                        </select>
                    </div>
                    <div>
                        <label for="identificacion" class="block text-sm font-medium text-gray-700">Número:</label>
                        <input type="text" id="identificacion" v-model="identificacion"
                            class="mt-1 block w-full border rounded-md p-2" required>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                    <div>
                        <label for="descripcion" class="block text-sm font-medium text-gray-700">Descripción:</label>
                        <input type="text" id="descripcion" v-model="descripcion"
                            class="mt-1 block w-full border rounded-md p-2" required>
                    </div>
                    <div>
                        <label for="valor" class="block text-sm font-medium text-gray-700">Valor:</label>
                        <input type="text" id="valor" v-model="valor" class="mt-1 block w-full border rounded-md p-2"
                            required>
                    </div>
                    <div>
                        <label for="autorizado" class="block text-sm font-medium text-gray-700">Autorizado por:</label>
                        <input type="text" id="autorizado" v-model="autorizado"
                            class="mt-1 block w-full border rounded-md p-2" required>
                    </div>
                </div>

                <div class="flex justify-between mt-6">
                    <button type="submit"
                        class="w-1/2 bg-blue-600 text-white font-semibold py-2 rounded-md hover:bg-blue-700 transition">Registrar</button>
                    <button type="reset"
                        class="w-1/2 bg-gray-300 text-gray-700 font-semibold py-2 rounded-md hover:bg-gray-400 transition">Cancelar</button>
                </div>
            </form>
        </div>
    </LayoutAuthenticated>
</template>

<script>
export default {
    name: 'SolicitudAvanceEfectivo',
    data() {
        return {
            fecha: '',
            habitacion: '',
            huesped: '',
            tipoIdentificacion: '',
            identificacion: '',
            descripcion: '',
            valor: '',
            autorizado: ''
        }
    },
    methods: {
        submitForm() {
            // Aquí puedes agregar la lógica para enviar el formulario
            console.log('Formulario enviado:', {
                fecha: this.fecha,
                habitacion: this.habitacion,
                huesped: this.huesped,
                tipoIdentificacion: this.tipoIdentificacion,
                identificacion: this.identificacion,
                descripcion: this.descripcion,
                valor: this.valor,
                autorizado: this.autorizado
            });
        }
    }
}
</script>