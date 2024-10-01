import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import { useAuthStore } from '@/stores' // Importa el store de autenticación

export const useMainStore = defineStore('main', () => {

  const authStore = useAuthStore();

  const userName = computed(() => authStore.user?.nombre_completo || 'undefined');
  const userEmail = computed(() => authStore.user?.email || 'undefined');
  const userRole = computed(() => authStore.user?.usuario_rol || 'undefined');
  const userID = computed(() => authStore.user?.user_id || 'undefined');
  // Sirve para mostrar la imagen de perfil del usuario
  const userProfile = computed(() => {
    return authStore.user?.img_profile ? `${import.meta.env.VITE_API_URL}/${authStore.user.img_profile}` : null;
  });

  // Función para obtener la imagen de perfil del usuario
  const userAvatar = computed(() => {
    // Si el usuario tiene una imagen de perfil, la devuelve
    if (userProfile.value) {
      console.log(userProfile.value);
      return userProfile.value;
      // Si no tiene imagen de perfil, devuelve una imagen por defecto según el rol
    } else {
      if (userRole.value === 'SuperAdmin') {
        return 'src/assets/img/super-admin.png';
      } else if (userRole.value === 'Recepcionista') {
        return 'src/assets/img/recepcionista.png';
      } else if (userRole.value === 'Cajero') {
        return 'src/assets/img/cajero.png';
      } else if (userRole.value === 'AuditorNocturno') {
        return 'src/assets/img/auditor-nocturno.png';
      } else if (userRole.value === 'JefeRecepcion') {
        return 'src/assets/img/jefe-recepcion.png';
      } else {
        return 'src/assets/img/default.png';
      }
    }
  });
  
  const isFieldFocusRegistered = ref(false)

  const clients = ref([])
  const history = ref([])

  function setUser(payload) {
    const user = JSON.parse(localStorage.getItem('user')) || {};

    if (payload.name) {
      user.nombre_completo = payload.name;
    }
    if (payload.email) {
      user.email = payload.email;
    }
    if (payload.usuario_rol) {
      user.usuario_rol = payload.usuario_rol;
    }
    if (payload.user_id) {
      user.user_id = payload.user_id;
    }

    // Actualiza el store de autenticación
    authStore.user = { ...authStore.user, ...user };

    localStorage.setItem('user', JSON.stringify(user));
  }

  function fetchSampleClients() {
    axios
      .get(`data-sources/clients.json?v=3`)
      .then((result) => {
        clients.value = result?.data?.data
      })
      .catch((error) => {
        alert(error.message)
      })
  }

  function fetchSampleHistory() {
    axios
      .get(`data-sources/history.json`)
      .then((result) => {
        history.value = result?.data?.data
      })
      .catch((error) => {
        alert(error.message)
      })
  }

  return {
    userName,
    userEmail,
    userAvatar,
    isFieldFocusRegistered,
    clients,
    history,
    userRole,
    userID,
    setUser,
    fetchSampleClients,
    fetchSampleHistory
  }
})
