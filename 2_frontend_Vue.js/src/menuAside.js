

import {
  mdiMonitor,
  mdiCalendar,
  mdiHistory,
  mdiHumanMaleFemale,
  mdiTicket,
  mdiFileChart,
  mdiViewGridPlus,
  mdiExitRun,
  mdiReproduction,
  mdiAccountGroup,
  mdiAccountSupervisorCircle,
  mdiDoorOpen,
  mdiCityVariantOutline,
  mdiInvoice,
  mdiInvoiceCheckOutline,
  mdiFoodForkDrink,
  mdiCardAccountDetails 
} from '@mdi/js'

export default [
  {
    to: '/dashboard',
    icon: mdiMonitor,
    label: 'Dashboard',
    modulo: 'home_recepcionista' // Asumiendo que el dashboard es para usuarios
  },
  {
    to: '/inicio-jefe-recepcionista',
    icon: mdiMonitor,
    label: 'Jefe recepcion',
    modulo: 'home_recepcionista'
  },
  {
    to: '/inicio-cajero',
    icon: mdiMonitor,
    label: 'Inicio Cajero',
    modulo: 'home_cajero',
  },
  {
    to: '/informe-pasajeros',
    icon: mdiMonitor,
    label: 'informe pasajeros',
    modulo: 'huespedes'
  },
  {
    to: '/informacion-reserva',
    icon: mdiMonitor,
    label: 'Info reserva',
    modulo: 'reservas'
  },
  {
    to: '/tarjeta-reserva',
    icon: mdiMonitor,
    label: 'tarjeta reserva',
    modulo: 'reservas'
  },
  {
    to: '/transpaso-particulares',
    icon: mdiMonitor,
    label: 'Transpaso a particulares',
    modulo: 'reservas'
  },
  {
    to: '/reservas',
    label: 'Reservas',
    icon: mdiCalendar,
    modulo: 'reservas'
  },
  {
    to: '/historial-reservas',
    label: 'His. Reservas',
    icon: mdiHistory,
    modulo: 'reservas'
  },
  {
    to: '/movimiento-pasajeros-correspondiente',
    label: 'Mv. Pasajero corres',
    icon: mdiHumanMaleFemale,
    modulo: 'huespedes'
  },
  {
    to: '/huespedes',
    label: 'Huespedes',
    icon: mdiAccountSupervisorCircle,
    modulo: 'huespedes'
  },{
    to: '/habitaciones',
    label: 'Habitaciones',
    icon: mdiDoorOpen ,
    modulo: 'habitacion'
  },
  /* {
    to: '/comprobante-descuento',
    label: 'Com. Descuento',
    icon: mdiTicket,
    modulo: 'facturacion'
  }, */
  {
    to: '/informe-ama-llaves',
    label: 'Inf. Ama llaves',
    icon: mdiFileChart,
    modulo: 'habitacion'
  },
  /* {
    to: '/gestor-hoteles',
    label: 'Gestor de hoteles',
    icon: mdiViewGridPlus,
    modulo: 'hoteles'
  }, */
  {
    to: '/checkOut',
    label: 'CheckOut',
    icon: mdiInvoiceCheckOutline ,
    modulo: 'check_in'
  },
  {
    to: '/productos',
    label: 'Productos',
    icon: mdiFoodForkDrink ,
    modulo: 'productos'
  },
  {
    to: '/hoteles',
    label: 'Hoteles',
    icon: mdiCityVariantOutline ,
    modulo: 'hoteles'
  },
  {
    to: '/facturas',
    label: 'Facturas',
    icon: mdiInvoice ,
    modulo: 'facturacion'
  },
  /* {
    to: '/lista-pasajeros',
    label: 'Lista pasajeros',
    icon: mdiReproduction,
    modulo: 'huespedes'
  }, */{
    to: '/control-usuarios',
    label: 'Control Usuarios',
    icon: mdiAccountGroup,
    modulo: 'usuarios'
  }

]