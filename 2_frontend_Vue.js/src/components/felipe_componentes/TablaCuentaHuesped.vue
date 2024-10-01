<template>
 <BaseButton @click="openCreateModal" color="info" label="Insertar Cuenta-Huesped" class="mb-4" />

 <div class="mb-6 max-w-3xl mx-auto">
  <div class="flex flex-col md:flex-row items-center gap-4">
    <input
      type="search"
      id="buscarReserva"
      placeholder="Buscar Cuenta por numero de reserva"
      class="w-full md:flex-grow px-4 py-2 border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      v-model="buscarReserva"
      @input="fetchCuentasReserva"
    />
    <input
      type="search"
      id="buscarCedula"
      placeholder="Buscar Cuenta por cedula de huesped"
      class="w-full md:flex-grow px-4 py-2 border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
      v-model="buscarCedula"
      @input="fetchCuentasHuesped"
    />
  </div>
  </div>
  <div class="w-full overflow-auto mb-4 mt-4">
            <table v-if="cuentasHuesped.length > 0">
              <thead>
                <tr>
                  <th />
                  <th>ID Cuenta</th>
                  <th>Huesped</th>
                  <th>Reserva</th>
                  <th>Tipo Movimiento</th>
                  <th>Monto</th>
                  
                  <th>Estado</th>
                  <th>Fecha</th>
                  <th>Acciones</th>
                  <th />
                </tr>
              </thead>
              <tbody>
                <tr  v-for="cuenta in cuentasHuesped" :key="cuenta.id_cuenta">
                  <td></td>
                  <td data-label="ID CUENTA" >{{ cuenta.id_cuenta }}</td>  
                  <td data-label="HUESPED"> <BaseButton  @click="openHuespedModal(cuenta)" label="Detalles Huesped" color="success"  class="g-4" /></td>
                  <td data-label="RESERVA" > <BaseButton @click="openReservaModal(cuenta)"  label="Detalles Reserva" color="info"  class="g-4" /></td>
                  <td data-label="TIPO MOVIMIENTO" >{{ cuenta.tipo_movimiento }}</td>
                  <td data-label="MONTO" >{{ cuenta.monto }}</td>
                
                  <td data-label="ESTADO" >{{ cuenta.estado }}</td>
                  <td data-label="FECHA" >{{ cuenta.fecha_movimiento }}</td>
                  <td class="before:hidden lg:w-1 whitespace-nowrap">
                    <BaseButtons type="justify-start lg:justify-end" no-wrap>
                        <BaseButton @click="openEditModal(hotel)" :icon="mdiEye" small color="warning"  class="g-4" />
                        <BaseButton @click="openConfirmDeleteModal(hotel)" :icon="mdiTrashCan" small color="danger"  class="g-4" />
                   
                    </BaseButtons>
                  </td>
                  
                </tr>
              </tbody>
            </table>
            <p v-if="cuentasHuesped.length === 0">Ingresa cedula o reserva del cliente valido</p>
          
    
          </div>
        <div v-if="isHuespedModalVisible" class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50">
            <div class="bg-white dark:bg-gray-800 rounded-lg p-4 w-11/12 max-w-lg">
              <h2 class="text-xl font-bold mb-4">Detalles del Huésped</h2>
              <div >
                <p><strong>Cedula:</strong> {{ selectedHuesped.id_huesped }}</p>
                <p><strong>Nombre Completo:</strong> {{ selectedHuesped.nombre_completo }}</p>
                <p><strong>Tipo de Documento:</strong> {{ selectedHuesped.tipo_documento }}</p>
                <p><strong>Número de Documento:</strong> {{ selectedHuesped.numero_documento }}</p>
                <p><strong>Estado:</strong> {{ selectedHuesped.huesped_estado }}</p>
              
             
              </div>
              <button @click="isHuespedModalVisible = false" class="mt-4 bg-blue-500 text-white px-4 py-2 rounded">Cerrar</button>
            </div>
       </div>
       <div v-if="isReservaModalVisible" class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50">
            <div class="bg-white dark:bg-gray-800 rounded-lg p-4 w-11/12 max-w-lg">
              <h2 class="text-xl font-bold mb-4">Detalles de la reserva</h2>
              <div >
                <p><strong>Numero Reserva:</strong> {{ selectedReserva.id_reserva }}</p>
                <p><strong>Fecha Reserva:</strong> {{ selectedReserva.fecha_reserva }}</p>
                <p><strong>Empresa:</strong> {{ selectedReserva.empresa }}</p>
                <p><strong>Valor Deposito:</strong> {{ selectedReserva.valor_deposito }}</p>
                <p><strong>Forma Pago:</strong> {{ selectedReserva.forma_pago }}</p>
              
             
              </div>
              <button @click="isReservaModalVisible = false" class="mt-4 bg-blue-500 text-white px-4 py-2 rounded">Cerrar</button>
            </div>
       </div>


