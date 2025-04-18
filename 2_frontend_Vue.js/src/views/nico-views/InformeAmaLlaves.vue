<script setup>
import { onMounted, ref } from 'vue';
import { mdiTrashCan } from '@mdi/js';
import { createReport, getReportByPage, deleteReport, getReservaAndHabitacion } from '@/services/informeLlavesService';
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseLevel from '@/components/BaseLevel.vue';
import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue';
import NotificationBar from '@/components/alejo_components/NotificationBar.vue';

const reports = ref([]);
const TotalPages = ref(0);
const currentPage = ref(1);
const isModalOpen = ref(false);
const habitacionesReservadas = ref([]);
const currentReport = ref({
    id_habitacion: '',
    clave: '',
    ama_de_llaves_numero_de_personas: '',
    estado_reportado: '',
    causa: '',
    id_reserva: ''
});

const colorAlert = ref('');
const modalMessage = ref('');
const isAlertVisible = ref(false);
const isDropdownReservationOpen = ref(false);
const selectedReservaText = ref('');

const selectReserva = (reserva) => {
    currentReport.value.id_habitacion = reserva.id_habitacion;
    currentReport.value.id_reserva = reserva.id_reserva;
    selectedReservaText.value = `Habitacion: ${reserva.numero_habitacion} - Reserva: ${reserva.id_reserva}`;
    isDropdownReservationOpen.value = false;
};

const openCreateModal = () => {
    isModalOpen.value = true;
    currentReport.value = { id_habitacion: '', clave: '', ama_de_llaves_numero_de_personas: '', estado_reportado: '', causa: '', id_reserva: '' };
    selectedReservaText.value = '';
};

const closeModal = () => {
    isModalOpen.value = false;
    currentReport.value = { id_habitacion: '', clave: '', ama_de_llaves_numero_de_personas: '', estado_reportado: '', causa: '', id_reserva: '' };
    selectedReservaText.value = '';
    isDropdownReservationOpen.value = false;
};

const fetchReports = async () => {
    try {
        const response = await getReportByPage(currentPage.value);
        const responseReservation = await getReservaAndHabitacion();

        const habitacionesEnUso = response.data.informes.map(informe => informe.id_habitacion);

        habitacionesReservadas.value = responseReservation.filter(reserva => !habitacionesEnUso.includes(reserva.id_habitacion));


        reports.value = response.data.informes || [];
        TotalPages.value = response.data.total_pages || 0;
        habitacionesReservadas.value = responseReservation;

        if (currentPage.value > TotalPages.value) {
            currentPage.value = TotalPages.value;
        }
        closeModal();
    } catch (error) {
        modalMessage.value = 'No hay informes disponibles';
        isModalOpen.value = false;
        colorAlert.value = 'info';
        isAlertVisible.value = true;
        setTimeout(() => {
            isAlertVisible.value = false;
        }, 10000);
    }
};

const saveReport = async () => {
    try {
        if (!currentReport.value.id_habitacion || !currentReport.value.id_reserva || !currentReport.value.estado_reportado) {
            isModalOpen.value = false;
            isAlertVisible.value = true;
            modalMessage.value = 'Por favor completa todos los campos';
            colorAlert.value = 'info';
            setTimeout(() => {
                isAlertVisible.value = false;
            }, 3000);
            return;
        }

        const numeroPersonas = parseInt(currentReport.value.ama_de_llaves_numero_de_personas, 10);
        if (isNaN(numeroPersonas) || numeroPersonas <= 0) {
            alert('Número de personas es obligatorio y debe ser un número válido mayor que 0.');
            return;
        }

        await createReport(
            currentReport.value.clave,
            numeroPersonas,
            currentReport.value.estado_reportado,
            currentReport.value.causa,
            currentReport.value.id_habitacion,
            currentReport.value.id_reserva
        );

        modalMessage.value = "Informe creado con éxito";
        colorAlert.value = 'success';
        isAlertVisible.value = true;

        fetchReports();
        closeModal();

        setTimeout(() => {
            isAlertVisible.value = false;
        }, 3000);
    } catch (error) {
        console.log('Error capturado:', error);
        console.log('Respuesta del servidor:', error.response?.data);
        modalMessage.value = 'Error al guardar informe';
        isModalOpen.value = false;
        colorAlert.value = 'danger';
        isAlertVisible.value = true;
        setTimeout(() => {
            isAlertVisible.value = false;
        }, 3000);
    }
};

