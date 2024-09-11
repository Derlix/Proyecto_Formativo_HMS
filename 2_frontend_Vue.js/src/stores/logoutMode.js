import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useAuthStore } from '@/stores'; // Asegúrate de que esta ruta sea correcta
import { useRouter } from 'vue-router';

export const useLogoutModeStore = defineStore('logoutMode', () => {
    const isEnabled = ref(false);

    // Obtén las instancias del authStore y router
    const authStore = useAuthStore();
    const router = useRouter();

    // Acción para cerrar sesión
    const logout = () => {
        authStore.logout(); // Llama a la acción de logout del store de autenticación
        router.push('/'); // Redirige a la ruta raíz
    };

    // Función que cambia el estado de 'isEnabled' y ejecuta un alert
    function set(payload = null) {
        isEnabled.value = payload !== null ? payload : !isEnabled.value;

        // // Mostrar el mensaje de alerta
        // alert("Hola");

        // Llamar a la acción de logout
        logout();
    }

    return {
        isEnabled,
        set
    };
});
