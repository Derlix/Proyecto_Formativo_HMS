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
import { info_descuentos, crear_descuento } from '@/services/arce_service/descuentoService';
import {
  mdiBallotOutline,
} from '@mdi/js';

const form = ref({
  tipo_descuento: '',
  porcentaje_descuento: 0,
  fecha_aplicacion: "",
  quien_aplico: '',
});

const descuentos = ref([]);

const submitForm = async () => {
  try {
    const nuevoDescuento = {
      tipo_descuento: form.value.tipo_descuento,
      porcentaje_descuento: form.value.porcentaje_descuento,
      fecha_aplicacion: form.value.fecha_aplicacion,
      quien_aplico: form.value.quien_aplico,
    };

    const respuesta = await crear_descuento(nuevoDescuento);
    console.log('Descuento creado:', respuesta);

    await fetchDescuentos();

    form.value = {
      tipo_descuento: '',
      porcentaje_descuento: 0,
      fecha_aplicacion: new Date().toISOString(),
      quien_aplico: '',
    };
  } catch (error) {
    console.error('Error al crear descuento:', error);
  }
};

const fetchDescuentos = async () => {
  try {
    descuentos.value = await info_descuentos();
  } catch (error) {
    console.error('Error al obtener descuentos:', error);
  }
};

// Llama a fetchDescuentos cuando el componente se monta
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
            <BaseButton type="reset" color="info" outline label="Reset" />
          </BaseButtons>
        </div>
      </form>

      <!-- Tabla para mostrar descuentos -->
      <SectionTitle>Lista de Descuentos</SectionTitle>
      <table class="min-w-full mt-4">
        <thead>
          <tr>
            <th class="text-left">Tipo de Descuento</th>
            <th class="text-left">Porcentaje</th>
            <th class="text-left">Fecha de Aplicación</th>
            <th class="text-left">Aplicado Por</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="descuento in descuentos" :key="descuento.id_descuento">
            <td>{{ descuento.tipo_descuento }}</td>
            <td>{{ descuento.porcentaje_descuento }}%</td>
            <td>{{ new Date(descuento.fecha_aplicacion).toLocaleDateString() }}</td>
            <td>{{ descuento.quien_aplico }}</td>
          </tr>
        </tbody>
      </table>

    </SectionMain>
  </LayoutAuthenticated>
</template>
