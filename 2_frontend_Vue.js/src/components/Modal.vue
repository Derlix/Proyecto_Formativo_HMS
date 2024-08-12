<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white p-6 rounded-lg shadow-lg max-w-sm w-full">
      <h2 class="text-xl font-semibold mb-4">Modal de ejemplo</h2>
      <p class="text-gray-700 mb-4">This is the content of the modal of the best hotel bbs</p>
      <button @click="close" class="bg-blue-500 text-white px-4 py-2 rounded">Cerrar</button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
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
