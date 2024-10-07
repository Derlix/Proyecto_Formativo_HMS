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

      <CardBox class="mt-6">
        <div class="flex justify-between text-lg font-bold">
          <h1>Dinero inicial: $120000</h1>
          <h1>Dinero final en caja: $180000</h1>
        </div>
      </CardBox>

      <div class="grid grid-cols-1 gap-4 lg:grid-cols-3 mb-6 mt-4 text-white">
        <CardBoxWidget
          :number="facturasEmitidas"
          label="Pagos recibidos"
          :icon="mdiCurrencyUsd"
          :cardColor="'bg-green-500'"
        />
        <CardBoxWidget
          :number="depositosEmitidos"
          label="Depósitos recibidos"
          :icon="mdiCash"
          :cardColor="'bg-sky-500'"
        />
        <CardBoxWidget
          :number="facturasEmitidas"
          label="Facturas emitidas"
          :icon="mdiFileDocument"
          :cardColor="'bg-blue-950'"
        />
      </div>

      <div class="flex gap-4 text-white">
        <CardBoxWidget
          class="flex-1"
          :number="facturasProceso"
          label="Facturas en proceso recibidos"
          :icon="mdiInboxArrowDown"
          :cardColor="'bg-amber-500'"
        />
        <CardBoxWidget
          class="flex-1"
          :number="habitacionesMantenimiento"
          label="Habitaciones en mantenimiento"
          :icon="mdiTools"
          :cardColor="'bg-red-500'"
        />
      </div>

      <div class="text-center w-1/2 mt-8">
        <CardBox class="shadow-md">
          <SectionTitle>Registro Fondos Caja de Recepción</SectionTitle>
          <div class="grid grid-cols-2 gap-4">
            <button 
            @click="showModalRegistrarFondos = true"
            class="bg-blue-600 h-12 rounded-lg font-bold hover:bg-blue-900 text-white">
              Registrar Fondos
            </button>
            <ModalRegistrarFondos :visible="showModalRegistrarFondos" @cerrar="showModalRegistrarFondos = false" />
            <button class="bg-blue-600 h-12 rounded-lg font-bold hover:bg-blue-900 text-white">
              Ver todos los registros
            </button>
            <button class="bg-blue-600 h-12 rounded-lg font-bold hover:bg-blue-900 text-white">
              Modificar Registro
            </button>
            <button class="bg-blue-600 h-12 rounded-lg font-bold hover:bg-blue-900 text-white">
              Eliminar Registro
            </button>
          </div>
        </CardBox>
      </div>

      <div class="flex justify-end mt-5">
        <button class="bg-green-500 text-white py-2 px-4 rounded m-1">¿Necesitas ayuda?</button>
      </div>
    </SectionMain>
  </LayoutAuthenticated>
</template>
