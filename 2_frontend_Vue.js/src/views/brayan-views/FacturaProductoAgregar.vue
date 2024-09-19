<template>
  <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
    <div class="bg-blue-200 p-6 rounded-lg shadow-lg w-1/3">
      <h2 class="text-xl font-bold text-gray-800 mt-4 mb-1">Agregar Producto a la Factura</h2>
      <form @submit.prevent="addProducto">
        <div class="mb-4">
          <label class="block text-gray-700">ID facturación</label>
          <input v-model="producto.id_facturacion" type="number" disabled class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 bg-gray-100 focus:outline-none focus:border-blue-500" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">ID producto</label>
          <input v-model="producto.id_producto" type="number" class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Cantidad</label>
          <input v-model="producto.cantidad" type="number" class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Fecha</label>
          <input v-model="producto.fecha" type="date" class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Precio U</label>
          <input v-model="producto.precio_unitario" type="text" class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" />
        </div>
        <div class="flex justify-end">
          <button type="button" @click="cancelEdit" class="bg-gray-500 text-white px-4 py-2 rounded mr-2 hover:bg-gray-600 transition">Cancelar</button>
          <button type="submit" class="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-700 transition">Agregar</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue';
import { addProductoToFactura } from '@/services/brayan_service/FacturaProductoService';

const props = defineProps({
  factura: Object,
});

const emit = defineEmits(['update', 'close']);

const producto = ref({
  id_facturacion: props.factura.id_facturacion,
  id_producto: '',
  cantidad: '',
  fecha: '',
  precio_unitario: '',
});

const addProducto = async () => {
  try {
    await addProductoToFactura(
      producto.value.id_facturacion,
      producto.value.id_producto,
      producto.value.cantidad,
      producto.value.fecha,
      producto.value.precio_unitario
    );
    alert('El producto se agregó correctamente a la factura');
    emit('update');
    emit('close');
  } catch (error) {
    alert('Error al agregar el producto:', error);
  }
};

const cancelEdit = () => {
  emit('close');
};
</script>

<style scoped>
.fixed {
  position: absolute;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

input {
  color: #333333;
}

button {
  transition: background-color 0.3s;
}

h2 {
  color: #2d3748; 
}
</style>
