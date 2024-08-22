<script setup>
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
</script>

<template>
    <LayoutAuthenticated>
        <div class="p-5 flex flex-col items-center">
            <h1 class="text-3xl font-bold mb-5 text-center">Habitaciones Disponibles</h1>
            <div id="card-container" class="flex flex-wrap justify-center"></div>

            <div class="flex justify-center mt-5 gap-4">
                <button id="prev-button" class="px-4 py-2 bg-blue-500 text-white rounded-md"
                    @click="changePage(-1)">Anterior</button>
                <span id="page-info" class="text-lg"></span>
                <button id="next-button" class="px-4 py-2 bg-blue-500 text-white rounded-md"
                    @click="changePage(1)">Siguiente</button>
            </div>

            <div class="mt-10 w-full max-w-4xl">
                <table class="w-full border border-gray-300 bg-white">
                    <thead>
                        <tr>
                            <td colspan="3" class="table-header text-center py-2 text-lg font-bold">Tabla de
                                Recopilación</td>
                        </tr>
                        <tr>
                            <th class="border px-4 py-2 table-column-header">Piso</th>
                            <th class="border px-4 py-2 table-column-header">Pax</th>
                            <th class="border px-4 py-2 table-column-header">Habitaciones</th>
                        </tr>
                    </thead>
                    <tbody id="recopilation-body">
                        <!-- Las filas se agregarán aquí dinámicamente -->
                    </tbody>
                </table>
                <div class="mt-4">
                    <label for="created-by" class="block text-lg font-medium text-gray-700">Elaborado por:</label>
                    <input type="text" id="created-by"
                        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                        placeholder="Nombre del creador">
                </div>
            </div>
        </div>
    </LayoutAuthenticated>
</template>

<script>
export default {
    name: 'InformePasajeros',
    mounted() {
        this.initializeCards();
        this.fillRecopilationTable(10);
    },
    data() {
        return {
            CARDS_PER_PAGE: 4,
            currentPage: 1,
            totalCards: 20
        }
    },
    methods: {
        initializeCards() {
            this.updatePage();
        },
        generateCards(quantity) {
            const container = document.getElementById('card-container');
            container.innerHTML = '';
            for (let i = 1; i <= quantity; i++) {
                container.appendChild(this.createCard(i));
            }
        },
        createCard(floor) {
            const card = document.createElement('div');
            card.className = 'card bg-white border border-gray-300';
            card.innerHTML = `
        <table class="w-full border border-gray-300">
          <thead>
            <tr>
              <td colspan="3" class="text-center text-lg font-bold table-card-header">Piso ${floor}</td>
            </tr>
            <tr>
              <th class="px-4 py-2 table-card-column-header border">Habitación</th>
              <th class="px-4 py-2 table-card-column-header border">Pax</th>
              <th class="px-4 py-2 table-card-column-header border">Nombre</th>
            </tr>
          </thead>
          <tbody>
            ${Array.from({ length: 10 }, (_, j) => this.createTableRow(floor, j)).join('')}
          </tbody>
        </table>
      `;
            return card;
        },
        createTableRow(floor, index) {
            const room = 100 + (floor * 10) + index;
            const pax = Math.floor(Math.random() * 4) + 1;
            const name = `Nombre ${room}`;
            return `
        <tr class="border-b">
          <td class="px-4 py-2 border">${room}</td>
          <td class="px-4 py-2 border">${pax}</td>
          <td class="px-4 py-2 border">${name}</td>
        </tr>
      `;
        },
        fillRecopilationTable(rows) {
            const tbody = document.getElementById('recopilation-body');
            tbody.innerHTML = Array.from({ length: rows }, () => `
        <tr>
          <td class="border px-4 py-2"></td>
          <td class="border px-4 py-2"></td>
          <td class="border px-4 py-2"></td>
        </tr>
      `).join('');
        },
        updatePage() {
            const container = document.getElementById('card-container');
            container.innerHTML = '';
            const start = (this.currentPage - 1) * this.CARDS_PER_PAGE + 1;
            const end = Math.min(this.currentPage * this.CARDS_PER_PAGE, this.totalCards);
            for (let i = start; i <= end; i++) {
                container.appendChild(this.createCard(i));
            }
            document.getElementById('page-info').textContent = `Página ${this.currentPage} de ${Math.ceil(this.totalCards / this.CARDS_PER_PAGE)}`;
            document.getElementById('prev-button').disabled = this.currentPage === 1;
            document.getElementById('next-button').disabled = this.currentPage === Math.ceil(this.totalCards / this.CARDS_PER_PAGE);
        },
        changePage(direction) {
            this.currentPage += direction;
            this.updatePage();
        }
    }
}
</script>

<style scoped>
body {
    background-color: #edf8ff;
}

.table-header,
.table-card-header {
    background-color: #5589b9;
    color: white;
}

.table-column-header,
.table-card-column-header {
    background-color: #d9d9d9;
}

.card {
    min-width: 300px;
}
</style>