<script setup>
import { mdiForwardburger, mdiBackburger, mdiMenu } from '@mdi/js'
import { ref, computed, onMounted } from 'vue'
import { useMainStore } from '@/stores/main'
import { useRouter } from 'vue-router'
import menuAside from '@/menuAside.js'
import menuNavBar from '@/menuNavBar.js'
import { useDarkModeStore } from '@/stores/darkMode.js'
import { useLogoutModeStore } from '@/stores/logoutMode.js'
import { useAuthStore } from '@/stores/index.js' // Importar el authStore
import BaseIcon from '@/components/BaseIcon.vue'
import NavBar from '@/components/NavBar.vue'
import NavBarItemPlain from '@/components/NavBarItemPlain.vue'
import AsideMenu from '@/components/AsideMenu.vue'
import FooterBar from '@/components/FooterBar.vue'

// Estados y stores
const layoutAsidePadding = 'xl:pl-60'
const darkModeStore = useDarkModeStore()
const LogoutModeStore = useLogoutModeStore()
const mainStore = useMainStore()
const authStore = useAuthStore() // Usar el store de autenticación
const router = useRouter()

const isAsideMobileExpanded = ref(false)
const isAsideLgActive = ref(false)

// onMounted(() => {
//   mainStore.fetchADatosUsuario();
// });

// const userRole = computed(() => mainStore.userRole)

// Filtrado de menú basado en permisos
const filteredMenuAside = computed(() => {
  return menuAside.filter(menuItem => {
    return authStore.permissions.some(permission =>
      permission.module_name === menuItem.modulo && permission.p_select
    )
  })
})


// Control del estado de navegación
router.beforeEach(() => {
  isAsideMobileExpanded.value = false
  isAsideLgActive.value = false
})

// Control de eventos en el menú
const menuClick = (event, item) => {
  if (item.isToggleLightDark) {
    darkModeStore.set()
  }

  if (item.isLogout) {
    LogoutModeStore.set()
  }
}
</script>

<template>
  <div
    :class="{
      'overflow-hidden lg:overflow-visible': isAsideMobileExpanded
    }"
  >
    <div
      :class="[layoutAsidePadding, { 'ml-60 lg:ml-0': isAsideMobileExpanded }]"
      class="pt-14 min-h-screen w-screen transition-position lg:w-auto bg-gray-50 dark:bg-slate-800 dark:text-slate-100"
    >
      <NavBar
        :menu="menuNavBar"
        :class="[layoutAsidePadding, { 'ml-60 lg:ml-0': isAsideMobileExpanded }]"
        @menu-click="menuClick"
      >
        <NavBarItemPlain
          display="flex lg:hidden"
          @click.prevent="isAsideMobileExpanded = !isAsideMobileExpanded"
        >
          <BaseIcon :path="isAsideMobileExpanded ? mdiBackburger : mdiForwardburger" size="24" />
        </NavBarItemPlain>
        <NavBarItemPlain display="hidden lg:flex xl:hidden" @click.prevent="isAsideLgActive = true">
          <BaseIcon :path="mdiMenu" size="24" />
        </NavBarItemPlain>
      </NavBar>
      <!-- Usamos el menú filtrado -->
      <AsideMenu
        :is-aside-mobile-expanded="isAsideMobileExpanded"
        :is-aside-lg-active="isAsideLgActive"
        :menu="filteredMenuAside"
        @menu-click="menuClick"
        @aside-lg-close-click="isAsideLgActive = false"
      />
      <slot />
      <FooterBar></FooterBar>
    </div>
  </div>
</template>
