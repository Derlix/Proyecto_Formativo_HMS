<script setup>
import { reactive, computed } from 'vue'
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

const submit = () => {
  if (form.login == "admin" && form.pass == "admin") {
    // Aquí puedes agregar la lógica para el inicio de sesión
    router.push('/dashboard')
  }
}

const goToRegister = () => {
  router.push('/registrar')
}

const goToForgotPassword = () => {
  router.push('/recuperar')
}

// Computed property to enable/disable the submit button
const isSubmitDisabled = computed(() => {
  return !form.login || !form.pass
})
</script>

<template>
  <LayoutGuest>
    <SectionFullScreen v-slot="{ cardClass }" bg="purplePink">
      <CardBox :class="cardClass" is-form @submit.prevent="submit">
        <FormField label="Usuario" help="Por favor ingrese su usuario">
          <FormControl
            v-model="form.login"
            :icon="mdiAccount"
            name="login"
            autocomplete="username"
          />
        </FormField>

        <FormField label="Contraseña" help="Por favor ingrese su contraseña">
          <FormControl
            v-model="form.pass"
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
            <BaseButton @click="goToForgotPassword" color="info" outline label="Olvidé mi Contraseña" />
            <BaseButton :disabled="isSubmitDisabled" type="submit" color="info" label="Iniciar Sesión" />
          </BaseButtons>
        </template>
      </CardBox>
    </SectionFullScreen>
  </LayoutGuest>
</template>
