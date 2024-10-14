<script setup>
import { computed, ref, onMounted } from 'vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionMain from '@/components/SectionMain.vue'
import CardBoxModal from '@/components/CardBoxModal.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import { obtener_anticipos, actualizar_anticipo, eliminar_anticipo, crear_anticipo } from '@/services/arce_service/anticipoService'
import { mdiPencil, mdiTrashCan, mdiBallotOutline } from '@mdi/js'
import TitleIconOnly from '@/components/TitleIconOnly.vue'
import BaseDivider from '@/components/BaseDivider.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import SectionTitle from '@/components/SectionTitle.vue'
import CardBox from '@/components/CardBox.vue'

const anticipos = ref([])
const editarAnticipo = ref(false)
const eliminarAnticipoModal = ref(false)
const perPage = ref(5)
const currentPage = ref(0)
const advanceId = ref(null)
const crearAnticipoModal = ref(false);


const formData = ref({
    id_reserva: 0,
    id_huesped: 0,
    monto_solicitado: 0,
    monto_aprobado: 0,
    quien_aplico: '',
    metodo_devolucion: 'EFECTIVO',
})

const message = ref('')

// Obtener los anticipos al montar el componente
onMounted(async () => {
    await loadAnticipos()
})

const loadAnticipos = async () => {
    try {
        anticipos.value = await obtener_anticipos()
    } catch (error) {
        message.value = 'Error al obtener los anticipos: ' + (error.data || error.message)
        console.error(error)
    }
}

// Computados para paginación
const itemsPaginated = computed(() =>
    anticipos.value.slice(perPage.value * currentPage.value, perPage.value * (currentPage.value + 1))
)

const numPages = computed(() => Math.ceil(anticipos.value.length / perPage.value))
const currentPageHuman = computed(() => currentPage.value + 1)

const pagesList = computed(() => Array.from({ length: numPages.value }, (_, i) => i))

const submitForm = async () => {
    try {
        const result = await actualizar_anticipo(advanceId.value, formData.value)
        message.value = 'Anticipo actualizado con éxito!'
        console.log(result)
        await loadAnticipos() // Actualiza la lista después de la edición
        editarAnticipo.value = false // Cierra el modal
    } catch (error) {
        message.value = 'Error al actualizar el anticipo: ' + (error.data || error.message)
        console.error(error)
    }
}

const deleteAnticipo = async () => {
    try {
        await eliminar_anticipo(advanceId.value)
        message.value = 'Anticipo eliminado con éxito!'
        await loadAnticipos() // Actualiza la lista después de la eliminación
        eliminarAnticipoModal.value = false // Cierra el modal
    } catch (error) {
        message.value = 'Error al eliminar el anticipo: ' + (error.data || error.message)
        console.error(error)
    }
}

const crearAnticipo = async () => {
    try {
        const result = await crear_anticipo(formData.value);
        message.value = 'Anticipo creado con éxito!';
        console.log(result);
        await loadAnticipos(); // Actualiza la lista después de la creación
    } catch (error) {
        message.value = 'Error al crear el anticipo: ' + (error.data || error.message);
        console.error(error);
    }
}


// Función para abrir el modal de edición y llenar el formulario
const openEditModal = (anticipo) => {
    advanceId.value = anticipo.id_avance
    formData.value = { ...anticipo } // Cargar datos en el formulario
    editarAnticipo.value = true
}

// Función para abrir el modal de eliminación
const openDeleteModal = (anticipo) => {
    advanceId.value = anticipo.id_avance // Guardar el ID del anticipo a eliminar
    eliminarAnticipoModal.value = true
}
</script>

