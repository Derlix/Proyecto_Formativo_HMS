<script setup>
import SectionMain from '@/components/SectionMain.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import TablaUsuario from '@/components/arias_components/TablaUsuario.vue';

</script>


<template>
    <LayoutAuthenticated>
        <SectionMain class=" rounded-lg">
            <h1 class="text-black dark:text-white text-2xl font-bold mb-8">Control de Usuarios</h1>

            <TablaUsuario ></TablaUsuario>

        </SectionMain>
    </LayoutAuthenticated>
</template>

