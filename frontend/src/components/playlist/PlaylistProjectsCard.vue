<template>
    <a :href="link" v-if="link=='#albums'">
        <img :src="'/src/assets/images/playlist/' + cover" alt="Albums">
    </a>
    <router-link :to="link" v-else>
        <img :src="'/src/assets/images/playlist/' + cover" alt="Albums">
    </router-link>
</template>
<script setup>
defineProps({
    link: String,
    cover: String
})
</script>