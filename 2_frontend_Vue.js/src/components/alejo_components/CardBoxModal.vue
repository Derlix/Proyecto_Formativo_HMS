<template>
  <OverlayLayer v-show="modelValue" @overlay-click="cancel">
    <CardBox
      v-show="modelValue"
      class="shadow-lg max-h-modal w-11/12 md:w-3/5 lg:w-2/5 xl:w-4/12 z-50"
      is-modal
    >
      <CardBoxComponentTitle :title="title">
        <BaseButton
          v-if="hasCancel"
          :icon="mdiClose"
          color="whiteDark"
          small
          rounded-full
          @click.prevent="cancel"
        />
      </CardBoxComponentTitle>

      <div class="space-y-3 ">
        <slot />
      </div>

      <template #footer>
        <BaseButtons>
          <BaseButton
            type="submit" 
            :label="buttonLabel"
            :color="button"
            @click="handleButtonClick"
            class="pr-2 mr-2"
          />
          <BaseButton v-if="hasCancel" label="Cancelar" :color="button" outline @click="cancel" />
        </BaseButtons>
      </template>
    </CardBox>
  </OverlayLayer>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'
import BaseButton from '@/components/BaseButton.vue'
import OverlayLayer from '@/components/OverlayLayer.vue'
import CardBox from '@/components/CardBox.vue'
import CardBoxComponentTitle from '@/components/CardBoxComponentTitle.vue'
import { mdiClose } from '@mdi/js'

const props = defineProps({
  title: String,
  button: {
    type: String,
    default: 'info'
  },
  buttonLabel: {
    type: String,
    default: 'Done'
  },
  hasCancel: Boolean,
  modelValue: Boolean
})

const emit = defineEmits(['update:modelValue', 'cancel', 'confirm'])

const cancel = () => {
  emit('cancel')
}

const handleButtonClick = (event) => {
  event.preventDefault()  // Prevent default button behavior
  emit('confirm')  // Emit the 'confirm' event to the parent component
}
</script>
