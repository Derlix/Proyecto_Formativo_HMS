<template>
  <NotificationBar
    v-if="isAlertVisible"
    :color="colorAlert"
    :description="modalMessage"
    :visible="isModalVisible"
  />
  <BaseButton @click="openCreateModal" color="info" label="Insertar Cuenta-Huesped" class="mb-4" />
  
  <div class="mb-6 max-w-3xl mx-auto">
    <div class="flex flex-col md:flex-row items-center gap-4">
      <input
        type="search"
        id="buscarReserva"
        placeholder="Buscar Cuenta por número de reserva"
        class="text-light w-full md:flex-grow px-4 py-2 border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
        v-model="buscarReserva"
      />
      <input
        type="search"
        id="buscarCedula"
        placeholder="Buscar Cuenta por cédula de huésped"
        class="w-full md:flex-grow px-4 py-2 border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
        v-model="buscarCedula"
      />
      <BaseButton @click="realizarBusqueda" small color="warning" label="Buscar" />
    </div>
  </div>

  <div v-if="selectedHuesped || selectedReserva" class="flex justify-between gap-4 mb-6">
    <!-- Información del Huésped -->
    <div v-if="selectedHuesped" class="p-4 shadow-lg rounded w-1/2">
      <h2 class="text-lg font-bold mb-2">Información del Huésped</h2>
      <p><strong>Nombre:</strong> {{ selectedHuesped.nombre }}</p>
      <p><strong>Cédula:</strong> {{ selectedHuesped.cedula }}</p>
      <p><strong>Tipo Documento:</strong> {{ selectedHuesped.telefono }}</p>
      <p><strong>Estado:</strong> {{ selectedHuesped.email }}</p>
    </div>

    <!-- Información de la Reserva -->
    <div v-if="selectedReserva" class="  p-4 shadow-lg rounded w-1/2">
      <h2 class="text-lg font-bold mb-2">Información de la Reserva</h2>
      <p><strong>Número de Reserva:</strong> {{ selectedReserva.numero_reserva }}</p>
      <p><strong>Fecha de Movimiento:</strong> {{ formatDate(selectedReserva.fecha_entrada) }}</p>
      <p><strong>Empresa:</strong> {{ selectedReserva.fecha_salida }}</p>
      <p><strong>Deposito:</strong> {{ selectedReserva.estado }}</p>
    </div>
  </div>

  <div class="w-full overflow-auto mb-4 mt-4">
    <h1 class="text-lg font-bold mb-2 text-center">Lista de Transacciones</h1>
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
        <tr v-for="cuenta in cuentasHuesped" :key="cuenta.id_cuenta">
          <td></td>
          <td data-label="ID CUENTA">{{ cuenta.id_cuenta }}</td>
          <td data-label="TIPO MOVIMIENTO">{{ cuenta.tipo_movimiento }}</td>
          <td data-label="MONTO">{{ cuenta.monto }}</td>
          <td data-label="ESTADO">{{ cuenta.estado }}</td>
          <td data-label="FECHA">{{ formatDate(cuenta.fecha_movimiento) }}</td>
          <td class="before:hidden lg:w-1 whitespace-nowrap">
            <BaseButtons type="justify-start lg:justify-end" no-wrap>
              <BaseButton @click="openEditModal(cuenta)" :icon="mdiEye" small color="warning" class="g-4" />
              <BaseButton @click="openConfirmDeleteModal(cuenta)" :icon="mdiTrashCan" small color="danger" class="g-4" />
            </BaseButtons>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="total-container">
      <strong>Total PENDIENTE: {{ totalPendiente.toFixed(2) }}</strong> 
    </div>

    <div v-if="cuentasHuesped.length === 0 && !selectedReserva && !selectedHuesped" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mt-4" role="alert">
  <strong class="font-bold">Atención: </strong>
  <span class="block sm:inline text-center">Por favor, busque una reserva o un huésped en el buscador.</span>
