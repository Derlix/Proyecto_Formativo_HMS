<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { mdiCodeEqual, mdiEmail, mdiAsterisk } from '@mdi/js'
import SectionFullScreen from '@/components/SectionFullScreen.vue'
import CardBox from '@/components/CardBox.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import BaseButton from '@/components/BaseButton.vue'
import LayoutGuest from '@/layouts/LayoutGuest.vue'
import { requestResetCode, changePassword } from '@/services/authService'

const email = ref('')
const newPassword = ref('')
const confirmPassword = ref('')
const code = ref('')
const errorMessage = ref(null)
const showPasswordForm = ref(false)

const router = useRouter()

const sendResetCode = async () => {
    errorMessage.value = null

    // Validar email antes de enviar
    if (!email.value.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
        errorMessage.value = "Por favor, ingresa un correo electrónico válido."
        setTimeout(() => {
                errorMessage.value = null;
            }, 3000);
        return
    }

    try {
        await requestResetCode(email.value)
        showPasswordForm.value = true
    } catch (err) {
        errorMessage.value = err.response?.data?.detail || "Error enviando el código. Intente de nuevo."
        setTimeout(() => {
                errorMessage.value = null;
            }, 3000);
    }
}

const resetPassword = async () => {
    errorMessage.value = null // Limpiar error previo

    // Validar que las contraseñas coincidan
    if (newPassword.value !== confirmPassword.value) {
        errorMessage.value = "Las contraseñas no coinciden."
        setTimeout(() => {
                errorMessage.value = null;
            }, 3000);
        return
    }

    try {
        await changePassword(email.value, newPassword.value, code.value)
        alert("¡Contraseña actualizada con éxito!")
        router.push("/") // Redirigir a la página de inicio después de cambiar la contraseña
    } catch (err) {
        errorMessage.value = err.response?.data?.detail || "Error actualizando la contraseña. Verifique el código."
        setTimeout(() => {
                errorMessage.value = null;
            }, 3000);
    }
}
</script>

<template>
    <LayoutGuest>
        <SectionFullScreen>
            <CardBox class="sm:w-3/6 md:w-3/5 lg:w-3/6 xl:w-2/6 mx-auto">
                <div class="flex justify-center mb-4">
                    <img src="@/assets/img/sena-agro.png" alt="Logo Sena" class="w-12 sm:w-16">
                </div>
                <h1 class="text-center mb-4 font-bold text-lg sm:text-xl">Recuperar Contraseña</h1>

                <!-- Mostrar error si existe -->
                <div v-if="errorMessage" class="bg-red-600 text-white p-2 sm:p-4 rounded-md mb-4" role="alert">
                    {{ errorMessage }}
                </div>

                <!-- Formulario de envío de código -->
                <form v-if="!showPasswordForm" @submit.prevent="sendResetCode" class="user">
                    <FormField label="Email" help="Ingresa Tu Correo Valido.">
                        <FormControl v-model="email" :icon="mdiEmail" name="login" autocomplete="usermail" required/>
                    </FormField>

                    <div class="mb-7">
                        <BaseButton
                            type="submit"
                            color="info"
                            label="Enviar Código"
                            class="w-full"
                        />
                    </div>
                </form>

                <!-- Formulario para cambiar la contraseña después de enviar el código -->
                <form v-if="showPasswordForm" @submit.prevent="resetPassword" class="user">
                    <FormField label="Nueva Contraseña" help="Ingresa Tu Nueva Contraseña.">
                        <FormControl v-model="newPassword" :icon="mdiAsterisk" type="password" name="new-password" required/>
                    </FormField>

                    <FormField label="Confirmar Contraseña" help="Confirma Tu Nueva Contraseña.">
                        <FormControl v-model="confirmPassword" :icon="mdiAsterisk" type="password" name="confirm-password" required/>
                    </FormField>

                    <FormField label="Código" help="Ingresa el código enviado a tu correo.">
                        <FormControl v-model="code" :icon="mdiCodeEqual" name="code" required/>
                    </FormField>

                    <div class="mb-7">
                        <BaseButton
                            type="submit"
                            color="info"
                            label="Cambiar Contraseña"
                            class="w-full"
                        />
                    </div>
                </form>

                <div class="text-center m-2">
                    <router-link to="/" class="text-xs sm:text-sm text-blue-600 hover:text-black">¿Ya tienes cuenta? Inicia Sesión</router-link>
                </div>
            </CardBox>
        </SectionFullScreen>
    </LayoutGuest>
</template>
