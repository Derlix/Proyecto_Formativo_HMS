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
import{ changeHotel } from '@/services/authService'
import NotificationBar from '@/components/alejo_components/NotificationBar.vue';

const email = ref('')
const password = ref('')
const errorMessage = ref(null)
const newHotelCode = ref('')
const isAlertVisible = ref(false);
const colorAlert = ref('');
const isModalVisible = ref(false);
const modalMessage = ref('');

const router = useRouter()


// Cambiar codigo de hotel con changeHotel, parametro son : email, password, newHotelCode
const changeHotelNew = async () => {
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
        await changeHotel(email.value, password.value, newHotelCode.value)
        
        modalMessage.value = "¡Código de hotel actualizado con éxito! Regresa a login";
        isAlertVisible.value = true;
        colorAlert.value = 'success';

        setTimeout(() => {
            isAlertVisible.value = false;
        }, 10000);
        
    } catch (err) {

            modalMessage.value = err.response?.data?.detail || "Error actualizando el código de hotel. Verifique el código.";
            isAlertVisible.value = true;
            colorAlert.value = 'danger';

            setTimeout(() => {
                isAlertVisible.value = false;
            }, 10000);

    }
}

</script>

<template>
    <LayoutGuest>
        <SectionFullScreen>
            <CardBox is-form @submit.prevent="changeHotelNew" class="sm:w-3/6 md:w-3/5 lg:w-3/6 xl:w-2/6 mx-auto">
                <NotificationBar
                    v-if="isAlertVisible"
                    :color="colorAlert" 
                    :description="modalMessage"
                    :visible="isModalVisible"
                />

                <div class="flex justify-center mb-4">
                    <img src="@/assets/img/sena-agro.png" alt="Logo Sena" class="w-12 sm:w-16">
                </div>
                <h1 class="text-center mb-4 font-bold text-lg sm:text-xl">Cambiar Hotel</h1>

                <!-- Mostrar error si existe -->
                <div v-if="errorMessage" class="bg-red-600 text-white p-2 sm:p-4 rounded-md mb-4" role="alert">
                    {{ errorMessage }}
                </div>

                <FormField label="Email" help="Por Favor Ingrese Su Correo">
                    <FormControl v-model="email" :icon="mdiEmail" name="login" autocomplete="usermail" required/>
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

                <!-- FormFiel para el nuevo codigo de hotel tipo numero -->
                <FormField label="Nuevo Código de Hotel" help="Por favor ingrese el nuevo código de hotel">
                    <FormControl
                        v-model="newHotelCode"
                        :icon="mdiCodeEqual"
                        type="number"
                        name="newHotelCode"
                        autocomplete="newHotelCode"
                        required
                    />
                </FormField>


                <div class="mb-7">
                    <BaseButton
                        type="submit"
                        color="info"
                        label="Confirmar cambio"
                        class="w-full"
                    />
                </div>

                <div class="text-center m-2">
                    <router-link to="/" class="text-xs sm:text-sm text-blue-600 hover:text-black">¿Quieres volver? Inicio de Sesión</router-link>
                </div>
            </CardBox>
        </SectionFullScreen>
    </LayoutGuest>
</template>
