<script setup>
import { ref, onMounted } from 'vue';
import TitleIconOnly from '@/components/TitleIconOnly.vue';
import FormControl from '@/components/FormControl.vue';
import FormField from '@/components/FormField.vue';
import SectionTitle from '@/components/SectionTitle.vue';
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import editarDescuentoModal from '@/components/arce_components/editarDescuentoModal.vue';
import { info_descuentos, crear_descuento, actualizar_descuento, eliminar_descuento, autorizar_descuento } from '@/services/arce_service/descuentoService';
import { mdiBallotOutline, mdiInformation, mdiCheckBold } from '@mdi/js';
import { useMainStore } from '@/stores/main';
import { computed } from 'vue';
import NotificationBar from '@/components/NotificationBar.vue';
import { mdiPencil, mdiTrashCan } from '@mdi/js';


const mainStore = useMainStore();

const userRole = computed(() => mainStore.userRole).value;

console.log(userRole)


const form = ref({
  tipo_descuento: '',
  porcentaje_descuento: 0,
  fecha_aplicacion: new Date().toISOString(),
  quien_aplico: '',
});

const descuentos = ref([]);
const errorMessage = ref('');
const editingDiscountId = ref(null);
const modalVisible = ref(false);
const notificationMessage = ref('');
const showNotification = ref(false);
const notificationColor = ref('info');

// Función para mostrar notificación
const showNotificationMessage = (message, color) => {
  notificationMessage.value = message;
  notificationColor.value = color;
  showNotification.value = true;

  // Ocultar la notificación después de 3 segundos
  setTimeout(() => {
    showNotification.value = false;
  }, 3000);
};

const submitForm = async () => {
  if (form.value.porcentaje_descuento < 0 || form.value.porcentaje_descuento > 100) {
    errorMessage.value = 'El porcentaje debe estar entre 0 y 100.';
    return;
  }

  try {
    const nuevoDescuento = { ...form.value };

    if (editingDiscountId.value) {
      await actualizar_descuento(editingDiscountId.value, nuevoDescuento);
      showNotificationMessage('Descuento actualizado correctamente.', 'success');
    } else {
      await crear_descuento(nuevoDescuento);
      showNotificationMessage('Descuento creado correctamente.', 'success');
    }

    await fetchDescuentos();
    resetForm();
  } catch (error) {
    console.error('Error al guardar descuento:', error);
    showNotificationMessage('Hubo un error al guardar el descuento. Intenta nuevamente.', 'danger');
  }
};

const fetchDescuentos = async () => {
  try {
    descuentos.value = await info_descuentos();
  } catch (error) {
    console.error('Error al obtener descuentos:', error);
  }
};

const resetForm = () => {
  form.value = {
    tipo_descuento: '',
    porcentaje_descuento: 0,
    fecha_aplicacion: new Date().toISOString(),
    quien_aplico: '',
  };
  editingDiscountId.value = null;
  errorMessage.value = '';
  modalVisible.value = false;
};

const editDescuento = (descuento) => {
  form.value = { ...descuento };
  editingDiscountId.value = descuento.id_descuento;
  modalVisible.value = true;
};

const deleteDescuento = async (discountId) => {
  if (confirm('¿Estás seguro de que quieres eliminar este descuento?')) {
    try {
      await eliminar_descuento(discountId);
      await fetchDescuentos();
      showNotificationMessage('Descuento eliminado correctamente.', 'success');
    } catch (error) {
      console.error('Error al eliminar descuento:', error);
      showNotificationMessage('Hubo un error al eliminar el descuento. Intenta nuevamente.', 'danger');
    }
  }
};

const autorizarDescuento = async (discountId) => {
  if (confirm('¿Quieres confirmar este descuento?')) {
    try {
      await autorizar_descuento(discountId, ""); // Enviamos un string vacío
      await fetchDescuentos();
      showNotificationMessage('Descuento autorizado correctamente.', 'success');
    } catch (error) {
      console.error('Error al autorizar descuento:', error);
      showNotificationMessage('Hubo un error al autorizar el descuento. Intenta nuevamente.', 'danger');
    }
  }
};

