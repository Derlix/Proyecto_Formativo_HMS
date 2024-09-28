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

  const userAvatar = computed(() => {
    if (authStore.user?.usuario_foto) {
      return authStore.user.usuario_foto;
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
    if (payload.name) {
      userName.value = payload.name
    }
    if (payload.email) {
      userEmail.value = payload.email
    }
    if (payload.usuario_rol) {
      userRole.value = payload.usuario_rol
    }
    if (payload.user_id) {
      userID.value = payload.user_id
    }
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
