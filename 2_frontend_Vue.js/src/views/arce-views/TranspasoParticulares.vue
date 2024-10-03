<script setup>
import { reactive } from 'vue'
import SectionMain from '@/components/SectionMain.vue'
import CardBox from '@/components/CardBox.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import BaseDivider from '@/components/BaseDivider.vue'
import BaseButton from '@/components/BaseButton.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import { mdiBallotOutline } from '@mdi/js';
import TitleIconOnly from '@/components/TitleIconOnly.vue'

// Opciones para los selectores
const selectOptions = [
  { id: '1', label: 'Tipo de documento' },
  { id: '2', label: 'Cédula de Ciudadanía' },
  { id: '3', label: 'Tarjeta de Identidad' },
]
 
const form = reactive({
  actual_tipo_cc: selectOptions[0],
  nuevo_tipo_cc: selectOptions[0],
  monto: "$100.000.00"
})

// Función para manejar el envío del formulario
const submit = () => {
  console.log('Formulario enviado:', form)
}
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <TitleIconOnly :icon="mdiBallotOutline" title="Transpaso cuenta" />
      <CardBox form @submit.prevent="submit" class="mt-6">
        <FormField label="Cuenta actual">
          <FormControl v-model="form.actual_tipo_cc" :options="selectOptions" />
          <FormControl v-model="form.actual_numero_cc" type="text" placeholder="Número documento" required=""/>
        </FormField>
        <BaseDivider />
        <FormField label="Transferir A">
          <FormControl v-model="form.nuevo_tipo_cc" :options="selectOptions" />
          <FormControl v-model="form.nuervo_numero_cc" type="text" placeholder="Número documento" required=""/>
        </FormField>
        <BaseDivider />
        <FormField label="Monto transferencia">
          <FormControl v-model="form.monto"  type="text" placeholder="" disabled="true" />
        </FormField>
        <template #footer>
          <BaseButtons>
            <BaseButton type="submit" color="info" label="Tranferir" />
          </BaseButtons>
        </template>
      </CardBox>
    </SectionMain>
  </LayoutAuthenticated>
</template>