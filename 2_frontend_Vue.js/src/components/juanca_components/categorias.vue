<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
    <div class="bg-white rounded-lg shadow-lg p-6 max-w-sm w-full">
      <h2 class="text-xl font-bold mb-4 dark:text-black">{{ isEditing ? 'Editar' : 'Crear' }} Categoría</h2>
      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label for="tipo_habitacion" class="block text-sm font-medium text-gray-700">Tipo de habitación:</label>
          <input
            v-model="tipo_habitacion"
            type="text"
            id="tipo_habitacion"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:text-black"
          />
        </div>
        <div class="mb-4">
          <label for="precio_fijo" class="block text-sm font-medium text-gray-700">Precio fijo:</label>
          <input
            v-model="precio_fijo"
            type="number"
            id="precio_fijo"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:text-black"
          />
        </div>
        <div class="flex justify-end">
          <button
            type="submit"
            class="inline-flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            {{ isEditing ? 'Actualizar' : 'Crear' }}
          </button>
          <button
            type="button"
            @click="cancelar"
            class="ml-2 inline-flex justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            Cancelar
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue';
import { useAuthStore } from '@/stores';
import { crearCategoria, actualizarCategoria } from '@/services/juanca_service/categoriaService';

export default {
  props: {
    visible: Boolean,
    categoria: Object,
  },
  setup(props, { emit }) {
    const tipo_habitacion = ref('');
    const precio_fijo = ref(0);
    const isEditing = ref(false);

    // Acceder al store de autenticación para obtener el ID del hotel
    const authStore = useAuthStore();
    const id_hotel = authStore.user.id_hotel;

    watch(
      () => props.categoria,
      (newValue) => {
        if (newValue) {
          tipo_habitacion.value = newValue.tipo_habitacion;
          precio_fijo.value = newValue.precio_fijo;
          isEditing.value = true;
        } else {
          tipo_habitacion.value = '';
          precio_fijo.value = 0;
          isEditing.value = false;
        }
      }
    );

    const handleSubmit = async () => {
      const data = {
        tipo_habitacion: tipo_habitacion.value,
        precio_fijo: precio_fijo.value,
        id_hotel: id_hotel,
      };

      console.log('Datos a enviar:', data); // Log para depuración

      try {
        if (isEditing.value) {
          const categoriaId = props.categoria.id_categoria_habitacion; // Asegúrate de que esto sea correcto
          await actualizarCategoria(categoriaId, data.tipo_habitacion, data.precio_fijo, id_hotel); // Enviar el ID correcto
        } else {
          await crearCategoria(data.precio_fijo, data.tipo_habitacion, id_hotel); // Enviar el ID correcto para creación
        }
        emit('save');
        emit('close');
      } catch (error) {
        console.error('Error al guardar la categoría:', error);
      }
    };

    // Función para limpiar campos al cancelar
    const cancelar = () => {
      tipo_habitacion.value = '';
      precio_fijo.value = 0;
      isEditing.value = false;
      emit('close');
    };

    return {
      tipo_habitacion,
      precio_fijo,
      isEditing,
      handleSubmit,
      cancelar, // Agregar la función cancelar
    };
  },
};
</script>
