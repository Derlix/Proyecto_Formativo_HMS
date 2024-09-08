<script>
import BaseIcon from './BaseIcon.vue';
</script>

<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white p-6 rounded-lg shadow-lg max-w-sm w-full flex justify-center">
      <BaseIcon v-if="icon" :path="icon" size="70" w="" h="h-16" :class="color" />
      <p class="text-gray-700 mb-4">{{ descripcion }}</p>
      <button @click="close" class="bg-blue-500 text-white px-4 py-2 rounded">{{ boton }}</button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  visible: {
    type: Boolean,
    required: true
  },
  titulo: {
    type: String,
    default: ''
  },
  descripcion: {
    type: String,
    default: ''
  },
  boton: {
    type: String,
    default: 'Cerrar'
  },
  icon: {
    type: String,
    default: null
  },
  color: {
    type: String,
    default: 'text-green-400'
  }
})

const emit = defineEmits(['close'])

const close = () => {
  emit('close')
}
</script>
