import {
  mdiMenu,
  mdiClockOutline,
  mdiCloud,
  mdiCrop,
  mdiCogOutline,
  mdiEmail,
  mdiLogout,
  mdiThemeLightDark,
  mdiGithub,
  mdiReact,
  mdiBell
} from '@mdi/js'

export default [

  // {
  //   icon: mdiBell,
  //   label: 'Notificaciones',
  //   isDesktopNoLabel: true,
  // },
  {
    isCurrentUser: true,
    label: 'Mi perfil',
    to: '/profile'
  },
  {
    icon: mdiThemeLightDark,
    label: 'Light/Dark',
    isDesktopNoLabel: true,
    isToggleLightDark: true
  },
  {
    icon: mdiLogout,
    label: 'Cerrar sesión',
    isDesktopNoLabel: true,
    isLogout: true
  }


  // {
  //   icon: mdiMenu,
  //   label: 'Sample menu',
  //   menu: [
  //     {
  //       icon: mdiClockOutline,
  //       label: 'Item One'
  //     },
  //     {
  //       icon: mdiCloud,
  //       label: 'Item Two'
  //     },
  //     {
  //       isDivider: true
  //     },
  //     {
  //       icon: mdiCrop,
  //       label: 'Item Last'
  //     }
  //   ]
  // },
  // {
  
]
