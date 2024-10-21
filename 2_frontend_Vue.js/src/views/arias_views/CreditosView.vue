<script setup>
import { ref, onMounted } from 'vue';

const profiles = ref([]);
const errorMessage = ref(null);
const isLoading = ref(true); // Variable para manejar el estado de carga

// Lista de usuarios de GitHub y sus LinkedIns
const usernames = [
  { github: 'Derlix', linkedin: 'christian-325615306' },
  { github: '8ustamante', linkedin: 'su_linkedin' },
  { github: 'Nicolas-tv17', linkedin: 'su_linkedin' },
  { github: 'destroyer012134', linkedin: 'miguel-angel-mora-galeano-72975428a' },
  { github: 'Juan-Camilo-MH', linkedin: 'su_linkedin' },
  { github: 'Alejo412', linkedin: 'su_linkedin' },
  { github: 'Felipe0521', linkedin: 'su_linkedin' },
  { github: 'BrayanAlexisCar', linkedin: 'su_linkedin' }
];

const fetchGitHubProfiles = async () => {
  try {
    profiles.value = await Promise.all(usernames.map(user => fetchGitHubProfile(user.github)));
  } catch (error) {
    errorMessage.value = 'Error fetching profiles: ' + error.message;
  } finally {
    isLoading.value = false; // Finaliza la carga
  }
};

