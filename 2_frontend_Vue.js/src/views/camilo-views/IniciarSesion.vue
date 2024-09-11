<script setup>
import { ref, reactive, computed } from 'vue'
import { useAuthStore } from '@/stores' // Importa el store de autenticación

import { useRouter } from 'vue-router'
import { mdiAccount, mdiAsterisk } from '@mdi/js'
import SectionFullScreen from '@/components/SectionFullScreen.vue'
import CardBox from '@/components/CardBox.vue'
import FormCheckRadio from '@/components/FormCheckRadio.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
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


const goToRegister = () => {
  router.push('/registrar')
}

const goToForgotPassword = () => {
  router.push('/recuperar')
}

</script>

<template>
  <LayoutGuest>
    <SectionFullScreen v-slot="{ cardClass }" bg="purplePink">
      <CardBox :class="cardClass" is-form @submit.prevent="handleLogin">
        <!-- Mostrar error si existe -->
        <div v-if="errorMessage" class="alert alert-danger" role="alert">
          {{ errorMessage }}
        </div>
        <FormField label="Usuario" help="Por favor ingrese su usuario">
          <FormControl v-model="email" :icon="mdiAccount" name="login" autocomplete="username" />
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

        <FormCheckRadio
          v-model="form.remember"
          name="remember"
          label="Recordarme"
          :input-value="true"
        />

        <template #footer>
          <BaseButtons>
            <BaseButton @click="goToRegister" color="info" outline label="Registrarse" />
            <BaseButton
              @click="goToForgotPassword"
              color="info"
              outline
              label="Olvidé mi Contraseña"
            />
            <BaseButton
              type="submit"
              color="info"
              label="Iniciar Sesión"
            />
          </BaseButtons>
        </template>
      </CardBox>
    </SectionFullScreen>
  </LayoutGuest>
</template>
