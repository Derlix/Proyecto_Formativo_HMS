<template>
  <div
    v-if="visible"
    class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
  >
    <div
      class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-2xl w-full relative transition-all"
    >
      <button
        @click="closeAlert"
        class="absolute top-4 right-4 text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300 z-10"
      >
        &times;
      </button>
      <h1 class="text-xl font-semibold mb-4 text-center text-gray-900 dark:text-white">
        Formulario crear reserva
      </h1>

      <div class="flex justify-center mb-6">
        <span class="text-gray-700 dark:text-gray-300 mx-2">Reserva para:</span>
        <p class="text-gray-900 dark:text-gray-100">{{ huesped.nombre_completo }}</p>

      </div>
      <NotificationBar
          v-if="isAlertVisible"
          :color="colorAlert"
          :description="modalMessage"
          :visible="isModalVisible"
        />

      <!-- Paso 1 - Datos de la reserva -->
      <div v-if="paso === 1" class="grid grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Fecha de Reserva</label
          >
          <input
            type="date"
            v-model="fecha_reserva"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Empresa</label>
          <input
            type="text"
            v-model="empresa"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            placeholder="Ingrese el nombre de la empresa"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Numero de adultos</label
          >
          <input
            type="number"
            v-model="num_adultos"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            placeholder="Ingrese el numero de adultos"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Numero de niños</label
          >
          <input
            type="number"
            v-model="num_niños"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            placeholder="Ingrese el numero de niños"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Fecha de llegada</label
          >
          <input
            type="date"
            v-model="fecha_llegada"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">
            Fecha de salida
          </label>
          <input
            type="date"
            v-model="fecha_salida"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          />
        </div>


        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Depósito</label>
          <input
            type="number"
            v-model="deposito"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
            placeholder="Ingrese el monto del depósito"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300"
            >Forma de Pago</label
          >
          <select
            v-model="forma_pago"
            class="block w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-white"
          >
            <option value="">Seleccione una opción</option>
            <option value="EFECTIVO">Efectivo</option>
            <option value="DEBITO">Débito</option>
            <option value="CREDITO">Crédito</option>
          </select>
        </div>
      </div>

      <div
        v-if="paso === 2"
        class="overflow-x-auto bg-gray-50 dark:bg-gray-800 rounded-lg shadow-md p-4 max-h-64"
      >
        <table class="min-w-full bg-white dark:bg-gray-700 border-gray-300">
          <thead>
            <tr class="bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-200">
              <th class="px-4 py-2">ID Reserva</th>
              <th class="px-4 py-2">Fecha de Reserva</th>
              <!-- <th class="px-4 py-2">Fecha de Llegada</th>
              <th class="px-4 py-2">Fecha de Salida</th> -->
              <th class="px-4 py-2">Estado</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="reserva in reservas.filter((r) => r.estado_reserva === 'ACTIVO')"
              :key="reserva.id_reserva"
              class="hover:bg-gray-100 dark:hover:bg-gray-600"
            >
              <td class="border px-4 py-2 dark:text-white">{{ reserva.id_reserva }}</td>
              <td class="border px-4 py-2 dark:text-white">{{ reserva.fecha_reserva }}</td>
              <!-- <td class="border px-4 py-2 dark:text-white">{{ reserva.fecha_llegada }}</td>
              <td class="border px-4 py-2 dark:text-white">{{ reserva.fecha_salida }}</td> -->
              <td class="border px-4 py-2 dark:text-white">{{ reserva.estado_reserva }}</td>
              <td class="border px-4 py-2 flex justify-center items-center">
                <input
                  type="checkbox"
                  :value="reserva.id_reserva"
                  v-model="seleccionaridReservaSeleccionada"
                  @change="seleccionaridReserva(reserva.id_reserva)"
                />
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div
        v-else-if="paso === 3"
        class="overflow-x-auto bg-gray-50 dark:bg-gray-800 rounded-lg shadow-md p-4 max-h-64"
      >
        <table class="min-w-full bg-white dark:bg-gray-700 border-gray-300">
          <thead>
            <tr class="bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-200">
              <th class="px-4 py-2">Habitación</th>
              <th class="px-4 py-2">Características</th>
              <th class="px-4 py-2">Piso</th>
              <th class="px-4 py-2">Precio</th>
              <th class="px-4 py-2">Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="habitacion in habitaciones.filter((h) => h.estado)"
              :key="habitacion.id_habitacion"
              class="hover:bg-gray-100 dark:hover:bg-gray-600"
            >
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.numero_habitacion }}</td>
              <td class="border px-4 py-2 dark:text-white">
                <button @click="verCaracteristicas(habitacion)" class="bg-blue-500 text-white px-2 py-1 rounded hover:bg-blue-600 transition">
                  Ver características
                </button>
              </td>
              <td class="border px-4 py-2 dark:text-white">{{ habitacion.piso }}</td>
              <td class="border px-4 py-2 dark:text-white">{{ calcularPrecioTotal(habitacion) }}</td>
              <td class="border px-4 py-2 flex justify-center items-center">
                <input
                  type="checkbox"
                  :value="habitacion.id_habitacion"
                  v-model="habitacionSeleccionada"
                  @change="seleccionarHabitacion(habitacion.id_habitacion)"
                />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- Alerta de éxito -->
      <div
        v-if="showSuccessAlert"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white"
      >
        <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-sm w-full relative">
          <button
            @click="closeAlert"
            class="absolute top-2 right-2 text-gray-600 dark:text-gray-300"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
          <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            Reserva realizada con éxito
          </h3>
          <p>La reserva se ha completado correctamente.</p>
          <button
            @click="closeAlert"
            class="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg w-full"
          >
            Regresar
          </button>
        </div>
      </div>

      <!-- Alerta de error -->
      <div
        v-if="showError"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 dark:bg-opacity-70 text-black dark:text-white"
      >
        <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-sm w-full relative">
          <button
            @click="closeError"
            class="absolute top-2 right-2 text-gray-600 dark:text-gray-300"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
          <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            Error al realizar la reserva
          </h3>
          <p>Hubo un problema al procesar la reserva. Intenta nuevamente.</p>
          <button
            @click="closeError"
            class="mt-4 bg-red-600 text-white px-4 py-2 rounded-lg w-full"
          >
            Cerrar
          </button>
        </div>
      </div>

      <div class="flex justify-between mt-6">
        <button
          v-if="paso === 1"
          @click="closeAlert"
          class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-200 font-semibold py-2 px-4 rounded-md hover:bg-gray-400 dark:hover:bg-gray-500 transition"
        >
          Cancelar
        </button>
        <button
          v-if="paso > 1"
          @click="atras"
          class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-200 font-semibold py-2 px-4 rounded-md hover:bg-gray-400 dark:hover:bg-gray-500 transition"
        >
          Atrás
        </button>
        <button
          @click="siguiente"
          class="bg-blue-600 dark:bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 dark:hover:bg-blue-600 transition"
        >
          Siguiente
        </button>
      </div>
    </div>
  </div>
  <CardBoxModal v-model="activarModalCaracteristicas" title="Características de la habitación" has-cancel :showPrimaryButton="false" @cancel="activarModalCaracteristicas = false">
        <ul v-if="habitacionSeleccionada?.caracteristicas.length">
          <li v-for="caracteristica in habitacionSeleccionada.caracteristicas" :key="caracteristica.id_caracteristica">
            {{ caracteristica.nombre_caracteristicas }} (Adicional: {{ caracteristica.adicional }})
          </li>
        </ul>
        <ul v-else>
          <p> No hay caracteristicas para esta habitación</p>
        </ul>
      </CardBoxModal>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { obtenerTodasHabitaciones } from '@/services/habitacionService'
