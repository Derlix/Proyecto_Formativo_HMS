<template>
  <div class="max-w-4xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <h1 class="text-3xl font-semibold text-gray-800 mb-6">Gestión de Habitaciones</h1>

    <!-- Formulario de habitación -->
    <form @submit.prevent="guardarHabitacion" class="bg-white shadow-lg rounded-lg p-6 mb-8">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 mb-6">
        <!-- Estado -->
        <div>
          <label for="estado" class="block text-sm font-medium text-gray-700">Estado</label>
          <select v-model="habitacion.estado" id="estado" class="mt-1 block w-full bg-gray-50 border border-gray-300 rounded-md shadow-sm py-2 px-3 text-gray-700 focus:ring-indigo-500 focus:border-indigo-500">
            <option value="ACTIVO">Activo</option>
            <option value="INACTIVO">Inactivo</option>
            <option value="MANTENIMIENTO">Mantenimiento</option>
          </select>
        </div>

        <!-- Piso -->
        <div>
          <label for="piso" class="block text-sm font-medium text-gray-700">Piso</label>
          <input type="text" v-model="habitacion.piso" id="piso" class="mt-1 block w-full bg-gray-50 border border-gray-300 rounded-md shadow-sm py-2 px-3 text-gray-700 focus:ring-indigo-500 focus:border-indigo-500" required>
        </div>

        <!-- Precio Actual -->
        <div>
          <label for="precio_actual" class="block text-sm font-medium text-gray-700">Precio Actual</label>
          <input type="number" v-model="habitacion.precio_actual" id="precio_actual" class="mt-1 block w-full bg-gray-50 border border-gray-300 rounded-md shadow-sm py-2 px-3 text-gray-700 focus:ring-indigo-500 focus:border-indigo-500" required>
        </div>

        <!-- Usuario -->
        <div>
          <label for="id_usuario" class="block text-sm font-medium text-gray-700">ID de Usuario</label>
          <input type="text" v-model="habitacion.id_usuario" id="id_usuario" class="mt-1 block w-full bg-gray-50 border border-gray-300 rounded-md shadow-sm py-2 px-3 text-gray-700 focus:ring-indigo-500 focus:border-indigo-500" required>
        </div>

        <!-- Número de Habitación -->
        <div>
          <label for="numero_habitacion" class="block text-sm font-medium text-gray-700">Número de Habitación</label>
          <input type="text" v-model="habitacion.numero_habitacion" id="numero_habitacion" class="mt-1 block w-full bg-gray-50 border border-gray-300 rounded-md shadow-sm py-2 px-3 text-gray-700 focus:ring-indigo-500 focus:border-indigo-500" required>
        </div>

        <!-- Categoría de Habitación -->
        <div>
          <label for="id_categoria_habitacion" class="block text-sm font-medium text-gray-700">Categoría de Habitación</label>
          <input type="text" v-model="habitacion.id_categoria_habitacion" id="id_categoria_habitacion" class="mt-1 block w-full bg-gray-50 border border-gray-300 rounded-md shadow-sm py-2 px-3 text-gray-700 focus:ring-indigo-500 focus:border-indigo-500" required>
        </div>
      </div>

      <!-- Botones -->
      <div class="flex justify-end space-x-4">
        <button type="button" @click="resetForm" class="px-4 py-2 bg-gray-500 text-white rounded-md shadow hover:bg-gray-600 focus:outline-none">
          Cancelar
        </button>
        <button type="submit" class="px-4 py-2 bg-indigo-600 text-white rounded-md shadow hover:bg-indigo-700 focus:outline-none">
          {{ isEdit ? 'Actualizar' : 'Crear' }} Habitación
        </button>
      </div>
    </form>

    <!-- Tabla de Habitaciones -->
    <div class="overflow-x-auto">
      <table class="min-w-full bg-white shadow-md rounded-lg">
        <thead>
          <tr>
            <th class="px-4 py-2 border-b-2 border-gray-300 text-left text-xs font-semibold text-gray-600 uppercase">Número</th>
            <th class="px-4 py-2 border-b-2 border-gray-300 text-left text-xs font-semibold text-gray-600 uppercase">Estado</th>
            <th class="px-4 py-2 border-b-2 border-gray-300 text-left text-xs font-semibold text-gray-600 uppercase">Piso</th>
            <th class="px-4 py-2 border-b-2 border-gray-300 text-left text-xs font-semibold text-gray-600 uppercase">Precio</th>
            <th class="px-4 py-2 border-b-2 border-gray-300 text-left text-xs font-semibold text-gray-600 uppercase">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="habitacion in habitaciones" :key="habitacion.id_habitacion" class="hover:bg-gray-100">
            <td class="px-4 py-2 border-b border-gray-300">{{ habitacion.numero_habitacion }}</td>
            <td class="px-4 py-2 border-b border-gray-300">{{ habitacion.estado }}</td>
            <td class="px-4 py-2 border-b border-gray-300">{{ habitacion.piso }}</td>
            <td class="px-4 py-2 border-b border-gray-300">{{ habitacion.precio_actual }}</td>
            <td class="px-4 py-2 border-b border-gray-300 space-x-4">
              <button @click="editarHabitacion(habitacion)" class="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600">
                Editar
              </button>
              <button @click="eliminarHabitacion(habitacion.id_habitacion)" class="px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600">
                Eliminar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import {
  crearHabitacion,
  obtenerTodasHabitaciones,
  actualizarHabitacion,
  eliminarHabitacion
} from '../../services/juanca_service/habitacionService';

