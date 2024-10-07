<script setup>
import { ref } from 'vue'
import TitleIconOnly from '@/components/TitleIconOnly.vue'
import FormControl from '@/components/FormControl.vue'
import FormField from '@/components/FormField.vue'
import SectionTitle from '@/components/SectionTitle.vue'
import SectionMain from '@/components/SectionMain.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'

import {
  mdiBallotOutline,
} from '@mdi/js'

// Aquí puedes definir cualquier ref o reactive que necesites para el formulario
const form = ref({
  habitacion: '',
  huesped: '',
  descripcion: '',
  descuento: '',
  elaboradoPor: '',
  autorizadoPor: '',
});

const submitForm = () => {
  console.log('Formulario enviado', form.value);
}
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>

      <TitleIconOnly :icon="mdiBallotOutline" title="Descuentos" />

      <SectionTitle>Registrar descuento</SectionTitle>

      <form @submit.prevent="submitForm" class="mt-6">

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <FormField label="Habitación">
            <FormControl v-model="form.habitacion" type="text" required />
          </FormField>
          <FormField label="Huésped">
            <FormControl v-model="form.huesped" type="text" required />
          </FormField>
        </div>

        <FormField label="Descripción">
          <FormControl v-model="form.descripcion" type="text" required />
        </FormField>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <FormField label="Descuento">
            <FormControl v-model="form.descuento" type="text" required />
          </FormField>
          <FormField label="Elaborado por">
            <FormControl v-model="form.elaboradoPor" type="text" required />
          </FormField>
          <FormField label="Autorizado por">
            <FormControl v-model="form.autorizadoPor" type="text" required />
          </FormField>
        </div>

        <div class="flex justify-between">
          <BaseButtons>
            <BaseButton type="submit" color="info" label="Submit" />
            <BaseButton type="reset" color="info" outline label="Reset" />
          </BaseButtons>
        </div>

      </form>
      
    </SectionMain>
  </LayoutAuthenticated>
</template>
