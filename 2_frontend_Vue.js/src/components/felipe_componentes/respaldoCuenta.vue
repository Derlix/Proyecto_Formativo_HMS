<template>
      <BaseButton @click="openCreateModal" color="info" label="Insertar Cuenta-Huesped" class="mb-4" />
     
      <div class="mb-6 max-w-3xl mx-auto">
       <div class="flex flex-col md:flex-row items-center gap-4">
         <input
           type="search"
           id="buscarReserva"
           placeholder="Buscar Cuenta por numero de reserva"
           class=" w-full md:flex-grow px-4 py-2 border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
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
         <div v-if="selectedHuesped || selectedReserva">
             <!-- Información del Huésped -->
             <div v-if="selectedHuesped" class="guest-info">
               <h2>Información del Huésped</h2>
               <p><strong>Nombre:</strong> {{ selectedHuesped.nombre }}</p>
               <p><strong>Cédula:</strong> {{ selectedHuesped.cedula }}</p>
               <p><strong>Teléfono:</strong> {{ selectedHuesped.telefono }}</p>
               <p><strong>Email:</strong> {{ selectedHuesped.email }}</p>
             </div>
     
             <!-- Información de la Reserva -->
             <div v-if="selectedReserva" class="reservation-info">
               <h2>Información de la Reserva</h2>
               <p><strong>Número de Reserva:</strong> {{ selectedReserva.numero_reserva }}</p>
               <p><strong>Fecha de Entrada:</strong> {{ selectedReserva.fecha_entrada }}</p>
               <p><strong>Fecha de Salida:</strong> {{ selectedReserva.fecha_salida }}</p>
               <p><strong>Estado:</strong> {{ selectedReserva.estado }}</p>
             </div>
           </div>
                 <table v-if="cuentasHuesped.length > 0">
                   <thead>
                     <tr>
                       <th />
                       <th>ID Cuenta</th>      
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
                       <td data-label="TIPO MOVIMIENTO" >{{ cuenta.tipo_movimiento }}</td>
                       <td data-label="MONTO" >{{ cuenta.monto }}</td>
                       <td data-label="ESTADO" >{{ cuenta.estado }}</td>
                       <td data-label="FECHA" >{{ cuenta.fecha_movimiento }}</td>
                       <td class="before:hidden lg:w-1 whitespace-nowrap">
                         <BaseButtons type="justify-start lg:justify-end" no-wrap>
                             <BaseButton @click="openEditModal(cuenta)" :icon="mdiEye" small color="warning"  class="g-4" />
                             <BaseButton @click="openConfirmDeleteModal(cuenta)" :icon="mdiTrashCan" small color="danger"  class="g-4" />
                        
                         </BaseButtons>
                       </td>
                       
                     </tr>
                   </tbody>
                 </table>
                 <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800 relative" style="overflow-x: auto; white-space: nowrap;">
             <BaseLevel>
                 <BaseButtons style="display: inline-flex; overflow-x: auto; flex-wrap: nowrap;">
                     <BaseButton
                         v-for="page in TotalPages"
                         :key="page"
                         :active="page === currentPage"
                         :label="page"
                         :color="page === currentPage ? 'lightDark' : 'whiteDark'"
                         small
                         @click="currentPage = page; fetchCuentas()"
                     />
                 </BaseButtons>
                 <small>Página {{ currentPage }} de {{ TotalPages }}</small>
             </BaseLevel>
         </div>
               
         
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
              <!-- Modal de confirmación de eliminación -->
              <CardBoxModal
                 v-model="showConfirmDeleteModal"
                 title="Confirmar eliminación"
                 buttonLabel="Eliminar"
                 hasCancel
                 @confirm="confirmDeletecuenta"
                 @cancel="closeConfirmDeleteModal"
               >
                 <p>¿Estás seguro de que deseas eliminar esta cuenta?</p>
               </CardBoxModal>
               <CardBoxModal
                 v-model="showModal"
                 :title="isEditing ? 'Editar cuenta' : 'Agregar cuenta'"
                 buttonLabel="Guardar"
                 hasCancel
                 @confirm="saveCuenta"
                 @cancel="closeModal"
               >
                 <form @submit.prevent="saveCuenta" class="space-y-4">
                   <FormField label="numero reserva" help="Ingrese el numero de la reserva">
                     <FormControl v-model="cuentaForm.nombre" name="id_reserva" />
                   </FormField>
         
                   <FormField label="cedula huesped" help="Ingrese cedula del Huesped">
                     <FormControl v-model="cuentaForm.ubicacion" name="id_huesped" />
                   </FormField>
         
                   <FormField label="movimiento" help="Ingrese tipo de movimiento">
                     <FormControl v-model="cuentaForm.direccion" name="tipo_movimiento" />
                   </FormField>
         
                   <FormField label="monto" help="Ingrese el monto">
                     <FormControl v-model="cuentaForm.telefono" name="monto" type="text" />
                   </FormField>
                   <FormField label="estado" help="Ingrese el estado de la cuenta">
                     <FormControl v-model="cuentaForm.email" name="estado" type="text" />
                   </FormField>
                 </form>
               </CardBoxModal>
     
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
     import { getCuentaHuespedByIdReserva, getCuentaHuespedByIdHuesped, deleteCuentaHuesped, getCuentasHuespedesByPage} from '@/services/felipe_services/cuentaHuespedService';
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
           cuentaForm: {
                 id_reserva: '',
                 id_huesped: '',
                 tipo_movimiento: '',
                 monto: '',
                 estado: '',
                 fecha_movimiento: '',
               },
           cedula: '',
           isEditing: false,
           isReservaModalVisible: false,
           isHuespedModalVisible: false,
           showConfirmDeleteModal: false,
           cuentaToDelete: null,
           currentCuentaId: null,
           TotalPages : 0,
           currentPage : 1,
           reservaDetails: {},
           huespedDetails: {},
           mdiEye,  // Assign the icons to data directly
           mdiTrashCan,
         };
       },
       mounted() {
             this.fetchCuentas();
           },
       methods: {
         async fetchCuentas() {
             try {
               const response = await getCuentasHuespedesByPage(this.currentPage, 5);
               this.TotalPages = response.data.total_pages;
               this.cuentasHuesped = response.data.cuentas_huespedes;
             } catch (error) {
               console.error('Error al obtener los hoteles:', error);
             }
           },
         async fetchCuentasHuesped() {
           if (this.buscarCedula.trim() === '') {
             this.isLoading = false;
           }else{
             try {
               const cuentas = await getCuentaHuespedByIdHuesped(this.buscarCedula);
               if (cuentas.data) {
                 this.cuentasHuesped = cuentas.data;
                 this.selectedHuesped = cuentas.data[0].id_huesped;
                 this.selectedReserva = cuentas.data[0].id_reserva;
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
     
      },
           openConfirmDeleteModal(cuenta) {
             this.cuentaToDelete = cuenta;
             this.showConfirmDeleteModal = true;
           },
           closeConfirmDeleteModal() {
             this.showConfirmDeleteModal = false;
             this.cuentaToDelete = null;
           },
           async confirmDeletecuenta() {
             try {
               if (this.cuentaToDelete) {
                 await deleteCuentaHuesped(this.cuentaToDelete.id_cuenta);
                 this.fetchCuentasReserva();
                 this.closeConfirmDeleteModal();
               }
             } catch (error) {
               console.error('Error al eliminar el hotel:', error);
             }
           },
           openCreateModal() {
             this.isEditing = false;
             this.cuentaForm = { id_reserva: '', id_huesped: '', tipo_movimiento: '', monto: '', estado: '', fecha_movimiento: '' }; 
             this.showModal = true;
           },
           openEditModal(cuenta) {
             this.isEditing = true;
             this.currentCuentaId = cuenta.id_cuenta;
             this.cuentaForm = { ...cuenta };
             this.showModal = true;
           },
           closeModal() {
             this.showModal = false;
           },
           async saveCuenta() {
             // if (!this.validateForm()) {
             //   return;
             // }
         
             try {
               if (this.isEditing) {
                 await updateHotel(this.currentHotelId, this.hotelForm.nombre, this.hotelForm.ubicacion, this.hotelForm.direccion, this.hotelForm.telefono);
               } else {
                 await createHotel(this.hotelForm.nombre, this.hotelForm.ubicacion, this.hotelForm.direccion, this.hotelForm.telefono);
               }
               this.fetchHotels();
               this.closeModal();
             } catch (error) {
               console.error('Error al guardar el hotel:', error.response ? error.response.data : error);
             }
           },
     
       },
     }
         
     </script>