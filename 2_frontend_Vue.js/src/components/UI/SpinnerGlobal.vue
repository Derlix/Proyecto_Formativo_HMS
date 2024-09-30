<template>
  <!-- Capa que cubre toda la pantalla cuando loading está activo -->
  <div v-if="loading" class="spinner-overlay">
    <div class="spinner-container">
      <!-- Imagen personalizada del spinner -->
      <img src="https://res.cloudinary.com/dbe0nouku/image/upload/f_auto,q_auto/v1/actions/tbijj2txyfwiuuwitfse" alt="Loading..." class="spinner-image">
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useSpinnerStore } from "@/stores/spinner";

export default {
  setup() {
    const spinnerStore = useSpinnerStore();
    return {
      loading: computed(() => spinnerStore.loading),
    };
  },
};
</script>

<style scoped>
/* Capa que cubre toda la pantalla */
.spinner-overlay {
  @apply fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex justify-center items-center z-[9999];
}

/* Centrar el contenedor de la imagen */
.spinner-container {
  @apply flex justify-center items-center;
}

/* Imagen del spinner */
.spinner-image {
  @apply w-[100] h-[80px]; /* Tamaño personalizado de la imagen */
}
</style>
