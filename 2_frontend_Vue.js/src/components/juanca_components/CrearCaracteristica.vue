<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
    <div class="bg-white rounded-lg shadow-lg p-6 max-w-sm w-full">
      <h2 class="text-xl font-bold mb-4 dark:text-black">{{ isEditing ? 'Editar' : 'Crear' }} Característica</h2>
      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label for="nombre" class="block text-sm font-medium text-gray-700">Nombre:</label>
          <input
            v-model="nombre"
            type="text"
            id="nombre"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:text-black"
          />
        </div>
        <div class="mb-4">
          <label for="adicional" class="block text-sm font-medium text-gray-700">Precio adicional:</label>
          <input
            v-model="adicional"
            type="number"
            id="adicional"
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
            @click="handleCancel"
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
import { crearCaracteristica, editarCaracteristica } from '@/services/juanca_service/caracteristicasService';

export default {
  props: {
    visible: Boolean,
    caracteristica: Object,
  },
  setup(props, { emit }) {
    const nombre = ref('');
    const adicional = ref(0);
    const isEditing = ref(false);

    watch(
      () => props.caracteristica,
      (newValue) => {
        if (newValue) {
          nombre.value = newValue.nombre_caracteristicas;
          adicional.value = newValue.adicional;
          isEditing.value = true;
        } else {
          resetFields();
        }
      }
    );

    const resetFields = () => {
      nombre.value = '';
      adicional.value = 0;
      isEditing.value = false;
    };

    const handleCancel = () => {
      resetFields();
      emit('close');
    };

    const handleSubmit = async () => {
      const data = {
        nombre_caracteristicas: nombre.value,
        adicional: adicional.value,
      };

      try {
        if (isEditing.value) {
          const caracteristicaId = props.caracteristica.id_caracteristica;
          await editarCaracteristica(caracteristicaId, data.nombre_caracteristicas, data.adicional);
        } else {
          await crearCaracteristica(data);
        }
        emit('save');
        emit('close');
      } catch (error) {
        console.error('Error al guardar la característica:', error);
      }
    };

    return {
      nombre,
      adicional,
      isEditing,
      handleSubmit,
      handleCancel,
    };
  },
};
</script>
