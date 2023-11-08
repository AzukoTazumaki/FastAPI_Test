<template>
    <Header logo_src='../src/assets/logo_azuko.svg' />
    <router-view></router-view>
</template>
<script setup>
    import Header from './components/elements/Header.vue'
</script>
<style>
:root {
  --product-card-rgb: rgb(149, 149, 149);
}

@font-face {
  font-family: 'Exo';
  src: url(../assets/fonts/Exo2-VariableFont_wght.ttf)
}

@font-face {
  font-family: 'Extras';
  src: url(../assets/fonts/AlegreyaSC-Regular.ttf);
}

::-webkit-scrollbar {
  width: 0;
}

html {
  scroll-behavior: smooth;
}

* {
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  font-family: 'Exo';
}

body {
  background-color: var(--dark-gray-azuko-rgb) !important;
  padding: 0;
  margin: 0;
}

.welcome {
  color: var(--periwinkle-purple-rgb);
  text-shadow: var(--periwinkle-purple-shadow);
}
</style>