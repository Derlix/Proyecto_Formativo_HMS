<script setup>
import { ref } from 'vue'

// Crear referencias reactivas para los campos del formulario
const nombre = ref('')
const apellido = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const telefono = ref('')
const numeroDocumento = ref('')
const ciudad = ref('')
const rol = ref('')
const codigoInvitacion = ref('') // Añadido campo de código de invitación

// Array de roles de ejemplo para el campo de selección
const roles = ref(['Administrador', 'Recepcionista', 'Cajero'])

// Mensaje de error
const errorMessage = ref('')

// Función para manejar el registro
const register = () => {
  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Las contraseñas no coinciden'
    return
  }

  // Lógica de registro aquí
  console.log('Datos del registro:', {
    nombre: nombre.value,
    apellido: apellido.value,
    email: email.value,
    telefono: telefono.value,
    numeroDocumento: numeroDocumento.value,
    ciudad: ciudad.value,
    rol: rol.value,
    codigoInvitacion: codigoInvitacion.value
  })
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-lg w-full bg-white p-8 shadow-md rounded-lg">
      <h2 class="text-3xl font-semibold text-gray-700 text-center">Registrarse</h2>
      <p class="mt-2 text-center text-gray-600">Por favor, complete el formulario para crear una cuenta</p>

      <form @submit.prevent="register" class="mt-8 space-y-6">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="nombre" class="block text-sm font-medium text-gray-700">Nombre</label>
            <input v-model="nombre" id="nombre" type="text" required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Nombre">
          </div>
          <div>
            <label for="apellido" class="block text-sm font-medium text-gray-700">Apellido</label>
            <input v-model="apellido" id="apellido" type="text" required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Apellido">
          </div>
        </div>

        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">Correo Electrónico</label>
          <input v-model="email" id="email" type="email" required
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            placeholder="Correo Electrónico">
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700">Contraseña</label>
            <input v-model="password" id="password" type="password" required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Contraseña">
          </div>
          <div>
            <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Confirmar Contraseña</label>
            <input v-model="confirmPassword" id="confirmPassword" type="password" required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Confirmar Contraseña">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="telefono" class="block text-sm font-medium text-gray-700">Teléfono</label>
            <input v-model="telefono" id="telefono" type="text" required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Teléfono">
          </div>
          <div>
            <label for="numeroDocumento" class="block text-sm font-medium text-gray-700">Número de Documento</label>
            <input v-model="numeroDocumento" id="numeroDocumento" type="text" required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Número de Documento">
          </div>
        </div>

        <div>
            <label for="codigoInvitacion" class="block text-sm font-medium text-gray-700">Codigo de invitacion</label>
            <input v-model="codigoInvitacion" id="codigoInvitacion" type="number" required
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Codigo de invitacion">
        </div>
        <div>
          <label for="ciudad" class="block text-sm font-medium text-gray-700">Ciudad</label>
          <input v-model="ciudad" id="ciudad" type="text" required
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            placeholder="Ciudad">
        </div>

        <div>
          <label for="rol" class="block text-sm font-medium text-gray-700">Seleccionar Rol</label>
          <select v-model="rol" id="rol" required
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
            <option value="" disabled>Seleccione un rol</option>
            <option v-for="role in roles" :key="role" :value="role">{{ role }}</option>
          </select>
        </div>

        <div v-if="errorMessage" class="text-red-500 text-sm mt-2 text-center">
          {{ errorMessage }}
        </div>

        <div>
          <button type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Registrarse
          </button>
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
