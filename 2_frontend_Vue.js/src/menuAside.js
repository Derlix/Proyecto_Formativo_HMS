import {
  mdiMonitor,
  mdiCalendar,
  mdiHistory,
  mdiHumanMaleFemale,
  mdiTicket,
  mdiFileChart,
  mdiViewGridPlus,
  mdiExitRun
} from '@mdi/js'

export default [
  {
    to: '/dashboard',
    icon: mdiMonitor,
    label: 'Dashboard'
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
  {
    to: '/informe-pasajeros',
    label: 'Inf. Pasajero corres',
    icon: mdiHumanMaleFemale
  },
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