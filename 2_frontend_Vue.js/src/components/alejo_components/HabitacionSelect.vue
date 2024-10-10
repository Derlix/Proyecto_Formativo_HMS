<template>
  <div class="form-container" @click="toggleDropdown">
    <label for="HabitacionSelect">Seleccione una categoría</label>

    <!-- Contenedor que actúa como select -->
    <div class="custom-select">
      <div class="selected-option text-dark ">{{ selectedHabitacionNum || 'Seleccione una Habitacion' }}</div>

      <!-- Dropdown que contiene el input y las opciones -->
      <div v-if="dropdownOpen" class="dropdown-options" @click.stop>
        <!-- Input para buscar la categoría -->
        <input 
          type="text" 
          class="search-input" 
          placeholder="Buscar habitaciones..." 
          v-model="searchQuery" 
          @input="filterReservasHabitacion"
        />

        <!-- Opciones de categorías -->
        <div 
          v-for="habitacion in filteredHabitaciones" 
          :key="habitacion.id_habitacion" 
          class="option" 
          @click.stop="selectHabitacion(habitacion)"
        >
          {{ habitacion.numero_habitacion }}
        </div>

        <!-- Mensaje cuando no hay categorías -->
        <div v-if="filteredHabitaciones.length === 0" class="no-options">
          No se encontraron habitaciones
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, onBeforeUnmount, watch } from 'vue';
import { obtenerTodasHabitaciones } from '@/services/habitacionService'


export default {
  name: 'HabitacionSelect',
  props: {
    selectedIdHabitacion: {
      type: Number,
      default: null
    }
  },
  setup(props, { emit }){
    const habitaciones = ref([]); // Almacena las categorías
    const selectedHabitacion = ref(props.selectedIdHabitacion); // Inicializa con la categoría seleccionada
    const searchQuery = ref(''); 
    const dropdownOpen = ref(false); // Estado del dropdown
    const filteredHabitaciones = ref([]); 
    

    // Función para obtener todas las categorías activas al cargar el componente
    const fetchHabitacionesActivas = async () => {
      try {
        const response = await obtenerTodasHabitaciones();
        const activos = response.data.filter(habitacion => habitacion.estado === "ACTIVO");
        habitaciones.value = activos;
        console.log("Habitaciones activas",habitaciones);
        filteredHabitaciones.value = activos;
      } catch (error) {
        console.error('Error obteniendo reservas activas:', error);
      }
    };

    // Filtra las categorías según la búsqueda
    const filterReservasHabitacion = () => {
      const query = searchQuery.value.toLowerCase();
      filteredHabitaciones.value = habitaciones.value.filter(habitacion =>
        habitacion.numero_habitacion.toLowerCase().includes(query)
      );
    };

    // Función para seleccionar una categoría
    const selectHabitacion = (habitacion) => {
      selectedHabitacion.value = habitacion.id_habitacion;
      dropdownOpen.value = false; // Cierra el dropdown
      // Emitimos el evento `category-selected` al padre, pasando la categoría seleccionada
      emit('habitacion-selected', habitacion.id_habitacion);
    };

    // Función para alternar el dropdown
    const toggleDropdown = () => {
      dropdownOpen.value = !dropdownOpen.value;
    };

    // Cerrar el dropdown al hacer clic fuera del componente
    const closeDropdownOnClickOutside = (event) => {
      if (!event.target.closest('.form-container')) {
        dropdownOpen.value = false; 
      }
    };

    // Añadir el event listener al montar el componente
    onMounted(() => {
      fetchHabitacionesActivas();
      document.addEventListener('click', closeDropdownOnClickOutside);
    });

    // Quitar el event listener al desmontar el componente
    onBeforeUnmount(() => {
      document.removeEventListener('click', closeDropdownOnClickOutside);
    });

    // Sincronizar `selectedCategory` con `selectedIdHabitacion` prop cuando cambie
    watch(() => props.selectedIdHabitacion, (newVal) => {
      selectedHabitacion.value = newVal;
    });


    const selectedHabitacionNum = computed(() => {
        const habitacion = habitaciones.value.find(hab => hab.id_habitacion === selectedHabitacion.value);

        if (habitacion) {
          const habitacionCompuesta = {
            id_habitacion: habitacion.id_habitacion,
            numero_habitacion: habitacion.numero_habitacion
          };
          console.log("Habitacion-compuesta", habitacionCompuesta);
          emit('habitacionCompuesta', habitacionCompuesta); // Emitir el objeto al componente padre
          return habitacionCompuesta
         
          
        }   
    // Si no se encuentra, devuelve null
      return null;
    });


    return {
      habitaciones, 
      selectedHabitacion,
      searchQuery,
      dropdownOpen,
      filteredHabitaciones,
      selectedHabitacionNum,
      filterReservasHabitacion,
      selectHabitacion,
      toggleDropdown,
    };
  }
};
</script>

<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  max-width: 100%;
  margin: 0 auto;
}

label {
  margin-bottom: 8px;
}

/* Custom select styles */
.custom-select {
  position: relative;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 8px;
  cursor: pointer;
}

.selected-option {
  font-size: 16px;
  
}

.dropdown-options {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 4px;
  max-height: 200px;
  overflow-y: auto;
  z-index: 2;
  color: black;
}

.search-input {
  padding: 8px;
  width: calc(100% - 16px); /* Restar padding total */
  font-size: 16px;
  border: none;
  border-bottom: 1px solid #ccc;
}

.option {
  padding: 8px;
  font-size: 16px;
  cursor: pointer;
}

.option:hover {
  background-color: #f1f1f1;
}

.no-options {
  padding: 8px;
  font-size: 14px;
  color: #999;
}
</style>
