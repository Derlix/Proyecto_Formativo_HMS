<template>
    <div class="relative min-h-screen bg-gray-100 p-4 text-gray-800 transition-colors">
        <router-link
            to="/"
            class="absolute top-4 left-4 flex items-center gap-2 px-4 py-2 bg-white/80  backdrop-blur-md border border-gray-300 rounded-full shadow-md hover:shadow-lg transition-all duration-300 hover:scale-105 hover:bg-gray-400">
                <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 text-green-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
                </svg>
            <span class="font-medium text-gray-800">Regresar</span>
        </router-link>

        <div class="max-w-6xl mx-auto text-center space-y-6 pt-12">
            <div class="flex justify-center">
                <img src="../../assets/img/sena-agro.webp" alt="Logo SENA" class="w-20 h-20 object-contain drop-shadow-md" />
            </div>
            <h1 class="font-extrabold text-4xl sm:text-5xl">Centro de Ayuda</h1>
            <p class="text-lg sm:text-xl text-gray-600 max-w-2xl mx-auto">Explora nuestros videos para resolver tus dudas o aprender más sobre el sistema.</p>
            <div class="w-24 h-1 bg-green-500 mx-auto rounded-full"></div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-8 px-4">
                <VideoCard
                    title="Crear una nueva cuenta en HMS"
                    videoId="GfnSmsYfIGU?si=A4NTxosh2rduFKrQ"
                />
                <VideoCard
                    title="Y fuiste tú, mi baile inolvidable"
                    videoId="a1Femq4NPxs?si=qNFhtAvwnrVyALh4"
                />
                <VideoCard
                    title="No sé si vuelva a verte :("
                    videoId="75gaEbTLqpg?si=OTu4qldOsU3xYuNm"
                />
            </div>

            <div class="mt-10 text-sm text-gray-500 italic">🚧 Fase Beta (Segunda etapa de desarrollo)... no critiquen mucho 😅 ya casi</div>

            <div class="mt-8">
                <p class="text-base font-semibold">¿Aún tienes dudas?</p>
                <a rel="stylesheet" href="https://wa.link/658ee9" target="_blank" class="inline-block mt-2 px-5 py-2 bg-green-600 text-white rounded-full shadow hover:bg-gray-500 transition">Contáctanos</a>
            </div>
        </div>
    </div>
</template>

<script setup>
import VideoCard from '../../components/VideoCardUI.vue'
</script>
