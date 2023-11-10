<template>
    <div class="d-flex justify-content-between card_featuring rounded-3">
        <div class="project_left_part">
            <img :src="'/src/assets/images/projects/tracks/' + project.id + '.jpg'" class="rounded-start-3"
                :alt="project.title">
        </div>
        <div class="d-flex flex-column justify-content-center align-items-start p-4 project_right_part rounded-end-3">
            <div>
                <p class="fw-bold m-0">
                    <span class="single_info_span">Title:</span> {{ project.title }}
                </p>
                <p class="fw-bold m-0 my-2">
                    <span class="single_info_span">Artists:</span>
                    <template v-for="(artist, index) in project.artists">
                        {{ artist }}
                        <span v-if="index != project.artists.length - 1">, </span>
                    </template>
                </p>
                <p class="fw-bold m-0 my-2">
                    <span class="single_info_span">Date Release:</span> {{ project.date_release }}
                </p>
                <p class="fw-bold m-0">
                    <span class="single_info_span">Duration:</span> {{ project.duration }}
                </p>
            </div>
        </div>
    </div>
</template>
<script setup>
defineProps({
    project: Object
})
</script>
<style></style>