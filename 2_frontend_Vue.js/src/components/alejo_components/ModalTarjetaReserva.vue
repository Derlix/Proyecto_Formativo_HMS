
<template>
  <div class="content">
    <div v-if="isVisible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white ">
      <div class="bg-white dark:bg-gray-800 p-8 sm:p-12 rounded-lg shadow-lg max-w-2xl w-full relative max-h-[85vh]">
        <!-- Botón de cerrar -->
        <button class="absolute top-4 right-4 text-gray-600 dark:text-gray-300" @click="closeModal">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
        
        <SectionTitleLineWithButton :icon="mdiBallotOutline" title="Tarjeta Reserva" >
        </SectionTitleLineWithButton>
        

       <div class="max-h-[50vh] overflow-y-auto p-4 overflow-x-hidden">
        <div class="grid grid-cols-2 gap-4 mb-5">
          <div class="col-span-2 md:col-span-1">
            <label for="documento" class="block mb-1 text-sm font-medium">Documento</label>
            <input
              type="text"
              id="documento"
              v-model="documento"
              @blur="buscarReserva"
              class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
            >
          </div>
          <BaseDivider />

          <div class="col-span-2 md:col-span-1">
            <label for="nombre_completo" class="block mb-1 text-sm font-medium">Nombre Completo</label>
            <input
              type="text"
              id="nombre_completo"
              v-model="nombre_completo"
              :disabled="!reservaEncontrada"
              class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
            >
          </div>

          <!-- Segunda columna (Más información del huésped) -->
          <div class="col-span-2 md:col-span-1">
            <label for="email" class="block mb-1 text-sm font-medium">Email</label>
            <input
              type="text"
              id="email"
              v-model="email"
              :disabled="!reservaEncontrada"
              class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
            >
          </div>

          <div class="col-span-2 md:col-span-1">
            <label for="num_personas" class="block mb-1 text-sm font-medium">Número de personas</label>
            <input
              type="text"
              id="num_personas"
              v-model="num_personas"
              :disabled="!reservaEncontrada"
              class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
            >
          </div>

          <div class="col-span-2 md:col-span-1">
            <label for="empresa" class="block mb-1 text-sm font-medium">Empresa</label>
            <input
              type="text"
              id="empresa"
              v-model="empresa"
              :disabled="!reservaEncontrada"
              class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
            >
          </div>

   
          <BaseDivider />

          <!-- Fechas -->
          <div class="col-span-2">
            <h4 class="mb-2 font-semibold">Fechas</h4>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label for="fecha_entrada" class="block mb-1 text-sm font-medium">Fecha Entrada</label>
                <input
                  type="text"
                  id="fecha_entrada"
                  v-model="fecha_entrada"
                  :disabled="!reservaEncontrada"
                  class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
                >
              </div>
              <div>
                <label for="fecha_salida_propuesta" class="block mb-1 text-sm font-medium">Fecha Salida Propuesta</label>
                <input
                  type="text"
                  id="fecha_salida_propuesta"
                  v-model="fecha_salida_propuesta"
                  :disabled="!reservaEncontrada"
                  class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
                >
              </div>
            </div>
          </div>


          <BaseDivider />

          <!-- Reservada por -->
          <div class="col-span-2">
            <h4 class="mb-2 font-semibold">Reservada por</h4>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label for="nombreFuncionario" class="block mb-1 text-sm font-medium">Funcionario</label>
                <input
                  type="text"
                  id="nombreFuncionario"
                  v-model="nombreFuncionario"
                  :disabled="!reservaEncontrada"
                  class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
                >
              </div>
              <div>
                <label for="medioPago" class="block mb-1 text-sm font-medium">Medio de Pago</label>
                <input
                  type="text"
                  id="medioPago"
                  v-model="medioPago"
                  :disabled="!reservaEncontrada"
                  class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
                >
              </div>
              <div>
                <label for="fecha_reserva" class="block mb-1 text-sm font-medium">Fecha Reserva</label>
                <input
                  type="text"
                  id="fecha_reserva"
                  v-model="fecha_reserva"
                  :disabled="!reservaEncontrada"
                  class="w-full rounded-lg p-2 bg-gray-100 dark:bg-gray-700 dark:text-white border border-gray-300 dark:border-gray-600"
                >
              </div>
            </div>
          </div>
        </div>
      </div>
        <div class="sticky ">
          <BaseButtons>
            <BaseButton type="submit" color="info" label="PDF" @click="generarPDF()"/>
            <BaseButton type="reset" color="info" outline label="Cancelar"  @click="closeModal()" />
          </BaseButtons>
 
        </div>
          
      </div>
    </div>
  </div>
