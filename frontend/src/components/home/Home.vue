<script setup>
import Main_1 from './Main_1.vue'
import Main_2 from './Main_2.vue'
import Main_3 from './Main_3.vue'
import { useFetch } from '@vueuse/core'
async function fetchAPI(url) {
    const { data } = await useFetch(url).json()
    const API = data.value
    return API
}
const last_releases = await fetchAPI('http://localhost:8000/read_last_releases')
const all_products = await fetchAPI('http://localhost:8000/read_products')
const products = [all_products[1], all_products[3], all_products[4]]
</script>
<template>
    <div>
        <Main_1 />
        <Main_2 :last_releases="last_releases" />
        <Main_3 :products="products" />
    </div>
</template>