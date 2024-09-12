<script>
import { RouterView } from 'vue-router'
import SpinnerGlobal from "./components/UI/SpinnerGlobal.vue";

export default {
  components: {
    SpinnerGlobal, // Incluir el spinner global
  },
};
</script>

<template>
  <SpinnerGlobal />
  <RouterView />
</template>