</template> 

<script setup>
import { ref, defineProps, defineEmits } from 'vue'
import { obtenertodasReservasHabitacion } from '@/services/reservaHabitacionService'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import { mdiBallotOutline } from '@mdi/js'
import BaseDivider from '@/components/BaseDivider.vue'

// Definición de las referencias
const nombre_completo = ref('')
const documento = ref('')
const email = ref('')
const num_personas = ref(0)
const empresa = ref('') 
const fecha_entrada = ref('')
const fecha_salida_propuesta = ref('')
const reservaEncontrada = ref(false)
const idReserva = ref(null) 
const nombreFuncionario = ref('')
const medioPago = ref('')
const fecha_reserva = ref('')
import { jsPDF } from 'jspdf' // Importa jsPDF

// Props para el modal
defineProps({
  isVisible: {
    type: Boolean,
    required: true
  },
  title: {
    type: String,
    default: 'Modal Title'
  }
})

// Emitir evento para cerrar el modal
const emit = defineEmits(['close'])

// Función para resetear los inputs
const resetInputs = () => {
  documento.value = ''
  nombre_completo.value = ''
  email.value = ''
  num_personas.value = 0
  empresa.value = ''
  fecha_entrada.value = ''
  fecha_salida_propuesta.value = ''
  nombreFuncionario.value = ''
  medioPago.value = 'EFECTIVO'
  fecha_reserva.value = ''
  reservaEncontrada.value = false // Si necesitas restablecer también este estado
}

// Función para cerrar el modal
const closeModal = () => {
  emit('close')
  resetInputs() // Llama a resetInputs sin this
}

// Función para buscar reserva
const buscarReserva = async () => {
  try {
    const response = await obtenertodasReservasHabitacion()
    if (response.data && response.data.length) {
      console.log(response);
      const reservaHabitacion = response.data.find(r => r.huesped.numero_documento === documento.value);
      const numPersonas = (reservaHabitacion.num_adultos || 0) + (reservaHabitacion.num_niños || 0);
      if (reservaHabitacion) {
        reservaEncontrada.value = true;
        nombre_completo.value = reservaHabitacion.huesped.nombre_completo || 'No disponible';
        documento.value = reservaHabitacion.huesped.numero_documento || 'No disponible';
        email.value = reservaHabitacion.huesped.email || 'No disponible';
        num_personas.value = numPersonas;
        empresa.value = reservaHabitacion.reserva.empresa || 'No disponible';
        fecha_entrada.value = reservaHabitacion.fecha_entrada || 'No disponible';
        fecha_salida_propuesta.value = reservaHabitacion.fecha_salida_propuesta || 'No disponible';
        nombreFuncionario.value = reservaHabitacion.reserva.usuario?.nombre_completo || 'No disponible';
        medioPago.value = reservaHabitacion.reserva.forma_pago || 'No disponible';
        fecha_reserva.value = reservaHabitacion.reserva.fecha_reserva || 'No disponible';
        idReserva.value = reservaHabitacion.id_reserva || 'No disponible';
      } else {
        resetFields()
      }
    } else {
      resetFields()
    }
  } catch (error) {
    console.error('Error al buscar la reserva:', error)
    resetFields()
  }
}

