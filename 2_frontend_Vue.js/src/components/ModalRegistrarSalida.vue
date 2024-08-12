<template>
    <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 text-black">
      <div class="bg-blue-100 p-16 rounded-lg shadow-lg max-w-2xl w-full">
        <h2 class="text-2xl mb-6">Registrar Salida</h2>
        <div class="grid grid-cols-3 gap-4">
            <input type="text" name="Buscar" class="col-span-2 rounded-lg p-2">
            <button class="bg-blue-950 rounded-lg text-white p-2">Buscar</button>
        </div>
        <button class="bg-blue-950 rounded-lg text-white my-4 w-48 h-12">Registrar Adicional</button>
        <div class="overflow-x-auto max-h-64 mb-6">
            <table class="table-fixed border-4 bg-blue-300 border-blue-600 rounded-xl">
              <thead class="border-2 border-black">
                <tr>
                  <th class="text-center py-2 border border-black">N° Identificacion</th>
                  <th class="text-center py-2 border border-black">Reserva</th>
                  <th class="text-center py-2 border border-black">Nombre</th>
                  <th class="text-center py-2 border border-black">R. Entrada</th>
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
                  <td class="text-center py-2 "><input type="checkbox" class="rounded w-7 h-7"></td>
                </tr>
                <tr>
                  <td class="text-center py-2">0234314425</td>
                  <td class="text-center py-2">4233</td>
                  <td class="text-center py-2">Ivan Duque</td>
                  <td class="text-center py-2 "><input type="checkbox" class="rounded w-7 h-7"></td>
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
          
        <button @click="close" class="bg-blue-950 text-white px-6 py-3 rounded w-full">Confirmar Salida</button>
      </div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    visible: {
      type: Boolean,
      required: true
    }
  })
  
  const emit = defineEmits(['close'])
  
  const close = () => {
    emit('close')
  }
  </script>
  