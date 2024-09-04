<script setup>
import { computed, ref, onMounted } from 'vue'
import { useMainStore } from '@/stores/main'
import * as chartConfig from '@/components/Charts/chart.config.js'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import axios from 'axios'

// Reactive properties
const chartData = ref(null)
const mesActual = ref(new Date().getMonth())
const anioActual = ref(new Date().getFullYear())
const reservas = ref([])
const habitaciones = ref([])
const tituloNuevaReserva = ref('')
const fechaInicioNuevaReserva = ref('')
const fechaFinNuevaReserva = ref('')
const idHabitacionSeleccionada = ref('')

// Store
const mainStore = useMainStore()

// Computed properties
const clientBarItems = computed(() => mainStore.clients.slice(0, 4))
const transactionBarItems = computed(() => mainStore.history)
const nombreMesActual = computed(() =>
  new Date(anioActual.value, mesActual.value).toLocaleString('es-ES', { month: 'long' })
)
const diasDelMes = computed(() => {
  const fecha = new Date(anioActual.value, mesActual.value + 1, 0)
  return Array.from({ length: fecha.getDate() }, (_, i) => i + 1)
})

// Methods
const fillChartData = () => {
  chartData.value = chartConfig.sampleChartData()
}

const obtenerHabitaciones = async () => {
  try {
    const respuesta = await axios.get('http://localhost/reserva.php?action=getHabitacionesByHotel&idHotel=1')
    habitaciones.value = respuesta.data
  } catch (error) {
    console.error('Error al obtener las habitaciones:', error)
  }
}

const obtenerReservas = async () => {
  try {
    const respuesta = await axios.get(`http://localhost/reserva.php?action=getReservaPorMesAno&mes=${mesActual.value + 1}&anio=${anioActual.value}`)
    reservas.value = Array.isArray(respuesta.data) ? respuesta.data : []
  } catch (error) {
    console.error('Error al obtener las reservas:', error)
    reservas.value = []
  }
}

const mesAnterior = () => {
  if (mesActual.value === 0) {
    mesActual.value = 11
    anioActual.value -= 1
  } else {
    mesActual.value -= 1
  }
  obtenerReservas()
}

const mesSiguiente = () => {
  if (mesActual.value === 11) {
    mesActual.value = 0
    anioActual.value += 1
  } else {
    mesActual.value += 1
  }
  obtenerReservas()
}

const manejarClicFecha = (idHabitacion, dia) => {
  fechaInicioNuevaReserva.value = `${anioActual.value}-${String(mesActual.value + 1).padStart(2, '0')}-${String(dia).padStart(2, '0')}`
  idHabitacionSeleccionada.value = idHabitacion
}

const agregarReserva = () => {
  const fechaInicio = new Date(fechaInicioNuevaReserva.value)
  const fechaFin = new Date(fechaFinNuevaReserva.value)
  fechaFin.setDate(fechaFin.getDate() + 1)

  if (tituloNuevaReserva.value && fechaFin >= fechaInicio && idHabitacionSeleccionada.value) {
    reservas.value.push({
      id_reserva: reservas.value.length + 1,
      nombre_huesped: tituloNuevaReserva.value,
      fecha_entrada: fechaInicio,
      fecha_salida_propuesta: fechaFin,
      id_habitacion: idHabitacionSeleccionada.value,
    })

    tituloNuevaReserva.value = ''
    fechaInicioNuevaReserva.value = ''
    fechaFinNuevaReserva.value = ''
    idHabitacionSeleccionada.value = ''
  } else {
    alert('Por favor, complete todos los campos correctamente.')
  }
}

const manejarClicReserva = (reserva) => {
  if (confirm(`¿Está seguro de que desea eliminar la reserva de "${reserva.nombre_huesped}"?`)) {
    reservas.value = reservas.value.filter(r => r.id_reserva !== reserva.id_reserva)
  }
}

const obtenerReservasPorHabitacionYFecha = (idHabitacion, dia) => {
  return reservas.value.filter(reserva =>
    reserva.id_habitacion === idHabitacion &&
    estaFechaEnRango(new Date(anioActual.value, mesActual.value, dia), new Date(reserva.fecha_entrada), new Date(reserva.fecha_salida_propuesta))
  )
}

const estaFechaEnRango = (fecha, fechaInicio, fechaFin) => {
  return fecha >= fechaInicio && fecha <= fechaFin
}

const alIniciarArrastre = (evento, reservaArrastrada) => {
  evento.dataTransfer.setData('idReserva', reservaArrastrada.id_reserva)
}

