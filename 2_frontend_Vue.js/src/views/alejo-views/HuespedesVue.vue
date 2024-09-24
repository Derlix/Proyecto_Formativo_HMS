<script setup>
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import HuespedesTable from '@/components/alejo_components/HuespedesTable.vue';

</script>


<template>
  <LayoutAuthenticated>
    <SectionMain class=" rounded-lg">
      <h1 class="text-black dark:text-white text-2xl font-bold mb-8">Historial Huéspedes</h1>

    <HuespedesTable />

    </SectionMain>
  </LayoutAuthenticated>
</template>

