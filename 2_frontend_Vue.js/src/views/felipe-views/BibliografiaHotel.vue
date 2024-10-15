<script setup>
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue';
import VideosTabla from '@/components/felipe_componentes/VideosTabla.vue';

</script>
<template>
      <LayoutAuthenticated>
        <SectionMain>
          <SectionTitleLineWithButton title="Biblioteca de Videos de Ayuda" />
          
          <VideosTabla />
        </SectionMain>
    
       
      </LayoutAuthenticated>
</template>