const fetchGitHubProfile = async (username) => {
  try {
    const response = await fetch(`https://api.github.com/users/${username}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching GitHub profile:', error);
    return null;
  }
};

// Llamada a la API cuando se monta el componente
onMounted(() => {
  fetchGitHubProfiles();
});
</script>

<template>

    <section class="min-h-screen bg-gray-100 flex flex-col justify-center items-center py-10">
      <h1 class="text-4xl font-bold text-green-600 mb-8">Desarrolladores</h1>
  
      <div v-if="isLoading" class="flex justify-center items-center">
        <!-- Imagen de carga -->
        <img src="../../assets/img/loading.gif" alt="Cargando" class="w-32 h-32 animate-spin">
      </div>
  
      <div v-if="!isLoading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-6 max-w-4xl w-full px-4">
        <div v-if="errorMessage" class="col-span-full text-red-600">{{ errorMessage }}</div>
  
        <!-- Renderización de cada perfil -->
        <div v-for="(profile, index) in profiles" :key="profile.id"
          :class="[
            { 'manga-style': profile.login === 'Derlix', 
              'cowboy-style': profile.login === '8ustamante', 
              'space-style': profile.login === 'Nicolas-tv17', 
              'tech-style': profile.login === 'destroyer012134', 
              'floral-style': profile.login === 'Juan-Camilo-MH', 
              'mona-lisa-style': profile.login === 'Alejo412', 
              'basic-style': profile.login === 'Felipe0521', 
              'movie-style': profile.login === 'BrayanAlexisCar' 
            },
            'bg-white p-4 rounded-lg shadow-md flex items-center space-x-4'
          ]">
          <img :src="profile.avatar_url" alt="Avatar" class="w-16 h-16 rounded-full">
          <div>
            <h2 class="text-xl font-semibold">{{ profile.name || profile.login }}</h2>
            <p class="text-sm text-gray-600">@{{ profile.login }}</p>
            <div class="flex space-x-4 mt-2">
              <!-- Enlace a GitHub con icono -->
              <a :href="profile.html_url" target="_blank" class="text-gray-600 hover:text-gray-900">
                <i class="fab fa-github text-2xl"></i>
              </a>
              <!-- Enlace a LinkedIn con icono -->
              <a :href="`https://www.linkedin.com/in/${usernames[index].linkedin}/`" target="_blank" class="text-blue-600 hover:text-blue-700">
                <i class="fab fa-linkedin text-2xl"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
  
      <div class="text-center m-10">
        <router-link to="/" class="text-3xl text-blue-600 hover:text-black">Volver</router-link>
      </div>
    </section>
  </template>
  
  <style scoped>
  h1 {
    color: #1a202c;
  }
  
  i {
    transition: transform 0.2s ease;
  }
  
  i:hover {
    transform: scale(1.1);
  }
  
  /* Animación de giro */
  .animate-spin {
    animation: spin 2s linear infinite;
  }
  
  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
  
  /* Estilo de manga para Derlix */
  .manga-style {
    border: 4px solid black;
    background: linear-gradient(to bottom right, #f2f2f2, #ffffff);
    font-family: 'Comic Sans MS', cursive, sans-serif;
    box-shadow: 10px 10px 0px #000000;
    transition: transform 0.3s ease;
    position: relative;
    overflow: hidden;
  }
  
  .manga-style::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('../../assets/img/kitty.png'); /* Imagen de fondo */
    background-size: contain; /* Mantén los extremos visibles */
    background-repeat: no-repeat; /* Evita que la imagen se repita */
    background-position: center; /* Centra la imagen */
    z-index: -1;
    opacity: 0.5; /* Ajusta la opacidad según sea necesario */
  }
  
  .manga-style:hover {
    transform: scale(1.05);
    background-position: center;
  }
  
  /* Estilo de vaquero para 8ustamante */
  /* Estilo de vaquero para 8ustamante */
.cowboy-style {
    border: 4px solid saddlebrown;
     /* Fondo con textura de cuero o madera */
    
    font-family: 'Courier New', monospace;
    box-shadow: 8px 8px 0px #8b4513;
    transition: transform 0.3s ease;
    position: relative;
    
  }
  
  .cowboy-style::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(139, 69, 19, 0.6); /* Capa de color marrón semitransparente */
    z-index: -1;
    background: url('../../assets/img/pepito.jpeg');
    background-size: cover;
    opacity: 0.1;
  }
  
  .cowboy-style:hover {
    transform: scale(1.05);
  }
  
  
  /* Estilo del espacio para Nicolas-tv17 */
  .space-style {
    border: 3px solid #4a90e2;
    background: radial-gradient(circle, #191636, #0f0c29, #1a1a3d);
    color: white;

    box-shadow: 8px 8px 0px #000000;
    transition: transform 0.3s ease, background-position 0.3s ease;
    position: relative;
    overflow: hidden;
  }
  
  /* Añadir las estrellas animadas */
  .space-style::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 200%;
    height: 200%;
    background-image: url('https://www.transparenttextures.com/patterns/stardust.png'); /* Fondo de estrellas */
    background-size: cover;
    background-position: 0 0;
    opacity: 0.3;
    transition: transform 0.3s ease;
    z-index: -1;
  }
  
  .space-style:hover {
    transform: scale(1.05);
    /* Movimiento de las estrellas en el fondo */
    background-position: center;
  }
  
  .space-style:hover::before {
    transform: translate(-50%, -50%);
  }
  
  /* Estilo tecnológico para destroyer012134 */
  /* Estilo tecnológico para destroyer012134 */
/* Estilo tecnológico para destroyer012134 */
.tech-style {
    border: 4px solid #007acc;
    background: url('path/to/cpp-logo.png'); /* Fondo con logo de C++ */
    background-size: cover;
    font-family: 'Consolas', monospace;
    box-shadow: 10px 10px 0px #003366;
    transition: transform 0.3s ease, background-position 1s ease;
    position: relative;
  }
  
  .tech-style:hover {
    transform: scale(1.05);
    background-position: center;
  }
  
  /* Estilo floral con animación de hojas para Juan-Camilo-MH */
  .floral-style {
    border: 3px solid rgb(0, 30, 85);
    background: url('../../assets/img/blue-leaves-bg.jpg'); /* Fondo de hojas */
    background-size: cover;
    font-family: 'Verdana', sans-serif;
    box-shadow: 8px 8px 0px #111764;
    transition: transform 0.3s ease;
    position: relative;
  }
  
  .floral-style:hover {
    transform: scale(1.05);
  }
  
  .floral-style::after {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    width: 100px;
    height: 100px;
    background: url('../../assets/img/leaf.png');
    background-size: contain;
    animation: fall 3s infinite;
    opacity: 0.6;
  }
  
  @keyframes fall {
    0% {
      transform: translateY(-100px) rotate(0deg);
    }
    100% {
      transform: translateY(500px) rotate(360deg);
    }
  }
  
  /* Estilo Mona Lisa para Alejo412 con cuadro girando */
  .mona-lisa-style {
    border: 3px solid rgb(36, 63, 32);
    background: url('../../assets/img/mona-lisa.jpg'); /* Fondo de la Mona Lisa */
    background-size: cover;
    font-family: 'Times New Roman', serif;
    box-shadow: 8px 8px 0px #092e23;
    transition: transform 0.3s ease;
    position: relative;
  }
  
  .mona-lisa-style:hover {
    transform: scale(1.05) rotateY(360deg); /* Rotación 3D en hover */
    transition: transform 1s ease;
  }
  
  /* Estilo para Felipe0521 con temática de autos */
  .basic-style {
    border: 2px solid limegreen;
    background: url('../../assets/img/car-background.jpg'); /* Fondo de autos */
    background-size: cover;
    box-shadow: 6px 6px 0px #006400;
    transition: transform 0.3s ease;
    position: relative;
  }
  
  .basic-style:hover {
    transform: scale(1.05);
  }
  
  .basic-style::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 100px;
    height: 50px;
    background: url('../../assets/img/car.png'); /* Imagen de auto */
    background-size: contain;
    animation: drive 3s infinite;
    transform: translate(-50%, -50%);
  }
  
  @keyframes drive {
    0% {
      transform: translateX(-100px);
    }
    100% {
      transform: translateX(400px);
    }
  }
  
  /* Estilo para BrayanAlexisCar con telón de cine */
  .movie-style {
    border: 4px solid gray;
    background: url('../../assets/img/cinema-bg.jpg'); /* Fondo de cine */
    background-size: cover;
    font-family: 'Arial', sans-serif;
    box-shadow: 10px 10px 0px #000000;
    transition: transform 0.3s ease;
    position: relative;
  }
  
  .movie-style:hover {
    transform: scale(1.05);
  }
  
  .movie-style::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, rgba(0, 0, 0, 0.9) 30%, rgba(0, 0, 0, 0) 50%, rgba(0, 0, 0, 0.9) 70%);
    z-index: -1;
    transition: background-position 1s ease;
  }
  
  .movie-style:hover::before {
    background-position: right;
  }
  
  </style>
  