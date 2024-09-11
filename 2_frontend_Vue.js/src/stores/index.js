import { defineStore } from 'pinia';
import { login } from '@/services/authService'; // Importa el servicio de autenticación

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')) || null,
    permissions: JSON.parse(localStorage.getItem('permissions')) || [],
    accessToken: localStorage.getItem('access_token') || null,
    authError: null,
  }),
  actions: {
    async login(username, password) {
      try {
        const response = await login(username, password); // Usa el servicio para la autenticación
        
        this.user = response.data.user;
        this.permissions = response.data.permissions;
        this.accessToken = response.data.access_token;
        this.authError = null;

        // Guardar datos en localStorage
        localStorage.setItem('user', JSON.stringify(this.user));
        localStorage.setItem('permissions', JSON.stringify(this.permissions));
        localStorage.setItem('access_token', this.accessToken);
      } catch (error) {
        if (error.response && error.response.status === 401) {
          this.authError = error.response.data.detail;
        } else {
          this.authError = 'Ocurrió un error inesperado';
        }
      }
    },

    logout() {
      this.user = null;
      this.permissions = [];
      this.accessToken = null;
      this.authError = null;

      // Remover datos de localStorage
      localStorage.removeItem('user');
      localStorage.removeItem('permissions');
      localStorage.removeItem('access_token');
    }
  }
});
