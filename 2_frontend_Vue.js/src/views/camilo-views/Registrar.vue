<script setup>
import { ref } from 'vue'
import { creaateUser } from '../../services/juanca_service/registrarService';
import CardBox from '@/components/CardBox.vue'

const nombreCompleto = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const codigoInvitacion = ref('')
const errorMessage = ref('')
const registroExitoso = ref(false)

const register = async () => {
  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Las contraseñas no coinciden'
    return
  }

  try {
    const response = await creaateUser(
      nombreCompleto.value,
      email.value,
      codigoInvitacion.value, // Asumiendo que este campo es id_hotel
      password.value // La contraseña que se enviará como passhash
    );

    console.log('Registro exitoso:', response);
    registroExitoso.value = true;

    nombreCompleto.value = '';
    email.value = '';
    password.value = '';
    confirmPassword.value = '';
    codigoInvitacion.value = '';
    errorMessage.value = '';

  } catch (error) {
    registroExitoso.value = false;
    if (error.data && error.data.detail) {
      errorMessage.value = error.data.detail; // Mostrar detalles del error de la API
    } else {
      errorMessage.value = 'Hubo un error al registrar. Intente nuevamente.';
    }
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-lg w-full bg-white p-8 shadow-md rounded-lg">
      <div class="flex justify-center mb-4">
        <img src="@/assets/img/sena-agro.png" alt="Logo Sena" class="w-12 sm:w-16">
      </div>
      <h2 class="text-center mb-4 font-bold text-lg sm:text-xl">Registrarse</h2>
      <p class="mt-2 text-center text-gray-600">Por favor, complete el formulario para crear una cuenta</p>

      <CardBox v-if="registroExitoso" color="bg-green-500" class="mb-4">
        <template #default>
          <p class="text-white">¡Registro exitoso!</p>
        </template>
      </CardBox>

      <form @submit.prevent="register" class="mt-8 space-y-6">
        <div>
          <div>
            <label for="nombreCompleto" class="block text-sm font-bold ">Nombre</label>
            <input v-model="nombreCompleto" id="nombreCompleto" type="text" required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Nombre">
          </div>
        </div>

        <div>
          <label for="email" class="block text-sm font-bold ">Correo Electrónico</label>
          <input v-model="email" id="email" type="email" required
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            placeholder="Correo Electrónico">
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="password" class="block text-sm font-bold ">Contraseña</label>
            <input v-model="password" id="password" type="password" required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Contraseña">
          </div>
          <div>
            <label for="confirmPassword" class="block text-sm font-bold ">Confirmar Contraseña</label>
            <input v-model="confirmPassword" id="confirmPassword" type="password" required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Confirmar Contraseña">
          </div>
        </div>


        <div>
            <label for="codigoInvitacion" class="block text-sm font-bold ">Codigo de invitacion</label>
            <input v-model="codigoInvitacion" id="codigoInvitacion" type="number" required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Codigo de invitacion">
        </div>

        <div v-if="errorMessage" class="text-red-500 text-sm mt-2 text-center">
          {{ errorMessage }}
        </div>

        <div>
          <button type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-bold rounded-md text-white bg-blue-500 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
            Registrarse
          </button>
          <div class="text-center mt-3">
            <router-link to="/inicio" class="underline font-bold text-base">Volver</router-link>
        </div>
        </div>
      </form>
    </div>
  </div>
</template>

<style>
body {
  font-family: 'Inter', sans-serif;
}
</style>
