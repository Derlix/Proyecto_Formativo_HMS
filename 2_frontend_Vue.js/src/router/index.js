import { createRouter, createWebHashHistory } from 'vue-router'
import { useAuthStore } from '@/stores' // Importa el store de autenticación

// import Style from '@/views/StyleView.vue'
import Home from '@/views/HomeView.vue'
import Profile from '@/views/ProfileView.vue'
import Reservas from '@/views/busta-views/ReservasVue.vue'
import HistorialReservas from '@/views/busta-views/HistorialReservas.vue'
import InformeAmaLlaves from '@/views/nico-views/InformeAmaLlaves.vue'
import ListaPasajeros from '@/views/busta-views/ListaPasajeros.vue'
import ComprobanteDescuentos from '@/views/busta-views/ComprobanteDescuentos.vue'
import GestorHotel from '@/views/busta-views/GestorHotel.vue'
import Error404 from '@/views/camilo-views/404.vue'
import IniciarSesion from '@/views/camilo-views/IniciarSesion.vue'
import Registrar from '@/views/camilo-views/Registrar.vue'
import Recuperar from '@/views/camilo-views/RecuperarContrasena.vue'
import MovimientoPasajeros from '@/views/camilo-views/MovimientoPasajerosCorrespondiente.vue'
import InformePasajeros from '@/views/arce-views/InformePasajeros.vue'
import TranspasoParticulares from '@/views/arce-views/TranspasoParticulares.vue'
import InicioCajero from '@/views/arce-views/InicioCajero.vue'
import VistaHabitaciones from '@/views/camilo-views/VistaHabitaciones.vue'
import InicioJefeRecepcionista from '@/views/arce-views/DashboardAdmin.vue'
import UsuariosView from '@/views/arias_views/UsuariosView.vue'
import InformacionReserva from '@/views/arce-views/InformacionReserva.vue'
import ComprobanteDeposito from '@/views/miguel-views/ComprobanteDeposito.vue'
import AvancesEfectivo from '@/views/arce-views/AvancesEfectivo.vue'
import GestionCajero from '@/views/miguel-views/GestionCajero.vue'
import vistaMasAjustes from '@/views/camilo-views/vistaMasAjustes.vue'
import vistaCategorias from '@/views/camilo-views/vistaCategorias.vue'
import { Title } from 'chart.js'


