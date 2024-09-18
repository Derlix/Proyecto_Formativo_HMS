<template>
    <div v-if="visible" class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50">
      <div :class="['modal-container', darkMode ? 'bg-gray-800 text-white' : 'bg-white text-gray-800']">
        <!-- Header del modal -->
        <div class="modal-header flex justify-between items-center p-4 border-b border-gray-300">
          <h2 class="text-lg font-bold">Selección de Habitación</h2>
          <button @click="closeModal" class="text-xl">×</button>
        </div>
  
        <!-- Campo de búsqueda -->
        <div class="modal-body p-4">
          <input
            v-model="searchQuery"
            type="text"
            class="form-input w-full mb-4"
            placeholder="Ingresa cualquier característica para encontrar la habitación deseada"
          />
          <button @click="buscarHabitacion" class="btn btn-primary mb-4">Buscar Habitación</button>
  
          <!-- Tabla de habitaciones -->
          <div class="overflow-x-auto">
            <table class="table-auto w-full bg-white rounded-lg shadow-md">
              <thead>
                <tr :class="darkMode ? 'bg-gray-700 text-white' : 'bg-gray-100'">
                  <th class="p-2">Habitación</th>
                  <th class="p-2">Categoría</th>
                  <th class="p-2">Ubicación</th>
                  <th class="p-2">Características</th>
                  <th class="p-2">Precio</th>
                  <th class="p-2">Acción</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="habitacion in habitaciones" :key="habitacion.id" :class="darkMode ? 'bg-gray-800' : ''">
                  <td class="p-2">{{ habitacion.numero }}</td>
                  <td class="p-2">{{ habitacion.categoria }}</td>
                  <td class="p-2">{{ habitacion.ubicacion }}</td>
                  <td class="p-2">{{ habitacion.caracteristicas }}</td>
                  <td class="p-2">{{ habitacion.precio }}</td>
                  <td class="p-2">
                    <button @click="elegirHabitacion(habitacion)" class="btn btn-success">Elegir Habitación</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
  
        <!-- Footer del modal -->
        <div class="modal-footer flex justify-end p-4 border-t border-gray-300">
          <button @click="closeModal" class="btn btn-secondary mr-2">Cerrar</button>
          <button @click="siguientePaso" class="btn btn-primary">Siguiente</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      visible: {
        type: Boolean,
        required: true,
      },
      darkMode: {
        type: Boolean,
        default: false,
      },
    },
    data() {
      return {
        searchQuery: '',
        habitaciones: [
          // Datos de ejemplo
          { id: 1, numero: '1003', categoria: 'Suite Jr', ubicacion: 'Interior', caracteristicas: 'Vista al mar', precio: '100.000$' },
          { id: 2, numero: '10044', categoria: 'Suite', ubicacion: 'Exterior', caracteristicas: 'Sin ventanas', precio: '100.000$' },
        ],
      };
    },
    methods: {
      buscarHabitacion() {
        // Lógica para filtrar habitaciones según `searchQuery`
      },
      elegirHabitacion() {
        // Lógica para elegir la habitación
      },
      siguientePaso() {
        // Lógica para ir al siguiente paso
      },
      closeModal() {
        this.$emit('close');
      },
    },
  };
  </script>
  
 