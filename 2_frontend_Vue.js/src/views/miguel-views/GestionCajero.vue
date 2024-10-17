<script setup>
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import ListaCaja from '@/components/miguel_compnents/ListaCaja.vue';

</script>


<template>
  <LayoutAuthenticated>
    <SectionMain class=" rounded-lg">
      <h1 class="text-black dark:text-white text-2xl font-bold mb-8">Lista de registros</h1>

    <ListaCaja />

    </SectionMain>
  </LayoutAuthenticated>
</template>

