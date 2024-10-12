<template>
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
    <FormField label="Numero de reserva" help="Ingrese el numero de la reserva">
      <FormControl v-model="cuentaForm.id_reserva" name="id_reserva" />
    </FormField>

    <!-- Campo cédula del huésped -->
    <FormField label="Cédula del huésped" help="Ingrese cédula del huésped">
      <FormControl v-model="cuentaForm.id_huesped" name="id_huesped" />
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
      <FormControl v-model="cuentaForm.monto" name="monto" type="text" />
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
        <p v-else>No hay transacciones para mostrar.</p>
      </div>
      
      <!-- Botón para descargar PDF -->
     
    </div>
    
  </div>
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
    
    };
  },
  methods: {
  async openDetallesmodal() {

  this.showDetalles = true;
  console.log(showDetalles.value);
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

    async realizarBusqueda() {
      if (this.buscarReserva.trim()) {
        await this.fetchCuentasReserva();
        this.busqueda = 0;
      } else if (this.buscarCedula.trim()) {
        await this.fetchCuentasHuesped();
        this.busqueda = 1;
      } else {
        alert('Por favor ingrese un número de reserva o una cédula');
      }
    },
    async fetchCuentasHuesped() {
      try {
        const response = await getCuentaHuespedByIdHuesped(this.buscarCedula);
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
        } else {
        this.limpiarResultados();
        this.mostrarAdvertencia('No se encontraron cuentas para este huésped');
      }
    } catch (error) {
      this.limpiarResultados();
      this.mostrarAdvertencia('Hubo un error al buscar el huésped');
      console.error(error);
    }
  },
    async fetchCuentasReserva() {
      try {
        const response = await getCuentaHuespedByIdReserva(this.buscarReserva);
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
        }else {
        this.limpiarResultados();
        this.mostrarAdvertencia('No se encontraron cuentas para esta reserva');
      }
    } catch (error) {
      this.limpiarResultados();
      this.mostrarAdvertencia('Hubo un error al buscar la reserva');
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
                 this.fetchCuentasReserva();
                 this.closeConfirmDeleteModal();

                 if (this.busqueda == 0) {
                 await this.fetchCuentasReserva();
                
               }else{
                 await this.fetchCuentasHuesped();
                
               }
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
              alert('Todos los campos son obligatorios.');
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
               } else {
                this.cuentaForm.fecha_movimiento = new Date().toISOString();
                 await createCuentaHuesped(this.cuentaForm.id_reserva, this.cuentaForm.id_huesped,this.cuentaForm.tipo_movimiento, this.cuentaForm.monto, this.cuentaForm.estado, this.cuentaForm.fecha_movimiento);
               }
               if (this.busqueda == 0) {
                 await this.fetchCuentasReserva();
                
               }else{
                 await this.fetchCuentasHuesped();
                 
               } 
               this.closeModal();
             } catch (error) {
              this.mostrarAdvertencia('Hubo un error al guardar la cuenta');
               console.error('Error al guardar la cuenta:', error.response ? error.response.data : error);
             }
           },
  async downloadPDF() {
  const facturaDetalles = document.getElementById('facturaDetalles');

  // Guarda el estado actual del estilo
  const originalMaxHeight = facturaDetalles.style.maxHeight;
  facturaDetalles.style.maxHeight = 'none'; // Elimina el límite de altura

  // Captura el contenido del modal
  html2canvas(facturaDetalles, { scale: 1, width: facturaDetalles.offsetWidth, height: facturaDetalles.scrollHeight }).then((canvas) => {
    const imgData = canvas.toDataURL('image/png', 1);
    const pdf = new jsPDF();

    const imgWidth = 190; // Ancho del PDF
    const pageHeight = pdf.internal.pageSize.height;
    const imgHeight = (canvas.height * imgWidth) / canvas.width;
    let heightLeft = imgHeight;

    let position = 0;

    // Agregar la primera imagen
    pdf.addImage(imgData, 'PNG', 10, position, imgWidth, imgHeight);
    heightLeft -= pageHeight;

    // Manejar el contenido que excede la altura de la página
    while (heightLeft >= 0) {
      position = heightLeft - imgHeight;
      pdf.addPage();
      pdf.addImage(imgData, 'PNG', 10, position, imgWidth, imgHeight);
      heightLeft -= pageHeight;
    }

    // Almacenar el PDF
    pdf.save('factura.pdf');

    // Restaura el estilo original
    facturaDetalles.style.maxHeight = originalMaxHeight;
  }).catch((error) => {
    console.error('Error al generar el PDF:', error);
    // Restaura el estilo original en caso de error
    facturaDetalles.style.maxHeight = originalMaxHeight;
  });
},
fechaActual() {
  const hoy = new Date();

  return hoy.toLocaleDateString('es-ES'); // Cambia el idioma según sea necesario
},

  },
};
</script>

