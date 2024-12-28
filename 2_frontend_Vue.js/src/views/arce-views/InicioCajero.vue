<script setup>
import { ref, onMounted } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionMain from '@/components/SectionMain.vue'
import CardBoxWidget from '@/components/CardBoxWidget.vue'
import TitleIconOnly from '@/components/TitleIconOnly.vue'
import CardBox from '@/components/CardBox.vue'


import {
  mdiCash,
  mdiTools,
  mdiFileDocument,
  mdiCurrencyUsd,
  mdiInboxArrowDown,
  mdiBallotOutline
} from '@mdi/js'
import { obtenerTodasHabitacion } from '@/services/habitacionService'
import { getAllFacturas } from '@/services/brayan_service/FacturacionService'
import { obtenerTodasCuentasHuesped } from '@/services/cuentahuespedService'
import ModalRegistrarFondos from '@/components/miguel_compnents/ModalRegistrarFondos.vue'
import { useAuthStore } from '@/stores'
import { createFondo } from '@/services/gestionfondosService'

const authStore = useAuthStore()
const id_usuario = authStore.user.user_id
const activarvisibleModal = ref(false)
const activarvisibleModalFondos = ref(false)
const habitacionesMantenimiento = ref(0)
const depositosEmitidos = ref(0)
const facturasEmitidas = ref(0)
const facturasProceso = ref(0)
const dinero_inicial = ref(0)
const fecha_inicial = ref(new Date().toISOString().substring(0, 10)) // Establecer fecha actual
const dinero_final = ref(0)
const fecha_final = ref(' ') // Inicializa la fecha como un ref

const dineroInicialTemporal = ref(0) // Cambia esto

const openVisibleModal = () => {
  activarvisibleModal.value = true
}

const openVisibleModalFondos = () => {
  activarvisibleModalFondos.value = true
}

const fetchCuentas = async () => {
  try {
    const response = await obtenerTodasCuentasHuesped()
    const cuentas = response.data

    if (Array.isArray(cuentas)) {
      depositosEmitidos.value = cuentas.filter((c) => c.id_reserva.valor_deposito > 0).length
    } else {
      console.error('La respuesta no es un array:', cuentas)
    }
  } catch (error) {
    console.error('Error al obtener cuentas:', error)
  }
}

const fetchFacturas = async () => {
  try {
    const facturas = await getAllFacturas()
    facturasEmitidas.value = facturas.filter((f) => f.estado === 'PAGADA').length
    facturasProceso.value = facturas.filter((f) => f.estado === 'PENDIENTE').length
  } catch (error) {
    console.error('Error al obtener facturas:', error)
  }
}

const fetchHabitaciones = async () => {
  try {
    const habitaciones = await obtenerTodasHabitacion()
    habitacionesMantenimiento.value = habitaciones.filter(
      (h) => h.estado === 'MANTENIMIENTO'
    ).length
  } catch (error) {
    console.error('Error al obtener habitaciones:', error)
  }
}
const registrarFondos = async () => {
  try {
    dineroInicialTemporal.value = dinero_inicial.value // Usa .value para acceder al ref
    console.log('Fondos registrados:', dineroInicialTemporal.value)

    activarvisibleModal.value = false
    dinero_inicial.value = 0;
    fecha_inicial.value = new Date().toISOString().substring(0, 10);
  } catch (error) {
    console.error('Error al registrar fondos:', error)
  }
}

async function cerrarFondos() {
  try {
    console.log(
      'Datos a enviar a createFondo:',
      id_usuario.value,
      dineroInicialTemporal.value,
      dinero_final.value,
      fecha_final.value
    )
    activarvisibleModalFondos.value = false;
      
    const response = await createFondo({
      id_usuario: authStore.user.user_id,
      dinero_inicial: dineroInicialTemporal.value, 
      dinero_final: dinero_final.value,
      fecha_final: fecha_final.value
    })

    
    console.log('Fondos cerrados correctamente:', response)
  } catch (error) {
    console.error('Error al cerrar fondos:', error.response.detail || error)
  }
}

onMounted(() => {
  fetchCuentas()
  fetchFacturas()
  fetchHabitaciones()
})
</script>

