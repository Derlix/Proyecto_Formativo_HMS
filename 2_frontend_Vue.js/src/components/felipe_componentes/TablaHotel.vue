<template>
  <div class="text-right">
    <p class="py-5 text-xl">Hotel que opera actualmente: <span class="font-bold">{{ userNombreHotel }}</span></p>
  </div>
       
           <!-- Botón para agregar hotel -->
        <BaseButton @click="openCreateModal" color="info" label="Agregar Hotel" class="mb-4" />

            <NotificationBar
        v-if="isAlertVisible"
        :color="colorAlert"
        :description="modalMessage"
        :visible="isModalVisible"
          />

        <div class="mb-6 max-w-md mx-left">
          <div class=" flex items-center border rounded-lg shadow-sm ">
            <input
              type="search"
              id="buscarHotel"
              placeholder="Buscar hotel por id"
              class="search-input flex-grow px-4 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:text-white dark:bg-gray-700 "
              v-model="buscarHotel"
              @input="buscar_Hotel"
            />
          </div>
        </div>
            <!-- Tabla de hoteles -->
            <div class="w-full overflow-auto mb-4">
              <table>
                <thead>
                  <tr>
                    <th />
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Ubicación</th>
                    <th>Dirección</th>
                    <th>Teléfono</th>
                   
                    <th />
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="hotel in hoteles" :key="hotel.id_hotel">
                    <td class="border-b-0 lg:w-6 before:hidden">
                
              </td>
                    <td data-label="ID HOTEL">
                      {{ hotel.id_hotel }}
                    </td>
                    <td data-label="NOMBRE HOTEL" >{{ hotel.nombre }}</td>
                    <td data-label="UBICACION HOTEL" >{{ hotel.ubicacion }}</td>
                    <td data-label="DIRECCION HOTEL" >{{ hotel.direccion }}</td>
                    <td data-label="TELEFONO HOTEL" >{{ hotel.telefono }}</td>
                    <td class="before:hidden lg:w-1 whitespace-nowrap">
                      <BaseButtons type="justify-start lg:justify-end" no-wrap>
                        <BaseButton @click="openCambiarHotelModal(hotel)"  :icon="mdiRotateRight" small color="success"  class="g-4" />
                        <BaseButton @click="openEditModal(hotel)" :icon="mdiEye" small color="warning"  class="g-4" />
                        <BaseButton @click="openConfirmDeleteModal(hotel)" :icon="mdiTrashCan" small color="danger"  class="g-4" />
                      </BaseButtons>
                    </td>
                    
                  </tr>
                </tbody>
              </table>
            
            </div>
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
                  @click="handlePageClick(page)"
                />
              </BaseButtons>
              <small>Página {{ currentPage }} de {{ TotalPages }}</small>
          </BaseLevel>
      </div>
      
      
      
            <!-- Modal para crear/editar hotel -->
            <CardBoxModal
              v-model="showModal"
              :title="isEditing ? 'Editar Hotel' : 'Agregar Hotel'"
              buttonLabel="Guardar"
              hasCancel
              @confirm="saveHotel"
              @cancel="closeModal"
            >
              <form @submit.prevent="saveHotel" class="space-y-4">
                <FormField label="Nombre del Hotel" help="Ingrese el nombre del hotel">
                  <FormControl v-model="hotelForm.nombre" name="nombre" />
                </FormField>
      
                <FormField label="Ubicación" help="Ingrese la ubicación del hotel">
                  <FormControl v-model="hotelForm.ubicacion" name="ubicacion" />
                </FormField>
      
                <FormField label="Dirección" help="Ingrese la dirección del hotel">
                  <FormControl v-model="hotelForm.direccion" name="direccion" />
                </FormField>
      
                <FormField label="Teléfono" help="Ingrese el teléfono del hotel">
                  <FormControl v-model="hotelForm.telefono" name="telefono" type="text" />
                </FormField>
              </form>
            </CardBoxModal>
  
            <!-- Modal de cambiar id de hotel -->
            <CardBoxModal
              v-model="showModalCambiarHotelId"
              title="Cambiar de hotel"
              buttonLabel="Confirmar"
              hasCancel
              @confirm="confirmCambiarHotel"
              @cancel="closeConfirmCambiarHotelModal"
            >
            <!-- Mostrar mensaje y id del hotel al que va cambiar -->
              <p class="text-center text-2xl">¿Estás seguro de cambiar a <b class="text-blue-600	">{{ hotelToCambiar?.nombre }}</b>?</p> 
            </CardBoxModal>
      
            <!-- Modal de confirmación de eliminación -->
            <CardBoxModal
              v-model="showConfirmDeleteModal"
              title="Confirmar eliminación"
              buttonLabel="Eliminar"
              hasCancel
              @confirm="confirmDeleteHotel"
              @cancel="closeConfirmDeleteModal"
            >
              <p>¿Estás seguro de que deseas eliminar este hotel?</p>
            </CardBoxModal>
      
      </template>
      
  <script>
  import { computed, ref, onMounted } from 'vue'
  import { useMainStore } from '@/stores/main'
  import FormField from '@/components/FormField.vue';
  import NotificationBar from '../alejo_components/NotificationBar.vue';
  import FormControl from '@/components/FormControl.vue';
  import BaseButton from '@/components/BaseButton.vue';
  import BaseButtons from '@/components/BaseButtons.vue';
  import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue';
  import ModalForm from '@/components/ModalFormHotel.vue';
  import SectionMain from '@/components/SectionMain.vue';
  import CardBoxModal  from '@/components/felipe_componentes/CardBoxModal.vue';
  import { mdiEye, mdiTrashCan,mdiRotateRight } from '@mdi/js';
  import { createHotel, getHotels, updateHotel, deleteHotel, getHotelsByPage, getHotelsByPageUser, getHotelById, getHotelByIdAll } from '@/services/felipe_services/hotelService';
  import BaseLevel from '@/components/BaseLevel.vue';
  import {updateIdHotel} from '@/services/busta_service/CambiarHotelService'
  const mainStore = useMainStore()
  export default {
    components: {
      FormField,
      FormControl,
      BaseButton,
      BaseButtons,
      SectionTitleLineWithButton,
      ModalForm,
      SectionMain,
      CardBoxModal,
      BaseLevel,
      NotificationBar,
    },
    data() {
      return {
        hoteles: [],
        hotelForm: {
          nombre: '',
          ubicacion: '',
          direccion: '',
          telefono: '',
        },
        showModal: false,
        showConfirmDeleteModal: false,
        showModalCambiarHotelId: false,
        isEditing: false,
        currentHotelId: null,
        hotelToDelete: null,
        hotelToCambiar: null,
        mdiEye,  // Assign the icons to data directly
        mdiTrashCan,
        mdiRotateRight,
        TotalPages : 0,
        isSuperAdmin: false,
        currentPage : 1,
        buscarHotel : '',
        hotel : {},
        hotelActivo: '',
        isModalVisible: false,
        modalMessage: '',
        isAlertVisible : false,
        colorAlert: '',
      };
    },
    computed: {
      userIdHotel() {
        return mainStore.userIdHotel;
      },
      userNombreHotel() {
        return mainStore.nombreHotelOperando;
      }
    },
    mounted() {
      if (mainStore.userRole === 'SuperAdmin') {
        this.fetchHotels();
      } else {
        this.fetchHotelsUser();
      }
    },
    methods: {
    handlePageClick(page) {
        this.currentPage = page;
        if (mainStore.userRole === 'SuperAdmin') {
          this.fetchHotels();
        } else {
          this.fetchHotelsUser();
        }
      },
    async fetchHotelsUser() {
      try {
        const response = await getHotelsByPageUser(this.currentPage, 5);
        this.TotalPages = response.data.total_pages;
        this.hoteles = response.data.hoteles;
      } catch (error) {
        console.error('Error al obtener los hoteles:', error);
      }
    },
    async fetchHotels() {
      try {
        const response = await getHotelsByPage(this.currentPage, 5);
        this.TotalPages = response.data.total_pages;
        this.hoteles = response.data.hoteles;
      } catch (error) {
        console.error('Error al obtener los hoteles:', error);
      }
    },
    async buscar_Hotel() {
    if (this.buscarHotel.trim() === '') {
      if (mainStore.userRole === 'SuperAdmin') {
        this.fetchHotels();
      } else {
        this.fetchHotelsUser();
      }
    } else {
      // Search for a specific hotel by ID
      try {
        // Si rol es SuperAdmin debe ser getHotelByIdAll y si es JefeRecepcion getHotelById
        let response;
        if (mainStore.userRole === 'SuperAdmin') {
          response = await getHotelByIdAll(this.buscarHotel);
        } else {
          response = await getHotelById(this.buscarHotel);
        }
        if (response && response.data) {
          this.hotel = response.data;
          this.hoteles = [this.hotel]; // Set the search result in the list
        } else {
          this.hoteles = []; // No hotel found
          this.hotel = null;
          alert('Hotel no encontrado');
        }
      } catch (error) {
       
        this.hoteles = [];
        this.hotel = null;
      }
    }
  },
    openCreateModal() {
      this.isEditing = false;
      this.hotelForm = { nombre: '', ubicacion: '', direccion: '', telefono: '' };
      this.showModal = true;
    },
    openCambiarHotelModal() {
      this.isEditing = false;
      this.hotelForm = { nombre: '', ubicacion: '', direccion: '', telefono: '' };
      this.showModal = true;
    },
    openEditModal(hotel) {
      this.isEditing = true;
      this.currentHotelId = hotel.id_hotel;
      this.hotelForm = { ...hotel };
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    validateForm() {
      if (!this.hotelForm.nombre || !this.hotelForm.ubicacion || !this.hotelForm.direccion || !this.hotelForm.telefono) {
        alert('Todos los campos son obligatorios.');
        return false;
      }
      return true;
    },
    async saveHotel() {
      if (!this.validateForm()) {
        return;
      }
  
      try {
        if (this.isEditing) {
          await updateHotel(this.currentHotelId, this.hotelForm.nombre, this.hotelForm.ubicacion, this.hotelForm.direccion, this.hotelForm.telefono);
          this.modalMessage = "Hotel actualizado con éxito";
          this.isAlertVisible = true;
          this.colorAlert = 'warning';
          setTimeout(() => {
            this.isAlertVisible  = false;
          }, 3000);
        
        } else {
          await createHotel(this.hotelForm.nombre, this.hotelForm.ubicacion, this.hotelForm.direccion, this.hotelForm.telefono);
          this.modalMessage = "Hotel creado con éxito";
          this.isAlertVisible = true;
          this.colorAlert = 'success';
          setTimeout(() => {
            this.isAlertVisible  = false;
          }, 3000);
        
        }
          if (mainStore.userRole === 'SuperAdmin') {
          this.fetchHotels();
        } else {
          this.fetchHotelsUser();
        }
        this.closeModal();
      } catch (error) {
          this.modalMessage = "Error al actualizar el hotel";
          this.isAlertVisible = true;
          this.colorAlert = 'danger';
          setTimeout(() => {
            this.isAlertVisible  = false;
          }, 3000);
        // console.error('Error al guardar el hotel:', error.response ? error.response.data : error);
      }
    },
    openConfirmDeleteModal(hotel) {
      this.hotelToDelete = hotel;
      this.showConfirmDeleteModal = true;
    },
    closeConfirmDeleteModal() {
      this.showConfirmDeleteModal = false;
      this.hotelToDelete = null;
    },
    openCambiarHotelModal(hotel) {
        this.hotelToCambiar = hotel; // Asigna el hotel a hotelToCambiar
        this.showModalCambiarHotelId = true;
    },
    closeConfirmCambiarHotelModal() {
      this.showModalCambiarHotelId = false;
      this.hotelToCambiar = null;
    },
    async confirmDeleteHotel() {
      try {
        if (this.hotelToDelete) {
          await deleteHotel(this.hotelToDelete.id_hotel);
          this.modalMessage = "Hotel eliminado con éxito";
          this.isAlertVisible = true;
          this.colorAlert = 'success';
          setTimeout(() => {
            this.isAlertVisible  = false;
          }, 3000);
              if (mainStore.userRole === 'SuperAdmin') {
            this.fetchHotels();
          } else {
            this.fetchHotelsUser();
          }
          this.closeConfirmDeleteModal();
        }
      } catch (error) {
          this.modalMessage = "Error de integridad al eliminar hotel";
          this.isAlertVisible = true;
          this.colorAlert = 'danger';
          setTimeout(() => {
            this.isAlertVisible  = false;
          }, 3000);
        // console.error('Error al eliminar el hotel:', error);
      }
    },
    // cambiar hotel por id del hotel seleccionado
    async confirmCambiarHotel() {
        try {
          if (this.hotelToCambiar) {
            await updateIdHotel(this.hotelToCambiar.id_hotel);
  
            mainStore.setUser({
              id_hotel: this.hotelToCambiar.id_hotel,
              nombre_hotel: this.hotelToCambiar.nombre,
            });
            if (mainStore.userRole === 'SuperAdmin') {
              this.fetchHotels();
            } else {
              this.fetchHotelsUser();
            }
            this.closeConfirmCambiarHotelModal();
          }
        } catch (error) {
          console.error('Error al cambiar el hotel:', error);
        }
      },
    },
  };
  </script>