import { crearReserva } from '@/services/reservaService'
import { crearReservaHabitacion } from '@/services/reservaHabitacionService'
import { obtenerReservasPorHuesped } from '@/services/reservaService'
import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue';
import NotificationBar from '@/components/alejo_components/NotificationBar.vue';
const modalMessage = ref('');
const isAlertVisible = ref(false);
const colorAlert = ref('');
import api from '@/services/api'; // Asegúrate de tener configurada tu API


const props = defineProps({
  visible: Boolean, // Prop que controla la visibilidad del modal
  huesped: Object
})

const emit = defineEmits(['close', 'confirm'])
const reservas = ref([])
const paso = ref(1)
const fecha_reserva = ref('')
const fecha_llegada = ref('')
const fecha_salida = ref('')
const num_adultos = ref('1')
const num_niños = ref('0')
const empresa = ref('')
const habitaciones = ref([])
const deposito = ref('')
const forma_pago = ref('')
const habitacionSeleccionada = ref(null)
const seleccionaridReservaSeleccionada = ref(null)
const activarModalCaracteristicas = ref(false);
const showSuccessAlert = ref(false) // Estado para mostrar la alerta
const showError = ref(false) // Estado para mostrar la alerta de error
const fetchReser = ref([]);

const today = new Date();
today.setHours(today.getHours() - today.getTimezoneOffset() / 60); // Ajusta la fecha para la zona horaria local
fecha_reserva.value = today.toISOString().slice(0, 10); // Asigna la fecha actual al campo de fecha de reserva

const calcularPrecioTotal = (habitacion) => {
  let precioTotal = habitacion.categoria?.precio_fijo || 0;

  if (habitacion.caracteristicas?.length > 0) {
    habitacion.caracteristicas.forEach((caracteristica) => {
      precioTotal += caracteristica.adicional || 0;
    });
  }

  return new Intl.NumberFormat('es-CO', {
    style: 'currency',
    currency: 'COP',
    minimumFractionDigits: 0,
  }).format(precioTotal);
};

