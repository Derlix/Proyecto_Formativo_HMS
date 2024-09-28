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
  import resourceTimelinePlugin from '@fullcalendar/resource-timeline'; // Para la vista de recursos
  import api from '@/services/api'; // Asegúrate de tener configurada tu API
  
  export default {
    components: {
      FullCalendar, // Hacemos disponible el componente FullCalendar
    },
    data() {
      return {
        calendarOptions: {
          plugins: [dayGridPlugin, interactionPlugin],
          initialView: 'dayGridMonth', // Muestra el calendario en vista de línea de tiempo de recursos
          events: [], // Aquí almacenaremos las reservas
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
          const response = await api.get('/path/to/habitaciones'); // Cambia esta ruta por la de tus habitaciones
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
    },
  };
  </script>
  
  <style scoped>
  /* Puedes personalizar los estilos aquí si es necesario */
  </style>
  