<template>
  <div class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
    <div class="bg-white p-6 rounded-lg shadow-lg w-1/3">
      <h2 class="text-xl font-bold mt-4 mb-1">Eliminar Factura</h2>
      <p id="texto_" class="mb-4">¿Está seguro que desea eliminar la factura con el ID {{ factura.id_facturacion }}?</p>
      <div class="flex justify-end">
        <button type="button" @click="cancelEdit" class="bg-gray-500 text-white px-4 py-2 rounded mr-2">Cancelar</button>
        <button type="button" @click="confirmDelete" class="bg-red-500 text-white px-4 py-2 rounded">Eliminar</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

import { deleteFactura } from "@/services/brayan_service/FacturacionService";

const props = defineProps({
  factura: Object,
});

const emit = defineEmits(['delete', 'close']);

const confirmDelete = async () => {
  try {
    await deleteFactura(props.factura.id_facturacion);
    alert('Factura eliminada exitosamente');
    emit('delete');  // Emite el evento correcto para que lo maneje el componente padre
    emit('close');   // Cierra el modal
  } catch (error) {
    if (error.response?.status === 400) {
      alert('No se puede eliminar la factura porque tiene productos asociados. Elimine los productos primero.');
    } else {
      alert('Error al eliminar la factura: ' + (error.response?.data?.message || error.message));
    }
  }
};

const cancelEdit = () => {
  emit('close');
};
</script>