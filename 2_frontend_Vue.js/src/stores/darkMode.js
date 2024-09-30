import { defineStore } from 'pinia'
import { ref, onMounted } from 'vue'

export const useDarkModeStore = defineStore('darkMode', () => {
  const isEnabled = ref(false)

  // Inicializar el estado de modo oscuro basado en localStorage
  function initialize() {
    if (typeof localStorage !== 'undefined') {
      const storedDarkMode = localStorage.getItem('darkMode')
      isEnabled.value = storedDarkMode === '1'
      applyDarkModeClasses(isEnabled.value)
    }
  }

  // Aplicar o remover clases CSS de modo oscuro
  function applyDarkModeClasses(isDarkMode) {
    if (typeof document !== 'undefined') {
      document.body.classList[isDarkMode ? 'add' : 'remove']('dark-scrollbars')
      document.documentElement.classList[isDarkMode ? 'add' : 'remove'](
        'dark',
        'dark-scrollbars-compat'
      )
    }
  }

  // Alternar el modo oscuro y persistir en localStorage
  function set(payload = null) {
    isEnabled.value = payload !== null ? payload : !isEnabled.value
    applyDarkModeClasses(isEnabled.value)

    if (typeof localStorage !== 'undefined') {
      localStorage.setItem('darkMode', isEnabled.value ? '1' : '0')
    }
  }

  // Ejecutar la inicialización al montar el store
  onMounted(() => {
    initialize()
  })

  return {
    isEnabled,
    set,
    initialize
  }
})
