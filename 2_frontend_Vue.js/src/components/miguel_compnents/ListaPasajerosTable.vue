        <script setup>
        import { ref, onMounted } from 'vue'
        import { mdiEye, mdiTrashCan } from '@mdi/js'
        import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue'
        import BaseLevel from '@/components/BaseLevel.vue'
        import BaseButtons from '@/components/BaseButtons.vue'
        import BaseButton from '@/components/BaseButton.vue'
        import { getListaPasajerosBypage, getAllPasajeros } from '@/services/listapasajerosService'

        defineProps({
        checkable: Boolean
        })

        const allpasajeros = ref('')
        const buscarHuesped = ref(''); 
        const currentHuesped = ref({});
        const TotalPages = ref(0);
        const currentPage = ref(1);
        const isEditMode = ref(false);
        const activarModalEdit = ref(false);
        const activarModalDelete = ref({
        visible: false,
        huesped: null
        });

        const fetchAllHuespedes = async () => {
        try {
            const response = await getAllPasajeros();
            allpasajeros.value = response.data;
            console.log('all huespedes:',allpasajeros.value);
        } catch (error) {
            alert(error.response?.data?.detail || 'Error al obtener los huéspedes');
        }
        }; 
        fetchAllHuespedes();



        const fetchHuespedesByPage = async () => {
        try {
            const response = await getListaPasajerosBypage(currentPage.value);
            response.data
            TotalPages.value = response.data.total_pages;
        } catch (error) {
            alert(error.response?.data?.detail || 'Error al obtener los huéspedes');
        }
        };




        const openEditModal = (huesped = {}) => {
        isEditMode.value = true;
        currentHuesped.value = { ...huesped };
        activarModalEdit.value = true;
        };

        // // Actualiza un huésped
        // const update_Huesped = async () => {
        // try {
        //     await updateHuesped(
        //     currentHuesped.value.id_huesped,
        //     currentHuesped.value.nombre_completo,
        //     currentHuesped.value.tipo_documento,
        //     currentHuesped.value.numero_documento,
        //     currentHuesped.value.fecha_expedicion,
        //     currentHuesped.value.email,
        //     currentHuesped.value.telefono,
        //     currentHuesped.value.ocupacion,
        //     currentHuesped.value.direccion
        //     );
        //     modalMessage.value = 'Huésped actualizado exitosamente';
        //     activarModalEdit.value = false;

        //     setTimeout(() => {
        //     }, 3000);
        //     //cierra el modal en tres segundos

        //     await fetchHuespedesByPage();
        // } catch (error) {
        //     modalMessage.value = error.data.detail;
        //     activarModalEdit.value = false;

        //     setTimeout(() => {
        //     }, 3000);

        // }
        // };


        // const cancelEdit = () => {
        // activarModalEdit.value = false;
        // // Solo cierra el modal
        // };



        // // Método para abrir el modal
        // const openDeleteModal = (huesped) => {
        // activarModalDelete.value = {
        //     visible: true,
        //     huesped: huesped
            
        // };
        // };


        // // Método para confirmar la eliminación
        // const confirmDelete = async () => {
        // const huespedTemp = activarModalDelete.value.huesped;
        // if (!huespedTemp) return;

        // try {
        //     await deleteHuesped(huespedTemp.id_huesped);
        //     modalMessage.value = 'Huésped eliminado exitosamente';
        //     setTimeout(() => {
        //     }, 3000);

        //     await fetchHuespedesByPage(); // Actualiza la lista de huéspedes
        //     activarModalDelete.value.visible = false; 
        // } catch (error) {
        //     modalMessage.value = error.data.detail;
        //     activarModalDelete.value.visible = false; 

        // }
        // };

        // // Método para cancelar la eliminación
        // const cancelDelete = () => {
        // activarModalDelete.value.visible = false; // Solo cierra el modal
        // };



        // const formatDate = (dateString) => {
        // const options = {
        //     year: 'numeric',
        //     month: 'numeric',
        //     day: 'numeric',
        //     timeZone: 'UTC'
        // };
        // return new Date(dateString).toLocaleDateString('es-ES', options);
        // };


        onMounted(() => {
        fetchHuespedesByPage();
        });

        </script>

        <template>


        <CardBoxModal v-model="activarModalEdit" title="Editar huésped"  buttonLabel="Guardar cambios" has-cancel @cancel="cancelEdit"
        @confirm="update_Huesped " >
            <form @submit.prevent="update_Huesped()">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
                <!-- Primer par de campos -->
                <div class="mb-4">
                <label for="huespedNombre_completo" class="block text-gray-700  font-medium dark:text-white">Nombre completo</label>
                <input
                    type="text"
                    id="fecha_entrada"
                    class="mt-1 block w-full border-gray-300 rounded-md shado dark:text-white dark:border-gray-600 rounded-mdw-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
                    v-model="currentHuesped.fecha_entrada"
                    required
                />
                </div>
                <div class="mb-4">
                <label for="huespedTipo_documento" class="block text-gray-700  font-medium dark:text-white">Tipo documento</label>
                <input
                    type="text"
                    id="fecha_salida"
                    class="mt-1 block w-full border-gray-300 rounded-md shad dark:text-white dark:border-gray-600 rounded-mdow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
                    v-model="currentHuesped.fecha_salida"
                    required
                />
                </div>
                <!-- Segundo par de campos -->
                <div class="mb-4">
                <label for="huespedNumero_documento" class="block text-gray-700  font-medium dark:text-white">Número documento</label>
                <input
                    type="text"
                    id="huespedNumero_documento"
                    class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 rounded-md-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
                    
                    required
                />
                </div>
                <div class="mb-4">
                <label for="huespedFecha_expedicion" class="block text-gray-700  font-medium dark:text-white">Fecha expedición</label>
                <input
                    type="date"
                    id="huespedFecha_expedicion"
                    class="mt-1 block w-full border-gray-300 rounded-md shadow dark:text-white dark:border-gray-600 rounded-md-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
                    v-model="currentHuesped.fecha_expedicion"
                    required
                />
                </div>
                <!-- Tercer par de campos -->
                <div class="mb-4">
                <label for="huespedEmail" class="block text-gray-700 font-medium dark:text-white">Email</label>
                <input
                    type="email"
                    id="huespedEmail"
                    class="mt-1 block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
                    v-model="currentHuesped.email"
                    required
                />
                </div>
                <div class="mb-4">
                <label for="huespedTelefono" class="block text-gray-700  font-medium dark:text-white">Teléfono</label>
                <input
                    type="text"
                    id="huespedTelefono"
                    class="mt-1 block w-full border-gray-300 rounded-md dark:text-white dark:border-gray-600 shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
                    v-model="currentHuesped.telefono"
                    required
                />
                </div>
                <!-- Último par de campos -->
                <div class="mb-4">
                <label for="huespedOcupacion" class="block text-gray-700  font-medium dark:text-white">Ocupación</label>
                <input
                    type="text"
                    id="huespedOcupacion"
                    class="mt-1 block w-full border-gray-300 rounded-md dark:text-white dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700"
                    v-model="currentHuesped.ocupacion"
                    required
                />
                </div>
                <div class="mb-4">
                <label for="huespedDireccion" class="block text-gray-700  font-medium dark:text-white">Dirección</label>
                <input
                    type="text"
                    id="huespedDireccion"
                    class="mt-1 block w-full border-gray-300 rounded-md dark:text-white dark:bg-gray-700  dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                    v-model="currentHuesped.direccion"
                    required
                />
                </div>
            </div>

            </form>
        </CardBoxModal >

        <CardBoxModal v-model="activarModalDelete.visible"  v-if="activarModalDelete.huesped" title="Eliminar huésped" buttonLabel="Eliminar" button="danger" has-cancel @confirm="confirmDelete"
        @cancel="cancelDelete" >
            <p class="text-xl">Esta seguro de eliminar a: </p>
            <b>{{ activarModalDelete.huesped.nombre_completo }}</b><br>
            <small>{{ activarModalDelete.huesped.tipo_documento }}: {{ activarModalDelete.huesped.numero_documento }}</small>
        </CardBoxModal>

        <div class="mb-6 max-w-md mx-left">
            <div class=" flex items-center border rounded-lg shadow-sm">
            <input
                type="text"
                placeholder="Buscar huésped por documento"
                class="search-input flex-grow px-4 py-2 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:text-white dark:bg-gray-700 " 
                v-model="buscarHuesped"
                @input="filterHuespedes"
            />

            </div>
        </div>

        <table>
            <thead>
            <tr>
            
                <th>Nombre completo</th>
                <th>Fecha de entrada</th>
                <th>Fecha de salida</th>
                <th>Documento</th>
                <th>Expedido N.</th>
                <th>Registro N.</th>
                <th>Profesion</th>


                <th />
            </tr>
            </thead>
            <tbody>
            <tr v-for="huesped in huespedes" :key="huesped.id_huesped">
                
                
                <td data-label="Nombre completo">
                {{ huesped.nombre_completo }}
                </td>
                <td data-label="Tipo documento">
                {{ huesped.tipo_documento }}
                </td>
                <td data-label="Número documento">
                {{ huesped.numero_documento }}
                </td>
                <td data-label="Fecha expedición">
                {{ formatDate(huesped.fecha_expedicion) }}
                </td>
                <td data-label="Email">
                {{ huesped.email }}
                </td>
                <td data-label="Teléfono">
                {{ huesped.telefono }}
                </td>
                <td data-label="Ocupación">
                {{ huesped.ocupacion }}
                </td>
                <td data-label="Dirección">
                {{ huesped.direccion  }}
                </td>
                <td data-label="Estado">
                {{ huesped.huesped_estado ? 'Activo' : 'Inactivo' }}
                </td>
                
                <td class="before:hidden lg:w-1 whitespace-nowrap">
                <BaseButtons type="justify-start lg:justify-end" no-wrap>
                    <BaseButton color="info" :icon="mdiEye" small @click="openEditModal(huesped)" />
                    <BaseButton color="danger" :icon="mdiTrashCan" small @click="openDeleteModal(huesped)"/>
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
                    @click="currentPage = page; fetchHuespedesByPage()"
                    />
                </BaseButtons>
                <small>Página {{ currentPage }} de {{ TotalPages }}</small>
            </BaseLevel>
            </div>
        


        </template>
