<script setup>
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import TablaHotel from '@/components/felipe_componentes/TablaHotel.vue';
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue';

</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton title="Administración De Hoteles" />

      <div class="text-right">
        <p class="py-5 text-xl">ID del hotel que opera actualmente: <span class="font-bold">{{ userIdHotel }}</span></p>
      </div>
      
      <TablaHotel></TablaHotel>
    </SectionMain>

  </LayoutAuthenticated>
</template>