onMounted(fetchDescuentos);
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <TitleIconOnly :icon="mdiBallotOutline" title="Descuentos" />

      <div v-if="userRole === 'SuperAdmin' || userRole === 'JefeRecepcion'">


        <SectionTitle>Registrar descuento</SectionTitle>

        <form @submit.prevent="submitForm" class="mt-6">

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FormField label="Tipo de Descuento">
              <FormControl v-model="form.tipo_descuento" type="text" required />
            </FormField>
            <FormField label="Porcentaje de Descuento">
              <FormControl v-model.number="form.porcentaje_descuento" type="number" required />
            </FormField>
          </div>

          <div class="flex justify-between">
            <BaseButtons>
              <BaseButton type="submit" color="info" label="Registrar" />
              <BaseButton type="button" color="info" outline label="Reset" @click="resetForm" />
            </BaseButtons>
          </div>

          <p v-if="errorMessage" class="text-red-500">{{ errorMessage }}</p>

          <NotificationBar class="mt-6" v-if="showNotification" :color="notificationColor" :icon="mdiInformation">
            {{ notificationMessage }}
          </NotificationBar>

        </form>

      </div>


      <SectionTitle>Lista de Descuentos</SectionTitle>
      <div class="mt-4">
        <table class="min-w-full hidden md:table">
          <thead class="bg-gray-200">
            <tr>
              <th class="text-left px-4 py-2">Tipo de Descuento</th>
              <th class="text-left px-4 py-2">Porcentaje</th>
              <th class="text-left px-4 py-2">Fecha de Aplicación</th>
              <th class="text-left px-4 py-2">Aplicó</th>
              <th class="text-left px-4 py-2">Autorizó</th>
              <th class="text-left px-4 py-2">Estado</th>
              <th class="text-left px-4 py-2">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="descuento in descuentos" :key="descuento.id_descuento">
              <td class="border px-4 py-2">{{ descuento.tipo_descuento }}</td>
              <td class="border px-4 py-2">{{ descuento.porcentaje_descuento }}%</td>
              <td class="border px-4 py-2">{{ new Date(descuento.fecha_aplicacion).toLocaleDateString() }}</td>
              <td class="border px-4 py-2">{{ descuento.quien_aplico }}</td>
              <td class="border px-4 py-2">{{ descuento.quien_autorizo ? descuento.quien_autorizo : 'Sin autorizar' }}
              </td>
              <td class="border px-4 py-2">{{ descuento.autorizado === 1 ? 'Autorizado' : 'Pendiente' }}</td>
              <td class="border px-4 py-2">
                <BaseButtons v-if="userRole === 'SuperAdmin' || userRole === 'JefeRecepcion'">
                  <BaseButton color="success" :icon="mdiPencil" @click="editDescuento(descuento)" />
                  <BaseButton color="danger" :icon="mdiTrashCan" @click="deleteDescuento(descuento.id_descuento)" />
                  <BaseButton color="warning" :icon="mdiCheckBold"
                    @click="autorizarDescuento(descuento.id_descuento)" />
                </BaseButtons>
              </td>
            </tr>
          </tbody>
        </table>

        <div class="md:hidden">
          <div v-for="descuento in descuentos" :key="descuento.id_descuento" class="border-b border-gray-200 py-4">
            <div class="flex justify-between">
              <span class="font-bold">Tipo de Descuento:</span>
              <span>{{ descuento.tipo_descuento }}</span>
            </div>
            <div class="flex justify-between">
              <span class="font-bold">Porcentaje:</span>
              <span>{{ descuento.porcentaje_descuento }}%</span>
            </div>
            <div class="flex justify-between">
              <span class="font-bold">Fecha de Aplicación:</span>
              <span>{{ new Date(descuento.fecha_aplicacion).toLocaleDateString() }}</span>
            </div>
            <div class="flex justify-between">
              <span class="font-bold">Aplicó:</span>
              <span>{{ descuento.quien_aplico }}</span>
            </div>
            <div class="flex justify-between">
              <span class="font-bold">Autorizó:</span>
              <span>{{ descuento.quien_autorizo ? descuento.quien_autorizo : 'Sin autorizar' }}</span>
            </div>
            <div class="flex justify-between">
              <span class="font-bold">Estado:</span>
              <span>{{ descuento.autorizado === 1 ? 'Autorizado' : 'Pendiente' }}</span>
            </div>
            <div class="flex justify-between">
              <span class="font-bold">Acciones:</span>
              <span>
                <BaseButtons v-if="userRole === 'SuperAdmin' || userRole === 'JefeRecepcion'">
                  <BaseButton color="success" :icon="mdiPencil" @click="editDescuento(descuento)" />
                  <BaseButton color="danger" :icon="mdiTrashCan" @click="deleteDescuento(descuento.id_descuento)" />
                  <BaseButton color="warning" :icon="mdiCheckBold"
                    @click="autorizarDescuento(descuento.id_descuento)" />
                </BaseButtons>
              </span>
            </div>
          </div>
        </div>
      </div>



      <editarDescuentoModal :visible="modalVisible" :form="form" @update:visible="modalVisible = $event"
        @save="submitForm" />
    </SectionMain>
  </LayoutAuthenticated>
</template>
