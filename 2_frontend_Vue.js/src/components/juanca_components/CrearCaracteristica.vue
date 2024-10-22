<template>
  <div v-if="visible" class="modal">
    <h2 class="text-xl">{{ isEditing ? 'Editar' : 'Crear' }} Característica</h2>
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="nombre">Nombre:</label>
        <input v-model="nombre" type="text" id="nombre" required />
      </div>
      <div>
        <label for="adicional">Precio adicional:</label>
        <input v-model="adicional" type="number" id="adicional" required />
      </div>
      <button type="submit">{{ isEditing ? 'Actualizar' : 'Crear' }}</button>
      <button type="button" @click="$emit('close')">Cancelar</button>
    </form>
  </div>
</template>

<script>
import { ref, watch } from 'vue';
import { crearCaracteristica, editarCaracteristica } from '@/services/juanca_service/caracteristicasService'; // Asegúrate de que la ruta sea correcta

export default {
  props: {
    visible: Boolean,
    caracteristica: Object,
  },
  setup(props, { emit }) {
    const nombre = ref('');
    const adicional = ref(0);
    const isEditing = ref(false);

    watch(
      () => props.caracteristica,
      (newValue) => {
        console.log('Característica recibida:', newValue); // Añadir esta línea
        if (newValue) {
          nombre.value = newValue.nombre_caracteristicas;
          adicional.value = newValue.adicional;
          isEditing.value = true;
        } else {
          nombre.value = '';
          adicional.value = 0;
          isEditing.value = false;
        }
      }
    );


    const handleSubmit = async () => {
      const data = {
        nombre_caracteristicas: nombre.value,
        adicional: adicional.value,
      };

      try {
        if (isEditing.value) {
          // Accede al ID correcto
          const caracteristicaId = props.caracteristica.id_caracteristica; // Cambia aquí
          console.log('ID de la característica en handleSubmit:', caracteristicaId);
          await editarCaracteristica(caracteristicaId, data.nombre_caracteristicas, data.adicional);
        } else {
          await crearCaracteristica(data);
        }
        emit('save');
        emit('close');
      } catch (error) {
        console.error('Error al guardar la característica:', error);
      }
    };




    return {
      nombre,
      adicional,
      isEditing,
      handleSubmit,
    };
  },
};
</script>
