<template>
    <div>
        <p class="footer_title">{{ menu.title }}</p>
        <hr>
        <ul>
            <template v-for="link in menu.links">
                <router-link :to="'/' + link.url" class="footer_link">
                    <li class="text-capitalize" v-if="menu.title != 'ALBUMS'">{{ link.text }}</li>
                    <li v-else>{{ link.text }}</li>
                </router-link>
            </template>
        </ul>
    </div>
</template>
<script setup>
defineProps({
    menu: Object
})
</script>