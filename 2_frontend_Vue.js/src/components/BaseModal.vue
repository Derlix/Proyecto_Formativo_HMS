<script setup>
import { ref, computed } from 'vue'
import { mdiClose } from '@mdi/js'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import CardBox from '@/components/CardBox.vue'
import OverlayLayer from '@/components/OverlayLayer.vue'
import CardBoxComponentTitle from '@/components/CardBoxComponentTitle.vue'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  button: {
    type: String,
    default: 'info'
  },
  buttonLabel: {
    type: String,
    default: 'Guardar cambios'
  },
  hasCancel: Boolean,
  modelValue: {
    type: [String, Number, Boolean],
    default: null
  }
})

const emit = defineEmits(['update:modelValue', 'cancel', 'confirm'])

const value = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})

// Campos del formulario
const nombreCompleto = ref('');
const email = ref('');
const usuarioRol = ref('');
const usuarioEstado = ref('');
const fileImg = ref(null);

const confirmCancel = (mode) => {
  value.value = false
  emit(mode)
}

const confirm = () => {
  // Aquí llamamos al método de confirmación con los valores del formulario
  emit('confirm', { nombreCompleto: nombreCompleto.value, email: email.value, usuarioRol: usuarioRol.value, usuarioEstado: usuarioEstado.value, fileImg: fileImg.value });
  confirmCancel('confirm');
}

const cancel = () => confirmCancel('cancel')

window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && value.value) {
    cancel()
  }
})
</script>

<template>
  <OverlayLayer v-show="value" @overlay-click="cancel">
    <CardBox
      v-show="value"
      class="shadow-lg max-h-modal w-11/12 md:w-3/5 lg:w-2/5 xl:w-4/12 z-50"
      is-modal
    >
      <CardBoxComponentTitle :title="title">
        <BaseButton
          v-if="hasCancel"
          :icon="mdiClose"
          color="whiteDark"
          small
          rounded-full
          @click.prevent="cancel"
        />
      </CardBoxComponentTitle>

      <div class="space-y-3">
        <!-- Formulario -->
        <div class="mb-4">
          <label for="nombre_completo" class="block text-gray-700 font-medium dark:text-white">Nombre Completo:</label>
          <input
            type="text"
            id="nombre_completo"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600"
            v-model="nombreCompleto"
            required
          />
        </div>

        <div class="mb-4">
          <label for="email" class="block text-gray-700 font-medium dark:text-white">Email:</label>
          <input
            type="email"
            id="email"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600"
            v-model="email"
            required
          />
        </div>

        <div class="mb-4">
          <label for="usuario_rol" class="block text-gray-700 font-medium dark:text-white">Rol del Usuario:</label>
          <input
            type="text"
            id="usuario_rol"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600"
            v-model="usuarioRol"
            required
          />
        </div>

        <div class="mb-4">
          <label for="usuario_estado" class="block text-gray-700 font-medium dark:text-white">Estado del Usuario:</label>
          <input
            type="text"
            id="usuario_estado"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600"
            v-model="usuarioEstado"
            required
          />
        </div>

        <div class="mb-4">
          <label for="file_img" class="block text-gray-700 font-medium dark:text-white">Imagen de Perfil:</label>
          <input
            type="file"
            id="file_img"
            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600"
            @change="event => fileImg = event.target.files[0]"
          />
        </div>
      </div>

      <template #footer>
        <BaseButtons>
          <BaseButton :label="buttonLabel" :color="button" @click="confirm" />
          <BaseButton v-if="hasCancel" label="Cancelar" :color="button" outline @click="cancel" />
        </BaseButtons>
      </template>
    </CardBox>
  </OverlayLayer>
</template>
