<script setup>
import { ref, watch } from 'vue'

// Definir propiedades para recibir el estado de visibilidad del modal
const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  }
})

// Emitir evento de cierre
const emit = defineEmits(['close'])

const mostrarModal = ref(false)

// Sincronizar el estado local del modal con la propiedad 'visible'
watch(
  () => props.visible,
  (newValue) => {
    mostrarModal.value = newValue
  }
)

function cerrarModal() {
  mostrarModal.value = false
  emit('close')
}

function siguientePaso() {
  // Lógica para avanzar al siguiente paso
}
</script>

<template>
  <!-- Modal -->
  <div
    v-if="mostrarModal"
    class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50"
  >
    <div class="max-w-3xl w-full p-8 bg-white shadow-lg rounded-lg relative">
      <button @click="cerrarModal" class="absolute top-4 right-4 text-gray-500 hover:text-gray-700">
        &times;
      </button>

      <h1 class="text-lg font-bold mb-4 text-center">Formulario crear reserva</h1>

      <!-- Pasos del formulario -->
      <div class="flex items-center justify-center space-x-2 mb-8">
        <div class="flex items-center space-x-1">
          <div class="w-8 h-8 flex items-center justify-center bg-blue-600 text-white rounded-full">
            1
          </div>
          <span class="font-medium text-gray-700">Datos de la reserva</span>
        </div>
        <div class="flex-grow border-t border-gray-300"></div>
        <div class="w-8 h-8 flex items-center justify-center bg-gray-300 text-white rounded-full">
          2
        </div>
        <div class="w-8 h-8 flex items-center justify-center bg-gray-300 text-white rounded-full">
          3
        </div>
        <div class="w-8 h-8 flex items-center justify-center bg-gray-300 text-white rounded-full">
          4
        </div>
      </div>

      <!-- Formulario dentro del modal -->
      <form @submit.prevent="siguientePaso">
        <div class="grid grid-cols-2 gap-4 mb-4">
          <!-- Ocupantes -->
          <div>
            <label class="block text-sm font-medium text-gray-700">Ocupantes:</label>
            <div class="flex items-center space-x-2">
              <div class="flex items-center space-x-1">
                <button
                  type="button"
                  @click="decrementar(adultos)"
                  class="w-8 h-8 flex items-center justify-center bg-gray-300 text-gray-700 rounded"
                >
                  -
                </button>
                <span class="px-2">{{ adultos }}</span>
                <button
                  type="button"
                  @click="incrementar(adultos)"
                  class="w-8 h-8 flex items-center justify-center bg-gray-300 text-gray-700 rounded"
                >
                  +
                </button>
              </div>
              <span>Adultos</span>
            </div>
            <div class="flex items-center space-x-2 mt-2">
              <div class="flex items-center space-x-1">
                <button
                  type="button"
                  @click="decrementar(ninos)"
                  class="w-8 h-8 flex items-center justify-center bg-gray-300 text-gray-700 rounded"
                >
                  -
                </button>
                <span class="px-2">{{ ninos }}</span>
                <button
                  type="button"
                  @click="incrementar(ninos)"
                  class="w-8 h-8 flex items-center justify-center bg-gray-300 text-gray-700 rounded"
                >
                  +
                </button>
              </div>
              <span>Niños</span>
            </div>
          </div>

          <!-- Tarifa -->
          <div>
            <label for="tarifa" class="block text-sm font-medium text-gray-700">Tarifa:</label>
            <input type="text" id="tarifa" class="mt-1 block w-full border rounded-md p-2" />
          </div>

          <!-- Impuestos -->
          <div>
            <label for="impuestos" class="block text-sm font-medium text-gray-700"
              >Impuestos:</label
            >
            <input type="text" id="impuestos" class="mt-1 block w-full border rounded-md p-2" />
          </div>

          <!-- Fecha de llegada -->
          <div>
            <label for="fechaLlegada" class="block text-sm font-medium text-gray-700"
              >Llegada:</label
            >
            <input
              type="date"
              v-model="fechaLlegada"
              id="fechaLlegada"
              class="mt-1 block w-full border rounded-md p-2"
            />
          </div>

          <!-- Fecha de salida -->
          <div>
            <label for="fechaSalida" class="block text-sm font-medium text-gray-700">Salida:</label>
            <input
              type="date"
              v-model="fechaSalida"
              id="fechaSalida"
              class="mt-1 block w-full border rounded-md p-2"
            />
          </div>         
        </div>

        <!-- Botones para cerrar y avanzar en el formulario -->
        <div class="flex justify-between">
          <button
            type="button"
            @click="cerrarModal"
            class="bg-gray-300 text-gray-700 font-semibold py-2 px-4 rounded-md hover:bg-gray-400 transition"
          >
            Cerrar
          </button>
          <button
            type="submit"
            class="bg-blue-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 transition"
          >
            Siguiente
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
