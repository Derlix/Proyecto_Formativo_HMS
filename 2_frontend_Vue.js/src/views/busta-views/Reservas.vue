<script setup>
import { ref, onMounted } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import AlertaCrearReserva from '@/components/miguel_compnents/AlertaCrearReserva.vue'

const showModal = ref(false)

// No necesitamos un composable para el modo oscuro. Tailwind lo maneja automáticamente.
onMounted(() => {
  // Se puede agregar cualquier lógica extra aquí si es necesario
})
</script>

<template>
  <LayoutAuthenticated>
    <!-- Contenedor principal -->
    <div class="px-3 py-4">
      <h2 class="text-xl font-bold text-gray-900 dark:text-gray-100">Operador De Reservas</h2>

      <!-- Botones con Flexbox de Tailwind -->
      <div class="flex justify-center space-x-4 py-4">
        <button
          @click="showModal = true"
          class="text-sm font-semibold leading-6 text-white bg-blue-800 hover:bg-blue-900 rounded-md px-4 py-2 dark:bg-blue-700 dark:hover:bg-blue-800"
        >
          Crear reserva
        </button>

        <!-- Pasa showModal como prop y maneja el evento de cierre -->
        <AlertaCrearReserva :mostrarModal="showModal" @cerrar="showModal = false" />

        <button
          type="button"
          class="text-sm font-semibold leading-6 text-white bg-blue-800 hover:bg-blue-900 rounded-md px-4 py-2 dark:bg-blue-700 dark:hover:bg-blue-800"
        >
          Cambiar habitación
        </button>

        <button
          type="button"
          class="text-sm font-semibold leading-6 text-white bg-blue-800 hover:bg-blue-900 rounded-md px-4 py-2 dark:bg-blue-700 dark:hover:bg-blue-800"
        >
          Cambiar reserva
        </button>

        <button
          type="button"
          class="text-sm font-semibold leading-6 text-white bg-blue-800 hover:bg-blue-900 rounded-md px-4 py-2 dark:bg-blue-700 dark:hover:bg-blue-800"
        >
          Registrar comprobante de descuento
        </button>
      </div>
    </div>

    <!-- Buscador de Reservas -->
    <div class="px-3 mb-6">
      <h2 class="text-lg font-semibold text-gray-900 dark:text-gray-100">Reservas</h2>
      <div class="mb-6 max-w-md">
        <div class="flex items-center border rounded-lg shadow-sm dark:border-gray-600">
          <input
            type="search"
            id="buscarReserva"
            placeholder="Buscar reserva por huésped"
            class="flex-grow px-4 py-2 border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-800 dark:border-gray-600 dark:text-gray-100"
            v-model="buscarReserva"
            @input="Buscar_reserva"
          />
        </div>
      </div>
    </div>

    <!-- Tabla de Reservas -->
    <div class="overflow-x-auto">
      <table class="table-auto w-full text-left border-collapse">
        <thead class="bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100">
          <tr>
            
            <th class="px-4 py-2">Habitación</th>
            <th class="px-4 py-2">Fecha de reserva</th>
            <th class="px-4 py-2">Categoría de habitación</th>
            <th class="px-4 py-2">Piso</th>
            <th class="px-4 py-2">Nombre del huesped</th>
            <th class="px-4 py-2">Tipo documento</th>
            <th class="px-4 py-2">Número documento</th>
            <th class="px-4 py-2">Teléfono</th>
            <th class="px-4 py-2" />
          </tr>
        </thead>
        <tbody>
          <!-- Aquí irían los datos -->
        </tbody>
      </table>
    </div>
  </LayoutAuthenticated>
</template>
