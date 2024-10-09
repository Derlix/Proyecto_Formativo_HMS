<template>
  <div
    v-if="visible"
    class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white"
  >
    <div
      class="bg-white dark:bg-gray-800 p-8 sm:p-12 rounded-lg shadow-lg max-w-2xl w-full relative"
    >
      <!-- Botón de cerrar -->
      <button @click="close" class="absolute top-4 right-4 text-gray-600 dark:text-gray-300">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>

      <h2 class="text-2xl mb-6 font-semibold text-gray-900 dark:text-white">
        Movimiento de pasajeros - SALIDA
      </h2>

      <!-- Step 1: Factura List -->
      <div v-if="currentStep === 1">
        <div class="overflow-x-auto bg-gray-50 dark:bg-gray-800 rounded-lg shadow-md p-4 max-h-64">
          <table class="min-w-full bg-white dark:bg-gray-700 border-gray-300">
            <thead>
              <tr class="bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-200">
                <th class="px-4 py-2">Nombre Completo</th>
                <th class="px-4 py-2">Fecha Reserva</th>
                <th class="px-4 py-2">Empresa</th>
                <th class="px-4 py-2">Subtotal</th>
                <th class="px-4 py-2">Total</th>
                <th class="px-4 py-2">Accion</th>

              </tr>
            </thead>
            <tbody>
              <tr
                v-for="factura in facturasPendientes"
                :key="factura.id_facturacion"
                class="hover:bg-gray-100 dark:hover:bg-gray-600"
              >
                <td class="border px-4 py-2 dark:text-white">
                  {{ factura.huesped.nombre_completo }}
                </td>
                <td class="border px-4 py-2 dark:text-white">
                  {{ factura.reserva.fecha_reserva }}
                </td>
                <td class="border px-4 py-2 dark:text-white">{{ factura.reserva.empresa }}</td>
                <td class="border px-4 py-2 dark:text-white">{{ factura.subtotal }}</td>
                <td class="border px-4 py-2 dark:text-white">{{ factura.total }}</td>
                <td class="border px-4 py-2 text-center">
                  <div class="flex justify-center items-center">
                    <input
                      type="radio"
                      :value="factura.id_facturacion"
                      v-model="seleccionarFacturaSeleccionada"
                      @change="seleccionaridFactura(factura.id_facturacion)"
                    />
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- ALERTA DE EXITO -->
        <div
          v-if="showSuccess"
          class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white"
        >
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-sm w-full relative">
            <button
              @click="closeSuccess"
              class="absolute top-2 right-2 text-gray-600 dark:text-gray-300"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">
              Check-Out realizado con éxito
            </h3>
            <p>El Check-Out se ha completado correctamente.</p>
            <button
              @click="closeSuccess"
              class="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg w-full"
            >
              Cerrar
            </button>
          </div>
        </div>

        <!-- ALERTA DE ERROR -->
        <div
          v-if="showError"
          class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white"
        >
          <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-sm w-full relative">
            <button
              @click="closeError"
              class="absolute top-2 right-2 text-gray-600 dark:text-gray-300"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">
              Error al realizar el Check-Out
            </h3>
            <p>Hubo un problema al procesar el Check-Out. Intenta nuevamente.</p>
            <button
              @click="closeError"
              class="mt-4 bg-red-600 text-white px-4 py-2 rounded-lg w-full"
            >
              Cerrar
            </button>
          </div>
        </div>

        <button
          @click="confirmarSalida"
          class="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg"
          :disabled="!seleccionarFacturaSeleccionada"
        >
          Confirmar Salida
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { getAllFacturas, updateFacturaService } from '@/services/brayan_service/FacturacionService'

const props = defineProps({
  visible: {
    type: Boolean,
    required: true
  }
})

const showSuccess = ref(false)
const showError = ref(false)
const currentStep = ref(1)
const seleccionarFacturaSeleccionada = ref(null)
const facturas = ref([])
const facturasPendientes = computed(() => {
  return facturas.value.filter((factura) => factura.estado === 'PENDIENTE')
})

const emit = defineEmits(['close'])

const close = () => {
  currentStep.value = 1
  emit('close')
}

const fetchFacturas = async () => {
  try {
    const response = await getAllFacturas()
    facturas.value = response
  } catch (error) {
    console.error('Error al obtener las reservas:', error)
  }
}

const closeSuccess = () => {
  showSuccess.value = false
  currentStep.value = 1 // Restablecer el paso al cerrar el modal de éxito
  emit('close')
}

const closeError = () => {
  showError.value = false
  currentStep.value = 1 // Restablecer el paso al cerrar el modal de error
  emit('close')
}

const seleccionaridFactura = (id_facturacion) => {
  seleccionarFacturaSeleccionada.value = id_facturacion
  console.log(seleccionarFacturaSeleccionada.value)
}
const confirmarSalida = async () => {
  try {
    const facturaSeleccionada = facturas.value.find(
      (f) => f.id_facturacion === seleccionarFacturaSeleccionada.value
    )
    if (facturaSeleccionada) {
      await updateFacturaService(
        facturaSeleccionada.id_facturacion,
        facturaSeleccionada.subtotal,
        facturaSeleccionada.impuestos,
        facturaSeleccionada.total,
        facturaSeleccionada.total_precio_productos,
        facturaSeleccionada.metodo_pago,
        'PAGADA', // Estado actualizado
        new Date().toISOString() // Fecha de salida actualizada
      )
      showSuccess.value = true
      await fetchFacturas() // Actualiza las facturas sin recargar toda la página

    } else {
      showError.value = true
    }
  } catch (error) {
    console.error('Error al confirmar la salida:', error)
    showError.value = true
  }
}

onMounted(() => {
  fetchFacturas()
})
</script>
