<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-md w-full bg-white p-8 shadow-md rounded-lg">
      <h2 class="text-3xl font-semibold text-gray-700 text-center">Recuperar Contraseña</h2>
      <p class="mt-2 text-center text-gray-600">Ingresa tu correo electrónico para recibir un enlace de recuperación de contraseña.</p>

      <form @submit.prevent="recoverPassword" class="mt-8 space-y-6">
        <div class="rounded-md shadow-sm">
          <div>
            <label for="email" class="sr-only">Correo Electrónico</label>
            <input v-model="email" id="email" name="email" type="email" required
              class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Correo Electrónico">
          </div>
        </div>

        <div v-if="errorMessage" class="text-red-500 text-sm mt-2 text-center">
          {{ errorMessage }}
        </div>

        <div>
          <button type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Enviar Enlace de Recuperación
          </button>
        </div>

        <div class="mt-4 text-center">
          <div class="text-sm">
            <a @click.prevent="goToLogin" class="cursor-pointer font-medium text-indigo-600 hover:text-indigo-500">Volver al Inicio de Sesión</a>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const errorMessage = ref('')
const router = useRouter()

const recoverPassword = () => {
  // Aquí deberías implementar la lógica para enviar un enlace de recuperación al correo del usuario.
  // Este es un ejemplo básico de cómo podría funcionar.
  if (email.value) {
    // Simulación de éxito
    console.log(`Enlace de recuperación enviado a ${email.value}`)
    router.push('/')
  } else {
    errorMessage.value = 'Por favor ingrese un correo electrónico válido.'
  }
}

const goToLogin = () => {
  router.push('/')
}
</script>

<style>
body {
  font-family: 'Inter', sans-serif;
}
</style>
