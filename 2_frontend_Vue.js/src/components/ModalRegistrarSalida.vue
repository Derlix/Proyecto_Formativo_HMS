<script setup>
import { ref } from 'vue';
import { getAllFacturas, updateFacturaService } from '@/services/brayan_service/FacturacionService';

const props = defineProps({
  visible: {
    type: Boolean,
    required: true
  }
});

const showSuccess = ref(false);
const showError = ref(false);
const documento = ref('');
const nombre = ref('');
const mediollegada = ref('');
const situacionLlegada = ref('');
const equipaje = ref('');
const facturaEncontrada = ref(false);
const factura = ref(null); // Variable para guardar la factura encontrada

const emit = defineEmits(['close']);

const closeSuccess = () => {
  showSuccess.value = false;
  emit('close'); 
};

const closeError = () => {
  showError.value = false;
  emit('close'); 
};

const buscarCheckin = async () => {
  try {
    const facturasList = await getAllFacturas(); 
    console.log('Datos de la API:', facturasList); 
    if (facturasList && facturasList.length) {
      const facturaBuscada = facturasList.find(c => c.huesped.numero_documento === documento.value);

      if (facturaBuscada) {
        factura.value = facturaBuscada; // Guardar la factura encontrada
        facturaEncontrada.value = true;
        nombre.value = factura.value.huesped.nombre_completo;
        mediollegada.value = factura.value.check_in.medio_llegada;
        situacionLlegada.value = factura.value.check_in.llegada_situacion;
        equipaje.value = factura.value.check_in.equipaje;
      } else {
        resetFields();
      }
    } else {
      resetFields();
    }
  } catch (error) {
    console.error('Error al buscar la factura:', error);
    resetFields();
  }
};

const confirmarSalida = async () => {
  try {
    if (factura.value) {
      // Desestructurar la factura encontrada
      const {
        id_facturacion,
        subtotal,
        impuestos,
        total,
        total_precio_productos,
        metodo_pago,
      } = factura.value;

      const fecha_salida = new Date().toISOString();

      await updateFacturaService(
        id_facturacion,
        subtotal,
        impuestos,
        total,
        total_precio_productos,
        metodo_pago,
        'PAGADA', // Estado actualizado
        fecha_salida // Fecha de salida
      );

      showSuccess.value = true;
    } else {
      console.error('No se ha encontrado la factura para actualizar');
      showError.value = true;
    }
  } catch (error) {
    console.error('Error al actualizar la factura:', error.response ? error.response.data : error.message);
    showError.value = true;
  }
};

const resetFields = () => {
  facturaEncontrada.value = false;
  factura.value = null; // Reinicia la referencia a la factura
  nombre.value = '';
  mediollegada.value = '';
  situacionLlegada.value = '';
  equipaje.value = '';
};

const close = () => {
  emit('close');
};
</script>
<template>
  <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white">
    <div class="bg-white dark:bg-gray-800 p-8 sm:p-12 rounded-lg shadow-lg max-w-2xl w-full relative">
      <button @click="close" class="absolute top-4 right-4 text-gray-600 dark:text-gray-300">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <h2 class="text-2xl mb-6 font-semibold text-gray-900 dark:text-white">Movimiento de pasajeros - SALIDA</h2>

      <div class="grid grid-cols-2 gap-4 mb-5">
        <div>
          <label for="documento" class="block mb-1 text-sm font-medium">Documento</label>
          <input
            type="text"
            id="documento"
            v-model="documento"
            @blur="buscarCheckin"
            class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
          >
        </div>
        <div>
          <label for="nombre" class="block mb-1 text-sm font-medium">Nombre Completo</label>
          <input
            type="text"
            id="nombre"
            v-model="nombre"
            disabled
            class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
          >
        </div>
        <div>
          <label for="llegada" class="block mb-1 text-sm font-medium">Situación de llegada</label>
          <input
            type="text"
            id="llegada"
            v-model="situacionLlegada"
            disabled
            class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
          >
        </div>
        <div>
          <label for="mediollegada" class="block mb-1 text-sm font-medium">Medio de llegada</label>
          <input
            type="text"
            id="mediollegada"
            v-model="mediollegada"
            disabled
            class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
          >
        </div>
        <div>
          <label for="equipaje" class="block mb-1 text-sm font-medium">Equipaje</label>
          <input
            type="text"
            id="equipaje"
            v-model="equipaje"
            disabled
            class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
          >
        </div>
      </div>

      <button @click="confirmarSalida" class="bg-blue-600 text-white px-6 py-3 rounded w-full">
        Confirmar
      </button>
    </div>
  </div>

  <div v-if="showSuccess" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white">
    <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-sm w-full relative">
      <button @click="closeSuccess" class="absolute top-2 right-2 text-gray-600 dark:text-gray-300">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
      <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">Check-Out realizado con éxito</h3>
      <p>El Check-Out se ha completado correctamente.</p>
      <button @click="closeSuccess" class="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg w-full">
        Cerrar
      </button>
    </div>
  </div>

  <div v-if="showError" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white">
    <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-sm w-full relative">
      <button @click="closeError" class="absolute top-2 right-2 text-gray-600 dark:text-gray-300">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
      <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">Error al realizar el Check-Out</h3>
      <p>Hubo un problema al procesar el Check-Out. Intenta nuevamente.</p>
      <button @click="closeError" class="mt-4 bg-red-600 text-white px-4 py-2 rounded-lg w-full">
        Cerrar
      </button>
    </div>
  </div>
</template>