const alSoltar = (evento, idHabitacion, dia) => {
  const idReserva = evento.dataTransfer.getData('idReserva')
  const reservaArrastrada = reservas.value.find(r => r.id_reserva === parseInt(idReserva))

  if (reservaArrastrada) {
    const nuevaFechaInicio = new Date(anioActual.value, mesActual.value, dia)
    const duracionReserva = (new Date(reservaArrastrada.fecha_salida_propuesta) - new Date(reservaArrastrada.fecha_entrada)) / (1000 * 60 * 60 * 24)
    const nuevaFechaFin = new Date(nuevaFechaInicio)
    nuevaFechaFin.setDate(nuevaFechaInicio.getDate() + duracionReserva)

    reservaArrastrada.id_habitacion = idHabitacion
    reservaArrastrada.fecha_entrada = nuevaFechaInicio
    reservaArrastrada.fecha_salida_propuesta = nuevaFechaFin
  }
}

const permitirSoltar = (evento) => {
  evento.preventDefault()
}

// Lifecycle hooks
onMounted(() => {
  fillChartData()
  obtenerHabitaciones()
  obtenerReservas()
})
</script>


<template>
  <LayoutAuthenticated>

    <div class="px-3">
      <h2 class="">Reservas</h2>
    </div>

    <div class="calendar-app">
    <div class="calendar-container">
      <div class="calendar-header">
        <button @click="mesAnterior">Anterior</button>
        <span>{{ nombreMesActual }} {{ anioActual }}</span>
        <button @click="mesSiguiente">Siguiente</button>
      </div>
      <table class="calendar-table">
        <thead>
          <tr>
            <th>Habitaciones</th>
            <th v-for="dia in diasDelMes" :key="dia">{{ dia }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="habitacion in habitaciones" :key="habitacion.id_habitacion">
            <td>{{ habitacion.numero_habitacion }}</td>
            <td v-for="dia in diasDelMes" :key="`${habitacion.id_habitacion}-${dia}`" class="calendar-cell"
              @drop="alSoltar($event, habitacion.id_habitacion, dia)" @dragover="permitirSoltar"
              @click="manejarClicFecha(habitacion.id_habitacion, dia)">
              <div v-for="reserva in obtenerReservasPorHabitacionYFecha(habitacion.id_habitacion, dia)"
                :key="reserva.id_reserva" class="event" draggable="true" @dragstart="alIniciarArrastre($event, reserva)"
                @click.stop="manejarClicReserva(reserva)">
                {{ reserva.nombre_huesped }}
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="event-creation">
        <h3>Crear nueva reserva</h3>
        <input v-model="tituloNuevaReserva" type="text" placeholder="Título del evento" />
        <input v-model="fechaInicioNuevaReserva" type="date" />
        <input v-model="fechaFinNuevaReserva" type="date" />
        <select v-model="idHabitacionSeleccionada">
          <option v-for="habitacion in habitaciones" :value="habitacion.id_habitacion" :key="habitacion.id_habitacion">
            {{ habitacion.numero_habitacion }}
          </option>
        </select>
        <button @click="agregarReserva">Agregar reserva</button>
      </div>
    </div>
  </div>
  </LayoutAuthenticated>
</template>



<style scoped>
.calendar-app {
  display: flex;
  font-family: Arial, sans-serif;
}

.calendar-container {
  flex-grow: 1;
  padding: 1rem;
}

.calendar-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.calendar-table {
  width: 100%;
  border-collapse: collapse;
}

.calendar-table th,
.calendar-table td {
  border: 1px solid #d3e2e8;
  padding: 0.5rem;
}

.calendar-table th {
  text-align: center;
  background-color: #f3f4f6;
}

.calendar-table td:first-child {
  text-align: center; /* Centra el texto en la columna de "Habitaciones" */
  font-weight: bold;
  background-color: #f3f4f6; /* Puedes personalizar el color de fondo si es necesario */
}

.calendar-cell {
  border: 1px solid #d3e2e8;
  height: 100px;
  vertical-align: top;
  padding: 0.5rem;
  position: relative;
}

.event {
  background-color: #4caf50;
  color: white;
  padding: 0.3rem;
  margin-bottom: 0.3rem;
  cursor: pointer;
  position: absolute;
  top: 5px;
  left: 5px;
  right: 5px;
}

.event-creation {
  margin-top: 2rem;
}

.event-creation input,
.event-creation select {
  margin-right: 0.5rem;
}
</style>
