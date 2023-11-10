<template>
    <div>
        <div class="title d-flex justify-content-center align-items-center vh-100" id="projects">
            <span>Projects</span>

            <a href="#" class="slider_buttons slider_button_up_disabled"><i class="fa-solid fa-up-long fa-xl"></i></a>
            <a href="#albums_carousel_div" class="slider_buttons slider_button_down_1"><i
                    class="fa-solid fa-down-long fa-xl"></i></a>

        </div>
        <div class="projects">
            <div class="container-fluid">
                <Suspense timeout="0">
                    <div>
                        <ProjectsAlbums :albums="albums" />
                        <ProjectsTracks :projects="singles" :projects_info="singles_info" />
                        <ProjectsTracks class="mb-5" :projects="featurings" :projects_info="featurings_info" />
                    </div>
                    <template #fallback>
                        <div class="d-flex justify-content-center align-items-center vh-100">
                            <Spinner />
                        </div>
                    </template>
                </Suspense>
            </div>
        </div>
    </div>
</template>
<script setup>
import { defineAsyncComponent } from 'vue'
import { useFetch } from '@vueuse/core'
import Spinner from '../elements/Spinner.vue'
const ProjectsTracks = defineAsyncComponent(() => import('./ProjectsTracks.vue'))
const ProjectsAlbums = defineAsyncComponent(() => import('./ProjectsAlbums.vue'))
async function fetchAPI(url) {
    const { data } = await useFetch(url).json()
    return data.value
}
const albums = await fetchAPI('http://localhost:8000/read_albums')
const singles = await fetchAPI('http://localhost:8000/read_singles')
const featurings = await fetchAPI('http://localhost:8000/read_featurings')
setTimeout(fetchAPI, 5000);
const singles_info = {
    'cover': 'singles', 'alt': 'Singles', 'show_more_link': '#singles_cards',
    'up_link': '#albums_carousel_div', 'down_link': '#featurings_cards'
}
const featurings_info = {
    'cover': 'featurings', 'alt': 'Featurings', 'show_more_link': '#featurings_cards',
    'up_link': '#singles_cards', 'down_link': '#footer'
}
</script>

<script>
export default {
  mounted() {
    setTimeout(() => Spinner, 4000);
  },
}
</script>
<style></style>