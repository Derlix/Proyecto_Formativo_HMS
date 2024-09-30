<template>
    <transition name="modal">
      <div v-if="mostrarModal" class="fixed inset-0 z-50 flex items-center justify-center">
        <div class="absolute inset-0 bg-black opacity-50"></div>
        <div class="relative bg-white dark:bg-gray-800 rounded-lg shadow-lg w-full max-w-lg">
          <div class="p-6">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100">
              Cambiar Habitación
            </h3>
            <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">
              Ingresa el documento de la persona asociada a la reserva.
            </p>
            <!-- Input del documento -->
            <div class="mt-4">
              <label for="documento" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                Documento del Huésped
              </label>
              <input
                v-model="documento"
                id="documento"
                type="text"
                placeholder="Ingrese el documento"
                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                @input="buscarReservaporDoc"
              />
            </div>
  
            <!-- Campos que se activan después de ingresar el documento -->
            <div v-if="isDocumentValid" class="mt-6 space-y-4">
              <div>
                <label for="habitacion" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                  Nueva Habitación
                </label>
                <select
                  id="habitacion"
                  class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                >
                  <option>Seleccione la nueva habitación</option>
                </select>
              </div>
  
              <div>
                <label for="fecha-entrada" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                  Fecha de Entrada
                </label>
                <input
                  id="fecha-entrada"
                  type="date"
                  class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                />
              </div>
  
              <div>
                <label for="fecha-salida" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                  Fecha de Salida
                </label>
                <input
                  id="fecha-salida"
                  type="date"
                  class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                />
              </div>
            </div>
  
            <div class="mt-6 flex justify-end space-x-4">
              <button
                @click="closeModal"
                class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300 dark:bg-gray-600 dark:text-white dark:hover:bg-gray-500"
              >
                Cancelar
              </button>
              <button
                v-if="isDocumentValid"
                class="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 dark:bg-blue-500 dark:hover:bg-blue-600"
              >
                Guardar Cambios
              </button>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </template>
  
  
<script>
export default {
  props: {
    mostrarModal: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      documento: "",
      isDocumentValid: false 
    };
  },
  watch: {
    mostrarModal(newVal) {
      this.isModalOpen = newVal;
    }
  },
  methods: {
    handleDocumentInput() {
      this.isDocumentValid = this.documento.trim() !== "";
    },
    closeModal() {
      this.$emit('cerrar');
    }
  } 
  
};



</script>
