<template>
    <div class="last_release">

        <router-link :to="'/playlist/' + project + '/' + release.id" v-if="release.is_album">
            <img loading="lazy" :src="'/src/assets/images/projects/' + project + '/covers/' + release.id + '.jpg'" class="card-img-top img_release" :alt="release.title">
        </router-link>
        <router-link :to="'/playlist/' + project" v-else>
            <img loading="lazy" :src="'/src/assets/images/projects/tracks/' + release.id + '.jpg'" class="card-img-top img_release" :alt="release.title">
        </router-link>

        <div class="release_info">
            <p class="m-0 text-center align-middle release_title">{{ release.title }} |
                <span class="release_artist" v-for="(artist, index) in release.artists">
                    {{ artist }}
                    <span v-if="index != release.artists.length - 1">, </span>
                </span>
            </p>
            <p class="m-0 text-center release_date_release">
                Date release: {{ release.date_release }}
            </p>
        </div>
    </div>
</template>
<script setup>
defineProps({
    release: Object,
    project: String
})
</script>