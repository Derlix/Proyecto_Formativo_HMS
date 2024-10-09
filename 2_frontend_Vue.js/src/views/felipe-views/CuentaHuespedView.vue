<script setup>
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import TablaCuentaHuesped from '@/components/felipe_componentes/TablaCuentaHuesped.vue';
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue';

</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton title="Cuenta Huesped" />
      <TablaCuentaHuesped />
    </SectionMain>

   
  </LayoutAuthenticated>
</template>

