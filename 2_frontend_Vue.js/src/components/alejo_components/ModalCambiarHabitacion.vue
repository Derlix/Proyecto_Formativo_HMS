<template>
  <transition name="modal">
    <div v-if="isVisible" class="fixed inset-0 z-50 flex items-center justify-center">
      <div class="absolute inset-0 bg-black opacity-50"></div>
      <div class="relative bg-white dark:bg-gray-800 rounded-lg shadow-lg w-full max-w-lg">
        <div class="p-6">
          <button class="absolute top-4 right-4 text-gray-600 dark:text-gray-300" @click="closeModal()">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <h3 class="text-2xl font-semibold text-gray-900 dark:text-gray-100">
            Cambiar Habitación
          </h3>
          <p class="mt-2 text-lg text-gray-500 dark:text-gray-400">
            Ingresa los siguientes datos asociados de la reserva.
          </p>
          
          <!-- Input del documento -->
          <div class="mt-4">
            <label for="documento" class="block text-lg font-medium text-gray-700 dark:text-gray-300">
              Documento del Huésped
            </label>
            <input
              v-model="documento_huesped"
              id="documento_huesped"
              type="text"
              placeholder="Ingrese el documento"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white text-lg"
              @input="buscarReserva_Habitacion"
            />
          </div>

          <div class="mt-4">
            <label for="documento" class="block text-lg font-medium text-gray-700 dark:text-gray-300">
             Fecha Reserva
            </label>
            <input
              v-model="fecha_reserva"
              id="fecha_reserva"
              type="date"
              placeholder="Ingrese la fecha de reserva"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white text-lg"
              @input="buscarReserva_Habitacion"
            />
          </div>

          <BaseDivider />

          <!-- Campos que se activan después de ingresar el documento -->
          <form @submit.prevent="update_ReservaHabitacion()">
            <div v-if="reservaEncontrada" class="mt-6 space-y-4">
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label for="num_adultos" class="block text-lg font-medium text-gray-700 dark:text-gray-300">
                    Número adultos
                  </label>
                  <input
                    id="num_adultos"
                    type="text"
                    v-model="num_adultos"
                    class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white text-lg"
                  />
                </div>
                <div>
                  <label for="num_ninos" class="block text-lg font-medium text-gray-700 dark:text-gray-300">
                    Número niños
                  </label>
                  <input
                    id="num_ninos"
                    type="text"
                    v-model="num_ninos"
                    class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white text-lg"
                  />
                </div>
              </div>
  
              <div class="grid grid-cols-2 gap-4 mt-4">
                <div>
                  <label for="habitacion" class="block text-lg font-medium text-gray-700 dark:text-gray-300">
                   Nueva Habitación
                  </label>
                  <HabitacionSelect @habitacionCompuesta="recibirObjeto" />
                </div>
                <div>
                  <label for="new_fecha_entrada" class="block text-lg font-medium text-gray-700 dark:text-gray-300">
                    Fecha de Entrada
                  </label>
                  <input
                    id="new_fecha_entrada"
                    type="date"
                    v-model="new_fecha_entrada"
                    class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white text-lg"
                  />
                </div>
              </div>
  
              <div class="grid grid-cols-2 gap-4 mt-4">
                <div>
                  <label for="new_fecha_salida" class="block text-lg font-medium text-gray-700 dark:text-gray-300">
                    Fecha de Salida
                  </label>
                  <input
                    id="new_fecha_salida"
                    type="date"
                    v-model="new_fecha_salida"
                    class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white text-lg"
                  />
                </div>
              </div>
            </div>
  
            <div v-else-if="sinDatos">
              <p class="text-red-500 text-xl font-bold">No existen datos asociados a la solicitud.</p>
            </div>
  
            <div class="mt-6 flex justify-end space-x-4">
              <BaseButtons>
                <BaseButton v-if="reservaEncontrada" type="submit" color="info" label="Guardar Cambios" @click="update_ReservaHabitacion()  "/>
                <BaseButton type="reset" color="info" outline label="Cancelar"  @click="cancel()" />
              </BaseButtons>
            </div>
          </form>

        </div>
      </div>
    </div>
  </transition>
</template>

  
<script setup>
import { ref, defineProps, defineEmits } from 'vue'
import { obtenertodasReservasHabitacion, actualizarReservaHabitacion } from '@/services/reservaHabitacionService'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseDivider from '@/components/BaseDivider.vue'
import HabitacionSelect from './HabitacionSelect.vue'
// import { obtenerTodasHabitacion } from '@/services/habitacionService'

