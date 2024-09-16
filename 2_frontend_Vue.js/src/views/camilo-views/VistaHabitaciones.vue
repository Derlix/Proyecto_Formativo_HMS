<template>
  <LayoutAuthenticated>
    <div class="container mx-auto p-6">
      <h1 class="text-2xl font-bold mb-6">Lista de Habitaciones</h1>

      <!-- Botón para crear una nueva habitación -->
      <button
        @click="mostrarModalCrear"
        class="bg-green-500 text-white px-4 py-2 rounded-md mb-6 shadow-sm hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
      >
        Crear Habitación
      </button>

      <!-- Modal para crear/editar una habitación -->
      <RoomModal
        :visible="showModal"
        :habitacion="habitacionSeleccionada"
        @close="cerrarModal"
        @save="obtenerHabitaciones"
      />

      <!-- Modal para confirmar eliminación -->
      <ModalAlert
        :visible="showConfirmModal"
        descripcion="¿Estás seguro de que deseas eliminar esta habitación?"
        textBoton="Eliminar"
        @close="showConfirmModal = false"
        @confirm="eliminarHabitacionConfirmada"
      />

      <!-- Tabla de habitaciones -->
      <table class="min-w-full bg-white border border-gray-200 rounded-lg shadow-md overflow-hidden block lg:table">
        <thead>
          <tr class="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
            <th class="py-3 px-6 text-left">Número</th>
            <th class="py-3 px-6 text-left">Piso</th>
            <th class="py-3 px-6 text-left">Categoría</th>
            <th class="py-3 px-6 text-left">Estado</th>
            <th class="py-3 px-6 text-left">Precio</th>
            <th class="py-3 px-6 text-center">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="habitacion in habitaciones"
            :key="habitacion.id_habitacion"
            class="border-b border-gray-200 hover:bg-gray-100"
          >
            <td class="py-3 px-6 text-left whitespace-nowrap">{{ habitacion.numero_habitacion }}</td>
            <td class="py-3 px-6 text-left">{{ habitacion.piso }}</td>
            <td class="py-3 px-6 text-left">{{ habitacion.id_categoria_habitacion }}</td>
            <td class="py-3 px-6 text-left">{{ habitacion.estado }}</td>
            <td class="py-3 px-6 text-left">{{ habitacion.precio_actual }}</td>
            <td class="py-3 px-6 text-center">
              <button
                @click="editarHabitacion(habitacion)"
                class="bg-blue-500 text-white px-4 py-2 rounded-md mr-2 shadow-sm hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                Editar
              </button>
              <button
                @click="confirmarEliminacion(habitacion.id_habitacion)"
                class="bg-red-500 text-white px-4 py-2 rounded-md shadow-sm hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500"
              >
                Eliminar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </LayoutAuthenticated>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import RoomModal from '@/components/RoomModal.vue';
import ModalAlert from '@/components/ModalAlert.vue';

// Referencias y estados
const habitaciones = ref([]);
const showModal = ref(false);
const showConfirmModal = ref(false);
const habitacionSeleccionada = ref({});
const habitacionAEliminar = ref(null);

const url = 'https://api-hotel-suqt.onrender.com/habitacion';

// Función para obtener todas las habitaciones
const obtenerHabitaciones = async () => {
  try {
    const token = localStorage.getItem('access_token');
    if (!token) {
      throw new Error('Token no disponible');
    }
    const respuesta = await axios.get(url, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    habitaciones.value = respuesta.data;
  } catch (error) {
    if (error.response && error.response.status === 401) {
      console.error("No autorizado. Verifica el token.");
      // Lógica adicional si necesitas manejar el token, como redireccionar al login
    } else {
      console.error("Error al obtener las habitaciones:", error.message);
    }
  }
};

// Función para eliminar una habitación
const eliminarHabitacion = async (id_habitacion) => {
  try {
    const token = localStorage.getItem('access_token');
    if (!token) {
      throw new Error('Token no disponible');
    }
    await axios.delete(`${url}/${id_habitacion}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    await obtenerHabitaciones();
  } catch (error) {
    console.error("Error al eliminar la habitación:", error.message);
  }
};

// Confirmar eliminación
const confirmarEliminacion = (id_habitacion) => {
  habitacionAEliminar.value = id_habitacion;
  showConfirmModal.value = true;
};

// Confirmar eliminación después del modal
const eliminarHabitacionConfirmada = () => {
  if (habitacionAEliminar.value) {
    eliminarHabitacion(habitacionAEliminar.value);
    showConfirmModal.value = false;
    habitacionAEliminar.value = null;
  }
};

// Función para editar habitación
const editarHabitacion = (habitacion) => {
  habitacionSeleccionada.value = habitacion;
  showModal.value = true;
};

// Mostrar modal para crear habitación
const mostrarModalCrear = () => {
  habitacionSeleccionada.value = {
    id_habitacion: null,
    numero_habitacion: '',
    piso: '',
    id_categoria_habitacion: '',
    estado: '',
    precio_actual: '',
  };
  showModal.value = true;
};

// Cerrar el modal
const cerrarModal = () => {
  showModal.value = false;
};

// Obtener las habitaciones al montar el componente
onMounted(() => {
  obtenerHabitaciones();
});
</script>

<style scoped>
/* Ajusta el tamaño del modal */
.modal-content {
  max-width: 600px;
  margin: auto;
}

/* Personaliza el tamaño de los botones */
button {
  padding: 10px 15px;
}
</style>
