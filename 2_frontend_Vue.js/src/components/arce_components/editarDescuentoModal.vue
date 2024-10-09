
<template>
    <div v-if="visible" class="modal-overlay">
      <div class="modal">
        <h3>Editar Descuento</h3>
        <form @submit.prevent="submitForm">
          <div>
            <label>Tipo de Descuento:</label>
            <input v-model="form.tipo_descuento" type="text" required />
          </div>
          <div>
            <label>Porcentaje de Descuento:</label>
            <input v-model.number="form.porcentaje_descuento" type="number" required />
          </div>
          <div>
          </div>
          <button type="submit">Guardar Cambios</button>
          <button type="button" @click="close">Cancelar</button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue';
  
  const props = defineProps(['visible', 'form']);
  const emit = defineEmits(['update:visible', 'save']);
  
  const close = () => {
    emit('update:visible', false);
  };
  
  const submitForm = () => {
    emit('save', { ...props.form }); // Asegúrate de usar props.form
    close();
  };
  </script>
  
  <style>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal {
    background: white;
    padding: 20px;
    border-radius: 5px;
    max-width: 400px;
    width: 100%;
  }
  </style>
  