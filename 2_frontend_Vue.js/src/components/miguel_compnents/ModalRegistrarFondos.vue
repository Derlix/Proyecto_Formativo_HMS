
<template>
    <div class="content">
      <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white ">
        <div class="bg-white dark:bg-gray-800 p-8 sm:p-12 rounded-lg shadow-lg max-w-2xl w-full relative max-h-[85vh]">
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
              <BaseButton type="reset" color="info" outline label="Cancelar"  @click="closeModal()" />
            </BaseButtons>
   
          </div>
            
        </div>
      </div>
    </div>
</template> 

<script setup>
import { ref, defineProps, defineEmits } from 'vue'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import { mdiBallotOutline } from '@mdi/js'
import BaseDivider from '@/components/BaseDivider.vue'



defineProps({
  visible: {
    type: Boolean,
    required: true
  },
  title: {
    type: String,
    default: 'Registrar Fondos'
  }
})

const emit = defineEmits(['close'])



const closeModal = () => {
  emit('close')
}
</script>

