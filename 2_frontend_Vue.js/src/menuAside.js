import {
  mdiMonitor,
  mdiCalendar,
  mdiHistory,
  mdiHumanMaleFemale,
  mdiTicket,
  mdiFileChart,
  mdiViewGridPlus,
  mdiExitRun,
  mdiReproduction
} from '@mdi/js'

export default [
  {
    to: '/dashboard',
    icon: mdiMonitor,
    label: 'Dashboard'
  },
  {
    to: '/inicio-cajero',
    icon: mdiMonitor,
    label: 'Inicio Cajero'
  },
  {
    to: '/informe-pasajeros',
    icon: mdiMonitor,
    label: 'informe pasajeros'
  },
  {
    to: '/informacion-reserva',
    icon: mdiMonitor,
    label: 'Info reserva'
  },
  {
    to: '/tarjeta-reserva',
    icon: mdiMonitor,
    label: 'tarjeta reserva'
  },
  {
    to: '/transpaso-particulares',
    icon: mdiMonitor,
    label: 'Transpaso a particulares'
  },
  {
    to: '/reservas',
    label: 'Reservas',
    icon: mdiCalendar
  },
  {
    to: '/historial-reservas',
    label: 'His. Reservas',
    icon: mdiHistory
  },
  // movimiento-pasajeros-correspondiente
  {
    to: '/movimiento-pasajeros-correspondiente',
    label: 'Mv. Pasajero corres',
    icon: mdiHumanMaleFemale
  },
  // {
  //   to: '/informe-pasajeros',
  //   label: 'Inf. Pasajero corres',
  //   icon: mdiHumanMaleFemale
  // },
  {
    to: '/comprobante-descuento',
    label: 'Com. Descuento',
    icon: mdiTicket
  },
  {
    to: '/informe-ama-llaves',
    label: 'Inf. Ama llaves',
    icon: mdiFileChart
  },
  {
    to: '/gestor-hoteles',
    label: 'Gestor de hoteles',
    icon: mdiViewGridPlus
  },
  {
    to: '/checkOut',
    label: 'CheckOut',
    icon: mdiExitRun
  },
  {
    to: '/productos',
    label: 'Productos',
    icon: mdiReproduction
  },
  {
    to: '/hoteles',
    label: 'Hoteles',
    icon: mdiMonitor,
  }
  ,
  {
    to: '/facturas',
    label: 'Facturas',
    icon: mdiReproduction
  }
  

  // {
  //   to: '/tables',
  //   label: 'Tables',
  //   icon: mdiTable
  // },
  // {
  //   to: '/forms',
  //   label: 'Forms',
  //   icon: mdiSquareEditOutline
  // },
  // {
  //   to: '/ui',
  //   label: 'UI',
  //   icon: mdiTelevisionGuide
  // },
  // {
  //   to: '/responsive',
  //   label: 'Responsive',
  //   icon: mdiResponsive
  // },
  // {
  //   to: '/',
  //   label: 'Styles',
  //   icon: mdiPalette
  // },
  // {
  //   to: '/profile',
  //   label: 'Profile',
  //   icon: mdiAccountCircle
  // },
  // {
  //   to: '/login',
  //   label: 'Login',
  //   icon: mdiLock
  // },
  // {
  //   to: '/error',
  //   label: 'Error',
  //   icon: mdiAlertCircle
  // },
  // {
  //   label: 'Dropdown',
  //   icon: mdiViewList,
  //   menu: [
  //     {
  //       label: 'Item One'
  //     },
  //     {
  //       label: 'Item Two'
  //     }
  //   ]
  // },
  // {
  //   href: 'https://github.com/justboil/admin-one-vue-tailwind',
  //   label: 'GitHub',
  //   icon: mdiGithub,
  //   target: '_blank'
  // },
  // {
  //   href: 'https://github.com/justboil/admin-one-react-tailwind',
  //   label: 'React version',
  //   icon: mdiReact,
  //   target: '_blank'
  // }
]
