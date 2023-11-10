<script setup>
import Spinner from '../Spinner.vue'
import { defineAsyncComponent } from 'vue'
const HeaderLeftSide = defineAsyncComponent(() => import('./HeaderLeftSide.vue'))
const HeaderRightSide = defineAsyncComponent(() => import('./HeaderRightSide.vue'))
defineProps({
    logo_src: {
        type: String,
        required: true
    },
    links: Array,
})
const languages = [
    { 'code': 'en', 'description': 'english' },
    { 'code': 'ru', 'description': 'русский язык' },
    { 'code': 'zh', 'description': '汉语' },
    { 'code': 'ko', 'description': '한국어' },
    { 'code': 'fr', 'description': 'français' },
    { 'code': 'tr', 'description': 'Türkçe' }]
</script>

<template>
    <header>
        <nav class="navbar navbar-expand-lg fixed-top mx-5 py-md-0 py-sm-5 mt-3">
            <div class="container nav_container">
                <router-link to="/home" class="navbar-brand">
                    <img v-bind:src="logo_src" width="120" alt="AZUKO">
                </router-link>

                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav_links_content"
                    aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <i class="fa-solid fa-bars fa-xl"></i>
                </button>

                <div class="collapse navbar-collapse" id="nav_links_content">
                    <div class="navbar_links d-xxl-flex d-xl-flex d-lg-flex
                                        justify-content-xxl-between justify-content-xl-between justify-content-lg-between 
                                        align-items-xxl-center align-items-xl-center align-items-lg-center w-100">

                        <HeaderLeftSide :links="links" />

                        <div class="mb-xxl-0 mb-lg-0 mb-sm-3 mb-md-3 d-flex align-items-xxl-center">

                            <HeaderRightSide :languages="languages" />

                            <a href="#shop_modal" id="shopping_cart" data-bs-toggle="modal">
                                <i class="fa-solid fa-cart-shopping"></i> Azuko Shop
                            </a>

                        </div>
                    </div>
                </div>

            </div>
        </nav>
    </header>
</template>
<style>
.navbar-toggler {
    border: none !important;
    color: var(--periwinkle-purple-rgb);
    padding: 10px;
}

.navbar-toggler:focus,
.navbar-toggler:active {
    border-color: transparent !important;
}

.nav_container {
    background-color: var(--dark-gray-rgb);
    border-radius: 10px;
    box-shadow:
        3px -3px 10px rgba(30, 30, 30, .5),
        -3px 3px 10px rgba(30, 30, 30, .5);
    transition: .3s;
}

.nav_container:hover {
    transform: scale(1.05);
}

.navbar_links a,
.shopping_cart {
    text-decoration: none !important;
    color: var(--periwinkle-purple-rgb);
    text-shadow: var(--periwinkle-purple-shadow);
    border-radius: 5px;
    padding: 5px 10px;
    transition: .3s !important;
}

.navbar_links a:hover,
#shopping_cart:hover {
    background-color: var(--periwinkle-purple-rgb);
    color: var(--dark-gray-rgb);
    text-shadow: var(--dark-gray-shadow);
}

.navbar_links ul a:hover,
.navbar_links ul:hover {
    color: var(--dark-gray-rgb) !important;
    text-shadow: var(--dark-gray-shadow) !important;
}
</style>