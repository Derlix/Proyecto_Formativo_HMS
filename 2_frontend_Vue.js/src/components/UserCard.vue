<script setup>
import { computed, ref, onMounted } from 'vue'
import { useMainStore } from '@/stores/main'
import { mdiCheckDecagram } from '@mdi/js'
import BaseLevel from '@/components/BaseLevel.vue'
import UserAvatarCurrentUser from '@/components/UserAvatarCurrentUser.vue'
import CardBox from '@/components/CardBox.vue'
// import FormCheckRadio from '@/components/FormCheckRadio.vue'
import PillTag from '@/components/PillTag.vue'

const mainStore = useMainStore()

const userName = computed(() => {
  const fullName = mainStore.userName || '';
  const firstName = fullName.split(' ')[0]
  return firstName.length > 16 ? firstName.substring(0, 16) : firstName
})
const userRole = computed(() => mainStore.userRole)
const nombreHotel = computed(() => mainStore.nombreHotelOperando)
const dataIP = ref(null)

const obtenerDataIP = async () => {
  try {
    const response = await getIpLocation()
    dataIP.value = response
  } catch (error) {
    console.error('Error al cargar datos de IP:', error)
  }
}

const userSwitchVal = ref(false)
</script>

<template>
  <CardBox>
    <BaseLevel type="justify-around lg:justify-center">
      <UserAvatarCurrentUser class="lg:mx-12" />
      <div class="space-y-3 text-center md:text-left lg:mx-12">
        <!-- <div class="flex justify-center md:block">
          <FormCheckRadio
            v-model="userSwitchVal"
            name="notifications-switch"
            type="switch"
            label="Notifications"
            :input-value="true"
          />
        </div> -->
        
        <h1 class="text-2xl">
          Hola, <b>{{ userName }}</b
          >!
        </h1>
        <p class="text-base">Rol: <b>{{ userRole }}</b>.</p>
        <p v-if="nombreHotel !== 'undefined' && nombreHotel !== null" class="text-base">Hotel: <b>{{ nombreHotel }}</b>.</p>
        <!-- <div class="flex justify-center md:block">
          <PillTag label="Verificado" color="info" :icon="mdiCheckDecagram" />
        </div> -->
      </div>
    </BaseLevel>
  </CardBox>
</template>