</div>


    <BaseButton v-if="selectedHuesped && selectedReserva" 
    @click="openDetallesmodal" color="warning" label="Imprimir" />
  </div>

  <CardBoxModal 
  v-model="showModal"
  :title="isEditing ? 'Editar cuenta' : 'Agregar cuenta'"
  buttonLabel="Guardar"
  hasCancel
  @confirm="saveCuenta"
  @cancel="closeModal"
>
  <form @submit.prevent="saveCuenta" class="space-y-4">
    <!-- Campo número de reserva -->
    <FormField label="Número de reserva" help="Ingrese el número de la reserva">
      <FormControl v-model="cuentaForm.id_reserva" name="id_reserva" :disabled="isEditing" />
    </FormField>

    <!-- Campo cédula del huésped -->
    <FormField label="Cédula del huésped" help="Ingrese cédula del huésped">
      <FormControl v-model="cuentaForm.id_huesped" name="id_huesped" :disabled="isEditing" />
    </FormField>

    <!-- Campo tipo de movimiento con select -->
    <FormField label="Tipo de movimiento" help="Seleccione el tipo de movimiento">
      <select v-model="cuentaForm.tipo_movimiento" name="tipo_movimiento" class="form-select">
        <option value="FACTURA">FACTURA</option>
        <option value="AVANCE_EFECTIVO">AVANCE EFECTIVO</option>
      </select>
    </FormField>

    <!-- Campo monto -->
    <FormField label="Monto" help="Ingrese el monto">
      <FormControl v-model="cuentaForm.monto" name="monto" type="text"/>
    </FormField>

    <!-- Campo estado con select -->
    <FormField label="Estado" help="Seleccione el estado de la cuenta">
      <select v-model="cuentaForm.estado" name="estado" class="form-select">
        <option value="PENDIENTE">PENDIENTE</option>
        <option value="PAGADO">PAGADO</option>
      </select>
    </FormField>
  </form>
</CardBoxModal>


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


               <CardLista v-model="showDetalles">
  <!-- Sección de Información del Huésped y Reserva -->
  <div class="mb-2 overflow-y-auto max-h-96" id="facturaDetalles">
    <div>
      <!-- Título -->
      <div class="flex justify-between items-center mb-1">
        <h1 class="font-bold text-lg" style="font-size: 26px; color: darkgreen;">DETALLES CUENTA HUESPED</h1>
        <div class="flex items-center">
          <img src="@/assets/img/sena-agro.png" alt="" style="width: 70px; margin-right: 5px;">
        </div>
      </div>
      
      <!-- Información del Huésped -->
      <div v-if="selectedHuesped" class=" p-4 rounded-lg mb-4">
        <h2 class="font-bold text-lg mb-2">Información del Huésped</h2>
        <p><strong>Nombre:</strong> {{ selectedHuesped.nombre }}</p>
        <p><strong>Cédula:</strong> {{ selectedHuesped.cedula }}</p>
        <p><strong>Tipo Documento:</strong> {{ selectedHuesped.telefono }}</p>
      </div>
      
      <!-- Información de la Reserva -->
      <div v-if="selectedReserva" class=" p-4 rounded-lg mb-4">
        <h2 class="font-bold text-lg mb-2">Información de la Reserva</h2>
        <p><strong>Número de Reserva:</strong> {{ selectedReserva.numero_reserva }}</p>
        <p><strong>Fecha de Entrada:</strong> {{ formatDate(selectedReserva.fecha_entrada) }}</p>
        <p><strong>Empresa:</strong> {{ selectedReserva.fecha_salida }}</p>
        <p><strong>Depósito:</strong> {{ selectedReserva.estado }}</p>
      </div>
      
      <!-- Lista de Transacciones -->
      <div class="transaction-list">
        <h2 class="font-bold text-lg mb-2">Lista de Transacciones</h2>
        <table v-if="cuentasHuesped.length > 0" class="w-full table-auto border-collapse">
          <thead>
            <tr class="">
              <th class="border p-2">ID Cuenta</th>
              <th class="border p-2">Tipo Movimiento</th>
              <th class="border p-2">Monto</th>
              <th class="border p-2">Estado</th>
              <th class="border p-2">Fecha</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="cuenta in cuentasHuesped" :key="cuenta.id_cuenta">
              <td class="border p-2">{{ cuenta.id_cuenta }}</td>
              <td class="border p-2">{{ cuenta.tipo_movimiento }}</td>
              <td class="border p-2">{{ cuenta.monto }}</td>
              <td class="border p-2">{{ cuenta.estado }}</td>
              <td class="border p-2">{{ formatDate(cuenta.fecha_movimiento) }}</td>
            </tr>
          </tbody>
        </table>
        <div class="total-container">
          <strong>Total PENDIENTE: {{ totalPendiente.toFixed(2) }}</strong> 
       </div>

      </div>
      
     
     
    </div>
    
  </div>
   <!-- Botón para descargar PDF -->
  <button @click="downloadPDF()" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition mt-4">
        Descargar PDF
      </button>