const seleccionarHabitacion = (id_habitacion) => {
  habitacionSeleccionada.value = id_habitacion
  console.log('Habitación seleccionada:', habitacionSeleccionada.value)
}

const seleccionaridReserva = (id_reserva) => {
  seleccionaridReservaSeleccionada.value = id_reserva
  console.log('ID Reserva seleccionada:', seleccionaridReservaSeleccionada.value)
}

// Función para cargar las reservas por número de documento
const cargarReservasDelHuesped = async () => {
  try {
    const response = await obtenerReservasPorHuesped(props.huesped.numero_documento)
    reservas.value = response.data // Asigna las reservas obtenidas
    console.log('Reservas del huésped:', reservas.value) // Imprime las reservas en la consola
  } catch (error) {
    console.error('Error al obtener reservas:', error) // Imprime el error si falla la petición
  }
}

const fetchReservations = async () => {
  try {
    const response = await api.get('/Reserva-habitacion/get_all'); // Cambia esta ruta por la de tus reservas
    const reservasProcesadas = response.data.map((reserva) => ({
      idReserva: reserva.id_reserva,
      fechaEntrada: reserva.fecha_entrada,
      fechaSalidaPropuesta: reserva.fecha_salida_propuesta,
      numeroHabitacion: reserva.habitacion?.numero_habitacion,
    }));

    fetchReser.value = reservasProcesadas; // Actualizar fetchReser con los datos procesados
    console.log('Reservas procesadas:', fetchReser.value); // Agrega un mensaje descriptivo al console.log
  } catch (error) {
    console.error('Error al obtener las reservas:', error);
  }
};

// Cargar las reservas cuando se monte el componente
onMounted(() => {
  if (props.huesped && props.huesped.numero_documento) {
    cargarReservasDelHuesped();
  }
  fetchReservations();
});

// Vigila el paso actual para cargar reservas si es necesario
watch(paso, (nuevoPaso) => {
  if (nuevoPaso === 2) {
    cargarReservasDelHuesped()
  }
})

// Método para cerrar la alerta
const closeAlert = () => {
  showSuccessAlert.value = false // Cerrar la alerta
  closeModal()
}

const closeError = () => {
  showError.value = false // Cerrar la alerta de error
  closeModal()
}

const verCaracteristicas = (habitacion) => {
  habitacionSeleccionada.value = habitacion;
  activarModalCaracteristicas.value = true;
};

// fecha_reserva, empresa, num_adultos, num_niños, fecha_llegada, fecha_salida, deposito, forma_pago

// Método para avanzar en los pasos
const siguiente = async () => {
  if (paso.value === 1) {
    if (!fecha_reserva.value || !num_adultos.value || !fecha_llegada.value || !fecha_salida.value || !deposito.value || !forma_pago.value) {
      // console.error('Por favor, completa todos los campos antes de continuar.')

      modalMessage.value = 'Por favor, completa todos los campos antes de continuar.';
      isAlertVisible.value = true;
      colorAlert.value = 'danger';

      setTimeout(() => {
        isAlertVisible.value = false;
      }, 5000);

      return;
    }

    // Error si pone la fecha de llegada después de la fecha de salida
    if (new Date(fecha_llegada.value) > new Date(fecha_salida.value)) {
      // console.error('La fecha de llegada no puede ser mayor a la fecha de salida.')

      modalMessage.value = 'La fecha de llegada no puede ser mayor a la fecha de salida.';
      isAlertVisible.value = true;
      colorAlert.value = 'danger';

      setTimeout(() => {
        isAlertVisible.value = false;
      }, 5000);

      return;
    }

    await confirmarReserva()
  }

  if (paso.value === 2) {
    if (!seleccionaridReservaSeleccionada.value) {
      // console.error('Por favor, selecciona una reserva antes de continuar.')

      modalMessage.value = 'Por favor, selecciona una reserva antes de continuar.';
      isAlertVisible.value = true;
      colorAlert.value = 'danger';

      setTimeout(() => {
        isAlertVisible.value = false;
      }, 5000);

      return
    }
    cargarHabitaciones();
  }

  if (paso.value === 3) {
    if (!habitacionSeleccionada.value) {
      console.error('Por favor, selecciona una habitación antes de continuar.')

      modalMessage.value = 'Por favor, selecciona una habitación antes de continuar.';
      isAlertVisible.value = true;
      colorAlert.value = 'danger';

      setTimeout(() => {
        isAlertVisible.value = false;
      }, 6000);

      return;
    }

    try {
      await confirmarReservaHabitacion() // Llama a la función para confirmar la reserva de habitación
      paso.value = 0;
      limpiarCampos();
    }catch (error) {
      console.error('Error al finalizar el paso 3:', error);
    }

  }

  if (paso.value < 4) {
    paso.value++
  }
}