</template>
<script>
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import FormField from '@/components/FormField.vue';
import FormControl from '@/components/FormControl.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue';
import ModalForm from '@/components/ModalFormHotel.vue';
import SectionMain from '@/components/SectionMain.vue';
import CardBoxModal  from '@/components/felipe_componentes/CardBoxModal.vue';
import { mdiEye, mdiTrashCan } from '@mdi/js';
import { getCuentaHuespedByIdReserva, getCuentaHuespedByIdHuesped} from '@/services/felipe_services/cuentaHuespedService';
import BaseLevel from '@/components/BaseLevel.vue';
    export default {
      components: {
        LayoutAuthenticated,
        FormField,
        FormControl,
        BaseButton,
        BaseButtons,
        SectionTitleLineWithButton,
        ModalForm,
        SectionMain,
        CardBoxModal,
        BaseLevel,
      },
      data() {
    return {
      cuentasHuesped: [],
      cuenta: {},
      selectedHuesped: {},
      selectedReserva: {},
      cedula: '',
      isLoading: false,
      isReservaModalVisible: false,
      isHuespedModalVisible: false,
      reservaDetails: {},
      huespedDetails: {},
      mdiEye,  // Assign the icons to data directly
      mdiTrashCan,
    };
  },
  methods: {
    async fetchCuentasHuesped() {
      if (this.buscarCedula.trim() === '') {
        this.isLoading = false;
      }else{
        try {
          const cuentas = await getCuentaHuespedByIdHuesped(this.buscarCedula);
          if (cuentas.data) {
            this.cuentasHuesped = cuentas.data;
          } else {
            this.cuentasHuesped = []; // No hotel found
            this.cuenta = null;
            alert('Huesped no encontrado');
          }
        } catch (error) {
         
          this.cuentasHuesped = [];
          this.cuenta = null;
        }
      }
        // Search for a specific hotel by ID
     
      
    },
    async fetchCuentasReserva() {
      if (this.buscarReserva.trim() === '') {
        this.isLoading = false;
      }else{
        try {
       const cuentas = await getCuentaHuespedByIdReserva(this.buscarReserva);
       if (cuentas.data) {
         this.cuentasHuesped = cuentas.data;
       } else {
         this.cuentasHuesped = []; // No hotel found
         this.cuenta = null;
         alert('Reserva no encontrada');
       }
     } catch (error) {
      
       this.cuentasHuesped = [];
       this.cuenta = null;
     }
      }
     // Search for a specific hotel by ID
     try {
       const cuentas = await getCuentaHuespedByIdReserva(this.buscarReserva);
       if (cuentas.data) {
         this.cuentasHuesped = cuentas.data;
       } else {
         this.cuentasHuesped = []; // No hotel found
         this.cuenta = null;
         alert('Reserva no encontrada');
       }
     } catch (error) {
      
       this.cuentasHuesped = [];
       this.cuenta = null;
     }
   
 },
 async openHuespedModal(cuenta) {
  this.selectedHuesped = cuenta.id_huesped; // Asegúrate de que esto sea correcto según la respuesta de la API
  this.isHuespedModalVisible = true;

 },
 async openReservaModal(cuenta) {
  this.selectedReserva = cuenta.id_reserva; // Asegúrate de que esto sea correcto según la respuesta de la API
  this.isReservaModalVisible = true;

 }

  },
}
    
</script>