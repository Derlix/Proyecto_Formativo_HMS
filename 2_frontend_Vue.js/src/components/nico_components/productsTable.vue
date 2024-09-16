<script setup>
import { ref } from 'vue';
import { getProductsByPage } from '@/services/productService';
import BaseLevel from '@/components/BaseLevel.vue';
import BaseButtons from '@/components/BaseButtons.vue';
import BaseButton from '@/components/BaseButton.vue';

// Define `emit` para emitir eventos al componente padre
const emit = defineEmits(['accionEnviada']);

const productos = ref([]);
const currentPage = ref(1);
const TotalPages = ref(0);

const fechtProducts = async () => {
  try {
    const response = await getProductsByPage(currentPage.value);
    productos.value = response.data.productos;
    TotalPages.value = response.data.total_pages;
  } catch (error) {
    alert('Error al obtener productos: ', error);
  }
};

// Llamar a la función para obtener los productos al montar el componente
fechtProducts();

// Función para emitir acciones al padre
const emitirAccion = (tipoAccion, producto) => {
  emit('accionEnviada', { tipo: tipoAccion, producto });
};
</script>

<template>
  <table>
    <thead>
      <tr>
        <th>Id</th>
        <th>Nombre</th>
        <th>Descripcion</th>
        <th>Precio</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="producto in productos" :key="producto.id_producto">
        <td>{{ producto.id_producto }}</td>
        <td>{{ producto.nombre_producto }}</td>
        <td>{{ producto.descripcion }}</td>
        <td>{{ producto.precio_actual }}</td>
        <td class="before:hidden lg:w-1 whitespace-nowrap">
          <BaseButtons type="justify-start lg:justify-end" no-wrap>
            <BaseButton color="info" :icon="mdiBookEdit" small @click="emitirAccion('update', producto)" />
            <BaseButton color="danger" :icon="mdiTrashCan" small @click="emitirAccion('delete', producto)" />
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
          :label="page"
          :color="page === currentPage ? 'lightDark' : 'whiteDark'"
          small
          @click="currentPage = page; fechtProducts()"
        />
      </BaseButtons>
      <small>Página {{ currentPage }} de {{ TotalPages }}</small>
    </BaseLevel>
  </div>
</template>
