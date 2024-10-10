<script>
import BaseIcon from './BaseIcon.vue';
</script>
<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white p-6 rounded-lg shadow-lg max-w-2xl w-full">
      <div class="flex justify-center mb-4">
        <BaseIcon v-if="icon" :path="icon" size="100" h="h-40" :class="color"/>
      </div>
      <p class="text-gray-900 text-3xl mb-4 text-center p-4">{{ descripcion }}</p>
      <div class="flex justify-center">
        <button :class="`text-white px-4 py-2 rounded text-center mt-8 ${color === 'text-red-600' ? 'bg-red-600' : 'bg-blue-500'}`" @click="close">
          {{ textBoton }}
        </button>
      </div>
    </div>
  </div>
</template>

  
<script setup>
const props = defineProps({
    descripcion: {
        type: String,
        default: ''
    },
    icon: {
        type: String,
        default: ''
    },
    textBoton: {
        type: String,
        default: '' 
    },
    color: {
        type: String,
        default: 'text-red-300'
    },
    visible: {
        type: Boolean,
        required: true
    }
})

const emit = defineEmits(['close'])

const close = () => {
emit('close')
}
</script>