</CardLista>


<!-- Modal de advertencia cuando no se encuentra una reserva o huésped -->
<CardBoxModal 
  v-model="showModalAdvertencia" 
  title="Advertencia" 
  buttonLabel="Cerrar"
  hasCancel
  @confirm="showModalAdvertencia = false"
  @cancel="showModalAdvertencia = false"
>
  <h2>{{ advertenciaMensaje }}</h2>
</CardBoxModal>

              
</template>

<script>
 import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
     import FormField from '@/components/FormField.vue';
     import FormControl from '@/components/FormControl.vue';
     import NotificationBar from '../alejo_components/NotificationBar.vue';
     import BaseButton from '@/components/BaseButton.vue';
     import BaseButtons from '@/components/BaseButtons.vue';
     import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue';
     import ModalForm from '@/components/ModalFormHotel.vue';
     import SectionMain from '@/components/SectionMain.vue';
     import CardBoxModal  from '@/components/felipe_componentes/CardBoxModal.vue';
     import { mdiEye, mdiTrashCan } from '@mdi/js';
     import { getCuentaHuespedByIdReserva, getCuentaHuespedByIdHuesped, deleteCuentaHuesped, createCuentaHuesped, updateCuentaHuesped} from '@/services/felipe_services/cuentaHuespedService';
     import BaseLevel from '@/components/BaseLevel.vue';
     import CardLista from '../brayan_components/CardLista.vue';
     import jsPDF from "jspdf";
     import html2canvas from "html2canvas";
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
             CardLista,
             jsPDF,
             html2canvas,
             NotificationBar,
             

           },
  data() {
    return {
      cuentasHuesped: [],
      cuentaForm: {
        id_reserva: '',
        id_huesped: '',
        tipo_movimiento: '',
        monto: '',
        estado: '',
        fecha_movimiento: '',
      },
      showModal: false,
      isEditing: false,
      selectedHuesped: null,
      selectedReserva: null,
      showConfirmDeleteModal: false,
      showModalAdvertencia: false, 
      showDetalles: false,
      cuentaToDelete: null,
      busqueda: null,
      buscarReserva: '',
      buscarCedula: '',
      mdiEye,  // Assign the icons to data directly
      mdiTrashCan,
      modalMessage: '',
        isAlertVisible : false,
        colorAlert: '',
        valor: null,
        totalPendiente: 0,
    
    };
  },
  methods: {
   async realizarBusqueda() {
      if (this.buscarReserva && this.buscarCedula) {
        this.mostrarError('Solo puedes buscar por uno de los campos a la vez.', 'danger');
        return;
      }

      if (!this.buscarReserva && !this.buscarCedula) {
        this.mostrarError('Debes ingresar un número de reserva o cédula.', 'danger');
        return;
      }

      // Lógica para la búsqueda según el campo que esté lleno
      if (this.buscarReserva) {
        this.busqueda = 0;
        this.valor = this.buscarReserva;
        await this.fetchCuentasReserva();
      } else if (this.buscarCedula) {
        this.busqueda = 1;
        this.valor = this.buscarCedula;
        await this.fetchCuentasHuesped();
      }
    },

    mostrarError(mensaje, color) {
      this.modalMessage = mensaje;
      this.colorAlert = color;
      this.isAlertVisible = true;
  setTimeout(() => {
    this.isAlertVisible = false;
  }, 3000);
    },

  async openDetallesmodal() {
  this.showDetalles = true;
},
formatDate(fecha) {
      if (!fecha) return ''; // Manejo de casos donde la fecha sea nula o vacía
      const date = new Date(fecha);
      return date.toLocaleDateString('es-ES', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric'
      });
    },
    calculateTotalPendiente() {
      this.totalPendiente = this.cuentasHuesped
        .filter(cuenta => cuenta.estado === 'PENDIENTE') // Filtrar cuentas PENDIENTE
        .reduce((total, cuenta) => total + parseFloat(cuenta.monto), 0); // Sumar montos
    },

   
  
    async fetchCuentasHuesped() {
      try {
        const response = await getCuentaHuespedByIdHuesped(this.valor);
        if (response.data && response.data.length > 0) {
          const firstCuenta = response.data[0];
          this.cuentasHuesped = response.data;
          this.selectedHuesped = {
            nombre: firstCuenta.id_huesped.nombre_completo,
            cedula: firstCuenta.id_huesped.numero_documento,
            telefono: firstCuenta.id_huesped.tipo_documento,
            email: firstCuenta.id_huesped.huesped_estado,
          };
          this.selectedReserva = {
            numero_reserva: firstCuenta.id_reserva.id_reserva,
            fecha_entrada: firstCuenta.id_reserva.fecha_reserva,
            fecha_salida: firstCuenta.id_reserva.empresa,
            estado: firstCuenta.id_reserva.valor_deposito,
          };
          this.calculateTotalPendiente(); // Calcular el total de cuentas PENDIENTE
        } else {
        this.limpiarResultados();
        
        this.mostrarError('No se encontraron cuentas para este huésped, crea una', 'danger');
      }
    } catch (error) {
      this.limpiarResultados();
      this.mostrarError('No se encontraron cuentas para este huésped o el huesped no existe, crea una', 'danger');
      console.error(error);
    }
  },
    async fetchCuentasReserva() {
      try {
        const response = await getCuentaHuespedByIdReserva(this.valor);
        if (response.data) {
          const firstCuenta = response.data[0];
          this.cuentasHuesped = response.data;
          this.selectedHuesped = {
            nombre: firstCuenta.id_huesped.nombre_completo,
            cedula: firstCuenta.id_huesped.numero_documento,
            telefono: firstCuenta.id_huesped.tipo_documento,
            email: firstCuenta.id_huesped.huesped_estado,
          };
          this.selectedReserva = {
            numero_reserva: firstCuenta.id_reserva.id_reserva,
            fecha_entrada: firstCuenta.id_reserva.fecha_reserva,
            fecha_salida: firstCuenta.id_reserva.empresa,
            estado: firstCuenta.id_reserva.valor_deposito,
          };
          this.calculateTotalPendiente(); // Calcular el total de cuentas PENDIENTE
        }else {
        this.limpiarResultados();
        this.mostrarError('No se encontraron cuentas para esta reserva, crea una', 'danger');
      }
    } catch (error) {
      this.limpiarResultados();
      this.mostrarError('No se encontró reserva existente', 'danger');
      console.error(error);
    }
  },
  mostrarAdvertencia(mensaje) {
    this.advertenciaMensaje = mensaje;  // Establece el mensaje del modal
    this.showModalAdvertencia = true;  // Muestra el modal
  },
    limpiarResultados() {
      this.cuentasHuesped = [];
      this.selectedHuesped = null;
      this.selectedReserva = null;
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
                this.closeConfirmDeleteModal();
                this.mostrarError('Eliminacion del hotel exitosa', 'success');
                // Refrescar las cuentas según el tipo de búsqueda que se realizó
                this.busqueda === 0 ? await this.fetchCuentasReserva() : await this.fetchCuentasHuesped();
              }
            } catch (error) {
              this.mostrarError('Error de integridad al eliminar cuenta', 'danger');
              console.error('Error al eliminar la cuenta:', error.response ? error.response.data : error);
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
             this.cuentaForm = {id_reserva: cuenta.id_reserva.id_reserva, 
             id_huesped: cuenta.id_huesped.id_huesped,
             tipo_movimiento: cuenta.tipo_movimiento,
             monto: cuenta.monto,
             estado: cuenta.estado};

             this.showModal = true;
           },
           closeModal() {
             this.showModal = false;
           },
           validateForm() {
            if (!this.cuentaForm.id_reserva || !this.cuentaForm.id_huesped || !this.cuentaForm.tipo_movimiento || !this.cuentaForm.monto || !this.cuentaForm.estado) {
              this.mostrarAdvertencia('Complete todos los campos');
              return false;
            }
            return true;
          }, 
           async saveCuenta() {
             if (!this.validateForm()) {
                return;
              }
         
             try {
               if (this.isEditing) {
                this.cuentaForm.fecha_movimiento = new Date().toISOString();
                 await updateCuentaHuesped(this.currentCuentaId, this.cuentaForm);
                 this.mostrarError('Cuenta editada exitosamente', 'success');
                 
               } else {
                this.cuentaForm.fecha_movimiento = new Date().toISOString();
                 await createCuentaHuesped(this.cuentaForm.id_reserva, this.cuentaForm.id_huesped,this.cuentaForm.tipo_movimiento, this.cuentaForm.monto, this.cuentaForm.estado, this.cuentaForm.fecha_movimiento);
                 this.mostrarError('Cuenta creada exitosamente', 'success');
                }
               if (this.busqueda == 0) {
                 await this.fetchCuentasReserva();
                
               }else{
                 await this.fetchCuentasHuesped();
                 
               } 
               this.closeModal();
             } catch (error) {
              if (this.isEditing) {
                this.mostrarError('Error de integridad al editar cuenta', 'danger');
               } else {
                this.cuentaForm.fecha_movimiento = new Date().toISOString();
                this.mostrarError('Error de integridad al crear la cuenta', 'danger');
               }
               console.error('Error al guardar la cuenta:', error.response ? error.response.data : error);
             }
           },
           
           async downloadPDF() {
  const facturaDetalles = document.getElementById('facturaDetalles');
  const originalMaxHeight = facturaDetalles.style.maxHeight;
  facturaDetalles.style.maxHeight = 'none';

  try {
    const canvas = await html2canvas(facturaDetalles, { scale: 0.8 }); // Reducir la escala para mejorar rendimiento
    const imgData = canvas.toDataURL('image/png');
    const pdf = new jsPDF();

    const imgWidth = 190;
    const imgHeight = (canvas.height * imgWidth) / canvas.width;
    let heightLeft = imgHeight;
    let position = 0;

    pdf.addImage(imgData, 'PNG', 10, position, imgWidth, imgHeight);
    heightLeft -= pdf.internal.pageSize.height;

    while (heightLeft >= 0) {
      position = heightLeft - imgHeight;
      pdf.addPage();
      pdf.addImage(imgData, 'PNG', 10, position, imgWidth, imgHeight);
      heightLeft -= pdf.internal.pageSize.height;
    }

    pdf.save('factura.pdf');
  } catch (error) {
    console.error('Error al generar el PDF:', error);
  } finally {
    facturaDetalles.style.maxHeight = originalMaxHeight;
  }
},


  },
};
</script>
<style scoped>
.total-container {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin-top: 20px;
  padding: 5px;
  margin-right: 3.5rem;
  border-radius: 8px;

}

.total-container strong {
  font-size: 1.2rem;
  color: #2c3e50;
  font-weight: bold;
}
</style>
