<template>
    <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-blue-100 p-6 rounded-lg shadow-lg max-w-2xl w-full">
            <p class="text-black mb-4 rounded border-opacity-10 font-bold text-2xl text-center pt-3 pb-2">{{ descripcion }}</p>
            <div class="p-6">
                <form @submit.prevent="submitForm">
                    <div class="grid grid-cols-2 gap-3">
                        <div class="mb-4">
                            <label for="nombre" class="block text-gray-700">Nombre del producto</label>
                            <input v-model="form.nombre" type="text" id="nombre" class="w-full px-3 py-2 border rounded" required />
                        </div>
                        <div class="mb-4">
                            <label for="cantidad" class="block text-gray-700">Precio</label>
                            <input v-model="form.cantidad" type="number" step="0.01" id="precio" class="w-full px-3 py-2 border rounded" required />
                        </div>
                    </div>
                    <div class="mb-4">
                        <label for="precio" class="block text-gray-700">Descripcion</label>
                        <input v-model="form.precio" type="text" id="descripcion" class="w-full px-3 py-2 border rounded h-16" required />
                    </div>
                    <div class="flex justify-center space-x-4">
                        <button type="submit" class="bg-green-800 text-white px-4 py-2 rounded">{{ textBoton }}</button>
                        <button type="button" class="bg-red-500 text-white px-4 py-2 rounded" @click="close">Cancelar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
  
<script setup>
import { ref } from 'vue';
  
const props = defineProps({
    descripcion: {
        type: String,
          default: ''
    },
    textBoton: {
        type: String,
        default: ''
    },
    visible: {
        type: Boolean,
        required: true
    }
});
  
const emit = defineEmits(['close', 'submit']);
  
const form = ref({
    nombre: '',
    precio: '',
    cantidad: ''
});
  
const submitForm = () => {
    emit('submit', form.value);
    close();
};
  
const close = () => {
    emit('close');
};
</script>  