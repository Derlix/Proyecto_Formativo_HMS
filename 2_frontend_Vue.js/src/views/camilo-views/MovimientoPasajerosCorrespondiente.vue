<script setup>
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import ListaPasajerosTable from '@/components/miguel_compnents/ListaPasajerosTable.vue';

</script>


<template>
  <LayoutAuthenticated>
    <SectionMain class=" rounded-lg">
      <h1 class="text-black dark:text-white text-2xl font-bold mb-8">Movimiento de pasajeros correspondiente</h1>

    <ListaPasajerosTable />

    </SectionMain>
  </LayoutAuthenticated>
</template>

