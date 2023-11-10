<template>
    <div class="
            col-xxl-3 col-xl-4 col-lg-5 col-md-5 col-sm-7 px-0
            playlist_links" v-for="project in projects">
        <PlaylistProjectsCard :link="project.link" :cover="project.cover" />
    </div>
</template>
<script setup>
import PlaylistProjectsCard from './PlaylistProjectsCard.vue';
defineProps({
    projects: Array
})
</script>
<style>
#albums img {
    width: 100%;
    border-radius: 20px;
    border: 5px solid var(--light-gray-azuko-rgb);
    transition: .3s;
}

#albums img:hover,
.playlist_links img:hover {
    transform: scale(1.03);
    box-shadow: 2px 2px 10px var(--darker-gray-azuko-rgb);
}

.playlist_links img {
    width: 100%;
    border-radius: 15px;
    transition: .3s;
}
</style>