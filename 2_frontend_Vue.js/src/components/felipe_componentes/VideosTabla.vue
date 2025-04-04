<template>
  <div class="video-library">
    <div class="video-grid grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="video in paginatedVideos" :key="video.id" class="video-item">
        <h3>{{ video.title }}</h3>
        <p>{{ video.description }}</p>
        <iframe 
          width="100%" 
          height="200" 
          :src="video.url" 
          title="YouTube video player" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen>
        </iframe>
      </div>
    </div>
    
    <div class="pagination mt-8 flex justify-center items-center space-x-4">
      <button @click="prevPage" :disabled="currentPage === 1" class="pagination-btn">
        Anterior
      </button>
      <span class="text-lg">Página {{ currentPage }} de {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages" class="pagination-btn">
        Siguiente
      </button>
    </div>
    
    <div class="manual-download mt-8 flex justify-center">
      <a :href="manualUrl" download>
        <button class="download-button">
          <i class="fas fa-file-pdf"></i> Descargar Manual de Usuario
        </button>
      </a>
    </div>
  </div>
</template>

<script>
import manualDeUsuario from '@/assets/img/ManualDeUsuarioHMS.pdf';

export default {
  data() {
    return {
      videos: [
        { id: 1, title: "Cómo Registrarse", description: "Este video explica como puedes registrarte en sena_HMS", url: "https://www.youtube.com/embed/qog-mIuM3Pk" },
        { id: 2, title: "Gestión de cuentas de huéspedes", description: "Aprende a gestionar las cuentas de huéspedes con este tutorial.", url: "https://www.youtube.com/embed/jeVg0Br3D_8" },
        { id: 3, title: "Uso de los productos del hotel", description: "Este video muestra cómo gestionar los productos del hotel", url: "https://www.youtube.com/embed/UXJvMNZMHHE" },
        { id: 4, title: "Manejo de Hoteles", description: "Aprende a manejar los hoteles y sus datos", url: "https://www.youtube.com/embed/lmzgXQ9pPA0" },
      ],
      currentPage: 1,
      videosPerPage: 4,
      manualUrl: manualDeUsuario,
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.videos.length / this.videosPerPage);
    },
    paginatedVideos() {
      const start = (this.currentPage - 1) * this.videosPerPage;
      return this.videos.slice(start, start + this.videosPerPage);
    },
  },
  methods: {
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
  },
};
</script>

<style scoped>

.video-library {
  padding: 20px;
  text-align: center;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  margin-bottom: 20px;
  color: #333;
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: 20px;
}

.video-item {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
}

.video-item:hover {
  transform: translateY(-5px);
}

.video-item h3 {
  margin: 10px;
  font-size: 1.2em;
  color: #444;
}

.video-item p {
  margin: 10px;
  color: #666;
}

iframe {
  border: none;
  border-radius: 8px;
}

.pagination {
  margin-top: 20px;
}

.pagination-btn {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.pagination-btn:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.pagination span {
  margin: 0 10px;
}

.manual-download {
  margin-top: 20px;
}

.download-button {
  background-color: #d9534f;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 1em;
  display: flex;
  align-items: center;
}

.download-button i {
  margin-right: 10px;
  font-size: 1.2em;
}

.download-button:hover {
  background-color: #c9302c;
}

@media (min-width: 640px) {
  .video-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .video-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>