<template>
  <ModalRegistrarFondos v-model="activarvisibleModal">
    <h2 class="text-center text-lg font-semibold text-gray-800 dark:text-white">
      Registrar Fondos
    </h2>
    
    <form>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
        <div class="mb-4">
          <label for="dinero_inicial" class="block text-gray-700 font-medium dark:text-white">
            Dinero inicial
          </label>
          <input
            type="number"
            id="dinero_inicial"
            class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="dinero_inicial"
          />
        </div>
        <div class="mb-4">
          <label for="fecha_inicial" class="block text-gray-700 font-medium dark:text-white">
            Fecha Inicial
          </label>
          <input
            type="date"
            id="fecha_inicial"
            class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="fecha_inicial"
          />
        </div>
      </div>
    </form>
  
    <!-- Botones en la misma línea -->
    <div class="flex justify-end space-x-2 mt-4">
      <button
        class="inline-flex justify-center px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
        @click="registrarFondos"
      >
        Registrar Fondos
      </button>
      <button
        class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        @click="activarvisibleModal = false" 
      >
        Cancelar
      </button>
    </div>
  </ModalRegistrarFondos>
  
  

  <!-- MODAL DE CERRAR FONDOS -->
  <ModalRegistrarFondos v-model="activarvisibleModalFondos">
    <h2 class="text-center text-lg font-semibold text-gray-800 dark:text-white">Cerrar Fondos</h2>
    <form>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
        <div class="mb-4">
          <label for="dinero_final" class="block text-gray-700 font-medium dark:text-white"
            >Dinero Final</label
          >
          <input
            type="number"
            id="dinero_final"
            class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="dinero_final"
          />
        </div>
        <div class="mb-4">
          <label for="fecha_final" class="block text-gray-700 font-medium dark:text-white"
            >Fecha Final</label
          >
          <input
            type="datetime-local"
            id="fecha_final"
            class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="fecha_final"
          />
        </div>
      </div>
    </form>
    <!-- Botones en la misma línea -->
    <div class="flex justify-end space-x-2 mt-4">
      <button
        class="inline-flex justify-center px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
        @click="cerrarFondos"
        
      >
        Cerrar Fondos
      </button>
      <button
        class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        @click="activarvisibleModalFondos = false" 
      >
        Cancelar
      </button>
    </div>
  </ModalRegistrarFondos>

  <LayoutAuthenticated>
    <SectionMain>
      <TitleIconOnly :icon="mdiBallotOutline" title="Manejo de caja" />

      <CardBox
        class="mt-6 bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-200 shadow-lg rounded-lg p-4"
      >
        <div class="flex justify-between text-lg font-bold">
          <h1>
            Dinero inicial:
            <span class="text-green-600 dark:text-green-400">{{ dineroInicialTemporal }}</span>
          </h1>
          <h1>
            Dinero final en caja:
            <span class="text-green-600 dark:text-green-400">{{ dinero_final }}</span>
          </h1>
        </div>
      </CardBox>

      <div class="grid grid-cols-1 gap-4 lg:grid-cols-3 mb-6 mt-4 text-gray-100 dark:text-gray-800">
        <CardBoxWidget
          :number="facturasEmitidas"
          label="Pagos recibidos"
          :icon="mdiCurrencyUsd"
          :cardColor="'bg-green-400 dark:bg-green-600'"
        />
        <CardBoxWidget
          :number="depositosEmitidos"
          label="Depósitos recibidos"
          :icon="mdiCash"
          :cardColor="'bg-sky-400 dark:bg-sky-600'"
        />
        <CardBoxWidget
          :number="facturasEmitidas"
          label="Facturas emitidas"
          :icon="mdiFileDocument"
          :cardColor="'bg-blue-700 dark:bg-blue-700'"
        />
      </div>

      <div class="flex gap-4 text-gray-100 dark:text-gray-800">
        <CardBoxWidget
          class="flex-1"
          :number="facturasProceso"
          label="Facturas en proceso"
          :icon="mdiInboxArrowDown"
          :cardColor="'bg-amber-400 dark:bg-amber-600'"
        />
        <CardBoxWidget
          class="flex-1"
          :number="habitacionesMantenimiento"
          label="Habitaciones en mantenimiento"
          :icon="mdiTools"
          :cardColor="'bg-red-400 dark:bg-red-600'"
        />
      </div>

      <div class="text-center w-3/4 mt-8 mx-auto">
        <CardBox class="shadow-lg bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-200 rounded-lg p-6">
          <h2 class="text-center text-2xl mb-5">Registro Fondos Caja de Recepción</h2>
          <div class="grid grid-cols-2 gap-4 mt-3">
            <button
              class="bg-blue-600 hover:bg-blue-800 dark:bg-blue-700 dark:hover:bg-blue-900 text-white h-12 rounded-lg font-bold transition duration-300 ease-in-out shadow-md transform hover:scale-105"
              @click="openVisibleModal()"
            >
              Registrar Fondos
            </button>
            <button
              class="bg-blue-600 hover:bg-blue-800 dark:bg-blue-700 dark:hover:bg-blue-900 text-white h-12 rounded-lg font-bold transition duration-300 ease-in-out shadow-md transform hover:scale-105"
              @click="openVisibleModalFondos()"
            >
              Cerrar Fondos
            </button>
          </div>
          <!-- Contenedor adicional para el botón de administrar fondos -->
          <div class="mt-3 flex justify-center ">
            <router-link
              to="/gestion-cajero"
              class="btn bg-blue-600 hover:bg-blue-800 dark:bg-blue-700 dark:hover:bg-blue-900 text-white h-12 rounded-lg font-bold transition duration-300 ease-in-out shadow-md transform hover:scale-105"
            >
              Administrar fondos
            </router-link>
          </div>
        </CardBox>
      </div>
      
    </SectionMain>
  </LayoutAuthenticated>
</template>
