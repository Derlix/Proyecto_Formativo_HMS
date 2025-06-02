<template>
  <div class="relative h-screen overflow-auto p-4">
    <router-link
      to="/"
      class="absolute top-4 left-4 px-3 py-1 bg-gray-300 rounded-md hover:bg-gray-400 transition"
    >
      ← Regresar
    </router-link>

    <div class="flex flex-col justify-center items-center text-center space-y-4 max-w-full mx-auto">
      <h1 class="font-bold text-3xl">Ayuda</h1>
      <p class="text-lg max-w-md mx-auto">
        Aquí tienes una selección de videos que te pueden orientar o ayudarte con algún problema.
      </p>

      <!-- Grid de 2 columnas para videos -->
      <div class="grid grid-cols-2 gap-6 justify-center mt-4">
        <VideoCard
          title="ring ding d-d bem bem bem"
          videoId="k85mRPqvMbE?si=ALxX-v59TYznKJT5"
        />
        <VideoCard
          title="Y fuiste tu mi baile inolvidable "
          videoId="a1Femq4NPxs?si=qNFhtAvwnrVyALh4"
        />
        <VideoCard
          title="No se si vuelva a verteeee :("
          videoId="75gaEbTLqpg?si=OTu4qldOsU3xYuNm"
        />
        <VideoCard
          title="Ojala sintieras esto que estoy sintiendooo"
          videoId="Lf566pMNCOw?si=g7v-uqFPUUTjdei5"
        />
      </div>
      <h1>Fase Alphaaaaaaaa (Primera etapa de desarrollo), no critiquen :></h1>
    </div>
  </div>
</template>

<script setup>
import VideoCard from '../../components/VideoCardUI.vue'
</script>
