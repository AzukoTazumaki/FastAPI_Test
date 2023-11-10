<template>
    <ul class="navbar-nav d-xxl-flex align-items-xxl-center">
        <HeaderLeftSideLink v-for="link in links" :link="link"/>
    </ul>
</template>
<script setup>
import HeaderLeftSideLink from './HeaderLeftSideLink.vue'
defineProps({
    links: Array
})
</script>
<style></style>