<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Calendario de Reservas</h1>
    <FullCalendar :options="calendarOptions" />
  </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction'; // Para manejar interacciones
import esLocale from '@fullcalendar/core/locales/es'; // Importa el idioma español
import resourceTimelinePlugin from '@fullcalendar/resource-timeline'; // Importa el plugin de resource timeline
import api from '@/services/api'; // Asegúrate de tener configurada tu API

export default {
  components: {
    FullCalendar, // Hacemos disponible el componente FullCalendar
  },
  data() {
    return {
      calendarOptions: {
        plugins: [dayGridPlugin, interactionPlugin, resourceTimelinePlugin], // Incluye el plugin de recursos
        initialView: 'resourceTimelineMonth', // Cambia la vista inicial para usar recursos
        events: [], // Aquí almacenaremos las reservas
        resources: [], // Aquí se almacenarán las habitaciones (recursos)
        locale: esLocale, // Establece el idioma a español
        eventClick: this.handleEventClick,
      },
    };
  },
  mounted() {
    this.fetchResources();
    this.fetchReservations();
  },
  methods: {
    async fetchResources() {
      try {
        const response = await api.get('/habitacion/get_all_rooms'); // Cambia esta ruta por la de tus habitaciones
        this.calendarOptions.resources = response.data.map(habitacion => ({
          id: habitacion.id_habitacion,
          title: `Habitación ${habitacion.numero_habitacion}`,
        }));
      } catch (error) {
        console.error('Error al obtener las habitaciones:', error);
      }
    },
    async fetchReservations() {
      try {
        const response = await api.get('/Reserva-habitacion/get_all'); // Cambia esta ruta por la de tus reservas
        this.calendarOptions.events = response.data.map(reserva => ({
          id: reserva.id_reserva,
          resourceId: reserva.id_habitacion, // Asocia la reserva con la habitación correspondiente
          start: reserva.fecha_entrada, // Fecha de inicio de la reserva
          end: reserva.fecha_salida_propuesta, // Fecha de salida de la reserva
          title: `Huésped: ${reserva.huesped.nombre_completo}`, // Nombre del huésped
          backgroundColor: reserva.estado === 'ocupada' ? 'red' : 'green', // Color según el estado de la reserva
        }));
      } catch (error) {
        console.error('Error al obtener las reservas:', error);
      }
    },
    handleEventClick(info) {
      const reservaId = info.event.id; // Asegúrate de que tu evento tenga un ID
      this.$router.push({ name: 'informacion_reserva', params: { id: reservaId } });
    }
  },
};
</script>

<style scoped>
/* Puedes personalizar los estilos aquí si es necesario */
</style>
