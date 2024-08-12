import { createRouter, createWebHashHistory } from 'vue-router'
// import Style from '@/views/StyleView.vue'
import Home from '@/views/HomeView.vue'
import Profile from '@/views/ProfileView.vue'
import Reservas from '@/views/busta-views/Reservas.vue'
import HistorialReservas from '@/views/busta-views/HistorialReservas.vue'
import InformeAmaLlaves from '@/views/busta-views/InformeAmaLlaves.vue'
import ListaPasajeros from '@/views/busta-views/ListaPasajeros.vue'
import ComprobanteDescuentos from '@/views/busta-views/ComprobanteDescuentos.vue'
import GestorHotel from '@/views/busta-views/GestorHotel.vue'

const routes = [
  {
    // No va haber index por el momento, iniciar desde Dashboard.
    meta: {
      title: 'Dashboard'
    },
    path: '/',
    name: 'Dashboard',
    component: Home
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Dashboard'
    },
    path: '/dashboard',
    name: 'dashboard',
    component: Home
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Reservas'
    },
    path: '/reservas',
    name: 'reservas',
    component: Reservas
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Historial de reservas'
    },
    path: '/historial-reservas',
    name: 'historial de reservas',
    component: HistorialReservas
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Informe de Pasajeros'
    },
    path: '/informe-pasajeros',
    name: 'infomrme de pasajeros',
    component: ListaPasajeros
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Comprobante de descuento'
    },
    path: '/comprobante-descuento',
    name: 'Comprobante de descuento',
    component: ComprobanteDescuentos
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Informe ama de llaves'
    },
    path: '/informe-ama-llaves',
    name: 'informe ama de llaves',
    component: InformeAmaLlaves
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Gestor de hoteles'
    },
    path: '/gestor-hoteles',
    name: 'gestor de hoteles',
    component: GestorHotel
  },
  {
    meta: {
      title: 'Profile'
    },
    path: '/profile',
    name: 'profile',
    component: Profile
  },
  {
    meta: {
      title: 'checkOut'
    },
    path: '/checkOut',
    name: 'checkOut',
    component: () => import('@/views/nico-views/CheckOut.vue')
  }

  // Rutas de la plantilla

  // {
  //   meta: {
  //     title: 'Tables'
  //   },
  //   path: '/tables',
  //   name: 'tables',
  //   component: () => import('@/views/TablesView.vue')
  // },
  // {
  //   meta: {
  //     title: 'Forms'
  //   },
  //   path: '/forms',
  //   name: 'forms',
  //   component: () => import('@/views/FormsView.vue')
  // },
  // {
  //   meta: {
  //     title: 'Ui'
  //   },
  //   path: '/ui',
  //   name: 'ui',
  //   component: () => import('@/views/UiView.vue')
  // },
  // {
  //   meta: {
  //     title: 'Responsive layout'
  //   },
  //   path: '/responsive',
  //   name: 'responsive',
  //   component: () => import('@/views/ResponsiveView.vue')
  // },
  // {
  //   meta: {
  //     title: 'Login'
  //   },
  //   path: '/login',
  //   name: 'login',
  //   component: () => import('@/views/LoginView.vue')
  // },
  // {
  //   meta: {
  //     title: 'Error'
  //   },
  //   path: '/error',
  //   name: 'error',
  //   component: () => import('@/views/ErrorView.vue')
  // }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 }
  }
})

export default router
