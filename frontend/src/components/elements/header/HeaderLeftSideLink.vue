<template>
    <li class="nav-item mx-xxl-1 mx-lg-1 mx-md-0 mb-xxl-0 mb-lg-0 mb-md-2">
        <router-link class="text-center text-capitalize" :to="'/' + link">{{ link }}</router-link>
    </li>
</template>
<script setup>
defineProps({
    link: String
})
</script>