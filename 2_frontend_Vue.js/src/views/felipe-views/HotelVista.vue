<script setup>
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import { mdiPlus, mdiPencil, mdiDelete } from '@mdi/js'
import SectionFullScreen from '@/components/SectionFullScreen.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import CardBox from '@/components/CardBox.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import LayoutGuest from '@/layouts/LayoutGuest.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import * as chartConfig from '@/components/Charts/chart.config.js'
import SectionMain from '@/components/SectionMain.vue'
import ModalForm from '@/components/ModalFormHotel.vue' // Importar el nuevo componente


// Data reactiva para el formulario de hotel
const hotelForm = reactive({
  id: null,
  name: '',
  location: '',
  address: '',
  phone: '',
})

// Lista de hoteles (en una aplicación real, esto debería venir de una API)
const hotels = ref([
  { id: 1, name: 'Hotel Paradise', location: 'Miami', address: 'cll 12 avn 45', phone: '52143235' },
  { id: 2, name: 'Mountain Retreat', location: 'Denver', address: 'Main St 123', phone: '12345678' },
  { id: 3, name: 'City Lights', location: 'New York', address: '5th Avenue', phone: '87654321' },
])

// Estado de visibilidad del modal y edición
const showModal = ref(false)
const isEditing = ref(false)

// Router para la navegación
const router = useRouter()

// Función para mostrar el modal de creación de un nuevo hotel
const createHotel = () => {
  hotelForm.id = null
  hotelForm.name = ''
  hotelForm.location = ''
  hotelForm.address = ''
  hotelForm.phone = ''
  showModal.value = true
  isEditing.value = false
}

// Función para editar un hotel existente
const editHotel = (hotel) => {
  hotelForm.id = hotel.id
  hotelForm.name = hotel.name
  hotelForm.location = hotel.location
  hotelForm.address = hotel.address
  hotelForm.phone = hotel.phone
  showModal.value = true
  isEditing.value = true
}

// Función para eliminar un hotel
const deleteHotel = (hotelId) => {
  hotels.value = hotels.value.filter(hotel => hotel.id !== hotelId)
}

// Función para guardar (crear o editar) un hotel
const saveHotel = () => {
  if (isEditing.value) {
    // Actualizar hotel existente
    const index = hotels.value.findIndex(hotel => hotel.id === hotelForm.id)
    if (index !== -1) {
      hotels.value[index] = { ...hotelForm }
    }
  } else {
    // Crear nuevo hotel
    hotels.value.push({ ...hotelForm, id: hotels.value.length + 1 })
  }
  showModal.value = false
}

// Computed para deshabilitar el botón de guardar si los campos están vacíos
const isSaveDisabled = computed(() => {
  return !hotelForm.name || !hotelForm.location || !hotelForm.address || !hotelForm.phone
})
</script>

<template>
 <LayoutAuthenticated>
      <sectionMain>
      <SectionTitleLineWithButton :icon="mdiChartTimelineVariant" title="Administracion De Hoteles"></SectionTitleLineWithButton>
    </sectionMain>

    <sectionMain>
      <BaseButton @click="createHotel" color="info" label="Agregar Hotel" :icon="mdiPlus" class="mb-4" />
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
              <tr v-for="hotel in hotels" :key="hotel.id">
                <td class="border px-4 py-2">{{ hotel.name }}</td>
                <td class="border px-4 py-2">{{ hotel.location }}</td>
                <td class="border px-4 py-2">{{ hotel.address }}</td>
                <td class="border px-4 py-2">{{ hotel.phone }}</td>
                <td class="border px-4 py-2">
                  <BaseButton @click="editHotel(hotel)" color="warning" outline label="Editar" :icon="mdiPencil" />
                  <BaseButton @click="deleteHotel(hotel.id)" color="danger" outline label="Eliminar" :icon="mdiDelete" />
                </td>
              </tr>
            </tbody>
          </table>
        </div>
    </sectionMain>
  <!-- Modal para creación/modificación de hotel -->
  <ModalForm :isVisible="showModal" :title="isEditing ? 'Editar Hotel' : 'Agregar Hotel'" @close="showModal = false">
          <form @submit.prevent="saveHotel">
            <FormField label="Nombre del Hotel" help="Ingrese el nombre del hotel">
              <FormControl v-model="hotelForm.name" name="name" />
            </FormField>

            <FormField label="Ubicación" help="Ingrese la ubicación del hotel">
              <FormControl v-model="hotelForm.location" name="location" />
            </FormField>

            <FormField label="Dirección" help="Ingrese la dirección del hotel">
              <FormControl v-model="hotelForm.address" name="address" />
            </FormField>

            <FormField label="Teléfono" help="Ingrese el teléfono del hotel">
              <FormControl v-model="hotelForm.phone" name="phone" type="text" />
            </FormField>

            <BaseButtons>
              <BaseButton :disabled="isSaveDisabled" type="submit" color="info" label="Guardar" />
              <BaseButton @click="showModal = false" color="secondary" label="Cancelar" />
            </BaseButtons>
          </form>
        </ModalForm>
 </LayoutAuthenticated>
</template>

<style scoped>
.table-auto {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}

.text-center {
  text-align: center;
}

.w-full {
  width: 100%;
}

.h-full {
  height: 100%;
}

.p-8 {
  padding: 2rem;
}

.overflow-auto {
  overflow: auto;
}
</style>
