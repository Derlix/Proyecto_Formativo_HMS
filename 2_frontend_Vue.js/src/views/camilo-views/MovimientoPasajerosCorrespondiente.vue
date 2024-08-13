<script setup>
import { ref } from 'vue'
import BaseButton from '@/components/BaseButton.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'

const nombre = ref('')
const apellido = ref('')
const fechaEntrada = ref('')
const fechaSalida = ref('')
const procedencia = ref('')
const destino = ref('')
const numeroDocumento = ref('')
const expedicion = ref('')
const registro = ref('')
const profesion = ref('')
const observaciones = ref('')

const verListaPasajeros = () => {
  // Lógica para ver la lista de pasajeros
}

const registrar = () => {
  // Lógica para registrar
}

const regresar = () => {
  // Lógica para regresar
}
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton title="Registro de Pasajeros" />

      <form @submit.prevent="registrar" class="space-y-6 bg-white p-8 rounded-lg shadow-md">
        <div class="flex justify-between space-x-4 mt-6">
          <BaseButton @click="verListaPasajeros" color="info" outline label="Ver Lista de Pasajeros" />
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="nombre" class="block text-sm font-medium text-gray-700">Nombre</label>
            <input v-model="nombre" id="nombre" type="text" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Nombre">
          </div>

          <div>
            <label for="apellido" class="block text-sm font-medium text-gray-700">Apellido</label>
            <input v-model="apellido" id="apellido" type="text" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Apellido">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="fechaEntrada" class="block text-sm font-medium text-gray-700">Fecha de Entrada</label>
            <input v-model="fechaEntrada" id="fechaEntrada" type="date" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
          </div>

          <div>
            <label for="fechaSalida" class="block text-sm font-medium text-gray-700">Fecha de Salida</label>
            <input v-model="fechaSalida" id="fechaSalida" type="date" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="procedencia" class="block text-sm font-medium text-gray-700">Procedencia</label>
            <input v-model="procedencia" id="procedencia" type="text" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Procedencia">
          </div>

          <div>
            <label for="destino" class="block text-sm font-medium text-gray-700">Destino</label>
            <input v-model="destino" id="destino" type="text" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Destino">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="numeroDocumento" class="block text-sm font-medium text-gray-700">Número de Documento</label>
            <input v-model="numeroDocumento" id="numeroDocumento" type="number" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Número de Documento">
          </div>

          <div>
            <label for="expedicion" class="block text-sm font-medium text-gray-700">Expedición</label>
            <input v-model="expedicion" id="expedicion" type="text" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Expedición">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="registro" class="block text-sm font-medium text-gray-700">Registro</label>
            <input v-model="registro" id="registro" type="text" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Registro">
          </div>

          <div>
            <label for="profesion" class="block text-sm font-medium text-gray-700">Profesión</label>
            <input v-model="profesion" id="profesion" type="text" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Profesión">
          </div>
        </div>

        <div>
          <label for="observaciones" class="block text-sm font-medium text-gray-700">Observaciones</label>
          <textarea v-model="observaciones" id="observaciones" required class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" placeholder="Observaciones"></textarea>
        </div>

        <div class="flex justify-between space-x-4 mt-6">
          <BaseButton type="submit" color="info" label="Registrar" />
          <BaseButton @click="regresar" color="info" outline label="Regresar" />
        </div>
      </form>
    </SectionMain>
  </LayoutAuthenticated>
</template>
