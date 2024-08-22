<script setup>
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
</script>

<template>
  <LayoutAuthenticated>
    <div class="max-w-lg mx-auto p-8 rounded-lg shadow-md bg-[#6287B4]">
      <h2 class="text-2xl font-bold mb-6 text-center text-white">Traspaso a particulares</h2>

      <form @submit.prevent="submitForm">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="mb-4">
            <label for="factura" class="block text-sm font-medium text-white">Factura</label>
            <input type="text" id="factura" v-model="factura" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required>
          </div>

          <div class="mb-4">
            <label for="fecha" class="block text-sm font-medium text-white">Fecha</label>
            <input type="date" id="fecha" v-model="fecha" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required>
          </div>

          <div class="mb-4">
            <label for="tarjeta" class="block text-sm font-medium text-white">Tarjeta de Crédito</label>
            <select id="tarjeta" v-model="tarjeta" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required>
              <option value="">Seleccione...</option>
              <option value="diners">Diners</option>
              <option value="american">American Express</option>
              <option value="visa">Visa</option>
              <option value="master">MasterCard</option>
            </select>
          </div>

          <div class="mb-4">
            <label for="habitacion" class="block text-sm font-medium text-white">Habitación</label>
            <input type="text" id="habitacion" v-model="habitacion" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required>
          </div>

          <div class="mb-4">
            <label for="nombre" class="block text-sm font-medium text-white">Nombre</label>
            <input type="text" id="nombre" v-model="nombre" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required>
          </div>

          <div class="mb-4 col-span-1 md:col-span-2">
            <label for="document" class="block text-sm font-medium leading-6 text-white">Documento</label>
            <div class="relative mt-2 rounded-md shadow-sm flex">
              <div class="absolute inset-y-0 left-0 flex items-center">
                <label for="document-type" class="sr-only">Tipo de documento</label>
                <select id="document-type" v-model="documentType" class="h-full rounded-l-md border-0 bg-transparent py-0 pl-2 pr-7 text-gray-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm">
                  <option>C.C</option>
                  <option>T.I</option>
                  <option>EXT</option>
                </select>
              </div>
              <input type="text" v-model="document" id="document" class="block w-full rounded-r-md border-0 py-1.5 pl-24 pr-3 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Número de documento">
            </div>
          </div>

          <div class="mb-4">
            <label for="depositos" class="block text-sm font-medium text-white">Depósitos</label>
            <select id="depositos" v-model="depositos" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required>
              <option value="">Seleccionar</option>
              <option value="causados">Causados</option>
              <option value="pagos">Pagos</option>
            </select>
          </div>

          <div class="mb-4">
            <label for="particulares" class="block text-sm font-medium text-white">Particulares</label>
            <input type="text" id="particulares" v-model="particulares" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required>
          </div>

          <div class="mb-4">
            <label for="elaborado_por" class="block text-sm font-medium text-white">Elaborado por</label>
            <input type="text" id="elaborado_por" v-model="elaboradoPor" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required>
          </div>

          <div class="mb-4">
            <label for="turno" class="block text-sm font-medium text-white">Turno</label>
            <input type="text" id="turno" v-model="turno" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required>
          </div>
        </div>

        <button type="submit" class="w-full bg-green-600 text-white p-2 rounded-md hover:bg-green-500">Registrar</button>
      </form>
    </div>
  </LayoutAuthenticated>
</template>

<script>
export default {
  name: 'TraspasoAParticulares',
  data() {
    return {
      factura: '',
      fecha: '',
      tarjeta: '',
      habitacion: '',
      nombre: '',
      documentType: 'C.C',
      document: '',
      depositos: '',
      particulares: '',
      elaboradoPor: '',
      turno: ''
    }
  },
  methods: {
    submitForm() {
      // Aquí puedes agregar la lógica para enviar el formulario
      console.log('Formulario enviado:', {
        factura: this.factura,
        fecha: this.fecha,
        tarjeta: this.tarjeta,
        habitacion: this.habitacion,
        nombre: this.nombre,
        documentType: this.documentType,
        document: this.document,
        depositos: this.depositos,
        particulares: this.particulares,
        elaboradoPor: this.elaboradoPor,
        turno: this.turno
      });
    }
  }
}
</script>

<style scoped>
.color1 {
  background-color: #EFF8FF;
}
.color2 {
  background-color: #6287B4;
}
</style>