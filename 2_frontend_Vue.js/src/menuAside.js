import {
  mdiMonitor,
  mdiCalendar,
  mdiTicket,
  mdiFileChart,
  mdiExitRun,
  mdiAccountGroup,
  mdiDoorOpen,
  mdiReceiptTextOutline,
  mdiCityVariantOutline,
  mdiFoodForkDrink,
  mdiBookEducation,
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
    modulo: 'home_jefe_recepcionista'
  },
  {
    to: '/inicio-cajero',
    icon: mdiMonitor,
    label: 'Inicio Cajero',
    modulo: 'home_cajero',
  },
  {
    to: '/comprobante-descuento',
    label: 'Descuentos',
    icon: mdiTicket,
    modulo: 'facturacion'
  },
  // {
  //   to: '/avances-efectivo',
  //   label: 'Anticipo',
  //   icon: mdiTicket,
  //   modulo: 'avances_efectivo'
  // },
  {
    label: 'Reservas',
    icon: mdiCalendar,
    modulo: 'reservas',
    menu: [
      {
        to: '/reservas',
        label: 'Reservas',
        modulo: 'reservas'
      },
      {
        to: '/historial-reservas',
        label: 'His. Reservas',
        modulo: 'reservas'
      },
      // {
      //   to: '/transpaso-particulares',
      //   label: 'Transpaso a particulares',
      //   modulo: 'reservas'
      // },
    ]
  },
  {
    to: '/habitaciones',
    label: 'Habitaciones',
    icon: mdiDoorOpen ,
    modulo: 'habitacion'
  },


  {
    to: '/informe-ama-llaves',
    label: 'Inf. Ama llaves',
    icon: mdiFileChart,
    modulo: 'ama_llaves'
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
    modulo: 'gestor_hoteles_vista'
  },
  {
    to: '/facturas',
    label: 'Facturas',
    icon: mdiReceiptTextOutline ,
    modulo: 'facturacion'
  },
  {
    to: '/control-usuarios',
    label: 'Control Usuarios',
    icon: mdiAccountGroup,
    modulo: 'control_usuarios'
  },

  {
    label: 'Huespedes',
    icon: mdiFileChart,
    modulo: 'huespedes',
    menu: [
      {
        to: '/comprobante-deposito',
        label: 'Comprob. depositos',
        modulo: 'huespedes'
      },
      {
        to: '/informe-pasajeros',
        label: 'Informe pasajeros',
        modulo: 'huespedes'
      },
      // {
      //   to: '/cuenta-huesped',
      //   label: 'Cuentas Huesped',
      //   modulo: 'huespedes'
      // },
      {
        to: '/movimiento-pasajeros-correspondiente',
        label: 'Mv. Pasajero corres',
        modulo: 'huespedes'
      },
      {
        to: '/huespedes',
        label: 'Huespedes',
        modulo: 'huespedes'
      },
    ]
  },
  // {
  //   to: '/bibliografia-hotel',
  //   label: 'Blibliografia',
  //   icon: mdiBookEducation ,
  //   modulo: 'habitacion'
  // },
 

]