<script setup>
import { computed, ref, onMounted } from 'vue'
import { useMainStore } from '@/stores/main'
import {
  mdiAccountMultiple,
  mdiCartOutline,
  mdiChartTimelineVariant,
  mdiMonitorCellphone,
  mdiReload,
  mdiGithub,
  mdiChartPie
} from '@mdi/js'
import * as chartConfig from '@/components/Charts/chart.config.js'
import LineChart from '@/components/Charts/LineChart.vue'
import SectionMain from '@/components/SectionMain.vue'
import CardBoxWidget from '@/components/CardBoxWidget.vue'
import CardBox from '@/components/CardBox.vue'
import TableSampleClients from '@/components/TableSampleClients.vue'
import NotificationBar from '@/components/NotificationBar.vue'
import BaseButton from '@/components/BaseButton.vue'
import CardBoxTransaction from '@/components/CardBoxTransaction.vue'
import CardBoxClient from '@/components/CardBoxClient.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import SectionBannerStarOnGitHub from '@/components/SectionBannerStarOnGitHub.vue'

const chartData = ref(null)

const fillChartData = () => {
  chartData.value = chartConfig.sampleChartData()
}

onMounted(() => {
  fillChartData()
})

const mainStore = useMainStore()

const clientBarItems = computed(() => mainStore.clients.slice(0, 4))

const transactionBarItems = computed(() => mainStore.history)
</script>

<template>
  <LayoutAuthenticated>

    <div class="px-3">
      <h2 class="">Reservas</h2>
    </div>

    <div class="calendar-app">
      <div class="calendar-container">
        <div class="calendar-header">
          <button @click="prevMonth">Anterior</button>
          <span>{{ currentMonthName }} {{ currentYear }}</span>
          <button @click="nextMonth">Siguiente</button>
        </div>
        <table class="calendar-table">
          <thead>
            <tr>
              <th>Habitaciones</th>
              <th v-for="day in daysInMonth" :key="day">{{ day }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="resource in resources" :key="resource.id">
              <td>{{ resource.title }}</td>
              <td v-for="day in daysInMonth" :key="`${resource.id}-${day}`" class="calendar-cell"
                @drop="onDrop($event, resource.id, day)" @dragover="allowDrop"
                @click="handleDateClick(resource.id, day)">
                <div v-for="event in getEventsForResourceAndDate(resource.id, day)" :key="event.id" class="event"
                  draggable="true" @dragstart="onDragStart($event, event)" @click.stop="handleEventClick(event)">
                  {{ event.title }}
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="event-creation">
          <h3>Crear nueva reserva</h3>
          <input v-model="newEventTitle" type="text" placeholder="Título del evento" />
          <input v-model="newEventStartDate" type="date" />
          <input v-model="newEventEndDate" type="date" />
          <select v-model="selectedResourceId">
            <option v-for="resource in resources" :value="resource.id" :key="resource.id">{{ resource.title }}
            </option>
          </select>
          <button @click="addEvent">Agregar evento</button>
        </div>
      </div>
    </div>
  </LayoutAuthenticated>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      currentMonth: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      events: [],
      resources: [
        { id: '1001', title: 'Habitación 1001' },
        { id: '1002', title: 'Habitación 1002' },
        { id: '1003', title: 'Habitación 1003' },
        { id: '1004', title: 'Habitación 1004' },
        { id: '1005', title: 'Habitación 1005' },
      ],
      newEventTitle: '',
      newEventStartDate: '',
      newEventEndDate: '',
      selectedResourceId: '', // Nueva propiedad para almacenar la habitación seleccionada
    };
  },
  computed: {
    currentMonthName() {
      return new Date(this.currentYear, this.currentMonth).toLocaleString('default', { month: 'long' });
    },
    daysInMonth() {
      const date = new Date(this.currentYear, this.currentMonth + 1, 0);
      return Array.from({ length: date.getDate() }, (_, i) => i + 1);
    },
  },
  methods: {
    prevMonth() {
      if (this.currentMonth === 0) {
        this.currentMonth = 11;
        this.currentYear -= 1;
      } else {
        this.currentMonth -= 1;
      }
    },
    nextMonth() {
      if (this.currentMonth === 11) {
        this.currentMonth = 0;
        this.currentYear += 1;
      } else {
        this.currentMonth += 1;
      }
    },
    handleDateClick(resourceId, day) {
      this.newEventStartDate = `${this.currentYear}-${String(this.currentMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
      this.selectedResourceId = resourceId; // Asignar automáticamente la habitación seleccionada
    },
    addEvent() {
      const startDate = new Date(this.newEventStartDate);
      const endDate = new Date(this.newEventEndDate);

      // Agregar un día a la fecha de fin para hacerla inclusiva
      endDate.setDate(endDate.getDate() + 1);

      if (this.newEventTitle && endDate >= startDate && this.selectedResourceId) {
        this.events.push({
          id: this.events.length + 1,
          title: this.newEventTitle,
          startDate,
          endDate,
          resourceId: this.selectedResourceId,
        });

        // Reset the inputs
        this.newEventTitle = '';
        this.newEventStartDate = '';
        this.newEventEndDate = '';
        this.selectedResourceId = '';
      } else {
        alert('Por favor, complete todos los campos correctamente.');
      }
    },
    handleEventClick(event) {
      if (confirm(`¿Está seguro de que desea eliminar el evento "${event.title}"?`)) {
        this.events = this.events.filter(e => e.id !== event.id);
      }
    },
    getEventsForResourceAndDate(resourceId, day) {
      return this.events.filter(event =>
        event.resourceId === resourceId &&
        this.isDateInRange(new Date(this.currentYear, this.currentMonth, day), event.startDate, event.endDate)
      );
    },
    isDateInRange(date, startDate, endDate) {
      return date >= startDate && date < endDate;
    },
    onDragStart(event, draggedEvent) {
      event.dataTransfer.setData('eventId', draggedEvent.id);
    },
    onDrop(event, resourceId, day) {
      const eventId = event.dataTransfer.getData('eventId');
      const draggedEvent = this.events.find(e => e.id === parseInt(eventId));

      if (draggedEvent) {
        const newStartDate = new Date(this.currentYear, this.currentMonth, day);
        const eventDuration = (draggedEvent.endDate - draggedEvent.startDate) / (1000 * 60 * 60 * 24);
        const newEndDate = new Date(newStartDate);
        newEndDate.setDate(newStartDate.getDate() + eventDuration);

        draggedEvent.resourceId = resourceId;
        draggedEvent.startDate = newStartDate;
        draggedEvent.endDate = newEndDate;
      }
    },
    allowDrop(event) {
      event.preventDefault();
    },
  },
});
</script>

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
