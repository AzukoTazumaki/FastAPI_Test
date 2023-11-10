<template>
        <a href="/support" class="text-decoration-none">
            <button class="order_service_button">SUPPORT</button>
        </a>
        <p class="mb-0 mt-2 support_description">SUPPORT&nbsp;&nbsp;THE&nbsp;&nbsp;AUTHOR</p>
        <div class="d-flex justify-content-between align-items-center column-gap-2 mt-1 contacts">
            <a :href="'mailto:' + menu.mail + '?subject=' + menu.mail_subject">{{ menu.mail }}</a>
            <template v-for="link in menu.links">
            <a :href="link.url"><i :class="'fa-brands ' + link.icon + ' fa-xl'"></i></a>
            </template>
        </div>
</template>
<script setup>
defineProps({
    menu: Object
})
</script>