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
import { info_descuentos, crear_descuento, actualizar_descuento, eliminar_descuento } from '@/services/arce_service/descuentoService';
import { mdiBallotOutline } from '@mdi/js';

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

const submitForm = async () => {
  if (form.value.porcentaje_descuento < 0 || form.value.porcentaje_descuento > 100) {
    errorMessage.value = 'El porcentaje debe estar entre 0 y 100.';
    return;
  }

  try {
    const nuevoDescuento = {
      tipo_descuento: form.value.tipo_descuento,
      porcentaje_descuento: form.value.porcentaje_descuento,
      fecha_aplicacion: form.value.fecha_aplicacion,
      quien_aplico: form.value.quien_aplico,
    };

    if (editingDiscountId.value) {
      await actualizar_descuento(editingDiscountId.value, nuevoDescuento);
      errorMessage.value = 'Descuento actualizado correctamente.';
    } else {
      await crear_descuento(nuevoDescuento);
      errorMessage.value = 'Descuento creado correctamente.';
    }

    await fetchDescuentos();
    resetForm();
  } catch (error) {
    console.error('Error al guardar descuento:', error);
    errorMessage.value = 'Hubo un error al guardar el descuento. Intenta nuevamente.';
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
      errorMessage.value = 'Descuento eliminado correctamente.';
    } catch (error) {
      console.error('Error al eliminar descuento:', error);
      errorMessage.value = 'Hubo un error al eliminar el descuento. Intenta nuevamente.';
    }
  }
};

onMounted(fetchDescuentos);
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <TitleIconOnly :icon="mdiBallotOutline" title="Descuentos" />
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
      </form>

      <SectionTitle>Lista de Descuentos</SectionTitle>
      <table class="min-w-full mt-4">
        <thead>
          <tr>
            <th class="text-left">Tipo de Descuento</th>
            <th class="text-left">Porcentaje</th>
            <th class="text-left">Fecha de Aplicación</th>
            <th class="text-left">Aplicado Por</th>
            <th class="text-left">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="descuento in descuentos" :key="descuento.id_descuento">
            <td>{{ descuento.tipo_descuento }}</td>
            <td>{{ descuento.porcentaje_descuento }}%</td>
            <td>{{ new Date(descuento.fecha_aplicacion).toLocaleDateString() }}</td>
            <td>{{ descuento.quien_aplico }}</td>
            <td>
              <BaseButton color="success" @click="editDescuento(descuento)" label="Editar" />
            </td>
            <td>
              <BaseButton color="danger" @click="deleteDescuento(descuento.id_descuento)" label="Eliminar" />
            </td>
          </tr>
        </tbody>
      </table>

      <editarDescuentoModal :visible="modalVisible" :form="form" @update:visible="modalVisible = $event"
        @save="submitForm" />
    </SectionMain>
  </LayoutAuthenticated>
</template>