// Función para resetear los campos
const resetFields = () => {
  reservaEncontrada.value = false
  nombre_completo.value = ''
  documento.value = ''
  idReserva.value = null
  email.value = ''
  num_personas.value = 0
  empresa.value = ''
  fecha_entrada.value = ''
  fecha_salida_propuesta.value = ''
  nombreFuncionario.value = ''
  medioPago.value = ''
  fecha_reserva.value = ''
}

const generarPDF = () => {
  const doc = new jsPDF(); // Crea una nueva instancia de jsPDF

  // Agrega el título
  doc.setFontSize(20);
  doc.setFont('helvetica', 'bold');
  doc.text('TARJETA DE RESERVA', 14, 20); // Título
  doc.text('(HMS)', 45, 30); 

  doc.setFont('helvetica', 'normal')
  doc.setFontSize(16);

  // Configuración de la tabla
  const startY = 30; // Posición inicial Y
  const margin = 14; // Margen
  const lineHeight = 12; // Altura de línea
  const tableWidth = 180; // Ancho de la tabla
  const columnWidth = tableWidth / 2; // Ancho de cada columna

  // Datos de la reserva
  const data = [
    { field: 'Documento', value: documento.value },
    { field: 'Nombre Completo', value: nombre_completo.value },
    { field: 'Email', value: email.value },
    { field: 'Número de Personas', value: num_personas.value },
    { field: 'Fecha Entrada', value: fecha_entrada.value },
    { field: 'Fecha Salida Propuesta', value: fecha_salida_propuesta.value },
    { field: 'Empresa', value: empresa.value },
    { field: 'Medio de Pago', value: medioPago.value },
    { field: 'Reservada por', value: nombreFuncionario.value },
    { field: 'Fecha Reserva', value: fecha_reserva.value },
  ];

  // Posición Y inicial para los datos
  let currentY = startY + lineHeight * 2; // Espacio extra inicial

  // Agrega cada fila de datos
  data.forEach((item, index) => {
    const x = margin + (index % 2) * columnWidth; // Alternar entre dos columnas

    // Dibuja el recuadro para el campo
    doc.rect(x, currentY - lineHeight, columnWidth, lineHeight + 6);

    // Escribe el campo y su valor
    doc.text(item.field, x + 4, currentY); // Campo

    // Ajusta la posición Y para el valor (debajo del campo)
    const valueY = currentY + lineHeight + 2; // Espacio adicional entre campo y valor
    const valueToPrint = item.value !== undefined && item.value !== null ? String(item.value) : 'N/A';
    doc.text(valueToPrint, x + 4, valueY); // Valor

    // Cambia a la siguiente línea cada dos columnas
    if (index % 2 === 1) {
      currentY += lineHeight * 2 + 8; // Aumenta la altura entre filas (considerando espacio para el campo y valor)
    }
  });

  const imagePath = '/src/assets/img/sena-agro.png'; // Ruta relativa de tu imagen en la carpeta 'public'
  
  // Cargar la imagen y luego agregarla al PDF
  const img = new Image();
  img.src = imagePath;
  
  img.onload = function () {
    // Usamos el canvas para convertir la imagen a Base64
    const canvas = document.createElement('canvas');
    canvas.width = img.width;
    canvas.height = img.height;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0);
    const imgData = canvas.toDataURL('image/png'); // Convertir a Base64

    // Agregar la imagen al PDF
    const imgX = 175; // Posición X para la imagen
    const imgY = 10; // Posición Y para la imagen (después de la tabla)
    const imgWidth = 20; // Ancho de la imagen
    const imgHeight = (img.height * imgWidth) / img.width; // Mantener la proporción de la imagen

    doc.addImage(imgData, 'PNG', imgX, imgY, imgWidth, imgHeight); // Agregar imagen al PDF

    // Guarda el PDF después de que se haya agregado la imagen
    doc.save('Tarjeta_Reserva.pdf');
  };

  img.onerror = function () {
    console.error("Error loading image");
    doc.save('Tarjeta_Reserva.pdf'); // Guarda el PDF incluso si hay un error al cargar la imagen
  };
};

</script>

  
    
<style scoped>

.content {
  
  z-index: 9999;
}
</style>>
    