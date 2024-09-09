import { createRouter, createWebHashHistory } from 'vue-router'
// import Style from '@/views/StyleView.vue'
import Home from '@/views/HomeView.vue'
import Profile from '@/views/ProfileView.vue'
import Reservas from '@/views/busta-views/Reservas.vue'
import HistorialReservas from '@/views/busta-views/HistorialReservas.vue'
import InformeAmaLlaves from '@/views/busta-views/InformeAmaLlaves.vue'
// import ListaPasajeros from '@/views/busta-views/ListaPasajeros.vue'
import ComprobanteDescuentos from '@/views/busta-views/ComprobanteDescuentos.vue'
import GestorHotel from '@/views/busta-views/GestorHotel.vue'
import Error404 from '@/views/camilo-views/404.vue'
import IniciarSesion from '@/views/camilo-views/IniciarSesion.vue'
import Registrar from '@/views/camilo-views/Registrar.vue'
import Recuperar from '@/views/camilo-views/Recuperar_contraseña.vue'
import MovimientoPasajeros from '@/views/camilo-views/MovimientoPasajerosCorrespondiente.vue'
import InformePasajeros from '@/views/arce-views/InformePasajeros.vue'
import TarjetaReserva from '@/views/arce-views/TarjetaReserva.vue'
import TranspasoParticulares from '@/views/arce-views/TranspasoParticulares.vue'
import InformacionReserva from '@/views/arce-views/InformacionReserva.vue'


const routes = [
  {
    meta: {
      title: 'InformePasajeros'
    },
    path: '/informe-pasajeros',
    name: 'informe_pasajeros',
    component: InformePasajeros
  },
  {
    meta: {
      title: 'InformacionReserva'
    },
    path: '/informacion-reserva',
    name: 'informacion_reserva',
    component: InformacionReserva
  },
  {
    meta: {
      title: 'TarjetaReserva'
    },
    path: '/tarjeta-reserva',
    name: 'trajeta_reserva',
    component: TarjetaReserva
  },
  {
    meta: {
      title: 'TranspasoParticulares'
    },
    path: '/transpaso-particulares',
    name: 'transpaso_particulares',
    component: TranspasoParticulares
  },
  {
    // No va haber index por el momento, iniciar desde Dashboard.
    meta: {
      title: 'Iniciar sesión'
    },
    path: '/',
    name: 'iniciar sesión',
    component: IniciarSesion
  },
  {
    // No va haber index por el momento, iniciar desde Dashboard.
    meta: {
      title: 'Registrar'
    },
    path: '/registrar',
    name: 'registrar',
    component: Registrar
  },
  {
    // No va haber index por el momento, iniciar desde Dashboard.
    meta: {
      title: 'Recuperar'
    },
    path: '/recuperar',
    name: 'recuperar',
    component: Recuperar
  },
  {
    // No va haber index por el momento, iniciar desde Dashboard.
    meta: {
      title: 'Movimiento de pasajeros correspondiente'
    },
    path: '/movimiento-pasajeros-correspondiente',
    name: 'movimiento pasajeros correspondiente',
    component: MovimientoPasajeros
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
  // {
  //   // Document title tag
  //   // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
  //   meta: {
  //     title: 'Informe de Pasajeros'
  //   },
  //   path: '/informe-pasajeros',
  //   name: 'infomrme de pasajeros',
  //   component: ListaPasajeros
  // },
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
  },
  {
    meta: {
      title: 'Productos'
    },
    path: '/productos',
    name: 'productos',
    component: () => import('@/views/nico-views/ProductoVue.vue')
  },
  {
    meta: {
      title: 'Hoteles'
    },
    path: '/hoteles',
    name: 'hoteles',
    component: () => import('@/views/felipe-views/HotelVista.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    name: '404',
    component: Error404
  },

  {
    meta: {
      title: 'Facturas'
    },
    path: '/facturas',
    name: 'facturas',
    component: () => import('@/views/brayan-views/FacturasView.vue')
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
