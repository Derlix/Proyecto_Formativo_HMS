<script setup>
import { containerMaxW } from '@/config.js'
import BaseLevel from '@/components/BaseLevel.vue'
// import JustboilLogo from '@/components/JustboilLogo.vue'

const year = new Date().getFullYear()
</script>

<template>
  <footer class="py-2 px-6" :class="containerMaxW">
    <BaseLevel>
      <div class="flex text-center md:text-left">
        <b>&copy;{{ year }}, <span>SALAMANDRA S.A.S</span>.</b>
        <!-- <a href="#" target="_blank">SALAMANCA</a> -->
        <slot />
      </div>
      <!-- <div class="md:py-2">
        <a href="https://justboil.me">
          <JustboilLogo class="w-auto h-8 md:h-6" />
        </a>
      </div> -->
      <div class="flex justify-center md:py-2 rounded-md space-x-4 bg-white px-3">
        <a href="https://example.com">
          <img src="@/assets/img/sena-agro.png" class="w-auto h-10 md:h-10" alt="" srcset="">
        </a>
        <a href="https://example.com">
          <img src="@/assets/img/tucan.png" class="w-auto h-10 md:h-10" alt="" srcset="">
        </a>
        <a href="https://example.com">
          <img src="@/assets/img/colombia-potencia-vida-mininterior.png" class="w-auto h-10 md:h-10" alt="" srcset="">
        </a>
      </div>
    </BaseLevel>
  </footer>
</template>
