<script setup>
defineProps({
    logo_src: {
        type: String,
        required: true
    }
})
</script>

<template>
    <header>
        <nav class="navbar navbar-expand-lg fixed-top mx-5 py-0 mt-3">
            <div class="container nav_container d-flex justify-content-between">
                <router-link to="/" class="navbar-brand">
                    <img v-bind:src="logo_src" width="120" alt="AZUKO">
                </router-link>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse d-flex justify-content-between">
                    <div class="navbar_links">
                        <router-link to="/home">HOME</router-link>
                        <router-link class="mx-2" to="/playlist">PLAYLIST</router-link>
                        <router-link to="/projects">PROJECTS</router-link>
                        <router-link class="mx-2" to="/products">PRODUCTS</router-link>
                        <router-link to="/extras">EXTRAS</router-link>
                    </div>
                    <div>
                        <a href="#shop_modal" class="shopping_cart" data-bs-toggle="modal"><i
                                class="fa-solid fa-cart-shopping"></i></a>
                        <a href="https://github.com/AzukoTazumaki" class="github"><i
                                class="fa-brands fa-github fa-lg"></i></a>
                    </div>
                </div>

            </div>
        </nav>
    </header>
</template>