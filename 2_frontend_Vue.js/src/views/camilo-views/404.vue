<script setup>
import { useRouter } from 'vue-router'

// Obtener la instancia del router para redirigir
const router = useRouter()

const goToLogin = () => {
  router.push('/')
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-md w-full bg-white p-8 shadow-md rounded-lg flex items-center">
      <!-- Aquí puedes ajustar la ruta de la imagen según la ubicación de tu archivo -->
      <img src="@/assets/img/404.png" alt="404 Not Found" class="w-1/3 h-auto mr-6" />
      <div class="w-2/3">
        <h2 class="text-3xl font-semibold text-gray-700">¡Página No Encontrada!</h2>
        <p class="mt-2 text-gray-600">
          Tengo malas noticias para ti. Es posible que la página que buscas haya sido eliminada o no esté disponible temporalmente.
        </p>
        <button @click="goToLogin"
          class="mt-6 px-4 py-2 bg-indigo-600 text-white font-medium rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Volver al Inicio de Sesión
        </button>
      </div>
    </div>
  </div>
</template>

<style>
body {
  font-family: 'Inter', sans-serif;
}
</style>
