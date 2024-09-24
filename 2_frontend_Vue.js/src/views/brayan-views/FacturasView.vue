<template>
  <LayoutAuthenticated>
    <SectionMain class=" rounded-lg">
      <FacturasTable>
        


      </FacturasTable>
    </SectionMain>
  </LayoutAuthenticated>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';

import FacturasTable from '@/components/brayan_components/FacturasTable.vue';

// import { getAllFacturas, updateFacturaService } from "@/services/brayan_service/FacturacionService";

// const facturas = ref([]);
// const selectedFactura = ref(null);

// const showEditModal = ref(false);
// const showDeleteModal = ref(false);
// const showListaProductosModal = ref(false);
// const agregarProductosModal = ref(false);


// const fetchFacturas = async () => {
//   try {
//     const response = await getAllFacturas();
//     facturas.value = response;
//   } catch (error) {
//     console.error('Error al obtener facturas:', error.message);
//     if (error.response) {
//       console.error('Error en la respuesta:', error.response);
//     }
//   }
// };

// onMounted(() => {
//   fetchFacturas();
// });



// async function handleUpdate() {
//   try {
//     await fetchFacturas(); 
    
//     closeEditModal(); 
//   } catch (error) {
   
//     console.error('Error al actualizar la factura:', error);
//   }
// }

// async function handleDelete() {
//   try {
//     await fetchFacturas();  // Recarga las facturas después de eliminar una
//     closeDeleteModal();     // Cierra el modal de eliminación
//   } catch (error) {
//     console.error('Error al eliminar la factura:', error);
//   }
// }



// function openEditModal(factura) {
//   selectedFactura.value = { ...factura }; // Clona la factura seleccionada
//   showEditModal.value = true;
// }

// function openDeleteModal(factura) {
//   selectedFactura.value = { ...factura }; 
//   showDeleteModal.value = true;
// }

// function openListaProductosModal(factura) {
//   selectedFactura.value = factura;
//   showListaProductosModal.value = true;
// }

// function openAgregarProductosModal(factura) {
//   selectedFactura.value = factura;
//   agregarProductosModal.value = true;
// }

// function closeEditModal() {
//   showEditModal.value = false;
// }

// function closeDeleteModal() {
//   showDeleteModal.value = false;
// }

// function closeListaProductosModal() {
//   showListaProductosModal.value = false;
// }

// function closeAgregarProductosModal() {
//   agregarProductosModal.value = false;
// }



</script>