const activarModalDelete = ref({
    visible: false,
    id_informe: null,
});

const openDeleteModal = (report) => {
    activarModalDelete.value.visible = true;
    activarModalDelete.value.id_informe = report.id_informe;
};

const confirmDelete = async () => {
    try {
        await deleteReport(activarModalDelete.value.id_informe);
        modalMessage.value = "Informe eliminado con éxito";
        colorAlert.value = 'success';
        isAlertVisible.value = true;
        
        fetchReports();
        activarModalDelete.value.visible = false;

        setTimeout(() => {
            isAlertVisible.value = false;
        }, 3000);
    } catch (error) {
        modalMessage.value = 'Error al eliminar informe';
        colorAlert.value = 'danger';
        isAlertVisible.value = true;
        setTimeout(() => {
            isAlertVisible.value = false;
        }, 3000);
    }
};

const cancelDelete = () => {
    activarModalDelete.value.visible = false;
};

const formatDate = (dateString) => {
    const date = new Date(dateString);
    date.setMinutes(date.getMinutes() - date.getTimezoneOffset());
    const options = {
        year: 'numeric',
        month: 'numeric',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true,
    };
    return date.toLocaleString('es-ES', options);
};

onMounted(() => {
    fetchReports();
});
</script>

<template>
    <LayoutAuthenticated>
        <SectionMain>
            <h1 class="text-black dark:text-white text-2xl font-bold mb-3">Informes De Ama De Llaves</h1>

            <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
                <div class="w-full col-span-3">
                    <div class="text-center mb-2">
                        <p class="text-lg font-semibold">Claves</p>
                    </div>
                    <div class="bg-gray-300 shadow-lg rounded-lg p-4 dark:bg-gray-700 dark:text-white">
                        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-7 text-center gap-4">
                            <div class="p-2">
                                <p class="font-bold text-lg">O</p>
                                <p class="text-sm text-gray-600 dark:text-gray-300">Ocupada</p>
                            </div>
                            <div class="p-2">
                                <p class="font-bold text-lg">V</p>
                                <p class="text-sm text-gray-600 dark:text-gray-300">Vacia</p>
                            </div>
                            <div class="p-2">
                                <p class="font-bold text-lg">OOO</p>
                                <p class="text-sm text-gray-600 dark:text-gray-300">Reparación</p>
                            </div>
                            <div class="p-2">
                                <p class="font-bold text-lg">X</p>
                                <p class="text-sm text-gray-600 dark:text-gray-300">Ocupada con Equipaje</p>
                            </div>
                            <div class="p-2">
                                <p class="font-bold text-lg">B</p>
                                <p class="text-sm text-gray-600 dark:text-gray-300">Solo Equipaje</p>
                            </div>
                            <div class="p-2">
                                <p class="font-bold text-lg">CO</p>
                                <p class="text-sm text-gray-600 dark:text-gray-300">Check Out</p>
                            </div>
                            <div class="p-2">
                                <p class="font-bold text-lg">ND</p>
                                <p class="text-sm text-gray-600 dark:text-gray-300">No Durmió</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="flex items-center justify-center md:justify-start h-full">
                    <BaseButton color="info" label="Agregar Informe" class="w-35 h-12" @click="openCreateModal" />
                </div>
            </div>

            <NotificationBar v-if="isAlertVisible" :color="colorAlert" :description="modalMessage" :visible="isAlertVisible" />

            <table>
                <thead>
                    <tr>
                        <th>Informe N°</th>
                        <th>Habitación</th>
                        <th>Clave</th>
                        <th>N° Personas</th>
                        <th>Situación</th>
                        <th>N° Personas habitacion</th>
                        <th>Causa</th>
                        <th>Fecha y Hora</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="report in reports" :key="report.id_informe">
                        <td data-label="Informe: ">{{ report.id_informe }}</td>
                        <td data-label="Habitación: ">{{ report.habitacion.numero_habitacion }}</td>
                        <td data-label="Clave: ">{{ report.ama_de_llaves_clave }}</td>
                        <td data-label="N° Personas: ">{{ report.ama_de_llaves_numero_de_personas }}</td>
                        <td data-label="Situación: ">{{ report.estado_reportado }}</td>
                        <td data-label="N° Personas: ">{{ report.habitacion.numero_personas }}</td>
                        <td data-label="Causa: ">{{ report.causa }}</td>
                        <td data-label="Fecha y Hora: ">{{ formatDate(report.fecha_informe) }}</td>
                        <td class="before:hidden lg:w-1 whitespace-nowrap">
                            <BaseButtons type="justify-start lg:justify-end" no-wrap>
                                <BaseButton color="danger" :icon="mdiTrashCan" small @click="openDeleteModal(report)" />
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
                        small @click="() => { currentPage = page; fetchReports(); }"/>
                    </BaseButtons>
                    <small>Página {{ currentPage }} de {{ TotalPages }}</small>
                </BaseLevel>
            </div>
        </SectionMain>
    </LayoutAuthenticated>

    <CardBoxModal class="dark:text-white" v-model="isModalOpen" title="Crear Informe" buttonLabel="Crear Informe" has-cancel @cancel="closeModal" @confirm="saveReport">
    <form @submit.prevent="saveReport">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="md:col-span-2">
                <label for="id_reserva" class="text-gray-700 font-medium dark:text-white">Reserva Habitación:</label>
                <div class="relative">
                    <div @click="isDropdownReservationOpen = !isDropdownReservationOpen" class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500 dark:bg-gray-800 dark:text-white cursor-pointer">
                        {{ selectedReservaText || "Selecciona Reserva" }}
                    </div>
                    <div v-if="isDropdownReservationOpen" class="absolute z-10 w-full bg-white border border-gray-300 dark:bg-gray-800 dark:border-gray-600 rounded mt-1 max-h-48 overflow-y-auto">
                        <div v-for="reserva in habitacionesReservadas" :key="reserva.id_reserva" @click="selectReserva(reserva)" class="px-3 py-2 hover:bg-gray-200 dark:hover:bg-gray-700 cursor-pointer">
                            Habitación: {{ reserva.numero_habitacion }} <br>
                            Reserva: {{ reserva.id_reserva }}
                        </div>
                    </div>
                </div>
            </div>

            <div>
                <label for="clave" class="text-gray-700 font-medium dark:text-white">Clave:</label>
                <select id="clave" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700 dark:text-white" v-model="currentReport.clave" required>
                    <option value="O">O</option>
                    <option value="V">V</option>
                    <option value="OOO">OOO</option>
                    <option value="X">X</option>
                    <option value="B">B</option>
                    <option value="CO">CO</option>
                    <option value="ND">ND</option>
                </select>
            </div>

            <div>
                <label for="numeropersonas" class="block text-gray-700 font-medium dark:text-white">N° Personas:</label>
                <input type="number" id="numeropersonas" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700 dark:text-white" v-model="currentReport.ama_de_llaves_numero_de_personas" required />
            </div>

            <div>
                <label for="estado_reportado" class="block text-gray-700 font-medium dark:text-white">Situación:</label>
                <select id="estado_reportado" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700 dark:text-white" v-model="currentReport.estado_reportado" required>
                    <option value="LIMPIA">LIMPIA</option>
                    <option value="SUCIA">SUCIA</option>
                    <option value="EN REPARACIÓN">EN REPARACIÓN</option>
                </select>
            </div>

            <div class="md:col-span-2">
                <label for="causa" class="block text-gray-700 font-medium dark:text-white">Causa:</label>
                <input type="text" id="causa" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700 dark:text-white" v-model="currentReport.causa" required />
            </div>
        </div>
    </form>
</CardBoxModal>



    <CardBoxModal class="dark:text-white" v-model="activarModalDelete.visible" title="Eliminar Informe" button="danger" buttonLabel="Eliminar" has-cancel @confirm="confirmDelete" @cancel="cancelDelete">
        <p class="text-xl dark:text-white">¿Está seguro de eliminar el informe?</p>
    </CardBoxModal>

</template>