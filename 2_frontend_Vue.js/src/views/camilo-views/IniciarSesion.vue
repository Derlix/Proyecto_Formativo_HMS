<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useAuthStore } from '@/stores'; // Importa el store de autenticación
import { useRouter } from 'vue-router';
import { mdiAccount, mdiAsterisk } from '@mdi/js';
import SectionFullScreen from '@/components/SectionFullScreen.vue';
import CardBox from '@/components/CardBox.vue';
import FormCheckRadio from '@/components/FormCheckRadio.vue';
import FormField from '@/components/FormField.vue';
import FormControl from '@/components/FormControl.vue';
import BaseButton from '@/components/BaseButton.vue';
import LayoutGuest from '@/layouts/LayoutGuest.vue';
import { useDarkModeStore } from '@/stores/darkMode.js';
import { getHotelByIdAll } from '@/services/felipe_services/hotelService';

const darkModeStore = useDarkModeStore();
const form = reactive({
  login: '',
  pass: '',
  remember: false
});

const anio = new Date().getFullYear();
const router = useRouter();
const authStore = useAuthStore();
const email = ref('');
const password = ref('');
const errorMessage = ref(null);

const fetchADatosHotel = async () => {
  try {
    const response = await getHotelByIdAll(authStore.user.id_hotel);
    localStorage.setItem('hotelActual', response.data.nombre ? response.data.nombre : (authStore.user.id_hotel ? authStore.user.id_hotel : ''))
  } catch (error) {
    errorMessage.value = 'Error al obtener el hotel: ' + error.message
  }
};

onMounted(() => {
  const storedEmail = localStorage.getItem('email');
  if (storedEmail) {
    email.value = storedEmail;
    form.remember = true;
  }
  darkModeStore.set(false);
});

const handleLogin = async () => {
  try {
    await authStore.login(email.value, password.value);
    if (authStore.authError) {
      errorMessage.value = authStore.authError;
      setTimeout(() => {
        errorMessage.value = null;
      }, 3000);
    } else {
      if (form.remember) {
        localStorage.setItem('email', email.value);
      } else {
        localStorage.removeItem('email');
      }
      if (authStore.user.usuario_rol === 'SuperAdmin' || authStore.user.usuario_rol === 'JefeRecepcion') {
        router.push('/inicio-jefe-recepcionista');
      } else if (authStore.user.usuario_rol === 'Recepcionista') {
        router.push('/dashboard');
      } else if (authStore.user.usuario_rol === 'Cajero') {
        router.push('/inicio-cajero');
      }
      fetchADatosHotel(authStore.user.id_hotel);
    }
  } catch (error) {
    errorMessage.value = 'Error durante el login: ' + error.message;
  }
};
</script>

<template>
  <LayoutGuest>
    <SectionFullScreen class="flex flex-col lg:flex-row justify-center items-center min-h-screen bg-gray-100 relative px-4 lg:px-0">
      <!-- Sección izquierda: Formulario de inicio de sesión (arriba en móviles) -->
      <div class="w-full lg:w-1/4 bg-white p-4 lg:p-6 rounded-lg shadow-lg lg:order-1 order-2 mb-8 lg:mb-0 top-1">
        <CardBox is-form @submit.prevent="handleLogin">
          <!-- Mostrar error si existe -->
          <div v-if="errorMessage" class="bg-red-600 text-white p-2 sm:p-4 rounded-md mb-4" role="alert">
            {{ errorMessage }}
          </div>

          <!-- Campos de formulario -->
          <FormField label="Email" help="Por Favor Ingrese Su Correo">
            <FormControl v-model="email" :icon="mdiAccount" name="login" autocomplete="usermail" required />
          </FormField>

          <FormField label="Contraseña" help="Por favor ingrese su contraseña">
            <FormControl v-model="password" :icon="mdiAsterisk" type="password" name="password" autocomplete="current-password" required />
          </FormField>

          <!-- Botón de iniciar sesión -->
          <div class="mb-4">
            <BaseButton type="submit" color="info" label="Iniciar sesión" class="w-full bg-blue-600 text-white font-bold text-xl lg:text-2xl py-3 rounded-md hover:bg-blue-700" />
          </div>

          <!-- Recordarme -->
          <FormCheckRadio v-model="form.remember" name="remember" label="Recordarme" :inputValue="form.remember" />

          <!-- Links -->
          <div class="text-center mt-3">
            <router-link to="/recuperar" class="text-sm text-blue-700 hover:underline">¿Olvidaste tu contraseña? Restablecer contraseña</router-link>
          </div>

          <div class="text-center mt-3">
            <router-link to="/registrar" class="text-sm text-blue-700 hover:underline">Crear cuenta nueva</router-link>
          </div>

          <div class="text-center mt-3">
            <router-link to="/cambiarhotel" class="text-sm text-blue-700 hover:underline">¿Elegiste el hotel equivocado? Cambia tu selección aquí</router-link>
          </div>
        </CardBox>
      </div>

      <!-- Sección derecha: Texto SENA (arriba en móviles) -->
      <div class="flex flex-col justify-center w-full lg:w-1/2 lg:order-2 order-1 lg:pl-16 text-center lg:text-left">
        <h1 class="text-4xl lg:text-5xl font-bold text-green-600 mb-2 lg:mb-4">
          SENA
        </h1>
        <p class="text-lg lg:text-2xl text-gray-700 font-light">
          HMS es tu sistema integral de gestión hotelera que te permite manejar reservas,
          administrar habitaciones y optimizar la experiencia de tus clientes de manera sencilla y eficaz.
        </p>
      </div>

      <footer class="footer-container absolute bottom-0 left-0 w-full py-2 bg-gray-200">
        <div class="text-center">
          <p class="text-gray-500 text-sm mb-2">
            HMS &copy; <span id="currentYear">{{ anio }}</span>. Todos los derechos reservados.
            <router-link to="/desarollo" class="text-blue-700 hover:underline cursor-pointer">Creditos</router-link>
          </p>
        </div>
      </footer>
    </SectionFullScreen>
  </LayoutGuest>
</template>

<style scoped>
footer{
  margin-top: px;
}
</style>
