<template>
  <!-- Filtro por fecha -->
  <div class="flex items-center mb-5" style="width: 500px;">
    <h2 class="mr-3 text-lg dark:text-white">Filtrar por fecha inicio:</h2>
    <input
      id="selectedDate"
      v-model="selected_date"
      type="date"
      @change="filtrarRegistrosPorFechaInicio"
      class="w-48 px-4 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:text-white dark:bg-gray-700"
    />
  </div>

  <!-- Tabla de resultados -->
  <div class="relative overflow-x-auto">
    <table>
      <thead>
        <tr>
          <th>Dinero inicial</th>
          <th>Dinero final</th>
          <th>Fecha inicio</th>
          <th>Fecha fin</th>
          <th>Usuario</th>
          <th>Email</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="comprobante in filteredFondos" :key="comprobante.id_manejo_caja">
          <td>{{ comprobante.dinero_inicial }}</td>
          <td>{{ comprobante.dinero_final }}</td>
          <td>{{ formatDate(comprobante.fecha_inicio) }}</td>
          <td>{{ formatDate(comprobante.fecha_fin) }}</td>
          <td>{{ comprobante.usuario?.nombre_completo }}</td>
          <td>{{ comprobante.usuario?.email }}</td>
        </tr>
      </tbody>
    </table>

    <!-- Paginación -->
    <div class="flex justify-between mt-4">
      <button
        v-if="currentPage > 1"
        @click="handlePageClick(currentPage - 1)"
        class="btn btn-secondary"
      >
        Anterior
      </button>
      <button
        v-if="currentPage < TotalPages"
        @click="handlePageClick(currentPage + 1)"
        class="btn btn-secondary"
      >
        Siguiente
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { obtenerFondosPaginados } from '@/services/gestionfondosService'

const currentPage = ref(1)
const pageSize = ref(10)
const TotalPages = ref(0)
const allComprobantes = ref([])
const filteredFondos = ref([])
const selected_date = ref('')
const comprobantesOriginales = ref([])

// Cargar registros paginados
const fetchComprobantes = async () => {
  try {
    const response = await obtenerFondosPaginados(currentPage.value, pageSize.value)
    TotalPages.value = response.total_paginas || 1
    allComprobantes.value = response.manejo_cajas || []
    filteredFondos.value = allComprobantes.value
    comprobantesOriginales.value = [...allComprobantes.value]
  } catch (error) {
    console.error('Error al obtener comprobantes', error)
  }
}

// Navegación de páginas
const handlePageClick = (page) => {
  currentPage.value = page
  fetchComprobantes()
}

// Formatear fecha
const formatDate = (fecha) => {
  const opciones = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  }
  return new Date(fecha).toLocaleString('es-ES', opciones)
}

// Filtrar por fecha de inicio
const filtrarRegistrosPorFechaInicio = () => {
  if (selected_date.value === '') {
    filteredFondos.value = comprobantesOriginales.value
  } else {
    filteredFondos.value = comprobantesOriginales.value.filter((comprobante) => {
      const fechaInicio = comprobante.fecha_inicio.split('T')[0]
      return fechaInicio === selected_date.value
    })
  }
}

onMounted(() => {
  fetchComprobantes()
})
</script>
