<template>
    <div class="col-xxl-3 col-xl-4 col-lg-5 col-md-6 col-sm-8 d-flex justify-content-center p-4">
        <router-link :to="'playlist/albums/' + album.id">
            <img loading="lazy" :src="'/src/assets/images/projects/albums/covers/' + album.id + '.jpg'" :alt="album.title">
        </router-link>
    </div>
</template>
<script setup>
defineProps({
    album: Object
})
</script>