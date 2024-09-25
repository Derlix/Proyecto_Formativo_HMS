<script setup>
import { getUsersByPage } from '@/services/userService'
import { onMounted, ref } from 'vue'
import { mdiEye, mdiTrashCan } from '@mdi/js'
import TableCheckboxCell from '@/components/TableCheckboxCell.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import UserAvatar from '@/components/UserAvatar.vue'

defineProps({
  checkable: Boolean
})

const usuarios = ref([]);
const currentusuario = ref({});
const currentPage = ref(1);
const TotalPages = ref(0);

const fetchUsuarios = async () => {
    try {
        const response = await getUsersByPage(currentPage.value);
        console.log(response);
        const activos = response.data.usuarios.filter(usuario => usuario.estado_usuario === true);
        usuarios.value = activos;

        TotalPages.value = response.data.total_paginas;
    } catch (error) {
        alert('Error al obtener los usuarios');
    }
};

onMounted(() => {
    fetchUsuarios();
});
</script>

<template>
  <table>
    <thead>
      <tr>
        <th v-if="checkable" />
        <th />
        <th>Nombre Completo</th>
        <th>Correo</th>
        <th>Rol</th>
        <th>Estado</th>
        <th />
      </tr>
    </thead>
    <tbody>
      <tr v-for="usuario in usuarios" :key="usuario.id_usuario">
        <TableCheckboxCell v-if="checkable" @checked="checked($event, usuario)" />
        <td class="border-b-0 lg:w-6 before:hidden">
          <UserAvatar :username="usuario.nombre_completo" class="w-24 h-24 mx-auto lg:w-6 lg:h-6" />
        </td>
        <td data-label="Nombre Completo">
          {{ usuario.nombre_completo }}
        </td>
        <td data-label="Correo">
          {{ usuario.email }}
        </td>
        <td data-label="Rol">
          {{ usuario.usuario_rol }}
        </td>
        <td data-label="Estado">
          {{ usuario.usuario_estado ? 'Activo' : 'Inactivo' }}
        </td>
        <td class="before:hidden lg:w-1 whitespace-nowrap">
          <BaseButtons type="justify-start lg:justify-end" no-wrap>
            <BaseButton color="info" :icon="mdiEye" small @click="isModalActive = true" />
            <BaseButton color="danger" :icon="mdiTrashCan" small @click="isModalDangerActive = true" />
          </BaseButtons>
        </td>
      </tr>
    </tbody>
  </table>
  <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800">
    <BaseLevel>
      <BaseButtons>
        <BaseButton
          v-for="page in TotalPages"
          :key="page"
          :active="page === currentPage"
          :label="page + 1"
          :color="page === currentPage ? 'lightDark' : 'whiteDark'"
          small
          @click="currentPage = page; fetchUsuarios()"
        />
      </BaseButtons>
      <small>Página {{ currentPage }} de {{ TotalPages }}</small>
    </BaseLevel>
  </div>
</template>