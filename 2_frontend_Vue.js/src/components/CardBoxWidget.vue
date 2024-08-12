<script setup>
import { mdiCog } from '@mdi/js'
import CardBox from '@/components/CardBox.vue'
import NumberDynamic from '@/components/NumberDynamic.vue'
import BaseIcon from '@/components/BaseIcon.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import PillTagTrend from '@/components/PillTagTrend.vue'
import BaseButton from '@/components/BaseButton.vue'

defineProps({
  number: {
    type: Number,
    default: 0
  },
  icon: {
    type: String,
    default: null
  },
  prefix: {
    type: String,
    default: null
  },
  suffix: {
    type: String,
    default: null
  },
  label: {
    type: String,
    default: null
  },
  color: {
    type: String,
    default: null
  },
  trend: {
    type: String,
    default: null
  },
  trendType: {
    type: String,
    default: null
  },
  cardColor: {
    type: String,
    default: 'bg-green-500' // Color por defecto
  }
})
</script>

<template>
  <CardBox :color="cardColor">
    <BaseLevel v-if="trend" mobile>
      <PillTagTrend :trend="trend" :trend-type="trendType" small />
      <BaseButton :icon="mdiCog" icon-w="w-4" icon-h="h-4" color="lightDark" small />
    </BaseLevel>
    <BaseLevel mobile>
      <BaseIcon v-if="icon" :path="icon" size="70" w="" h="h-16" :class="color" />
      <div>
        <h1 class="text-4xl leading-tight font-semibold text-center text-white">
          <NumberDynamic :value="number" :prefix="prefix" :suffix="suffix" />
        </h1>
        <h3 class="text-lg leading-tight text-white dark:text-white mt-3">
          {{ label }}
        </h3>
      </div>
    </BaseLevel>
  </CardBox>
</template>
