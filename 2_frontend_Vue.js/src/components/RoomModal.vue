<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center z-50">
    <div class="bg-white w-full max-w-lg mx-auto rounded-lg shadow-lg p-6">
      <h2 class="text-2xl font-bold mb-4">{{ isEditing ? 'Editar' : 'Crear' }} Habitación</h2>
      <form @submit.prevent="guardarHabitacion">
        <!-- Campos del formulario -->
        <div class="mb-4">
          <label for="numero_habitacion" class="block text-sm font-medium text-gray-700">Número de Habitación</label>
          <input
            id="numero_habitacion"
            v-model="form.numero_habitacion"
            type="text"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          />
        </div>
        <div class="mb-4">
          <label for="piso" class="block text-sm font-medium text-gray-700">Piso</label>
          <input
            id="piso"
            v-model="form.piso"
            type="number"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          />
        </div>
        <div class="mb-4">
          <label for="id_categoria_habitacion" class="block text-sm font-medium text-gray-700">Categoría de Habitación</label>
          <input
            id="id_categoria_habitacion"
            v-model="form.id_categoria_habitacion"
            type="text"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          />
        </div>
        <div class="mb-4">
          <label for="estado" class="block text-sm font-medium text-gray-700">Estado</label>
          <select
            id="estado"
            v-model="form.estado"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          >
            <option value="">Seleccionar Estado</option>
            <option value="ACTIVO">Activo</option>
            <option value="INACTIVO">Inactivo</option>
            <option value="MANTENIMIENTO">Mantenimiento</option>
          </select>
        </div>
        <div class="mb-4">
          <label for="precio_actual" class="block text-sm font-medium text-gray-700">Precio Actual</label>
          <input
            id="precio_actual"
            v-model="form.precio_actual"
            type="number"
            step="0.01"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          />
        </div>

        <div class="flex justify-end space-x-4">
          <button
            type="button"
            @click="close"
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-gray-500 hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
          >
            Cancelar
          </button>
          <button
            type="submit"
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-500 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            {{ isEditing ? 'Actualizar' : 'Guardar' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { crearHabitacion, actualizarHabitacion } from '../services/juanca_service/habitacionService'; // Importar servicios
import { useMainStore } from '@/stores/main';

const mainStore = useMainStore();
const userID = computed(() => mainStore.userID);

const props = defineProps({
  visible: Boolean,
  habitacion: Object,
});

const emit = defineEmits(['close', 'save']);

const form = ref({
  id_habitacion: null,
  numero_habitacion: '',
  piso: '',
  id_categoria_habitacion: '',
  estado: '',
  precio_actual: '',
});

const isEditing = computed(() => !!form.value.id_habitacion);

// Actualiza el formulario cuando cambia la habitación
watch(() => props.habitacion, (newHabitacion) => {
  form.value = { ...newHabitacion };
});

const close = () => {
  emit('close');
};

const guardarHabitacion = async () => {
  try {
    const habitacionData = { ...form.value, id_usuario: userID.value }; // Asigna userID directamente

    // Verifica si hay un id_usuario válido
    if (!habitacionData.id_usuario) {
      throw new Error('ID del usuario es requerido');
    }

    if (isEditing.value) {
      // Actualizar habitación existente
      await actualizarHabitacion(
        habitacionData.id_habitacion,
        habitacionData.estado,
        habitacionData.piso,
        habitacionData.precio_actual.toString(),
        habitacionData.id_usuario,
        habitacionData.numero_habitacion,
        habitacionData.id_categoria_habitacion
      );
    } else {
      // Crear nueva habitación
      await crearHabitacion(
        habitacionData.estado,
        habitacionData.piso,
        habitacionData.precio_actual.toString(),
        habitacionData.id_usuario,
        habitacionData.numero_habitacion,
        habitacionData.id_categoria_habitacion
      );
    }

    emit('save');
    close();
  } catch (error) {
    if (error.response) {
      console.error('Detalles del error:', error.response.data);
      alert(`Error al guardar la habitación: ${error.response.data.detail || error.response.data.message}`);
    } else {
      console.error('Error al guardar la habitación:', error.message);
      alert(`Error al guardar la habitación: ${error.message}`);
    }
  }
};
</script>

<style scoped>
/* Ajusta el tamaño del modal */
.modal-content {
  max-width: 600px;
  margin: auto;
}

/* Personaliza el tamaño de los botones */
button {
  padding: 10px 15px;
}
</style>
