<script setup>
import { ref, reactive,onMounted } from 'vue'
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
import { useDarkModeStore } from '@/stores/darkMode.js'
const darkModeStore = useDarkModeStore()


const form = reactive({
    login: '',
    pass: '',
    remember: false
})

const router = useRouter()
const authStore = useAuthStore()
const email = ref('')
const password = ref('')
const errorMessage = ref(null)

onMounted(() => {
    const storedEmail = localStorage.getItem('email')
    if (storedEmail) {
        email.value = storedEmail
        form.remember = true
    }
    darkModeStore.set(false)
})

const handleLogin = async () => {
    try {
        await authStore.login(email.value, password.value)

        if (authStore.authError) {
            errorMessage.value = authStore.authError
            setTimeout(() => {
                errorMessage.value = null;
            }, 3000);
        } else {
            if (form.remember) {
                localStorage.setItem('email', email.value)
            } else {
                localStorage.removeItem('email')
            }
            if (authStore.user.usuario_rol === 'SuperAdmin' || authStore.user.usuario_rol === 'JefeRecepcion') {
                router.push('/dashboard')
            } else if (authStore.user.usuario_rol === 'Recepcionista') {
                router.push('/dashboard')
            }else if (authStore.user.usuario_rol === 'Cajero') {
                router.push('/inicio-cajero')
            }
        }
    } catch (error) {
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
        <SectionFullScreen>
            <CardBox is-form @submit.prevent="handleLogin" class="sm:w-3/6 md:w-3/5 lg:w-3/6 xl:w-2/6 mx-auto">
                <div class="flex justify-center mb-4">
                    <img src="@/assets/img/sena-agro.png" alt="Logo Sena" class="w-12 sm:w-16">
                </div>
                <h1 class="text-center mb-4 font-bold text-lg sm:text-xl">Iniciar Sesión</h1>
    
                <!-- Mostrar error si existe -->
                <div v-if="errorMessage" class="bg-red-600 text-white p-2 sm:p-4 rounded-md mb-4" role="alert">
                    {{ errorMessage }}
                </div>

                <FormField label="Email" help="Por Favor Ingrese Su Correo">
                    <FormControl v-model="email" :icon="mdiAccount" name="login" autocomplete="usermail" required/>
                </FormField>

                <FormField label="Contraseña" help="Por favor ingrese su contraseña">
                    <FormControl
                        v-model="password"
                        :icon="mdiAsterisk"
                        type="password"
                        name="password"
                        autocomplete="current-password"
                        required
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
                    :inputValue="form.remember"
                />

                <div class="text-center m-1">
                    <router-link to="/recuperar" class="text-xs sm:text-sm">¿Olvidaste tu contraseña? Restablecer contraseña</router-link>
                </div>
    
                <div class="text-center m-2">
                    <router-link to="/registrar" class="text-xs sm:text-sm">¿Aún no tienes cuenta? Regístrate</router-link>
                </div>
            </CardBox>
        </SectionFullScreen>
    </LayoutGuest>
</template>
