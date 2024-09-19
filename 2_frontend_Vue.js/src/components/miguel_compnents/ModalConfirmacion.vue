<template>
  <div
    v-if="visible"
    class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
  >
    <div
      class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-2xl w-full relative transition-all"
    >
      <button
        @click="cerrarModal"
        class="absolute top-4 right-4 text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300"
      >
        &times;
      </button>

      <h1 class="text-xl font-semibold mb-4 text-center text-gray-900 dark:text-white">
        Formulario crear reserva
      </h1>

      <div class="flex justify-center mb-6">
        <span class="text-gray-700 dark:text-gray-300 mx-2">Datos de la reserva</span>
      </div>

      <div class="grid grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Adultos</label>
          <div class="flex items-center">
            <button
              @click="disminuirAdultos"
              class="bg-gray-300 dark:bg-gray-700 text-gray-700 dark:text-white px-2 py-1 rounded-l"
            >
              -
            </button>
            <input
              type="number"
              v-model="adultos"
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-r bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
              readonly
            />
            <button
              @click="aumentarAdultos"
              class="bg-gray-300 dark:bg-gray-700 text-gray-700 dark:text-white px-2 py-1 rounded-r"
            >
              +
            </button>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Niños</label>
          <div class="flex items-center">
            <button
              @click="disminuirNinos"
              class="bg-gray-300 dark:bg-gray-700 text-gray-700 dark:text-white px-2 py-1 rounded-l"
            >
              -
            </button>
            <input
              type="number"
              v-model="ninos"
              class="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-r bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
              readonly
            />
            <button
              @click="aumentarNinos"
              class="bg-gray-300 dark:bg-gray-700 text-gray-700 dark:text-white px-2 py-1 rounded-r"
            >
              +
            </button>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Tarifa</label>
          <input
            type="text"
            v-model="tarifa"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Impuestos</label
          >
          <input
            type="text"
            v-model="impuestos"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Llegada</label>
          <div class="grid grid-cols-2 gap-2">
            <input
              type="text"
              v-model="llegadaDia"
              class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            />
            <input
              type="text"
              v-model="llegadaMes"
              class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            />
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Salida</label>
          <div class="grid grid-cols-2 gap-2">
            <input
              type="text"
              v-model="salidaDia"
              class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            />
            <input
              type="text"
              v-model="salidaMes"
              class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            />
          </div>
        </div>

        <div class="col-span-2">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Estadía</label>
          <input
            type="text"
            v-model="estadia"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>
      </div>

      <div class="flex justify-between mt-6">
        <button
          @click="atras"
          class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-200 font-semibold py-2 px-4 rounded-md hover:bg-gray-400 dark:hover:bg-gray-500 transition"
        >
          Atrás
        </button>
        <button
          @click="siguiente"
          class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition"
        >
          Siguiente
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  visible: Boolean,
  huesped: Object
})



const emit = defineEmits(['close', 'confirm'])


function cerrarModal() {
  emit('close')
}

function confirmarReserva() {
  cerrarModal()
}
</script>
