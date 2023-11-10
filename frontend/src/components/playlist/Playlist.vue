<template>
    <div id="playlist">
        <div class="title d-flex justify-content-center align-items-center vh-100" id="products">
            <span class="animate__animated animate__fadeIn">Playlist</span>

            <a href="#" class="slider_buttons slider_button_up_disabled"><i class="fa-solid fa-up-long fa-xl"></i></a>
            <a href="/playlist#playlist_projects" class="slider_buttons slider_button_down_1"><i
                    class="fa-solid fa-down-long fa-xl"></i></a>

        </div>
        <div class="container-fluid">
            <div class="row d-flex align-items-center" id="playlist_projects">
                <div class="row d-flex justify-content-center gap-5">
                    <PlaylistProjects :projects="projects" />
                </div>
            </div>
            <div class="row d-flex justify-content-center align-items-center" id="albums">
                <div class="col-10">
                    <div class="row d-flex justify-content-center align-items-center">

                        <PlaylistAlbumsCard v-for="album in albums" :album="album" />

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import PlaylistProjects from './PlaylistProjects.vue';
import PlaylistAlbumsCard from './PlaylistAlbumsCard.vue'
import { useFetch } from '@vueuse/core'
const url_albums = 'http://localhost:8000/read_albums'
async function fetchAPI(url) {
    const { data } = await useFetch(url).json()
    const API = data.value
    return API
}
const albums = await fetchAPI(url_albums)
const projects = [
    { 'link': '#albums', 'cover': 'albums.jpg' },
    { 'link': '/singles', 'cover': 'singles.jpg' },
    { 'link': '/featurings', 'cover': 'featurings.jpg' }
]
</script>
<style>
</style>