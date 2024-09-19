<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton title="Administración De Hoteles" />
    </SectionMain>

    <SectionMain>
      <!-- Botón para agregar hotel -->
      <BaseButton @click="openCreateModal" color="info" label="Agregar Hotel" class="mb-4" />

      <!-- Tabla de hoteles -->
      <div class="w-full overflow-auto mb-4">
        <table>
          <thead>
            <tr>
              <th />
              <th>Nombre</th>
              <th>Ubicación</th>
              <th>Dirección</th>
              <th>Teléfono</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr v-for="hotel in hoteles" :key="hotel.id_hotel">
              <td class="border-b-0 lg:w-6 before:hidden"></td>
              <td>{{ hotel.nombre }}</td>
              <td>{{ hotel.ubicacion }}</td>
              <td>{{ hotel.direccion }}</td>
              <td>{{ hotel.telefono }}</td>
              <td class="before:hidden lg:w-1 whitespace-nowrap">
                <BaseButtons type="justify-start lg:justify-end" no-wrap>
                  <BaseButton @click="openEditModal(hotel)" :icon="mdiEye" small color="warning" class="g-4" />
                  <BaseButton @click="openConfirmDeleteModal(hotel)" :icon="mdiTrashCan" small color="danger" class="g-4" />
                </BaseButtons>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Modal para crear/editar hotel usando CardBoxModal -->
<!-- Modal para crear/editar hotel usando CardBoxModal -->
<CardBoxModal
  v-model="showModal"
  :title="isEditing ? 'Editar Hotel' : 'Agregar Hotel'"
  :hasCancel="true"
  buttonLabel="Guardar"
  @confirm="saveHotel"
  @cancel="closeModal"
>
  <!-- Contenedor con padding y scroll -->
  <div class="p-4 max-h-[60vh] overflow-y-auto">
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
    </form>
  </div>

  <!-- Botones de acción bien alineados dentro del modal -->
  <template #footer>
    <BaseButtons class="justify-end p-4">
      <BaseButton @click="closeModal" color="secondary" label="Cancelar" />
      <BaseButton :disabled="isSaveDisabled" @click="saveHotel" color="info" label="Guardar" />
    </BaseButtons>
  </template>
</CardBoxModal>


      <!-- Modal de confirmación de eliminación usando CardBoxModal -->
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

    </SectionMain>
  </LayoutAuthenticated>
</template>

<script>
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import FormField from '@/components/FormField.vue';
import FormControl from '@/components/FormControl.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue';
import CardBoxModal from '@/components/CardBoxModal.vue';
import SectionMain from '@/components/SectionMain.vue';
import { mdiEye, mdiTrashCan } from '@mdi/js';
import { createHotel, getHotels, updateHotel, deleteHotel } from '@/services/hotelService';

export default {
  components: {
    LayoutAuthenticated,
    FormField,
    FormControl,
    BaseButton,
    BaseButtons,
    SectionTitleLineWithButton,
    CardBoxModal,
    SectionMain,
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
      isEditing: false,
      currentHotelId: null,
      hotelToDelete: null,
      mdiEye,
      mdiTrashCan,
    };
  },
  created() {
    this.fetchHotels();
  },
  methods: {
    async fetchHotels() {
      try {
        const response = await getHotels();
        this.hoteles = response.data;
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
      this.currentHotelId = hotel.id_hotel;
      this.hotelForm = { ...hotel };
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    async saveHotel() {
      try {
        if (this.isEditing) {
          await updateHotel(this.currentHotelId, this.hotelForm);
        } else {
          await createHotel(this.hotelForm);
        }
        this.fetchHotels();
        this.closeModal();
      } catch (error) {
        console.error('Error al guardar el hotel:', error.response ? error.response.data : error);
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
    async confirmDeleteHotel() {
      try {
        if (this.hotelToDelete) {
          await deleteHotel(this.hotelToDelete.id_hotel);
          this.fetchHotels();
          this.closeConfirmDeleteModal();
        }
      } catch (error) {
        console.error('Error al eliminar el hotel:', error);
      }
    },
  },
};
</script>
