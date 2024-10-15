<script setup>
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import ListaComprobantes from '@/components/miguel_compnents/ListaComprobantes.vue';

</script>


<template>
  <LayoutAuthenticated>
    <SectionMain class=" rounded-lg">
      <h1 class="text-black dark:text-white text-2xl font-bold mb-8">Lista de comprobantes</h1>

    <ListaComprobantes />

    </SectionMain>
  </LayoutAuthenticated>
</template>

