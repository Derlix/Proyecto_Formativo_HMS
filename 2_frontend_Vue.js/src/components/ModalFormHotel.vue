<!-- src/components/ModalForm.vue -->
<template>
      <div v-if="isVisible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
        <div class="bg-white p-6 rounded-md shadow-lg w-full max-w-lg relative">
          <!-- Botón de cierre -->
          <button @click="closeModal" class="absolute top-2 right-2 text-gray-600 hover:text-gray-900">
            ✖
          </button>
    
          <!-- Título del Modal -->
          <h3 class="text-center text-xl mb-4">{{ title }}</h3>
    
          <!-- Contenido del Modal -->
          <div>
            <slot></slot>
          </div>
        </div>
      </div>
    </template>
    
    <script setup>
    import { defineProps, defineEmits } from 'vue'
    
    // Props para el modal
    defineProps({
      isVisible: {
        type: Boolean,
        required: true
      },
      title: {
        type: String,
        default: 'Modal Title'
      }
    })
    
    // Emitir evento para cerrar el modal
    const emit = defineEmits(['close'])
    
    const closeModal = () => {
      emit('close')
    }
    </script>
    
    <style scoped>
   
    </style>
    