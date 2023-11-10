<template>
    <li class="nav-item dropdown list-unstyled">
        <a class="nav-link dropdown-toggle" href="#dropdown_header" role="button" data-bs-toggle="dropdown"
            aria-expanded="false">
            <i class="fa-solid fa-language fa-2xl"></i>
        </a>
        <ul class="dropdown-menu bg-dark" id="dropdown_header">

            <HeaderDropdownLink v-for="language in languages" :code="language.code" :description="language.description" />

        </ul>
    </li>
</template>
<script setup>
import HeaderDropdownLink from './HeaderDropdownLink.vue';
defineProps({
    languages: Array
})
</script>
<style>
.navbar_links ul.dropdown-menu {
    color: var(--periwinkle-purple-rgb) !important;
    text-shadow: var(--periwinkle-purple-shadow) !important;
}

.navbar_links a.dropdown-toggle:hover,
.navbar_links a.dropdown-toggle:focus,
.navbar_links a.dropdown-toggle:active {
    background-color: transparent;
    color: var(--periwinkle-purple-rgb) !important;
    text-shadow: var(--periwinkle-purple-shadow) !important;
}
</style>