export default {
  data() {
    return {
      habitaciones: [],
      habitacion: {
        estado: 'ACTIVO',
        piso: '',
        precio_actual: '',
        id_usuario: '',
        numero_habitacion: '',
        id_categoria_habitacion: '',
      },
      isEdit: false,
    };
  },
  methods: {
    async fetchHabitaciones() {
      try {
        const response = await obtenerTodasHabitaciones();
        this.habitaciones = response.data;
      } catch (error) {
        console.error("Error al obtener las habitaciones:", error);
      }
    },
    async guardarHabitacion() {
      try {
        const {
          estado,
          piso,
          precio_actual,
          id_usuario,
          numero_habitacion,
          id_categoria_habitacion
        } = this.habitacion;

        if (this.isEdit) {
          await actualizarHabitacion(
            this.habitacion.id_habitacion,
            estado,
            piso,
            precio_actual,
            id_usuario,
            numero_habitacion,
            id_categoria_habitacion
          );
        } else {
          await crearHabitacion(
            estado,
            piso,
            precio_actual,
            id_usuario,
            numero_habitacion,
            id_categoria_habitacion
          );
        }
        this.fetchHabitaciones();
        this.resetForm(); // Limpiar el formulario
      } catch (error) {
        console.error('Error al guardar la habitación:', error);
      }
    },

    editarHabitacion(habitacion) {
      this.isEdit = true;
      this.habitacion = {
        ...habitacion,
        piso: Number(habitacion.piso),
        precio_actual: String(habitacion.precio_actual),
        id_usuario: String(habitacion.id_usuario),
        numero_habitacion: String(habitacion.numero_habitacion),
        id_categoria_habitacion: Number(habitacion.id_categoria_habitacion)
      };
    },
    async eliminarHabitacion(id_habitacion) {
      try {
        await eliminarHabitacion(id_habitacion);
        this.fetchHabitaciones(); // Refrescar la lista de habitaciones
      } catch (error) {
        console.error('Error al eliminar la habitación:', error);
      }
    },
    cancelarEdicion() {
      this.isEdit = false;
      this.resetForm();
    },
    resetForm() {
      this.habitacion = {
        estado: 'ACTIVO',
        piso: 0,
        precio_actual: '',
        id_usuario: '',
        numero_habitacion: '',
        id_categoria_habitacion: 0,
      };
      this.isEdit = false;
    }
  },

  mounted() {
    this.fetchHabitaciones(); // Cargar la lista de habitaciones cuando el componente es montado
  }
};
</script>

<style scoped>
form {
  margin-bottom: 20px;
}
button {
  margin-left: 10px;
}
</style>
