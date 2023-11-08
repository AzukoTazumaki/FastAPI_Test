<template>
    <div class="main-2">
        <span class="position-absolute" style="margin-top: 20vh;" id="main-2"></span>
        <div class="container-fluid">
            <div class="row d-flex align-items-center main-2-row">
                <div class="row d-flex justify-content-center">
                    <div class="col-12 d-flex justify-content-center">
                        <p class="last_releases_title text-center m-0">LAST RELEASES</p>
                    </div>
                    
                    <div class="col-xxl-3 col-xl-4 col-md-5 col-sm-9 p-5" v-for="release in last_releases">
                        <LastRelease 
                            v-if="release.is_album"
                            :release="release"
                            project="albums"
                        />
                        <LastRelease 
                            v-if="release.is_single"
                            :release="release"
                            project="singles"
                        />
                        <LastRelease 
                            v-if="release.is_featuring"
                            :release="release"
                            project="featurings"
                        />
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>
<script setup>
import LastRelease from './LastRelease.vue'
defineProps({
    last_releases: Array,
    products: Array
})
</script>
<style>
.last_release {
    filter: grayscale(1) blur(4px);
    transition: .3s;
}

.last_release:hover {
    filter: none;
    transform: scale(1.05);
}

.last_release:hover .release_info {
    opacity: 1;
    transition: opacity .5s;
}

.last_releases_title,
.products_title {
    font-size: 3vh;
    color: var(--periwinkle-purple-rgb);
    font-weight: bold;
    text-shadow: 1px 1px 5px var(--periwinkle-purple-rgb);
}

.release_date_release,
.release_title {
    color: var(--whitesmoke-rgb);
    text-shadow: var(--whitesmoke-shadow);
}

.release_date_release {
    font-size: .9em;
}

.release_title {
    font-size: 1.1em;
}

.release_artist {
    font-size: .9em;
    color: var(--periwinkle-purple-rgb);
    text-shadow: var(--black-shadow);
}

.release_info {
    padding: 5px 15px;
    transition: .3s;
    opacity: 0;
}
</style>