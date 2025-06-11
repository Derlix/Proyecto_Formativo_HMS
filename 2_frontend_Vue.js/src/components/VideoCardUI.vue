<template>
    <div class="w-auto rounded-2xl shadow-md p-2 bg-gray-100 hover:bg-gray-400 transition cursor-pointer">
        <div class="relative" style="padding-top: 56.25%;">
            <iframe
                class="absolute top-0 left-0 w-full h-full rounded-xl"
                :src="`https://www.youtube.com/embed/${videoId}`"
                :title="title"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
            </iframe>
        </div>
        <h3 class="mt-2 text-center text-gray-900 font-semibold italic">{{ title }}</h3>
    </div>
</template>

<script setup>
defineProps({
    title: String,
    videoId: String,
})
</script>
