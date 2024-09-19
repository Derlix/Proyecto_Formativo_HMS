<script setup>
import { ref, reactive } from 'vue'
import { useAuthStore } from '@/stores' // Importa el store de autenticación

import { useRouter } from 'vue-router'
import { mdiAccount, mdiAsterisk } from '@mdi/js'
import SectionFullScreen from '@/components/SectionFullScreen.vue'
import CardBox from '@/components/CardBox.vue'
import FormCheckRadio from '@/components/FormCheckRadio.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import BaseButton from '@/components/BaseButton.vue'
import LayoutGuest from '@/layouts/LayoutGuest.vue'

const form = reactive({
  login: '',
  pass: '',
  remember: true
})

const router = useRouter()
const authStore = useAuthStore()

// Define las propiedades reactivas para el email, la contraseña y el mensaje de error
const email = ref('')
const password = ref('')
const errorMessage = ref(null) // Añade una propiedad para el mensaje de error

// Método para manejar el login
const handleLogin = async () => {
  try {
    await authStore.login(email.value, password.value) // Llama al método de login del store

    if (authStore.authError) {
      // Si hay un error de autenticación, establece el mensaje de error
      errorMessage.value = authStore.authError
    } else {
      // Redirige a la página de dashboard si el login es exitoso
      router.push('/dashboard') // Reemplaza '/dashboard' con la ruta que desees redirigir
    }
  } catch (error) {
    // Maneja errores inesperados
    errorMessage.value = 'Error durante el login: ' + error.message
  }
  return {
    email,
    password,
    errorMessage,
    handleLogin
  };
};

</script>

<template>
  <LayoutGuest>
    <SectionFullScreen bg="white">
      <CardBox is-form @submit.prevent="handleLogin" class=" w-2/6">
        <div class="flex justify-center mb-4">
          <!-- Logo (puedes colocar un ícono aquí) -->
          <img src="src/assets/img/sena-agro.png" alt="Logo Sena" class="w-16">
        </div>
        <h1 class="text-center mb-4 font-bold">Iniciar Sesion</h1>
        <!-- Mostrar error si existe -->
        <div v-if="errorMessage" class="alert alert-danger" role="alert">
          {{ errorMessage }}
        </div>
        <FormField label="Email" help="Por Favor Ingrese Su Correo">
          <FormControl v-model="email" :icon="mdiAccount" name="login" autocomplete="usermail" />
        </FormField>

        <FormField label="Contraseña" help="Por favor ingrese su contraseña">
          <FormControl
            v-model="password"
            :icon="mdiAsterisk"
            type="password"
            name="password"
            autocomplete="current-password"
          />
        </FormField>

        <div class="mb-7">
            <BaseButton
              type="submit"
              color="info"
              label="Ingresar"
              class="w-full"
            />
        </div>

        <FormCheckRadio
          v-model="form.remember"
          name="remember"
          label="Recordarme"
          :input-value="true"
        />

        <div class="text-center m-1">
            <router-link to="/recuperar" class="text-xs">¿Olvidaste tu contraseña? Restablecer contraseña</router-link>
        </div>
        <div class="text-center m-2">
            <router-link to="/registrar" class="text-xs">¿Aún no tienes cuenta? Registrate</router-link>
        </div>
      </CardBox>
    </SectionFullScreen>
  </LayoutGuest>
</template>
