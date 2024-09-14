import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import { useAuthStore } from '@/stores' // Importa el store de autenticación

export const useMainStore = defineStore('main', () => {

  const authStore = useAuthStore();

  const userName = computed(() => authStore.user?.nombre_completo || 'undefined');
  const userEmail = computed(() => authStore.user?.email || 'undefined');
  const userRole = computed(() => authStore.user?.usuario_rol || 'undefined');

  const userAvatar = computed(() => authStore.user?.usuario_foto || `/public/img/recepcionista.png`);

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
    setUser,
    fetchSampleClients,
    fetchSampleHistory
  }
})
