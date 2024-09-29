<script setup>
import ModalAlert from './ModalAlert.vue';
import { ref } from 'vue';
import { mdiAlert, mdiCheckCircle } from '@mdi/js'

const props = defineProps({
  visible: {
    type: Boolean,
    required: true
  }
})

const showModal = ref(false)

const emit = defineEmits(['close'])

const close = () => {
  emit('close')
}
</script>

<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 text-black dark:bg-opacity-70">
    <div class="bg-white dark:bg-gray-800 p-8 sm:p-12 rounded-lg shadow-lg max-w-2xl w-full relative">
      <!-- Botón de cerrar -->
      <button @click="close" class="absolute top-4 right-4 text-gray-600 dark:text-gray-300">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <h2 class="text-2xl mb-6 font-semibold text-gray-900 dark:text-white">Registrar Salida</h2>
      <div class="grid grid-cols-3 gap-4 mb-5">
        <input type="text" name="Buscar" class="col-span-2 rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600">
        <button class="bg-blue-600 hover:bg-blue-700 text-white p-2 rounded-lg">Buscar</button>
      </div>
      <div class="overflow-x-auto max-h-64 mb-6">
        <table class="table-fixed border-4 bg-gray-200 dark:bg-gray-700 border-gray-600 dark:border-gray-600 rounded-xl">
          <thead class="border-2 border-black dark:border-gray-500">
            <tr>
              <th class="text-center py-2 border border-black dark:border-gray-500">N° Identificacion</th>
              <th class="text-center py-2 border border-black dark:border-gray-500">Reserva</th>
              <th class="text-center py-2 border border-black dark:border-gray-500">Nombre</th>
              <th class="text-center py-2 border border-black dark:border-gray-500">R. Salida</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-center py-2">1042423239</td>
              <td class="text-center py-2">5234</td>
              <td class="text-center py-2">Jose David Petro</td>
              <td class="text-center py-2"><input type="checkbox" class="rounded w-7 h-7"></td>
            </tr>
            <tr>
              <td class="text-center py-2">1023333339</td>
              <td class="text-center py-2">5122</td>
              <td class="text-center py-2">Gustavo Petro</td>
              <td class="text-center py-2"><input type="checkbox" class="rounded w-7 h-7"></td>
            </tr>
            <tr>
              <td class="text-center py-2">0234314425</td>
              <td class="text-center py-2">4233</td>
              <td class="text-center py-2">Ivan Duque</td>
              <td class="text-center py-2"><input type="checkbox" class="rounded w-7 h-7"></td>
            </tr>
            <tr>
              <td class="text-center py-2">1333520098</td>
              <td class="text-center py-2">4124</td>
              <td class="text-center py-2">Madurito</td>
              <td class="text-center py-2"><input type="checkbox" class="rounded w-7 h-7"></td>
            </tr>
          </tbody>
        </table>
      </div>

      <button @click="showModal = true" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded w-full">Confirmar Salida</button>

      <ModalAlert
        :visible="showModal"
        @close="showModal = false"
        :icon="mdiCheckCircle"
        :color="'text-blue-600'"
        descripcion="Salida confirmada con éxito."
        textBoton="Cerrar"
        v-on:click="close"
      />
    </div>
  </div>
</template>
