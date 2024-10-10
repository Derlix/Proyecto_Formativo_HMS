<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center z-50">
    <div class="modal-overlay absolute inset-0 bg-black opacity-50"></div>
    <div class="modal-content bg-white rounded-lg p-6 z-10 max-w-md mx-auto">
      <h2 class="text-xl font-bold mb-4">Detalles de la Habitación</h2>

      <!-- Información básica de la habitación -->
      <p><strong>Número de Habitación:</strong> {{ habitacion.numero_habitacion }}</p>
      <p><strong>Estado:</strong> {{ habitacion.estado }}</p>
      <p><strong>Piso:</strong> {{ habitacion.piso }}</p>
      <p><strong>ID Usuario:</strong> {{ habitacion.id_usuario }}</p>

      <!-- Información de la categoría de la habitación -->
      <h3 class="text-lg font-semibold mt-4">Categoría</h3>
      <p><strong>Tipo de Habitación:</strong> {{ habitacion.categoria.tipo_habitacion }}</p>
      <p><strong>Precio Fijo:</strong> {{ habitacion.categoria.precio_fijo }}</p>
      <p><strong>ID Hotel:</strong> {{ habitacion.categoria.id_hotel }}</p>

      <!-- Información de las características de la habitación -->
      <h3 class="text-lg font-semibold mt-4">Características</h3>
      <ul>
        <li v-if="habitacion.caracteristicas">
          <strong>{{ habitacion.caracteristicas.nombre_caracteristicas }}</strong>
          (Adicional: {{ habitacion.caracteristicas.adicional }})
        </li>
      </ul>

      <button @click="close" class="mt-4 bg-blue-500 text-white px-4 py-2 rounded-md">Cerrar</button>
    </div>
  </div>
</template>

<script setup>
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
  emit("close");
};
</script>

<style scoped>
.modal-content {
  max-width: 600px;
  margin: auto;
  background-color: white; /* Asegura que el fondo sea siempre blanco */
  color: black; /* Asegura que el texto sea siempre negro */
}

.modal-overlay {
  background-color: rgba(0, 0, 0, 0.5); /* Fondo oscuro con opacidad */
}
</style>
