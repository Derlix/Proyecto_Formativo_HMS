<script setup>
import { ref, onMounted } from 'vue'
import { mdiEye, mdiTrashCan } from '@mdi/js'
import CardBoxModal from '@/components/alejo_components/CardBoxModal.vue'
import NotificationBar from '../alejo_components/NotificationBar.vue' 
import ModalAlert from '../ModalAlert.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import { getUsersByPage, deleteUser, updateUser } from '@/services/userService'

const usuarios = ref([]);
const currentUsuario = ref({});
const TotalPages = ref(0);
const isEditMode = ref(false);
const activarModalEdit = ref(false);
const currentPage = ref(1);
const isModalVisible = ref(false);
const modalMessage = ref('');
const isAlertVisible = ref(false);
const colorAlert = ref('');
const roles = ref([]); // Lista de roles

// Obtener roles desde la API
const fetchRoles = async () => {
  try {
    const response = await fetch('https://api-hotel-suqt.onrender.com/roles/get_all_roles');
    const data = await response.json();
    console.log('Roles recibidos:', data); // Verifica que la estructura contenga `rol_name`
    roles.value = data; // Almacenar los roles correctamente
  } catch (error) {
    console.error('Error al obtener los roles:', error);
  }
};

const activarModalDelete = ref({
  visible: false,
  usuario: null
});

// Obtener usuarios por página
const fetchUsuarios = async () => {
  try {
    const timestamp = new Date().getTime(); 
    const response = await getUsersByPage(currentPage.value);
    console.log('Respuesta de la API de usuarios:', response.data); // Inspecciona los datos recibidos

    usuarios.value = response.data.usuarios;
    TotalPages.value = response.data.total_paginas;
  } catch (error) {
    alert('Error al obtener usuarios');
  }
};

// Abrir modal de edición
const openEditModal = (usuario = {}) => {
  isEditMode.value = true;
  currentUsuario.value = { ...usuario };
  activarModalEdit.value = true;
  fetchRoles(); // Cargar roles al abrir el modal
};

// Actualizar usuario
const update_Usuario = async () => {
  try {
    await updateUser(
      currentUsuario.value.id_usuario,
      currentUsuario.value.nombre_completo,
      currentUsuario.value.email,
      currentUsuario.value.usuario_rol
    );
    modalMessage.value = "Usuario actualizado con éxito";
    isAlertVisible.value = true;
    colorAlert.value = 'success';
    activarModalEdit.value = false;
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
    fetchUsuarios();
  } catch (error) {
    modalMessage.value = error.response?.data?.detail || "Error al actualizar usuario";
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    activarModalEdit.value = false;
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
  }
};

// Manejar la carga de imagenes
const onFileChange = (event) => {
  const file = event.target.files[0];
  currentUsuario.value.file_img = file; // Guardar el archivo de imagen
};

// Cancelar edición
const cancelEdit = () => {
  activarModalEdit.value = false;
};

// Abrir modal de eliminación
const openDeleteModal = (usuario) => {
  activarModalDelete.value = {
    visible: true,
    usuario: usuario
  };
};

// Confirmar eliminación de usuario
const confirmDelete = async () => {
  const usuarioTemp = activarModalDelete.value.usuario;
  try {
    await deleteUser(usuarioTemp.id_usuario);
    modalMessage.value = "Usuario eliminado con éxito";
    isAlertVisible.value = true;
    colorAlert.value = 'success';
    await fetchUsuarios();
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
    fetchUsuarios();
    activarModalDelete.value.visible = false;
  } catch (error) {
    modalMessage.value = error.response?.data?.detail || "Error al eliminar usuario";
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
  }
};

// Cancelar eliminación
const cancelDelete = () => {
  activarModalDelete.value.visible = false;
};

onMounted(() => {
  fetchUsuarios();
});
</script>

<template>
  <NotificationBar
    v-if="isAlertVisible"
    :color="colorAlert"
    :description="modalMessage"
    :visible="isModalVisible"
  />

  <!-- Modal de edición de usuario -->
  <CardBoxModal v-model="activarModalEdit" title="Editar Usuario" buttonLabel="Guardar cambios" has-cancel @cancel="cancelEdit" @confirm="update_Usuario">
    <form @submit.prevent="update_Usuario()">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="mb-4">
          <label for="nombre" class="block text-gray-700 font-medium dark:text-white">Nombre Completo:</label>
          <input type="text" id="nombre" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" v-model="currentUsuario.nombre_completo" required/>
        </div>
        <div class="mb-4">
          <label for="email" class="block text-gray-700 font-medium dark:text-white">Correo:</label>
          <input type="email" id="email" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" v-model="currentUsuario.email" required/>
        </div>
        <div class="mb-4">
          <label for="rol" class="block text-gray-700 font-medium dark:text-white">Rol:</label>
          <select id="rol" v-model="currentUsuario.usuario_rol" required>
            <option value="" disabled>Selecciona un rol</option>
            <option v-for="rol in roles" :key="rol.rol_name" :value="rol.rol_name">{{ rol.rol_name }}</option>
          </select>
        </div>
        <div class="mb-4">
          <label for="imagen" class="block text-gray-700 font-medium dark:text-white">Imagen:</label>
          <input type="file" id="imagen" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-700" @change="onFileChange" accept="image/*"/>
        </div>
      </div>
    </form>
  </CardBoxModal>

  <!-- Modal de confirmación de eliminación -->
  <CardBoxModal v-model="activarModalDelete.visible" v-if="activarModalDelete.usuario" title="Eliminar Usuario" buttonLabel="Eliminar" button="danger" has-cancel @confirm="confirmDelete" @cancel="cancelDelete">
    <p class="text-xl">¿Está seguro de eliminar el usuario?</p>
    <li><b>{{ activarModalDelete.usuario.nombre_completo }}</b></li>
    <li><b>{{ activarModalDelete.usuario.email }}</b></li>
  </CardBoxModal>

  <!-- Tabla de usuarios -->
  <table>
    <thead>
      <tr>
        <th>Nombre</th>
        <th>Correo</th>
        <th>Rol</th>
        <th>Estado</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="usuario in usuarios" :key="usuario.id_usuario">
        <td data-label="Nombre: ">{{ usuario.nombre_completo }}</td>
        <td data-label="Correo: ">{{ usuario.email }}</td>
        <td data-label="Rol: ">{{ usuario.usuario_rol }}</td>
        <td data-label="Estado: ">{{ usuario.estado_usuario ? 'Activo' : 'Inactivo' }}</td>
        <td class="before:hidden lg:w-1 whitespace-nowrap">
          <BaseButtons type="justify-start lg:justify-end" no-wrap>
            <BaseButton color="info" :icon="mdiEye" small @click="openEditModal(usuario)"/>
            <BaseButton color="danger" :icon="mdiTrashCan" small @click="openDeleteModal(usuario)"/>
          </BaseButtons>
        </td>
      </tr>
    </tbody>
  </table>

  <!-- Paginación -->
  <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800">
    <BaseLevel>
      <BaseButtons>
        <BaseButton
          v-for="page in TotalPages"
          :key="page"
          :active="page === currentPage"
          :label="page"
          :color="page === currentPage ? 'lightDark' : 'whiteDark'"
          small
          @click="currentPage = page; fetchUsuarios()"
        />
      </BaseButtons>
      <small>Página {{ currentPage }} de {{ TotalPages }}</small>
    </BaseLevel>
  </div>

  <!-- Modal Alert -->
  <ModalAlert v-if="isModalVisible" :descripcion="modalMessage" textBoton="Cerrar" :visible="isModalVisible" @close="handleClose"/>
</template>
