<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton  title="Administración De Hoteles" />
    </SectionMain>

    <SectionMain>
      <!-- Botón para agregar hotel -->
      <BaseButton @click="openCreateModal" color="info" label="Agregar Hotel" class="mb-4" />

      <!-- Tabla de hoteles -->
      <div class="w-full overflow-auto mb-4">
        <table class="table-auto w-full">
          <thead>
            <tr>
              <th class="px-4 py-2 text-left">Nombre</th>
              <th class="px-4 py-2 text-left">Ubicación</th>
              <th class="px-4 py-2 text-left">Dirección</th>
              <th class="px-4 py-2 text-left">Teléfono</th>
              <th class="px-4 py-2 text-left">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="hotel in hoteles" :key="hotel.id_hotel">
              <td class="border px-4 py-2">{{ hotel.nombre }}</td>
              <td class="border px-4 py-2">{{ hotel.ubicacion }}</td>
              <td class="border px-4 py-2">{{ hotel.direccion }}</td>
              <td class="border px-4 py-2">{{ hotel.telefono }}</td>
              <td class="border px-4 py-2">
                <td class=" px-4 py-2">
                <BaseButton @click="openEditModal(hotel)" color="warning" outline label="Editar" class="g-4" />
                <BaseButton @click="openConfirmDeleteModal(hotel)" color="danger" outline label="Eliminar" class="g-4" />
               </td>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Modal para crear/editar hotel -->
      <ModalForm :isVisible="showModal" :title="isEditing ? 'Editar Hotel' : 'Agregar Hotel'" @close="closeModal">
        <form @submit.prevent="saveHotel">
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

          <BaseButtons>
            <BaseButton :disabled="isSaveDisabled" type="submit" color="info" label="Guardar" />
            <BaseButton @click="closeModal" color="secondary" label="Cancelar" />
          </BaseButtons>
        </form>
      </ModalForm>
  <ModalForm :isVisible="showConfirmDeleteModal" title="Confirmar eliminación" @close="closeConfirmDeleteModal">
  <p>¿Estás seguro de que deseas eliminar este hotel?</p>
  <BaseButtons>
    <BaseButton @click="confirmDeleteHotel" color="danger" label="Eliminar" />
    <BaseButton @click="closeConfirmDeleteModal" color="secondary" label="Cancelar" />
  </BaseButtons>
</ModalForm>
    </SectionMain>
  </LayoutAuthenticated>
</template>

<script>
import { mdiPlus, mdiPencil, mdiDelete } from '@mdi/js';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import FormField from '@/components/FormField.vue';
import FormControl from '@/components/FormControl.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue';
import ModalForm from '@/components/ModalFormHotel.vue';
import SectionMain from '@/components/SectionMain.vue';
import CardBoxModal from '@/components/CardBoxModal.vue';

import { createHotel, getHotels, updateHotel, deleteHotel } from '@/services/hotelService';

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
  },
  data() {
    return {
      hoteles: [],  // Lista de hoteles
      hotelForm: {
        nombre: '',
        ubicacion: '',
        direccion: '',
        telefono: '',
      },
      showModal: false,  // Control de visibilidad del modal
    showConfirmDeleteModal: false,  // Control de visibilidad del modal de confirmación
    isEditing: false,  // Indica si estamos en modo edición o creación
    currentHotelId: null, // ID del hotel que se está editando
    hotelToDelete: null, // Hotel seleccionado para eliminar
    };
  },
  created() {
    this.fetchHotels(); // Cargar hoteles al montar el componente
  },
  methods: {
    async fetchHotels() {
      try {
        const response = await getHotels();
        this.hoteles = response.data;  // Asigna la respuesta a la lista de hoteles
      } catch (error) {
        console.error('Error al obtener los hoteles:', error);
      }
    },
    openCreateModal() {
      this.isEditing = false;
      this.hotelForm = { nombre: '', ubicacion: '', direccion: '', telefono: '' };
      this.showModal = true;
    },
    openEditModal(hotel) {
      this.isEditing = true;
      this.currentHotelId = hotel.id_hotel; // Guarda el ID del hotel que se va a editar
      this.hotelForm = { ...hotel }; // Rellena el formulario con los datos del hotel
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    async saveHotel() {
      try {
        if (this.isEditing) {
          // Actualizar hotel
          await updateHotel(this.currentHotelId, this.hotelForm.nombre, this.hotelForm.ubicacion, this.hotelForm.direccion, this.hotelForm.telefono);
        } else {
          // Crear nuevo hotel
          await createHotel(this.hotelForm.nombre, this.hotelForm.ubicacion, this.hotelForm.direccion, this.hotelForm.telefono);
        }
        this.fetchHotels(); // Actualiza la lista de hoteles
        this.closeModal();  // Cierra el modal
      } catch (error) {
        console.error('Error al guardar el hotel:', error.response ? error.response.data : error);
      }
    },
    openConfirmDeleteModal(hotel) {
    this.hotelToDelete = hotel; // Almacena el hotel a eliminar
    this.showConfirmDeleteModal = true; // Muestra el modal de confirmación
  },
  closeConfirmDeleteModal() {
    this.showConfirmDeleteModal = false; // Cierra el modal de confirmación
    this.hotelToDelete = null; // Resetea el hotel seleccionado
  },
  async confirmDeleteHotel() {
    try {
      if (this.hotelToDelete) {
        await deleteHotel(this.hotelToDelete.id_hotel); // Llama a la función de servicio para eliminar el hotel
        this.fetchHotels(); // Actualiza la lista de hoteles
        this.closeConfirmDeleteModal(); // Cierra el modal
      }
    } catch (error) {
      console.error('Error al eliminar el hotel:', error);
    }
  },
  },
};
</script>

<style scoped>
.table-auto {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}
</style>
