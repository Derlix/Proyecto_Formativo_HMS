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
import { getHotelByIdAll } from '@/services/felipe_services/hotelService'

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

const fetchADatosHotel = async () => {
    try {
        const response = await getHotelByIdAll(authStore.user.id_hotel);
        localStorage.setItem('hotelActual', response.data.nombre ? response.data.nombre : (authStore.user.id_hotel ? authStore.user.id_hotel : ''))
    } catch (error) {
        errorMessage.value = 'Error al obtener el hotel: ' + error.message
    }
}

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
                router.push('/inicio-jefe-recepcionista')
            } else if (authStore.user.usuario_rol === 'Recepcionista') {
                router.push('/dashboard')
            }else if (authStore.user.usuario_rol === 'Cajero') {
                router.push('/inicio-cajero')
            }
            fetchADatosHotel(authStore.user.id_hotel);
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
        <SectionFullScreen class="flex justify-center items-center min-h-screen bg-gray-100">
            <!-- Sección izquierda: Logo y descripción -->
            <div class="hidden lg:flex flex-col justify-center items-start w-1/2 pl-16">
                <!-- Imagen y descripción del SENA -->
                <h1 class="text-center mb-4 font-bold text-5xl text-green-600">SENA </h1>
                <p class="text-2xl text-gray-700 font-light mb-4">El SENA te ayuda a mejorar tus habilidades y conectar con el sector agropecuario.</p>
            </div>

            <!-- Sección derecha: Formulario de inicio de sesión -->
            <div class="w-full lg:w-1/3 p-6 bg-white rounded-lg shadow-lg">
                <CardBox is-form @submit.prevent="handleLogin">

                    <!-- Título en verde similar a "Facebook" en azul -->


                    <!-- Mostrar error si existe -->
                    <div v-if="errorMessage" class="bg-red-600 text-white p-2 sm:p-4 rounded-md mb-4" role="alert">
                        {{ errorMessage }}
                    </div>

                    <!-- Campos de formulario -->
                    <FormField label="Email" help="Por Favor Ingrese Su Correo">
                        <FormControl v-model="email" :icon="mdiAccount" name="login" autocomplete="usermail" required/>
                    </FormField>

                    <FormField label="Contraseña" help="Por favor ingrese su contraseña">
                        <FormControl v-model="password" :icon="mdiAsterisk" type="password" name="password" autocomplete="current-password" required/>
                    </FormField>

                    <!-- Botón de iniciar sesión -->
                    <div class="mb-4">
                        <BaseButton type="submit" color="info" label="Iniciar sesión" class="w-full bg-blue-600 text-white font-bold text-xl py-3 rounded-md hover:bg-blue-700"/>
                    </div>

                    <!-- Recordarme -->
                    <FormCheckRadio v-model="form.remember" name="remember" label="Recordarme" :inputValue="form.remember"/>

                    <!-- Links -->
                    <div class="text-center mt-3">
                        <router-link to="/recuperar" class="text-sm text-blue-700 hover:underline">¿Olvidaste tu contraseña? Restablecer contraseña</router-link>
                    </div>

                    <div class="text-center mt-3">
                        <router-link to="/registrar" class="text-sm text-green-600 hover:underline font-bold">Crear cuenta nueva</router-link>
                    </div>

                    <div class="text-center mt-3">
                        <router-link to="/cambiarhotel" class="text-sm text-blue-700 hover:underline">¿Elegiste el hotel equivocado? Cambia tu selección aquí</router-link>
                    </div>
                </CardBox>
            </div>
        </SectionFullScreen>
    </LayoutGuest>
</template>
