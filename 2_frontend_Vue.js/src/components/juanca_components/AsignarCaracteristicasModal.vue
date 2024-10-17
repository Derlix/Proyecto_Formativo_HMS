<template>
  <div v-if="visible" class="fixed inset-0 z-50 flex items-center justify-center overflow-y-auto">
    <div class="bg-white rounded-lg shadow-lg p-6 w-96">
      <h2 class="text-xl font-bold mb-4">Asignar Características</h2>
      <div class="mb-4">
        <label class="block text-sm font-medium">Características</label>
        <select v-model="caracteristicasSeleccionadas" multiple class="mt-1 block w-full border border-gray-300 rounded-md">
          <option
            v-for="caracteristica in caracteristicasDisponibles"
            :key="caracteristica.id_caracteristica"
            :value="caracteristica.id_caracteristica"
          >
            {{ caracteristica.nombre_caracteristicas }}
          </option>
        </select>
      </div>
      <div class="flex justify-end">
        <button @click="asignarCaracteristicas" class="bg-blue-500 text-white px-4 py-2 rounded-md">Asignar</button>
        <button @click="$emit('close')" class="ml-2 bg-gray-200 text-gray-800 px-4 py-2 rounded-md">Cancelar</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { defineProps, defineEmits } from 'vue';
import { obtenerTodasCaracteristicas, crearRelacionHabitacionCaracteristica } from '@/services/juanca_service/caracteristicasService';

const props = defineProps({
  visible: {
    type: Boolean,
    required: true,
  },
  habitacion: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(['close', 'asignar', 'asignacionExitosa']);
const caracteristicasDisponibles = ref([]);
const caracteristicasSeleccionadas = ref([]);
const modalConfirmacionVisible = ref(false);

// Cargar características disponibles
const cargarCaracteristicas = async () => {
  try {
    const data = await obtenerTodasCaracteristicas();
    caracteristicasDisponibles.value = data;
  } catch (error) {
    console.error("Error al cargar características:", error);
  }
};

// Asignar características
const asignarCaracteristicas = async () => {
  try {
    for (const idCaracteristica of caracteristicasSeleccionadas.value) {
      await crearRelacionHabitacionCaracteristica(props.habitacion.id_habitacion, idCaracteristica);
    }
    emit('asignacionExitosa', true); // Emitir éxito

    // Limpiar la selección después de asignar
    caracteristicasSeleccionadas.value = [];
  } catch (error) {
    console.error("Error al asignar características:", error);
    emit('asignacionExitosa', false); // Emitir error
  }
};

// Cargar características cuando el componente se monte
onMounted(() => {
  cargarCaracteristicas();
});
</script>
