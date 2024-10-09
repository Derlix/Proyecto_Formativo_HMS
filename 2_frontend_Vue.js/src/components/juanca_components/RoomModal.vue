<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center z-50">
    <div class="bg-white w-full max-w-lg mx-auto rounded-lg shadow-lg p-6">
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
            type="number"
            v-model="form.precio_actual"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          />
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
import { ref, computed, watch, onMounted } from 'vue';
import { crearHabitacion, actualizarHabitacion } from '@/services/juanca_service/habitacionService';
import { useMainStore } from '@/stores/main';
import { obtenerCategoriasHabitacion } from '@/services/juanca_service/categoriaService';

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

const categorias = ref([]);

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
watch(() => props.habitacion, (newHabitacion) => {
  if (newHabitacion) {
    form.value = {
      id_habitacion: newHabitacion.id_habitacion,
      numero_habitacion: newHabitacion.numero_habitacion,
      piso: newHabitacion.piso,
      id_categoria_habitacion: newHabitacion.id_categoria_habitacion, // Asegúrate de que esto coincida
      estado: newHabitacion.estado,
      precio_actual: newHabitacion.precio_actual,
    };
  } else {
    form.value = {
      id_habitacion: null,
      numero_habitacion: '',
      piso: '',
      id_categoria_habitacion: '',
      estado: '',
      precio_actual: '',
    };
  }
});

// Funciones para cerrar el formulario y guardar los datos
const close = () => {
  emit('close');
};

const guardarHabitacion = async () => {
  try {
    const habitacionData = { ...form.value, id_usuario: userID.value };

    if (!habitacionData.id_usuario) {
      throw new Error('ID del usuario es requerido');
    }

    if (form.value.id_habitacion) { // Si estamos editando
      await actualizarHabitacion(
        habitacionData.id_habitacion,
        habitacionData.estado,
        habitacionData.piso,
        habitacionData.precio_actual.toString(),
        habitacionData.id_usuario,
        habitacionData.numero_habitacion,
        habitacionData.id_categoria_habitacion
      );
    } else { // Si estamos creando
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
    console.error('Error al guardar la habitación:', error.message);
    alert(`Error al guardar la habitación: ${error.message}`);
  }
};
</script>

<style scoped>
/* Fijar color de las letras para que no cambien */
label, input, select, option {
  color: #333; /* Color de texto fijo */
}

/* Asegurar que no cambien el color en foco o hover */
input:focus, select:focus {
  outline: none;
  border-color: #333; /* También asegurar que el borde no cambie de color */
}

.modal-content {
  max-width: 600px;
  margin: auto;
}
</style>
