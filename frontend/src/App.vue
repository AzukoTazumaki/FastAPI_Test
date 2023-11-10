<template>
  <div class="content">

    <router-view v-slot="{ Component, route }">
      <Header logo_src='/src/assets/logo_azuko.svg' :links="['home', 'playlist', 'projects', 'products', 'extras']" />
      <transition :enter-active-class="route.meta.enterClass" :leave-active-class="route.meta.leaveClass" mode="out-in">
        <Suspense timeout="0">


          <component :is='Component' />

          <template #fallback>
            <div class="d-flex justify-content-center align-items-center vh-100">
              <Spinner />
            </div>
          </template>
        </Suspense>
      </transition>
      <Footer />
    </router-view>
  </div>
</template>
<script setup>
import Header from './components/elements/header/Header.vue'
import Footer from './components/elements/footer/Footer.vue';
import Spinner from './components/elements/Spinner.vue'
</script>
<style>
:root {
  --product-card-rgb: rgb(149, 149, 149);
  --animate-duration: .8s;
}

@font-face {
  font-family: 'Exo';
  src: url(./assets/fonts/Tektur-VariableFont.ttf)
}

::-webkit-scrollbar {
  width: 0;
}

html {
  scroll-behavior: smooth;
  transition: scroll-behavior 1s all;
}

* {
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  font-family: 'Exo';
}

@-moz-document url-prefix() {

  /* Disable scrollbar Firefox */
  html {
    scrollbar-width: none;
  }
}

/* Disable scrollbar Chrome */
::-webkit-scrollbar {
  width: 0;
}

body {
  padding: 0;
  margin: 0;
}

.welcome {
  color: var(--periwinkle-purple-rgb);
  text-shadow: var(--periwinkle-purple-shadow);
}

.content {
  width: 100%;
  min-width: 500px;
  margin: 0 auto;
  position: relative;
}
</style>