<template>
    <div v-if="isOpen" class="fixed inset-0 bg-gray-800 bg-opacity-75 flex justify-center items-center">
      <div class="bg-white p-6 rounded-lg shadow-lg w-96">
        <h2 class="text-2xl mb-4">Crear nuevo producto</h2>
  
        <!-- Formulario para agregar producto -->
        <form @submit.prevent="handleSubmit">
          <div class="mb-4">
            <label for="productName" class="block text-gray-700">Nombre del Producto</label>
            <input
              type="text"
              id="productName"
              v-model="product.name"
              class="mt-1 p-2 w-full border rounded"
              required
            />
          </div>
  
          <div class="mb-4">
            <label for="productPrice" class="block text-gray-700">Precio</label>
            <input
              type="number"
              id="productPrice"
              v-model="product.price"
              class="mt-1 p-2 w-full border rounded"
              required
            />
          </div>
  
          <div class="flex justify-end">
            <button type="button" @click="closeModal" class="mr-4 text-gray-600 hover:text-gray-800">Cancelar</button>
            <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Guardar</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      isOpen: {
        type: Boolean,
        required: true,
      },
    },
    data() {
      return {
        product: {
          name: '',
          price: 0,
        },
      };
    },
    methods: {
      closeModal() {
        this.$emit('close');
      },
      handleSubmit() {
        this.$emit('save', this.product);
        this.product = { name: '', price: 0 }; // Reset form
      },
    },
  };
  </script>
  