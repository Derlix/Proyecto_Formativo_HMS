<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center z-50">
    <div :class="modalBackgroundClass" class="w-full max-w-lg mx-auto rounded-lg shadow-lg p-6">
      <h2 class="text-2xl font-bold mb-4">Crear Característica</h2>

      <NotificationBar
        v-if="isAlertVisible"
        :color="colorAlert"
        :description="modalMessage"
        :visible="isAlertVisible"
      />

      <form @submit.prevent="guardarCaracteristica">
        <!-- Campo Nombre de la Característica -->
        <div class="mb-4">
          <label for="nombre_caracteristica" class="block text-sm font-medium text-gray-700">
            Nombre de la Característica
          </label>
          <input
            id="nombre_caracteristica"
            v-model="form.nombre_caracteristica"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          />
        </div>

        <!-- Campo Precio Adicional -->
        <div class="mb-4">
          <label for="precio_adicional" class="block text-sm font-medium text-gray-700">
            Precio Adicional
          </label>
          <input
            type="number"
            step="0.01"
            id="precio_adicional"
            v-model="form.precio_adicional"
            required
            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          />
        </div>

        <!-- Botones de acción -->
        <div class="flex justify-between" v-if="userRole === 'SuperAdmin' || userRole === 'JefeRecepcion'">
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
            Crear
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { crearCaracteristica } from '@/services/juanca_service/caracteristicasService';
import { useMainStore } from '@/stores/main';
import NotificationBar from '@/components/alejo_components/NotificationBar.vue';

const mainStore = useMainStore();
const userRole = computed(() => mainStore.userRole);

const isAlertVisible = ref(false);
const modalMessage = ref('');
const colorAlert = ref('');

const props = defineProps({
  visible: Boolean,
});

const emit = defineEmits(['close', 'save']);

const form = ref({
  nombre_caracteristica: '',
  precio_adicional: '', // Añadimos el precio adicional al formulario
});

// Computed para determinar la clase de fondo según el tema
const modalBackgroundClass = computed(() => {
  return mainStore.isDarkTheme ? 'bg-gray-800 text-white' : 'bg-white text-gray-800';
});

const close = () => {
  emit('close');
  isAlertVisible.value = false;
  colorAlert.value = '';
  modalMessage.value = '';
};


const guardarCaracteristica = async () => {
  try {
    const caracteristicaData = { ...form.value };

    await crearCaracteristica(caracteristicaData.nombre_caracteristica, caracteristicaData.precio_adicional);

    isAlertVisible.value = true;
    colorAlert.value = 'success';
    modalMessage.value = 'Característica creada exitosamente';

    emit('save');
    close();
  } catch (error) {

    console.error('Error capturado pero ignorado:', error);

    form.value.nombre_caracteristica = '';
    form.value.precio_adicional = '';

    emit('save');
    setTimeout(() => {
      close();
    }, 1500);
  }
};

</script>