const routes = [
  {
    meta: {
      title: 'Iniciar Sesion'
    },
    path: '/',
    name: 'Iniciar Sesión',
    component: IniciarSesion,
  },
  {
    meta: {
      title: 'InicioCajero'
    },
    path: '/inicio-cajero',
    name: 'inicio_cajero',
    component: InicioCajero,
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'GestonCajero'
    },
    path: '/gestion-cajero',
    name: 'GestonCajero',
    component: GestionCajero,
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'InicioJefeRecepcionista'
    },
    path: '/inicio-jefe-recepcionista',
    name: 'inicio_jefe_recepcionista',
    component: InicioJefeRecepcionista,
    meta: { requiresAuth: true}

  },
  {
    meta: {
      title: 'comprobante-descuento'
    },
    path: '/comprobante-descuento',
    name: 'comprobante_descuento',
    component: ComprobanteDescuentos,
    meta: { requiresAuth: true}

  },
  {
    meta: {
      title: 'avances-efectivo'
    },
    path: '/avances-efectivo',
    name: 'avances_efectivo',
    component: AvancesEfectivo,
    meta: { requiresAuth: true}

  },
  {
    meta: {
      title: 'InformePasajeros'
    },
    path: '/informe-pasajeros',
    name: 'informe_pasajeros',
    component: InformePasajeros,
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'InformacionReserva'
    },
    path: '/informacion-reserva/:id',
    name: 'informacion_reserva',
    component: InformacionReserva,
    meta: { requiresAuth: true }
  },
  {
    meta: {
      title: 'TranspasoParticulares'
    },
    path: '/transpaso-particulares',
    name: 'transpaso_particulares',
    component: TranspasoParticulares,
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'ComprobanteDeposito'
    },
    path: '/comprobante-deposito',
    name: 'Comprob_depositos',
    component: ComprobanteDeposito,
    meta: { requiresAuth: true}
  },
  {
    // No va haber index por el momento, iniciar desde Dashboard.
    meta: {
      title: 'Registrar'
    },
    path: '/registrar',
    name: 'registrar',
    component: Registrar,
  },
  {
    // No va haber index por el momento, iniciar desde Dashboard.
    meta: {
      title: 'Recuperar'
    },
    path: '/recuperar',
    name: 'recuperar',
    component: Recuperar,
  },
  {
    // No va haber index por el momento, iniciar desde Dashboard.
    meta: {
      title: 'Movimiento de pasajeros correspondiente'
    },
    path: '/movimiento-pasajeros-correspondiente',
    name: 'movimiento pasajeros correspondiente',
    component: MovimientoPasajeros,
    meta: { requiresAuth: true}
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Dashboard'
    },
    path: '/dashboard',
    name: 'dashboard',
    component: Home,
    meta: { requiresAuth: true}
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Reservas'
    },
    path: '/reservas',
    name: 'reservas',
    component: Reservas,
    meta: { requiresAuth: true}
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Historial de reservas'
    },
    path: '/historial-reservas',
    name: 'historial de reservas',
    component: HistorialReservas,
    meta: { requiresAuth: true}
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
    component: ComprobanteDescuentos,
    meta: { requiresAuth: true}
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Informe ama de llaves'
    },
    path: '/informe-ama-llaves',
    name: 'informe ama de llaves',
    component: InformeAmaLlaves,
    meta: { requiresAuth: true}
  },
  {
    // Document title tag
    // We combine it with defaultDocumentTitle set in `src/main.js` on router.afterEach hook
    meta: {
      title: 'Gestor de hoteles'
    },
    path: '/gestor-hoteles',
    name: 'gestor de hoteles',
    component: GestorHotel,
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'Profile'
    },
    path: '/profile',
    name: 'profile',
    component: Profile,
    meta: { requiresAuth: true}
  },

  {
    meta: {
      title: 'Huespedes'
    },
    path: '/huespedes',
    name: 'huespedes',
    component: () => import('@/views/alejo-views/HuespedesVue.vue'),
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'VistaHabitaciones'
    },
    path: '/habitaciones',
    name: 'VistaHabitaciones',
    component: VistaHabitaciones,
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'mas_ajustes'
    },
    path: '/mas_ajustes',
    name: 'mas_ajustes',
    component: vistaMasAjustes,
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'Categorias'
    },
    path: '/vistaCategorias',
    name: 'Categorias',
    component: vistaCategorias,
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'Productos'
    },
    path: '/productos',
    name: 'productos',
    component: () => import('@/views/nico-views/ProductoVue.vue'),
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'Hoteles'
    },
    path: '/hoteles',
    name: 'hoteles',
    component: () => import('@/views/felipe-views/HotelVista.vue'),
    meta: { requiresAuth: true}
  },
  {
    path: '/:pathMatch(.*)*',
    name: '404',
    component: Error404,
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'Facturas'
    },
    path: '/facturas',
    name: 'facturas',
    component: () => import('@/views/brayan-views/FacturasView.vue'),
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'Trasunto'
    },
    path: '/trasunto-movimiento-huespedes',
    name: 'Trasunto',
    component: () => import('@/views/nico-views/TrasuntoMovimiento.vue'),
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'Lista Pasajeros'
    },
    path: '/lista-pasajeros',
    name: 'lista pasajeros',
    component: ListaPasajeros,
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'Control de usuarios'
    },
    path: '/control-usuarios',
    name: 'controUsuario',
    component: UsuariosView,
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'Cuenta Huesped'
    },
    path: '/cuenta-huesped',
    name: 'cuenta Huesped',
    component: () => import('@/views/felipe-views/CuentaHuespedView.vue'),
    meta: { requiresAuth: true}
  },
  {
    meta: {
      title: 'Cuenta Huesped'
    },
    path: '/cambiarhotel',
    name: 'cambiar hotel',
    component: () => import('@/views/busta-views/CambiarHotel.vue'),
  },
  {
    meta: {
      title: 'Bibliografia Hotel'
    },
    path: '/bibliografia-hotel',
    name: 'bibliografia Hotel',
    component: () => import('@/views/felipe-views/BibliografiaHotel.vue'),
    meta: { requiresAuth: true}
  },
  {
    meta:{
      title: 'Desarolladores'
    },
    path: '/desarollo',
    name: 'desarollo',
    component: () => import('@/views/arias_views/CreditosView.vue')
  },
  {
    meta:{
      title: 'Historial Cambio Habitacion'
    },
    path: '/historial-cambio-habitacion',
    name: 'Historial Cambio Habitacion',
    component: () => import('@/views/busta-views/HistorialCambioHabitacion.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 }
  }
})

// Verifica la autenticación antes de cada navegación
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore(); // Obtiene la instancia del store de autenticación

  // Si la ruta requiere autenticación y no hay token
  if (to.meta.requiresAuth && !authStore.accessToken) {
    next('/'); // Redirige al login
  } else if (to.path === '/' && authStore.accessToken) {
    next('/dashboard'); // Si está autenticado, redirige al dashboard
  } else {
    next(); // Si todo está bien, permite la navegación
  }
});

export default router