<template>
    <LayoutAuthenticated>
        <SectionMain>
            <TitleIconOnly :icon="mdiBallotOutline" title="Anticipos" />

            <div class="flex justify-end mb-4">
                <button class="bg-blue-500 h-12 rounded-lg font-bold text-white py-2 px-6 shadow-lg"
                    @click="crearAnticipoModal = true">
                    Registrar Anticipo
                </button>
            </div>



            <CardBoxModal v-model="crearAnticipoModal" title="Registrar Anticipo" buttonLabel="Registrar" has-cancel
                @cancel="() => crearAnticipoModal.value = false" @confirm="crearAnticipo">
                <div class="overflow-y-auto">
                    <form @submit.prevent="crearAnticipo" class="grid grid-cols-2 gap-4 p-4">
                        <FormField label="ID Reserva">
                            <FormControl v-model="formData.id_reserva" type="number" required />
                        </FormField>

                        <FormField label="ID Huésped">
                            <FormControl v-model="formData.id_huesped" type="number" required />
                        </FormField>

                        <FormField label="Monto Solicitado">
                            <FormControl v-model="formData.monto_solicitado" type="number" required />
                        </FormField>

                        <FormField label="Monto Aprobado">
                            <FormControl v-model="formData.monto_aprobado" type="number" required />
                        </FormField>

                        <FormField label="¿Quién Aplicó?">
                            <FormControl v-model="formData.quien_aplico" type="text" required />
                        </FormField>

                        <FormField label="Método de Devolución">
                            <select v-model="formData.metodo_devolucion" required>
                                <option value="EFECTIVO">Efectivo</option>
                                <option value="TARJETA">Tarjeta</option>
                                <option value="TRANSFERENCIA">Transferencia</option>
                            </select>
                        </FormField>

                        <div v-if="message" class="text-red-500">{{ message }}</div>
                    </form>
                </div>
            </CardBoxModal>


            <BaseDivider />
            <CardBoxModal v-model="editarAnticipo" title="Editar anticipo" buttonLabel="Enviar" has-cancel
                @cancel="() => editarAnticipo.value = false" @confirm="submitForm">
                <div class="overflow-y-auto">
                    <form @submit.prevent="submitForm" class="grid grid-cols-2 gap-4 p-4">
                        <FormField label="ID Reserva">
                            <FormControl v-model="formData.id_reserva" type="number" required />
                        </FormField>

                        <FormField label="ID Huésped">
                            <FormControl v-model="formData.id_huesped" type="number" required />
                        </FormField>

                        <FormField label="Monto Solicitado">
                            <FormControl v-model="formData.monto_solicitado" type="number" required />
                        </FormField>

                        <FormField label="Monto Aprobado">
                            <FormControl v-model="formData.monto_aprobado" type="number" required />
                        </FormField>

                        <FormField label="¿Quién Aplicó?">
                            <FormControl v-model="formData.quien_aplico" type="text" required />
                        </FormField>

                        <FormField label="Método de Devolución">
                            <select v-model="formData.metodo_devolucion" required>
                                <option value="EFECTIVO">Efectivo</option>
                                <option value="TARJETA">Tarjeta</option>
                                <option value="TRANSFERENCIA">Transferencia</option>
                            </select>
                        </FormField>

                        <div v-if="message" class="text-red-500">{{ message }}</div>
                    </form>
                </div>
            </CardBoxModal>

            <CardBoxModal v-model="eliminarAnticipoModal" title="Eliminar anticipo" buttonLabel="Confirmar" has-cancel
                @cancel="() => eliminarAnticipoModal.value = false" @confirm="deleteAnticipo">
                <p>¿Está seguro de que desea eliminar este anticipo?</p>
            </CardBoxModal>

            <table>
                <thead>
                    <tr>
                        <th>ID Reserva</th>
                        <th>ID Huesped</th>
                        <th>Monto Solicitado</th>
                        <th>Monto Aprobado</th>
                        <th>Quien Aplicó</th>
                        <th>Método Devolución</th>
                        <th />
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="anticipo in itemsPaginated" :key="anticipo.id_reserva">
                        <td data-label="Reserva">{{ anticipo.id_reserva }}</td>
                        <td data-label="Huesped">{{ anticipo.id_huesped }}</td>
                        <td data-label="Monto solicitado">{{ anticipo.monto_solicitado }}</td>
                        <td data-label="Monto aprobado">{{ anticipo.monto_aprobado }}</td>
                        <td data-label="Quien aplicó">{{ anticipo.quien_aplico }}</td>
                        <td data-label="Método de pago">{{ anticipo.metodo_devolucion }}</td>
                        <td>
                            <BaseButtons type="justify-start lg:justify-end" no-wrap>
                                <BaseButton color="info" :icon="mdiPencil" small @click="openEditModal(anticipo)" />
                                <BaseButton color="danger" :icon="mdiTrashCan" small
                                    @click="openDeleteModal(anticipo)" />
                            </BaseButtons>
                        </td>
                    </tr>
                </tbody>
            </table>

            <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800">
                <BaseLevel>
                    <BaseButtons>
                        <BaseButton v-for="page in pagesList" :key="page" :active="page === currentPage"
                            :label="page + 1" :color="page === currentPage ? 'lightDark' : 'whiteDark'" small
                            @click="currentPage = page" />
                    </BaseButtons>
                    <small>Page {{ currentPageHuman }} of {{ numPages }}</small>
                </BaseLevel>
            </div>
        </SectionMain>
    </LayoutAuthenticated>
</template>
