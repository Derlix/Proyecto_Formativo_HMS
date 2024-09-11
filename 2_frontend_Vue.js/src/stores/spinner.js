// src/store/spinner.js
import { defineStore } from 'pinia';

export const useSpinnerStore = defineStore("spinner", {
  state: () => ({
    loading: false, // Estado inicial del spinner
  }),
  actions: {
    showSpinner() {
      this.loading = true;
    },
    hideSpinner() {
      this.loading = false;
    },
  },
});
