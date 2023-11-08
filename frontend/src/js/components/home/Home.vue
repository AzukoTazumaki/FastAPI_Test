<script setup>
import Main_1 from './Main_1.vue'
import Main_2 from './Main_2.vue'
import Main_3 from './Main_3.vue'
import { useFetch } from '@vueuse/core'
const url = 'http://localhost:8000/home'
const { isFetching, error, data } = useFetch(url, {
    refetch: true
}).json()
</script>
<template>
    <Main_1 />
    <Main_2 :last_releases="data.last_releases" />
    <Main_3 :products="data.products" />
</template>