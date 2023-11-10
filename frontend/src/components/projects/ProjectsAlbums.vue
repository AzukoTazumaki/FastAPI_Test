<template>
    <div class="row justify-content-center align-items-center vh-100" id="albums_carousel_div">
        <div class="col-10">
            <div class="row justify-content-center rounded-5">
                <div class="col-12 d-flex justify-content-center">
                    <img src="src/assets/images/logos/albums_logo.png" alt="Albums" width="300">
                </div>
                <div class="col-12 px-0 rounded-5 mt-4">
                    <div id="albums_carousel" class="carousel slide carousel-fade">
                        <div class="carousel-indicators">

                            <template v-for="(item, index) in albums.length" :key="index">
                                <button 
                                v-if="index == 0"
                            type="button" data-bs-target="#albums_carousel" 
                            :data-bs-slide-to="index"
                                class="active" aria-current="true" :aria-label="'Slide ' + index + 1">
                            </button>

                            <button v-else
                            type="button" data-bs-target="#albums_carousel" :data-bs-slide-to="index"
                                aria-current="true" :aria-label="'Slide ' + index + 1">
                            </button>
                            </template>

                        </div>
                        <div class="carousel-inner">

                            <template v-for="(album, index) in albums">
                                <CarouselItem :album="album" :active="'active'" v-if="index == 0" />
                                <CarouselItem :album="album" :active="''" v-else />
                            </template>

                        </div>
                        <button class="carousel-control-prev" type="button" data-bs-target="#albums_carousel"
                            data-bs-slide="prev">
                            <span aria-hidden="true">
                                <i class="fa-solid fa-circle-chevron-left fa-2xl"></i>
                            </span>
                            <span class="visually-hidden">Previous</span>
                        </button>
                        <button class="carousel-control-next" type="button" data-bs-target="#albums_carousel"
                            data-bs-slide="next">
                            <span aria-hidden="true">
                                <i class="fa-solid fa-circle-chevron-right fa-2xl"></i>
                            </span>
                            <span class="visually-hidden">Next</span>
                        </button>

                    </div>
                </div>
                <div class="row justify-content-center mt-5">
                    <div class="col-xxl-2 col-xl-3 col-lg-5 col-md-7 col-sm-7 mb-xxl-0 mb-xl-0 mb-lg-0 mb-md-3 mb-sm-3 d-flex justify-content-center">
                        <a href="#projects" class="slider_products"><i class="fa-solid fa-up-long fa-xl"></i></a>
                    </div>
                    <div class="col-xxl-2 col-xl-3 col-lg-5 col-md-7 col-sm-7 d-flex justify-content-center">
                        <a href="#singles_cards" class="slider_products"><i class="fa-solid fa-down-long fa-xl"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import CarouselItem from './CarouselItem.vue';
defineProps({
    albums: Array
})
</script>
<style>
.carousel_image, .carousel-inner {
    border-radius: 25px !important;
}
</style>