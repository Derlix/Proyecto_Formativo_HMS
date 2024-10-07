import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useAuthStore } from '@/stores' // Importar el store de autenticación
import { getUserByEmail } from '@/services/userService' // Importar la función para obtener información del usuario por email

export const useMainStore = defineStore('main', () => {

  const authStore = useAuthStore();

  const userName = computed(() => authStore.user?.nombre_completo || 'undefined');
  const userEmail = computed(() => authStore.user?.email || 'undefined');
  const userRole = computed(() => authStore.user?.usuario_rol || 'undefined');
  const userID = computed(() => authStore.user?.user_id || 'undefined');
  const userIdHotel = computed(() => authStore.user?.id_hotel || 'undefined');

  // Usado para mostrar la imagen de perfil del usuario
  const userProfile = computed(() => {
    return authStore.user?.img_profile ? `${import.meta.env.VITE_API_URL}/${authStore.user.img_profile}` : null;
  });

  // Función para obtener la imagen de avatar del usuario
  const userAvatar = computed(() => {
  if (userProfile.value) {
    return userProfile.value;
  }});
  
  const isFieldFocusRegistered = ref(false)

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
    if (payload.id_hotel) {
      user.id_hotel = payload.id_hotel;
    }
    if (payload.img_profile) {
      user.img_profile = payload.img_profile;
    }

    // Actualizar el store de autenticación
    authStore.user = { ...authStore.user, ...user };

    localStorage.setItem('user', JSON.stringify(user));
  }

  const fetchADatosUsuario = async () => {
    if (typeof getUserByEmail !== 'function') {
      // Si getUserByEmail no está disponible, usar datos del localStorage
      const user = JSON.parse(localStorage.getItem('user')) || {};
      authStore.user = { ...authStore.user, ...user };
      return;
    }
    try {
      const response = await getUserByEmail(userEmail.value);
      setUser({
        name: response.data.nombre_completo,
        email: response.data.email,
        usuario_rol: response.data.usuario_rol,
        user_id: response.data.id_usuario,
        id_hotel: response.data.id_hotel,
        img_profile: response.data.img_profile
      });
    } catch (error) {
      // Si hay un error, usar datos del localStorage
      const user = JSON.parse(localStorage.getItem('user')) || {};
      authStore.user = { ...authStore.user, ...user };
    }
  };

  // fetchADatosUsuario();

  return {
    userName,
    userEmail,
    userAvatar,
    userIdHotel,
    isFieldFocusRegistered,
    userRole,
    userID,
    setUser,
    fetchADatosUsuario
  }
})
