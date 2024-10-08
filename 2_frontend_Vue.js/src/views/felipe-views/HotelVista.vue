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
      <TablaHotel></TablaHotel>
    </SectionMain>

  </LayoutAuthenticated>
</template>