const documento_huesped = ref('')
const fecha_reserva = ref('')
const id_reserva = ref(0)
const id_habitacion = ref(0)
const new_id_habitacion = ref(0)
const num_adultos = ref('')
const num_ninos = ref('')
const new_fecha_entrada = ref('')
const new_fecha_salida = ref('')
const reservaEncontrada = ref(false)
const sinDatos = ref(false)
const emit = defineEmits(['close'])


defineProps({
  isVisible: {
    type: Boolean,
    required: true
  }
})

const closeModal = () => {
  emit('close')
  resetFields() 
  sinDatos.value= false;
}

const cancel = () => {
  if(reservaEncontrada.value) {
    reservaEncontrada.value = false
  } else {
    emit('close')
    resetFields() 
    sinDatos.value= false;
  }
  
}


const resetFields = () => {
  reservaEncontrada.value = false
  documento_huesped.value = ''
  fecha_reserva.value = ' '
  num_ninos.value = ''
  num_adultos.value = ''
  fecha_reserva.value = ''
}




const buscarReserva_Habitacion = async () => {
  try {
    const response = await obtenertodasReservasHabitacion()
    if (response.data && response.data.length) {
      console.log(response);
      const reservaHabitacion = response.data.find(r => r.huesped.numero_documento === documento_huesped.value && r.reserva.fecha_reserva === fecha_reserva.value);
      if (reservaHabitacion) {
        console.log("Reserva habitacion",reservaHabitacion);
        reservaEncontrada.value = true;
        id_reserva.value = reservaHabitacion.id_reserva;
        id_habitacion.value = reservaHabitacion.id_habitacion;
        num_ninos.value = reservaHabitacion.num_niños || 'No disponible';
        num_adultos.value = reservaHabitacion.num_adultos || 'No disponible';
        fecha_reserva.value = reservaHabitacion.reserva.fecha_reserva || 'No disponible';
      } else {
       sinDatos.value= true;
       reservaEncontrada.value = false;
      }
    } else {
      resetFields()
    }
  } catch (error) {
    console.error('Error al buscar la reserva:', error)
    resetFields()
  }
};

const recibirObjeto = (habitacionCompuesta) => {
  new_id_habitacion.value = habitacionCompuesta.id_habitacion;
      console.log('Objeto recibido como constante en setup:', habitacionCompuesta);
    };


const update_ReservaHabitacion = async () => {
  try {
    console.log("old_id_habitacion", id_habitacion.value);
    console.log("new_id_habitacion", new_id_habitacion.value);
    console.log("id_reserva", id_reserva.value);
    await actualizarReservaHabitacion(
      id_reserva.value, 
      id_habitacion.value,
      new_id_habitacion.value, 
      num_adultos.value, 
      num_ninos.value, 
      new_fecha_entrada.value, 
      new_fecha_salida.value
    );
    // modalMessage.value = 'Huésped actualizado exitosamente';
    // isAlertVisible.value = true;
    // colorAlert.value = 'success';
    // activarModalEdit.value = false;

    // setTimeout(() => {
    //   isAlertVisible.value = false;
    // }, 3000);
    // //cierra el modal en tres segundos

    // await fetchHuespedesByPage();
  } catch (error) {
    // modalMessage.value = error.data.detail;
    // isAlertVisible.value = true;
    // colorAlert.value = 'danger';
    // activarModalEdit.value = false;

    // setTimeout(() => {
    //   isAlertVisible.value = false;
    // }, 3000);

  }
};

// # Supongamos que tienes un objeto reserva_habitacion_update con los datos que quieres actualizar
// reserva_habitacion_update = ReservaHabitacionUpdate(
//     id_habitacion=new_id_habitacion,  # nuevo ID que quieres establecer
//     num_adultos=2,
//     num_niños=1,
//     fecha_entrada='2024-10-08',
//     fecha_salida_propuesta='2024-10-10'
// )

// update_reserva_habitacion(db, id_reserva, id_habitacion, reserva_habitacion_update, id_hotel)






// const fetchHabitacionesActivas = async () => {
//   try {
//     const response = await obtenerTodasHabitacion();
    
//     const activos = response.data.habitaciones.filter(habitacion => habitacion.estado === "ACTIVO");
//     habitaciones.value = activos;
//     // originalHuespedes.value = activos;
//     console.log(habitaciones.value);
//     console.log('Total de habitaciones activas:', activos.length);
//   } catch (error) {
//     alert(error.response?.data?.detail || 'Error al obtener las habitaciones');
//   }
// }; 







</script>
