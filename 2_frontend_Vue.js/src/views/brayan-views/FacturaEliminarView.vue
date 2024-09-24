<template> 
  <CardBoxModal  
    title="Eliminar Factura" 
    v-model="showDeleteModal"
  >
    <h2 class="text-xl font-bold mt-4 mb-1">Eliminar Factura</h2>
    <p id="texto_" class="mb-4">¿Está seguro que desea eliminar la factura con el ID {{ factura.id_facturacion }}?</p>
    <div class="flex justify-end">
      <button type="button" @click="cancelEdit" class="bg-gray-500 text-white px-4 py-2 rounded mr-2">Cancelar</button>
      <button type="button" @click="confirmDelete" class="bg-red-500 text-white px-4 py-2 rounded">Eliminar</button>
    </div>
  </CardBoxModal>
</template>

<script setup>
import { ref, watch } from 'vue';
import { defineProps, defineEmits } from 'vue';
import CardBoxModal from '@/components/CardBoxModal.vue'
import { deleteFactura } from "@/services/brayan_service/FacturacionService";

const props = defineProps({
  factura: Object,
  modelValue: Boolean,
});

const emit = defineEmits(['delete', 'update:modelValue']);

const isVisible = ref(props.modelValue);

watch(() => props.modelValue, (newValue) => {
  isVisible.value = newValue;
});

const confirmDelete = async () => {
  try {
    await deleteFactura(props.factura.id_facturacion);
    alert('Factura eliminada exitosamente');
    emit('delete');  
    emit('update:modelValue', false); // Actualiza el valor del modal
  } catch (error) {
    if (error.response?.status === 400) {
      alert('No se puede eliminar la factura porque tiene productos asociados. Elimine los productos primero.');
    } else {
      alert('Error al eliminar la factura: ' + (error.response?.data?.message || error.message));
    }
  }
};

const cancelEdit = () => {
  emit('close', false); // Actualiza el valor del modal
};
</script>
