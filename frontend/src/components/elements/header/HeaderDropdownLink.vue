<template>
    <li class="dropdown-item bg-dark">
        <router-link class="text-center w-100" :to="'/' + code + '/home'">{{ code }} – {{ description }}</router-link>
    </li>
</template>
<script setup>
defineProps({
    code: String,
    description: String
})
</script>