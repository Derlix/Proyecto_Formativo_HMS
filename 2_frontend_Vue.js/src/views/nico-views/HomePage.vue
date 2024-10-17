<template>
    <LayoutGuest>
        <SectionFullScreen>
            <div class="w-full h-screen flex flex-col items-center justify-center bg-gradient-to-b from-blue-500 to-blue-800 text-white">
                <!-- Logo del sistema -->
                <div class="mb-8">
                    <img src="@/assets/img/sena-agro.png" alt="Logo HMS" class="w-20 sm:w-28">
                </div>

                <!-- Título de bienvenida -->
                <h1 class="text-4xl text-black font-bold mb-4">¡Bienvenido a HMS!</h1>

                <!-- Descripción breve del sistema -->
                <p class="text-lg text-black sm:text-xl mb-6 text-center w-4/5 sm:w-3/5">
                    HMS es tu sistema integral de gestión hotelera que te permite manejar reservas, administrar habitaciones y optimizar la experiencia de tus clientes de manera sencilla y eficaz.
                </p>

                <!-- Botón de Iniciar Sesión con ícono -->
                <div class="mb-5">
                    <router-link to="/iniciar" style="border: 1px solid rgba(0, 0, 0, 0.9)" class="rounded p-4 text-black flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" :viewBox="'0 0 24 24'" class="w-5 h-5 mr-2">
                            <path :d="mdiAccount" />
                        </svg>
                        Iniciar Sesión
                    </router-link>
                </div>

                <!-- Botón de Registro con ícono -->
                <div class="mt-5">
                    <router-link to="/registrar" style="border: 1px solid rgba(0, 0, 0, 0.9)" class="rounded p-4 text-black flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" :viewBox="'0 0 24 24'" class="w-5 h-5 mr-2">
                            <path :d="mdiAsterisk" />
                        </svg>
                        Registrarse
                    </router-link>
                </div>

                <!-- Pie de página con información adicional -->
                <div class="absolute bottom-5 text-center w-full">
                    <p class="text-black text-sm">
                        HMS &copy; 2024. Todos los derechos reservados.
                    </p>
                </div>
            </div>
        </SectionFullScreen>
    </LayoutGuest>
</template>

<script>
import { mdiAccount, mdiAsterisk } from '@mdi/js'

export default {
    name: 'HomePage',
    data() {
        return {
            mdiAccount,
            mdiAsterisk,
        }
    }
}
</script>

<style scoped>
.bg-gradient-to-b {
    background-image: linear-gradient(to bottom, rgb(233, 244, 208), #e6d1d1);
}
</style>
