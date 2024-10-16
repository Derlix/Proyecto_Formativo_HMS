<script setup>
import { ref, onMounted } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionMain from '@/components/SectionMain.vue'
import CardBoxWidget from '@/components/CardBoxWidget.vue'
import TitleIconOnly from '@/components/TitleIconOnly.vue'
import CardBox from '@/components/CardBox.vue'
import SectionTitle from '@/components/SectionTitle.vue'
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


const showModalRegistrarFondos = ref(false)
const habitacionesMantenimiento = ref(0)
const depositosEmitidos = ref(0)
const facturasEmitidas = ref(0)
const facturasProceso = ref(0)

const fetchCuentas = async () => {
  try {
    const response = await obtenerTodasCuentasHuesped()
    const cuentas = response.data 
    
    if (Array.isArray(cuentas)) {
      depositosEmitidos.value = cuentas.filter(
        (c) => c.id_reserva.valor_deposito > 0
      ).length
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
    facturasEmitidas.value = facturas.filter(
      (f) => f.estado === 'PAGADA'
    ).length
    facturasProceso.value = facturas.filter(
      (f) => f.estado === 'PENDIENTE'
    ).length
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

onMounted(() => {
  fetchCuentas()
  fetchFacturas()
  fetchHabitaciones()
})
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <TitleIconOnly :icon="mdiBallotOutline" title="Manejo de caja" />

      <CardBox class="mt-6 bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-200 shadow-lg rounded-lg p-4">
        <div class="flex justify-between text-lg font-bold">
          <h1>Dinero inicial: <span class="text-green-600 dark:text-green-400">$120000</span></h1>
          <h1>Dinero final en caja: <span class="text-green-600 dark:text-green-400">$180000</span></h1>
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
        <CardBox class="shadow-lg bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-200 rounded-lg p-6 ">
          <h2 class="text-center text-2xl mb-5">Registro Fondos Caja de Recepción</h2>
          <div class="grid grid-cols-2 gap-4 mt-3">
            <button 
              class="bg-blue-600 hover:bg-blue-800 dark:bg-blue-700 dark:hover:bg-blue-900 text-white h-12 rounded-lg font-bold transition duration-300 ease-in-out shadow-md transform hover:scale-105">
              Registrar Fondos
            </button>
            <button class="bg-blue-600 hover:bg-blue-800 dark:bg-blue-700 dark:hover:bg-blue-900 text-white h-12 rounded-lg font-bold transition duration-300 ease-in-out shadow-md transform hover:scale-105">
              Ver todos los registros
            </button>
            <button class="bg-blue-600 hover:bg-blue-800 dark:bg-blue-700 dark:hover:bg-blue-900 text-white h-12 rounded-lg font-bold transition duration-300 ease-in-out shadow-md transform hover:scale-105">
              Modificar Registro
            </button>
            <button class="bg-red-600 hover:bg-red-900 dark:bg-red-700 dark:hover:bg-red-900 text-white h-12 rounded-lg font-bold transition duration-300 ease-in-out shadow-md transform hover:scale-105">
              Eliminar Registro
            </button>
          </div>
        </CardBox>
      </div>
      
      
      
    </SectionMain>
  </LayoutAuthenticated>
</template>

