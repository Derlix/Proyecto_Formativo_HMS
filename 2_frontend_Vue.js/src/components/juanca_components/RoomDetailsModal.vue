<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center z-50">
    <div class="modal-overlay absolute inset-0 bg-black opacity-50"></div>
    <div class="modal-content bg-white rounded-lg p-6 z-10 max-w-md mx-auto">
      <h2 class="text-xl font-bold mb-4">Detalles de la Habitación</h2>

      <!-- Información básica de la habitación -->
      <p><strong>Número de Habitación:</strong> {{ habitacion.numero_habitacion }}</p>
      <p><strong>Estado:</strong> {{ habitacion.estado }}</p>
      <p><strong>Piso:</strong> {{ habitacion.piso }}</p>

      <!-- Información de la categoría de la habitación -->
      <h3 class="text-lg font-semibold mt-4">Categoría</h3>
      <p><strong>Tipo de Habitación:</strong> {{ habitacion.categoria.tipo_habitacion }}</p>
      <p><strong>Precio Fijo:</strong> {{ habitacion.categoria.precio_fijo }}</p>
      <p><strong>ID Hotel:</strong> {{ habitacion.categoria.id_hotel }}</p>

      <!-- Información de las características de la habitación -->
      <h3 class="text-lg font-semibold mt-4">Características</h3>
      <ul>
        <!-- Si tiene características, mostrar la lista -->
        <li v-if="habitacion.caracteristicas && habitacion.caracteristicas.length > 0" v-for="(caracteristica, index) in habitacion.caracteristicas" :key="index">
          <div class="caracteristica-item">
            <span>
              <strong>{{ caracteristica.nombre_caracteristicas }}</strong>
              (adicional: {{ caracteristica.adicional }} )
            </span>
            <!-- Botón de Eliminar alineado a la derecha con margen -->
            <BaseButton
              @click="confirmarEliminacion(habitacion.id_habitacion, caracteristica.id_caracteristica)"
              :icon="mdiTrashCan"
              small
              color="danger"
              class="eliminar-boton"
            />
          </div>
        </li>
        <!-- Si no tiene características, mostrar un mensaje -->
        <li v-else>
          Sin características asignadas
        </li>
      </ul>

      <button @click="close" class="mt-4 bg-blue-500 text-white px-4 py-2 rounded-md">Cerrar</button>
    </div>
  </div>
</template>

<script setup>
import BaseButton from '@/components/BaseButton.vue';
import { mdiTrashCan } from '@mdi/js';
import { eliminarRelacionHabitacionCaracteristica } from '@/services/juanca_service/caracteristicasService';

const props = defineProps({
  visible: {
    type: Boolean,
    required: true,
  },
  habitacion: {
    type: Object,
    required: true,
  },
});

// Definir el emisor de eventos
const emit = defineEmits();

// Función para cerrar el modal
const close = () => {
  emit('close');
};

// Función para confirmar la eliminación de una característica
const confirmarEliminacion = async (id_habitacion, id_caracteristica) => {
  try {
    await eliminarRelacionHabitacionCaracteristica(id_habitacion, id_caracteristica);
    alert('Relación eliminada correctamente');
    emit('habitacionActualizada');
    emit('close');
  } catch (error) {
    console.error('Error eliminando la relación:', error);
    alert('Ocurrió un error al eliminar la relación');
  }
};


</script>


<style scoped>
.modal-content {
  max-width: 600px;
  margin: auto;
  background-color: white;
  color: black;
}

.modal-overlay {
  background-color: rgba(0, 0, 0, 0.5);
}

.caracteristica-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.eliminar-boton {
  margin-left: auto; /* Asegura que el botón quede a la derecha */
  margin: 2px; /* Añade un margen alrededor del botón */
}
</style>
