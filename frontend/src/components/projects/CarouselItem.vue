<template>
    <div :class="'carousel-item ' + active">
        <div class="carousel_image bg_carousel py-5">
            <div class="d-flex justify-content-between align-items-center">
                <div class="carousel_left_part">
                    <div class="py-3 d-flex flex-column justify-content-between align-items-start h-100">
                        <span class="m-0 w-100">{{ album.title }}</span>
                        <p class="m-0 carousel_description">{{ album.description }}</p>
                        <a :href="'/playlist/albums/' + album.id">
                            <button class="project_slider_button albums_slider_button mt-3">
                                LISTEN
                            </button>
                        </a>
                    </div>
                </div>
                <div class="d-flex justify-content-end align-items-center carousel_right_part">
                    <img loading="lazy"
                        :src="'src/assets/images/projects/albums/covers/' + album.id + '.jpg'"
                        :alt="album.title" class="cover_carousel">
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
defineProps({
    album: Object,
    active: String
})
</script>
<style>
.bg_carousel {
    background: linear-gradient(121deg, rgba(29,29,29,1) 0%, rgba(54,52,52,1) 49%, rgb(83, 83, 147) 77%);
}

.carousel_description {
    font-weight: 200;
    font-size: 1.3em !important;
    color: var(--light-gray-azuko-rgb);
    text-shadow: 
        1px 1px 5px var(--dark-gray-azuko-rgb),
        2px 2px 1px var(--dark-gray-azuko-rgb);
}

.cover_carousel {
    border-radius: 15px;
    height: 40vh;
    box-shadow: 2px 2px 10px var(--dark-gray-rgb);
}

.carousel_left_part {
    margin-left: 10vw;
    margin-right: 2vw;
}

.carousel_left_part span {
    font-weight: 900;
    font-size: 2em;
    text-align: start;
    color: var(--light-gray-azuko-rgb);
    text-shadow: 
        1px 1px 5px var(--dark-gray-azuko-rgb),
        2px 2px 1px var(--dark-gray-azuko-rgb);
}

.carousel_right_part {
    margin-right: 10vw;
}

@media screen and (max-width: 1300px) {
    .cover_carousel {
        height: 25vh;
    }
    .carousel_description {
        font-size: 1em !important;
    }
    .carousel_left_part span {
        font-size: 1.3em;
    }
    .project_slider_button {
        font-size: 1em;
    }
}
@media screen and (max-width: 1000px) {
    .cover_carousel {
        width: 0;
    }
    .carousel_description {
        font-size: .8em !important;
    }
    .carousel_left_part span {
        font-size: 1.3em;
    }
    .project_slider_button {
        font-size: 1em;
    }
}
</style>