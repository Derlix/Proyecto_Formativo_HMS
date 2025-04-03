<script setup>
import { ref, reactive, onMounted } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionMain from '@/components/SectionMain.vue';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import CardBoxWidget from '@/components/CardBoxWidget.vue'
import SectionTitle from '@/components/SectionTitle.vue';
import ModalRegistrarEntrada from '@/components/ModalRegistrarEntrada.vue'
import ModalRegistrarSalida from '@/components/ModalRegistrarSalida.vue'
import { mdiBallotOutline, mdiBroom, mdiBed, mdiFileDocument, mdiBedEmpty, mdiWrenchClock, mdiBedClock, mdiCashLock, mdiCashCheck } from '@mdi/js';
import { obtenerTodasHabitaciones } from '@/services/habitacionService';
import { getAllFacturas } from '@/services/brayan_service/FacturacionService'
import { obtenerTodasCuentasHuesped } from '@/services/cuentahuespedService'

const showModal = ref(false)
const showModalSalidas = ref(false)

const depositosEmitidos = ref(0)
const facturasEmitidas = ref(0)
const facturasProceso = ref(0)
// const DineroInicial = ref(0)
// const DineroFinal = ref(0)

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

const habitaciones = reactive({
    totales: 0,
    disponibles: 0,
    ocupadas: 0,
    limpieza: 0,
    mantenimiento: 0,
});

const fetchHabitaciones = async () => {
    try {
        const response = await obtenerTodasHabitaciones();
        const data = response.data;
        
        habitaciones.totales = data.length;
        habitaciones.disponibles = data.filter(habitacion => habitacion.estado === 'ACTIVO').length;
        habitaciones.ocupadas = data.filter(habitacion => habitacion.estado === 'INACTIVO').length;
        habitaciones.limpieza = data.filter(habitacion => habitacion.estado === 'OPERACION').length;
        habitaciones.mantenimiento = data.filter(habitacion => habitacion.estado === 'MANTENIMIENTO').length;
    } catch (error) {
        console.error('Error al cargar habitaciones:', error);
    }
};

onMounted(() => {
    fetchCuentas()
    fetchFacturas()
    fetchHabitaciones();
});

</script>

<template>
    <LayoutAuthenticated>
        <SectionMain>
            <TitleIconOnly :icon="mdiBallotOutline" title="Jefe Recepcionista Home" />
            <SectionTitle>Estado de habitaciones</SectionTitle>

            <div class="grid grid-cols-1 gap-6 lg:grid-cols-3 mt-4 text-white">
                <CardBoxWidget :number="habitaciones.totales" label="Habitaciones totales" :icon="mdiBed" :cardColor="'bg-sky-500'" />
                <CardBoxWidget :number="habitaciones.disponibles" label="Habitaciones disponibles" :icon="mdiBedEmpty" :cardColor="'bg-green-500'" />
                <CardBoxWidget :number="habitaciones.ocupadas" label="Habitaciones ocupadas" :icon="mdiBedClock" :cardColor="'bg-pink-600'" />
            </div>

            <div class="grid grid-cols-1 gap-6 lg:grid-cols-2 mb-6 mt-4 text-white">
                <CardBoxWidget :number="habitaciones.limpieza" label="Habitaciones en limpieza" :icon="mdiBroom" :cardColor="'bg-amber-500'" />
                <CardBoxWidget :number="habitaciones.mantenimiento" label="Habitaciones en mantenimiento" :icon="mdiWrenchClock" :cardColor="'bg-rose-700'" />
            </div>

            <CardBox class="shadow-md">
                <SectionTitle>Check-In - Check-Out</SectionTitle>
                <div class="grid grid-cols-1 gap-4 lg:grid-cols-2">
                    <button @click="showModal = true" class="bg-blue-600 h-12 rounded-lg my-6 font-bold hover:bg-blue-900 text-white">Registrar Check-In</button>
                    <button @click="showModalSalidas = true" class="bg-blue-600 h-12 rounded-lg my-6 font-bold hover:bg-blue-900 text-white">Registrar Check-Out
                    </button>
                    <ModalRegistrarEntrada :visible="showModal" @close="showModal = false" />
                    <ModalRegistrarSalida :visible="showModalSalidas" @close="showModalSalidas = false"/>
                </div>
            </CardBox>

            <SectionTitle first>Transacciones</SectionTitle>
            <div class="grid grid-cols-1 gap-4 lg:grid-cols-2 mt-4 text-white">
                <CardBoxWidget :number="facturasEmitidas" label="Pagos recibidos" :icon="mdiBed" :cardColor="'bg-emerald-500'" />
                <CardBoxWidget :number="depositosEmitidos" label="Depositos recibidos" :icon="mdiBedEmpty" :cardColor="'bg-emerald-500'" />
            </div>

            <SectionTitle first>Facturación</SectionTitle>
            <div class="grid grid-cols-1 gap-4 lg:grid-cols-2 mt-4 text-white">
                <CardBoxWidget :number="facturasEmitidas" label="Facturas emitidas" :icon="mdiFileDocument" :cardColor="'bg-neutral-500'" />
                <CardBoxWidget :number="facturasProceso" label="Facturas en proceso" :icon="mdiFileDocument" :cardColor="'bg-neutral-500'" />
            </div>

            <!-- <SectionTitle first>Caja</SectionTitle>
            <div class="grid grid-cols-1 gap-4 lg:grid-cols-2 mt-4 text-white">
                <CardBoxWidget :number="50" label="Dinero inicial" :icon="mdiCashCheck" :cardColor="'bg-sky-500'" />
                <CardBoxWidget :number="50" label="Dinero final" :icon="mdiCashLock" :cardColor="'bg-sky-500'" />
            </div> -->
        </SectionMain>
    </LayoutAuthenticated>
</template>
