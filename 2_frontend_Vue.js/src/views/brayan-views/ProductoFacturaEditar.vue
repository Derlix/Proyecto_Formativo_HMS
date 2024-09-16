<template>
  <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
    <div class="bg-blue-200 p-6 rounded-lg shadow-lg w-1/3">
      <h2 class="text-xl font-bold text-gray-800 mt-4 mb-1">Editar Producto</h2>
      <form @submit.prevent="updateProducto">
        <div class="mb-4">
          <label for="cantidad" class="block text-gray-700">Cantidad</label>
          <input
            type="number"
            id="cantidad"
            v-model="producto.factura_producto.cantidad"
            class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500"
            required
          />
        </div>
        <div class="mb-4">
          <label for="fecha" class="block text-gray-700">Fecha</label>
          <input
            type="date"
            id="fecha"
            v-model="producto.fecha"
            class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500"
            required
          />
        </div>
        <div class="mb-4">
          <label for="precio_unitario" class="block text-gray-700">Precio Unitario</label>
          <input
            type="number"
            id="precio_unitario"
            v-model="producto.factura_producto.precio_unitario"
            class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500"
            required
          />
        </div>
        
        <div class="flex justify-end">
          <button @click="closeModal" type="button" class="bg-gray-500 text-white px-4 py-2 rounded mr-2 hover:bg-gray-600 transition">
            Cancelar
          </button>
          <button type="submit" class="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
            Editar
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue';
import { updateProductoFactura } from '@/services/brayan_service/FacturaProductoService';


const props = defineProps({
  producto: Object
});

const emit = defineEmits(['close', 'save']);

const updateProducto = async () => {
  try {
    console.log('Datos del producto en el modal:', props.producto);
    await updateProductoFactura(
      props.producto.factura_producto.id_factura_producto,
      props.producto.cantidad,
      props.producto.fecha,
      props.producto.precio_unitario
      
    ); 
    alert('Producto de la factura editado xitosamente');
    emit('update'); 
    emit('close'); 
  } catch (error) {
    alert('Error al actualizar la el producto de la factura: ' + (error.response?.data?.message || error.message));
  }
};

const closeModal = () => {
  emit('close');
};

const submitEdits = () => {
  emit('save', updateProducto.value);
  closeModal();
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
  color: #333333; /* Texto negro */
}

button {
  transition: background-color 0.3s;
}


h2 {
  color: #2d3748; /* Gris oscuro */
}
</style>
