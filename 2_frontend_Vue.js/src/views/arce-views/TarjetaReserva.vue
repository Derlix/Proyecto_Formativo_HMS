<script setup>
import { reactive } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionMain from '@/components/SectionMain.vue'
import CardBox from '@/components/CardBox.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import BaseButton from '@/components/BaseButton.vue'
import { mdiBallotOutline } from '@mdi/js'
import TitleIconOnly from '@/components/TitleIconOnly.vue'
import BaseButtons from '@/components/BaseButtons.vue'

const selectOptions = [
    { id: '1', label: 'Cédula de Ciudadanía' },
    { id: '2', label: 'Tarjeta de Identidad' },
]

const form = reactive({
    fecha: '2024-10-01',
    habitacion: '101',
    huesped: 'Juan Pérez',
    tipoIdentificacion: selectOptions[0],
    identificacion: '123456789',
    descripcion: 'Avance de efectivo para gastos',
    valor: '200.00',
    autorizado: 'María López'
})

const submitForm = () => {
    console.log('Formulario enviado:', form)
}
</script>

<template>
    <LayoutAuthenticated>
        <SectionMain>
            <TitleIconOnly :icon="mdiBallotOutline" title="Solicitud de Avance de Efectivo" />

            <CardBox @submit.prevent="submitForm" class="mt-6">

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <FormField label="N. Habitación">
                        <FormControl v-model="form.habitacion" type="text" required />
                    </FormField>

                    <FormField label="Huésped">
                        <FormControl v-model="form.huesped" type="text" required />
                    </FormField>

                    <FormField label="Tipo documento">
                        <FormControl v-model="form.tipoIdentificacion" :options="selectOptions" />
                    </FormField>

                    <FormField label="Número documento">
                        <FormControl v-model="form.identificacion" type="text" placeholder="Número documento"
                            required="" />
                    </FormField>

                    <FormField label="Descripción">
                        <FormControl v-model="form.descripcion" type="text" required />
                    </FormField>

                    <FormField label="Fecha">
                        <FormControl v-model="form.fecha" type="date" required />
                    </FormField>

                    <FormField label="Valor">
                        <FormControl v-model="form.valor" type="text" required />
                    </FormField>

                    <FormField label="Autorizado por">
                        <FormControl v-model="form.autorizado" type="text" required />
                    </FormField>
                </div>

                <template #footer>
                    <div class="flex justify-between">
                        <BaseButtons>
                            <BaseButton type="submit" color="info" label="Submit" />
                            <BaseButton type="reset" color="info" outline label="Reset" />
                        </BaseButtons>
                    </div>
                </template>

            </CardBox>
        </SectionMain>
    </LayoutAuthenticated>
</template>
