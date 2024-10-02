<script setup>
import { onMounted, ref } from 'vue';
import { mdiEye, mdiTrashCan } from '@mdi/js';
import { createReport, getReportByPage, updateReport } from '@/services/informeLlavesService';
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseLevel from '@/components/BaseLevel.vue';
import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue';

const reports = ref([]);
const TotalPages = ref(0);
const currentPage = ref(1);
const activarModal = ref(false);
const currentReport = ref({});

const openCreateModal = () => {
  activarModal.value = true;
};

const cancelCreate = () => {
  activarModal.value = false;
  currentReport.value = '';
};

const cancelEdit = () => {
  activarModal.value = false;
};

const fechtReports = async () => {
  try {
    const response = await getReportByPage(currentPage.value);
    reports.value = response.data.informes;
    TotalPages.value = response.data.total_pages;
  } catch (error) {
    alert("Error al obtener informes: ", error)
  }
}

const create_Report = async () => {
    try {
        await createReport(currentReport.value.habitacion, currentReport.value.estado_reportado);  // Cambiado a estado_reportado
        fechtReports();
        alert("Informe Creado Con Exito");
    } catch (error) {
        alert('Error al insertar informe: ', error);
    }
}

const update_Report = async () => {
    try {
        await updateReport(currentReport.value.id_informe, currentReport.value.habitacion, currentReport.value.estado_reportado);  // Cambiado a estado_reportado
        fechtReports();
        alert("Informe Actualizado Con Exito");
    } catch (error) {
        alert('Error al actualizar informe: ', error);
    }
}

onMounted(() => {
  fechtReports();
})

</script>

<template>
    <CardBoxModal v-model="activarModal" title="Editar Informe" buttonLabel="Guardar cambios" has-cancel @cancel="cancelEdit" @confirm="update_Report ">
        <form @submit.prevent="update_Report()">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="mb-4">
                    <label for="id_habitacion" class="block text-gray-700 font-medium dark:text-white">habitacion:</label>
                    <input type="text" id="id_habitacion" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" v-model="currentReport.id_habitacion" required/>
                </div>
                <div class="mb-4">
                    <label for="precio" class="block text-gray-700 font-medium dark:text-white">Estado Reportado:</label>
                    <input type="text" id="precio" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" v-model="currentReport.estado_reportado" required/>
                </div>
            </div>
        </form>
    </CardBoxModal>

    <CardBoxModal v-model="activarModal" title="Crear Informe" class="dark:text-white" buttonLabel="Crear Informe" has-cancel @cancel="cancelCreate" @confirm="create_Report">
        <form @submit.prevent="create_Report()">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="mb-4">
                    <label for="habitacion" class="block text-gray-700 font-medium dark:text-white">Habitacion:</label>
                    <input type="number" id="habitacion" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" v-model="currentReport.habitacion" required/>
                </div>
                <div class="mb-4">
                    <label for="estado" class="block text-gray-700 font-medium dark:text-white">Estado Reportado:</label>
                    <select id="estado" 
                            class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" 
                            v-model="currentReport.estado_reportado"
                            required>
                        <option value="LIMPIA">LIMPIA</option>
                        <option value="SUCIA">SUCIA</option>
                        <option value="MANTENIMIENTO">MANTENIMIENTO</option>
                    </select>
                </div>
            </div>
        </form>
    </CardBoxModal>
    <LayoutAuthenticated>
        <SectionMain>
            <h1 class="text-black dark:text-white text-2xl font-bold mb-8">Informes De Ama De llaves</h1>
            <div>
                <div class="flex">
                    <div>
                        <BaseButton @click="openCreateModal" color="info" label="Generar Informe en PDF" class="mb-4 mr-3" />
                    </div>
                    <div>
                        <BaseButton @click="openCreateModal" color="info" label="Agregar Informe" class="mb-4" />
                    </div>
                </div>
                <table>
                    <thead>
                        <tr>
                        <th>Informe N°</th>
                        <th>Estado Reportado</th>
                        <th>Fecha</th>
                        <th>Habitacion</th>
                        <th>Estado Habitacion</th>
                        <th>Piso</th>
                        <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="report in reports" :key="report.id_informe">
                        <td data-label="Informe: ">{{ report.id_informe }}</td>
                        <td data-label="Estado Resportado: ">{{ report.estado_reportado }}</td>
                        <td data-label="Fecha: ">{{ report.fecha_informe }}</td>
                        <td data-label="Habitacion: ">{{ report.habitacion.numero_habitacion }}</td>
                        <td data-label="Estado Habitacion: ">{{ report.habitacion.estado }}</td>
                        <td data-label="Piso: ">{{ report.habitacion.piso }}</td>
                        <td class="before:hidden lg:w-1 whitespace-nowrap">
                            <BaseButtons type="justify-start lg:justify-end" no-wrap>
                            <BaseButton color="info" :icon="mdiEye" small @click="openEditModal(producto)"/>
                            <BaseButton color="danger" :icon="mdiTrashCan" small @click="openDeleteModal(producto)"/>
                            </BaseButtons>
                        </td>
                        </tr>
                    </tbody>
                </table>
                <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800">
                    <BaseLevel>
                        <BaseButtons>
                            <BaseButton
                            v-for="page in TotalPages"
                            :key="page"
                            :active="page === currentPage"
                            :label="page"
                            :color="page === currentPage ? 'lightDark' : 'whiteDark'"
                            small
                            @click="currentPage = page; fechtReports()"
                            />
                        </BaseButtons>
                        <small>Página {{ currentPage }} de {{ TotalPages }}</small>
                    </BaseLevel>
                </div>
            </div>
        </SectionMain>
    </LayoutAuthenticated>
</template>