const limpiarCampos = () => {
  fecha_reserva.value = today.toISOString().slice(0, 10); // Asigna la fecha actual al campo de fecha de reserva
  empresa.value = '';
  num_adultos.value = '1';
  num_niños.value = '0';
  fecha_llegada.value = '';
  fecha_salida.value = '';
  deposito.value = '';
  forma_pago.value = '';
  habitacionSeleccionada.value = null;
  seleccionaridReservaSeleccionada.value = null;
}

const atras = () => {
  if (paso.value > 1) {
    paso.value--
  }
}

// Confirmar la reserva
const confirmarReserva = async () => {
  try {
    const response = await crearReserva(
      fecha_reserva.value,
      empresa.value,
      parseFloat(deposito.value),
      forma_pago.value,
      'ACTIVO',
      props.huesped.id_huesped
    )

    console.log('Reserva creada exitosamente:', response.data)
  } catch (error) {
    console.error('Error al crear la reserva:', error.response ? error.response.data : error)
  }
}

const confirmarReservaHabitacion = async () => {
  if (!fecha_salida.value) {
    console.error("La fecha de salida es requerida.");
    showError.value = true;
    return;
  }

  try {
    const response = await crearReservaHabitacion(
      seleccionaridReservaSeleccionada.value, // ID de la reserva creada
      habitacionSeleccionada.value,
      num_adultos.value,
      num_niños.value,
      fecha_llegada.value,
      fecha_salida.value // Este es el campo que debe pasar el valor para fecha_salida_propuesta
    );
    console.log('Habitación reservada exitosamente:', response.data);
    showSuccessAlert.value = true;
  } catch (error) {
    if (error.response) {
      console.error("Error en la API:", error.response.data); // Imprimir el mensaje de error completo
      throw error.response;
    } else {
      throw new Error('Error de red o de servidor');
    }
  }
};



// Cargar las habitaciones
const cargarHabitaciones = async () => {
  try {
    const response = await obtenerTodasHabitaciones()
    let todasHabitaciones = response.data

    // Filtrar habitaciones disponibles según las fechas seleccionadas
    if (fecha_llegada.value && fecha_salida.value) {
      const fechaLlegada = new Date(fecha_llegada.value)
      const fechaSalida = new Date(fecha_salida.value)

      // Filtrar habitaciones que no estén reservadas en el rango de fechas seleccionado
      todasHabitaciones = todasHabitaciones.filter(habitacion => {
        // Verificar si esta habitación tiene reservas que se solapan con las fechas seleccionadas
        const reservasConflicto = fetchReser.value.filter(reserva => {
          if (reserva.numeroHabitacion !== habitacion.numero_habitacion) {
            return false // No es la misma habitación, no hay conflicto
          }

          const reservaInicio = new Date(reserva.fechaEntrada)
          const reservaFin = new Date(reserva.fechaSalidaPropuesta)

          // Verificar si hay solapamiento entre las fechas
          // (Llegada antes de que termine otra reserva Y Salida después de que comience otra reserva)
          return !(fechaSalida <= reservaInicio || fechaLlegada >= reservaFin)
        })

        // La habitación está disponible si no hay reservas conflictivas
        return reservasConflicto.length === 0
      })
    }

    habitaciones.value = todasHabitaciones
    console.log('Fechas con habitaciones ocupadas:', fetchReser.value)
    console.log('Habitaciones disponibles para las fechas seleccionadas:', habitaciones.value)
  } catch (error) {
    console.error('Error al cargar las habitaciones:', error)
  }
}

// Manejo de los modales y el historial de navegación
const modalStack = ref([]) // Pila de modales abiertos

const handlePopState = () => {
  if (modalStack.value.length > 0) {
    modalStack.value.pop() // Elimina el último modal del historial
    if (modalStack.value.length === 0) {
      emit('close') // Cierra el modal si no hay más en la pila
    }
  }
}

const openModal = () => {
  modalStack.value.push('reservaModal') // Añade el modal al historial
  window.history.pushState({}, '', '') // Añade un nuevo estado al historial
}

const closeModal = () => {
  emit('close')
  modalStack.value = [] // Limpia la pila de modales
}

onMounted(() => {
  window.addEventListener('popstate', handlePopState) // Escucha el evento "popstate"
  if (props.visible) {
    openModal() // Abre el modal al montar si está visible
  }
})

watch(
  () => props.visible,
  (newValue) => {
    if (newValue) {
      paso.value = 1;
      limpiarCampos();
      openModal()
    }
  }
)

onUnmounted(() => {
  window.removeEventListener('popstate', handlePopState) // Elimina el listener al desmontar
  modalStack.value = [] // Limpia la pila de modales al desmontar
})


</script>
