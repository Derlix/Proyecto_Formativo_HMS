<template>
  <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
    <div class="bg-white p-6 rounded-lg shadow-lg w-1/3">
      <h2 class="text-xl font-bold mt-4 mb-1">Eliminar Producto</h2>
      <p id="texto_" class="mb-4">
  ¿Está seguro que desea eliminar el Producto con el id {{ producto.factura_producto.id_factura_producto }} de la factura?
</p>


      <div class="flex justify-end">
        <button type="button" @click="cancelEdit" class="bg-gray-500 text-white px-4 py-2 rounded mr-2">Cancelar</button>
        <button type="button" @click="confirmDelete" class="bg-red-500 text-white px-4 py-2 rounded">Eliminar</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';
import { deleteProductoFactura } from "@/services/brayan_service/FacturaProductoService";

const props = defineProps({
  producto: Object,
});

console.log('Producto recibido en el modal:', props.producto); 
const emit = defineEmits(['delete', 'close']);



const confirmDelete = async () => {
  try {
    console.log('Confirmar eliminación del producto:', props.producto); // Verifica que se muestra la información del producto
    await deleteProductoFactura(props.producto.factura_producto.id_factura_producto);
    alert('Producto de la Factura eliminado exitosamente');
    emit('delete');  // Emite el evento correcto para que lo maneje el componente padre
    emit('close');   // Cierra el modal
  } catch (error) {
    alert('Error al eliminar el producto: ' + (error.response?.data?.message || error.message));
  }
};



const cancelEdit = () => {
  emit('close');
};
</script>

<style scoped>
/* Estilos para el modal */
.fixed {
  position: fixed;
}
.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}
input {
  background-color: #ffffff; /* Fondo blanco para inputs */
  color: #333333; /* Texto negro para inputs */
}
h2 {
  color: #333333; /* Texto negro para el título */
}
#texto_ {
  color: #333333; /* Texto negro para el texto */
}
</style>
