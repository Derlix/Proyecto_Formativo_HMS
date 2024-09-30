<template>
    <CardBoxModal v-model="isModalOpen" title="Editar Usuario" buttonLabel="Guardar cambios" has-cancel @cancel="cancelEdit" @confirm="updateUser">
      <form @submit.prevent="updateUser">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="mb-4">
            <label for="id_usuario" class="block text-gray-700 font-medium dark:text-white">ID Usuario:</label>
            <input type="text" id="id_usuario" v-model="currentUsuario.id_usuario" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" disabled/>
          </div>
          <div class="mb-4">
            <label for="nombre_completo" class="block text-gray-700 font-medium dark:text-white">Nombre Completo:</label>
            <input type="text" id="nombre_completo" v-model="currentUsuario.nombre_completo" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" required/>
          </div>
          <div class="mb-4">
            <label for="email" class="block text-gray-700 font-medium dark:text-white">Correo:</label>
            <input type="email" id="email" v-model="currentUsuario.email" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" required/>
          </div>
          <div class="mb-4">
            <label for="usuario_rol" class="block text-gray-700 font-medium dark:text-white">Rol:</label>
            <input type="text" id="usuario_rol" v-model="currentUsuario.usuario_rol" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" required/>
          </div>
          <div class="mb-4">
            <label for="usuario_estado" class="block text-gray-700 font-medium dark:text-white">Estado:</label>
            <select id="usuario_estado" v-model="currentUsuario.usuario_estado" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700">
              <option value="activo">Activo</option>
              <option value="inactivo">Inactivo</option>
            </select>
          </div>
          <div class="mb-4">
            <label for="file_img" class="block text-gray-700 font-medium dark:text-white">Imagen:</label>
            <input type="file" id="file_img" @change="onFileChange" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" accept="image/*"/>
          </div>
        </div>
      </form>
    </CardBoxModal>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue';
  
  const isModalOpen = ref(false);
  const currentUsuario = ref({
    id_usuario: '',
    nombre_completo: '',
    email: '',
    usuario_rol: '',
    usuario_estado: 'activo',
    file_img: null,
  });
  
  const onFileChange = (e) => {
    const file = e.target.files[0];
    currentUsuario.value.file_img = file;
  };
  
  const updateUser = async () => {
    const formData = new FormData();
    formData.append('id_usuario', currentUsuario.value.id_usuario);
    formData.append('nombre_completo', currentUsuario.value.nombre_completo);
    formData.append('email', currentUsuario.value.email);
    formData.append('usuario_rol', currentUsuario.value.usuario_rol);
    formData.append('usuario_estado', currentUsuario.value.usuario_estado);
  
    if (currentUsuario.value.file_img) {
      formData.append('file_img', currentUsuario.value.file_img);
    }
  
    try {
      // Llama al servicio de actualización con formData
      await updateUser(formData);
      alert('Usuario actualizado con éxito');
      isModalOpen.value = false;
    } catch (error) {
      alert('Error al actualizar el usuario');
    }
  };
  
  const cancelEdit = () => {
    isModalOpen.value = false;
  };
  </script>
  