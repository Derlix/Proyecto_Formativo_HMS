<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center z-50">
    <div :class="modalBackgroundClass" class="w-full max-w-lg mx-auto rounded-lg shadow-lg p-6">
      <h2 class="text-2xl font-bold mb-4">{{ isEditing ? 'Editar' : 'Crear' }} Habitación</h2>
      <form @submit.prevent="guardarHabitacion">
        <div class="mb-4">
          <label for="numero_habitacion" class="block text-sm font-medium text-gray-700">Número de Habitación</label>
          <input
            id="numero_habitacion"
            v-model="form.numero_habitacion"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          />
        </div>

        <div class="mb-4">
          <label for="piso" class="block text-sm font-medium text-gray-700">Piso</label>
          <input
            id="piso"
            type="number"
            v-model="form.piso"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          />
        </div>

        <div class="mb-4">
          <label for="id_categoria_habitacion" class="block text-sm font-medium text-gray-700">Categoría de Habitación</label>
          <select
            id="id_categoria_habitacion"
            v-model="form.id_categoria_habitacion"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          >
            <option value="">Seleccionar Categoría</option>
            <option v-for="categoria in categorias" :key="categoria.id_categoria_habitacion" :value="categoria.id_categoria_habitacion">
              {{ categoria.tipo_habitacion }} <!-- Mostrar el nombre de la categoría -->
            </option>
          </select>
        </div>

        <div class="mb-4">
          <label for="estado" class="block text-sm font-medium text-gray-700">Estado</label>
          <select
            id="estado"
            v-model="form.estado"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          >
            <option value="">Seleccionar estado</option>
            <option v-for="estado in estados" :key="estado" :value="estado">
              {{ estado }}
            </option>
          </select>
        </div>

        <div class="flex justify-between">
          <button
            type="button"
            @click="close"
            class="bg-red-500 text-white px-4 py-2 rounded-md"
          >
            Cancelar
          </button>
          <button
            type="submit"
            class="bg-blue-500 text-white px-4 py-2 rounded-md"
          >
            {{ isEditing ? 'Actualizar' : 'Crear' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, nextTick } from 'vue';
import { crearHabitacion, actualizarHabitacion } from '@/services/juanca_service/habitacionService';
import { useMainStore } from '@/stores/main';
import { obtenerCategoriasHabitacion } from '@/services/juanca_service/categoriaService';

const mainStore = useMainStore();
const userID = computed(() => mainStore.userID);
const isEditing = ref(false);

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
});

const categorias = ref([]);
const estados = ref(['ACTIVO', 'INACTIVO', 'MANTENIMIENTO', 'OPERACION', 'OCUPADO']);

// Cargar las categorías al inicializar el componente
const cargarCategorias = async () => {
  try {
    categorias.value = await obtenerCategoriasHabitacion();
    console.log('Categorías cargadas:', categorias.value); // Verifica las categorías cargadas
  } catch (error) {
    console.error('Error al cargar las categorías:', error);
  }
};

onMounted(async () => {
  await cargarCategorias();
});

// Observa los cambios en la habitación y asigna los valores al formulario
watch(() => props.habitacion, async (newHabitacion) => {
  console.log('Habitación a editar:', newHabitacion); // Agrega este log para ver los valores
  if (newHabitacion && newHabitacion.id_habitacion) {
    isEditing.value = true;
    form.value = {
      id_habitacion: newHabitacion.id_habitacion,
      numero_habitacion: newHabitacion.numero_habitacion,
      piso: newHabitacion.piso,
      id_categoria_habitacion: newHabitacion.categoria.id_categoria_habitacion, // Obtiene el id de la categoría
      estado: newHabitacion.estado
    };
    await nextTick();
    console.log('Formulario después de la asignación:', form.value); // Verifica el valor del formulario
  } else {
    isEditing.value = false;
    form.value = {
      id_habitacion: null,
      numero_habitacion: '',
      piso: '',
      id_categoria_habitacion: '', // Reiniciar cuando no hay habitación
      estado: '',
    };
  }
});

// Computed para determinar la clase de fondo según el tema
const modalBackgroundClass = computed(() => {
  return mainStore.isDarkTheme ? 'bg-gray-800 text-white' : 'bg-white text-gray-800';
});

// Funciones para cerrar el formulario y guardar los datos
const close = () => {
  emit('close');
};

const guardarHabitacion = async () => {
  try {
    const habitacionData = { ...form.value, id_usuario: userID };

    if (!habitacionData.id_usuario) {
      throw new Error('ID del usuario es requerido');
    }

    if (isEditing.value) { // Si estamos editando
      await actualizarHabitacion(
        habitacionData.id_habitacion,
        habitacionData.estado,
        habitacionData.piso,
        habitacionData.numero_habitacion,
        habitacionData.id_categoria_habitacion
      );
    } else { // Si estamos creando
      await crearHabitacion(
        habitacionData.estado,
        habitacionData.piso,
        habitacionData.numero_habitacion,
        habitacionData.id_categoria_habitacion
      );
    }

    emit('save');
    close();
  } catch (error) {
    console.error('Error al guardar la habitación:', error.message);
    alert(`Error al guardar la habitación: ${error.message}`);
  }
};
</script>

<style scoped>
label, input, select, option {
  color: #333;
}

input:focus, select:focus {
  outline: none;
  border-color: #333;
}

.modal-content {
  max-width: 600px;
  margin: auto;
}
</style>
