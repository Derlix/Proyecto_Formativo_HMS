<!-- src/components/UserAvatar.vue -->

<template>
  <div>
    <img
      :src="userAvatar"
      @error="onImgError"
      class="rounded-full block h-auto w-full max-w-full bg-gray-100 dark:bg-slate-800"
    />
    <slot />
  </div>
</template>

<script>
import { computed } from 'vue';
import { useMainStore } from '@/stores/main';

// Importa las imágenes por defecto según los roles
import superAdminImg from '@/assets/img/super-admin.webp';
import recepcionistaImg from '@/assets/img/recepcionista.webp';
import cajeroImg from '@/assets/img/cajero.webp';
import auditorNocturnoImg from '@/assets/img/auditor-nocturno.webp';
import jefeRecepcionImg from '@/assets/img/jefe-recepcion.webp';
import defaultImg from '@/assets/img/default.webp';

export default {
  name: 'UserAvatar',
  setup() {
    const mainStore = useMainStore();

    const userAvatar = computed(() => mainStore.userAvatar);
    const userRole = computed(() => mainStore.userRole);

    const onImgError = (event) => {
      if (userRole.value === 'SuperAdmin') {
        event.target.src = superAdminImg;
      } else if (userRole.value === 'Recepcionista') {
        event.target.src = recepcionistaImg;
      } else if (userRole.value === 'Cajero') {
        event.target.src = cajeroImg;
      } else if (userRole.value === 'AuditorNocturno') {
        event.target.src = auditorNocturnoImg;
      } else if (userRole.value === 'JefeRecepcion') {
        event.target.src = jefeRecepcionImg;
      } else {
        event.target.src = defaultImg;
      }
    };

    return {
      userAvatar,
      onImgError,
    };
  },
};
</script>
