<template>
    <NotificationBar
      v-if="isAlertVisible"
      :color="colorAlert"
      :description="modalMessage"
      :visible="isAlertVisible"
    />
    
    <div class="mb-6 max-w-md mx-left">
      <div class="flex items-center border rounded-lg shadow-sm">
        <input
          type="text"
          placeholder="Buscar registros"
          class="search-input flex-grow px-4 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:text-white dark:bg-gray-700"
          v-model="buscarHuesped"
          @input="filterHuespedes"
        />
      </div>
    </div>
  
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
          <tr 
            v-for="comprobante in filteredHuespedes" 
            :key="comprobante.id_manejo_caja" 
            @click="openVisibleModal(comprobante)" 
            class="cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-600"
          >
            <td>{{ comprobante.dinero_inicial }}</td>
            <td>{{ comprobante.dinero_final }}</td>
            <td>{{ formatDate(comprobante.fecha_inicio) }}</td>
            <td>{{ formatDate(comprobante.fecha_fin) }}</td>
            <td>{{ comprobante.usuario?.nombre_completo }}</td>
            <td>{{ comprobante.usuario?.email }}</td>
            <td>
                <BaseButtons class="flex space-x-2">
                  <BaseButton color="info" :icon="mdiEye" small />
                  <BaseButton color="danger" :icon="mdiTrashCan" small />
                </BaseButtons>
              </td>
              
          </tr>
        </tbody>
      </table>
  
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
  
    <CardBoxModal 
      v-if="activarvisibleModal" 
      :huesped="currentHuesped" 
      :visible="activarvisibleModal" 
      @close="activarvisibleModal = false" 
    />
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { obtenerFondosPaginados } from '@/services/gestionfondosService'
  import CardBoxModal from '../CardBoxModal.vue'
  import NotificationBar from '../alejo_components/NotificationBar.vue'
  import BaseButton from '../BaseButton.vue'
  import { mdiEye , mdiTrashCan } from '@mdi/js'

  
  const currentPage = ref(1)
  const pageSize = ref(10)
  const TotalPages = ref(0)
  const allComprobantes = ref([])
  const filteredHuespedes = ref([])
  const buscarHuesped = ref('')
  const activarvisibleModal = ref(false)
  const currentHuesped = ref({})
  const isAlertVisible = ref(false)
  const modalMessage = ref('')
  const colorAlert = ref('')
  
  
  const fetchComprobantes = async () => {
    try {
      const response = await obtenerFondosPaginados(currentPage.value, pageSize.value)
  
      TotalPages.value = response.total_paginas || 1; 
      allComprobantes.value = response.manejo_cajas || [];
      filteredHuespedes.value = allComprobantes.value;
    } catch (error) {
      console.error('Error fetching comprobantes:', error)
      modalMessage.value = 'Error al encontrar comprobantes'
      isAlertVisible.value = true
      colorAlert.value = 'danger'
    }
  }
  
  const handlePageClick = (page) => {
    currentPage.value = page
    fetchComprobantes()
  }
  
  const openVisibleModal = (huesped) => {
    currentHuesped.value = huesped
    activarvisibleModal.value = true
  }
  
  const filterHuespedes = () => {
    filteredHuespedes.value = allComprobantes.value.filter(comprobante => {
      return (
        comprobante.usuario?.nombre_completo.toLowerCase().includes(buscarHuesped.value.toLowerCase()) ||
        comprobante.usuario?.email.toLowerCase().includes(buscarHuesped.value.toLowerCase())
      );
    });
  }
  
  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' };
    return new Date(dateString).toLocaleDateString('es-ES', options);
  }
  
  onMounted(() => {
    fetchComprobantes()
  })
  </script>
  
