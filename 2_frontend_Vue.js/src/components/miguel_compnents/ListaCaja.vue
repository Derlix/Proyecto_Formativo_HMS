<template>
  <NotificationBar
    :color="colorAlert"
    v-if="isAlertVisible"
    :description="modalMessage"
    :visible="isAlertVisible"
  />
  <CardBoxModal v-model="activarModalEdit" title="Editar Fondo"  buttonLabel="Guardar cambios" has-cancel @cancel="cancelEdit"
  @confirm="update_Fondo " >
    <form @submit.prevent="update_Fondo()">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
        
        <div class="mb-4">
          <label for="dinero_final" class="block text-gray-700  font-medium dark:text-white">Dinero final</label>
          <input
            type="number"
            id="dinero_final"
            class="mt-1 block w-full border-gray-300 rounded-md shado dark:text-white dark:border-gray-600 rounded-mdw-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentFondo.dinero_final"
            required
          />
        </div>
        <div class="mb-4">
          <label for="fecha_fin" class="block text-gray-700  font-medium dark:text-white">Fecha fin</label>
          <input
            type="datetime-local"
            id="fecha_fin"
            class="mt-1 block w-full border-gray-300 rounded-md shad dark:text-white dark:border-gray-600 rounded-mdow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
            v-model="currentFondo.fecha_fin"
            required
          />
        </div>
      </div>

    </form>
  </CardBoxModal >

  <CardBoxModal v-model="activarModalDelete.visible"  v-if="activarModalDelete.comprobante" title="Eliminar registro" buttonLabel="Eliminar" button="danger" has-cancel @confirm="confirmDelete"
  @cancel="cancelDelete" >
    <p class="text-xl">Esta seguro de eliminar el registro: </p>
    <b>Dinero inicial: ${{ activarModalDelete.comprobante.dinero_inicial }}</b><br>
    <b>Dinero final: ${{ activarModalDelete.comprobante.dinero_final }}</b><br>
    <small>{{ formatDate(activarModalDelete.comprobante.fecha_fin) }}</small>
  </CardBoxModal>
  
  <div class="flex items-center mb-5" style="width: 500px;">
    <h2 class="mr-3 text-lg">Filtrar por fecha inicio:</h2>
    <input id="selectedDate" 
      v-model="selected_date" 
      type="date"
      @change="filtrarRegistrosPorFechaInicio"
    />
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
            v-for="comprobante in filteredFondos" 
            :key="comprobante.id_manejo_caja" 
            >
            <td>{{ comprobante.dinero_inicial }}</td>
            <td>{{ comprobante.dinero_final }}</td>
            <td>{{ formatDate(comprobante.fecha_inicio) }}</td>
            <td>{{ formatDate(comprobante.fecha_fin) }}</td>
            <td>{{ comprobante.usuario?.nombre_completo }}</td>
            <td>{{ comprobante.usuario?.email }}</td>
            <td>
                <BaseButtons class="flex space-x-2">
                  <BaseButton color="info" :icon="mdiEye" small @click="openEditModal(comprobante)" />
                  <BaseButton color="danger" :icon="mdiTrashCan" small @click="openDeleteModal(comprobante)"/>
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
  import { deleteFondo, obtenerFondosPaginados, updateFondo } from '@/services/gestionfondosService'
  import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue'
  import NotificationBar from '../alejo_components/NotificationBar.vue'
  import BaseButton from '../BaseButton.vue'
  import { mdiEye , mdiTrashCan } from '@mdi/js'

  
  const currentPage = ref(1);
  const pageSize = ref(10);
  const TotalPages = ref(0);
  const allComprobantes = ref([]);
  const filteredFondos = ref([]);
  const buscarHuesped = ref('');
  const activarvisibleModal = ref(false);
  const currentFondo = ref({});
  const isAlertVisible = ref(false);
  const modalMessage = ref('');
  const colorAlert = ref('');
  const isEditMode = ref(false);
  const comprobantesOriginales = ref ([]);
  const activarModalEdit = ref(false);
  const activarModalDelete = ref({
    visible: false,
    comprobante: null
  });
  const selected_date = ref('');

  

  
  
  const fetchComprobantes = async () => {
    try {
      const response = await obtenerFondosPaginados(currentPage.value, pageSize.value)
      TotalPages.value = response.total_paginas || 1; 
      allComprobantes.value = response.manejo_cajas || [];
      filteredFondos.value = allComprobantes.value;

      comprobantesOriginales.value = [...allComprobantes.value];
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
  

  
  const filterHuespedes = () => {
    filteredFondos.value = allComprobantes.value.filter(comprobante => {
      return (
        comprobante.usuario?.nombre_completo.toLowerCase().includes(buscarHuesped.value.toLowerCase()) ||
        comprobante.usuario?.email.toLowerCase().includes(buscarHuesped.value.toLowerCase())
      );
    });
  }
  
  const formatDate = (dateString) => {
  const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  };

  return new Date(dateString).toLocaleString('es-ES', options);
};

const openEditModal = (comprobante = {}) => {
  isEditMode.value = true;
  currentFondo.value = { ...comprobante };
  activarModalEdit.value = true;
};

  // Actualiza un huésped
const update_Fondo = async () => {
  try {
    await updateFondo(
      currentFondo.value.id_manejo_caja,
      currentFondo.value.dinero_inicial,
      currentFondo.value.dinero_final,
      currentFondo.value.fecha_fin,
    );
    modalMessage.value = 'Registro actualizado exitosamente';
    isAlertVisible.value = true;
    colorAlert.value = 'success';
    activarModalEdit.value = false;

    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
    //cierra el modal en tres segundos

    await fetchComprobantes();
  } catch (error) {
    modalMessage.value ='Error al actualizar Registro';
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    activarModalEdit.value = false;

    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);

  }
};

const cancelEdit = () => {
  activarModalEdit.value = false;
  // Solo cierra el modal
};


// Método para abrir el modal
const openDeleteModal = (comprobante) => {
  activarModalDelete.value = {
    visible: true,
    comprobante: comprobante
    
  };
};


// Método para confirmar la eliminación
const confirmDelete = async () => {
  const fondoTemp = activarModalDelete.value.comprobante;
  if (!fondoTemp) return;
  console.log("id", fondoTemp.id_manejo_caja);

  try {
    await deleteFondo(fondoTemp.id_manejo_caja);
    modalMessage.value = 'Registro eliminado exitosamente';
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);

    await fetchComprobantes(); 
    activarModalDelete.value.visible = false; 
  } catch (error) {
    modalMessage.value = 'Error al eliminar Registro';
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    activarModalDelete.value.visible = false; 
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);

  }
};

// Método para cancelar la eliminación
const cancelDelete = () => {
  activarModalDelete.value.visible = false; // Solo cierra el modal
};


const filtrarRegistrosPorFechaInicio = () => {
  console.log("fecha_selected", selected_date.value);
  
  if (selected_date.value === "") {
    fetchComprobantes(); 
  } else {
    console.log(comprobantesOriginales);
    filteredFondos.value = comprobantesOriginales.value.filter(comprobante => {
      const fechaComprobante = comprobante.fecha_inicio.split('T')[0]; 
      return fechaComprobante === selected_date.value;
    });
    console.log(filteredFondos.value);
  }

  if (filteredFondos.value.length === 0) {
    modalMessage.value = 'No se encontraron registros en la fecha seleccionada';
    isAlertVisible.value = true;
    colorAlert.value = 'danger';

    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
  }
};



  
  onMounted(() => {
    fetchComprobantes()
  })
  </script>
  
