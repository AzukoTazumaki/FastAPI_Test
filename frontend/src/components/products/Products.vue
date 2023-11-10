<template>
    <div class="products">
        <div class="title d-flex justify-content-center align-items-center vh-100" id="products">
            <span>Products</span>

            <a href="#" class="slider_buttons slider_button_up_disabled"><i class="fa-solid fa-up-long fa-xl"></i></a>
            <a href="/products#product_1" class="slider_buttons slider_button_down_1"><i
                    class="fa-solid fa-down-long fa-xl"></i></a>

        </div>
        <div class="container">
            <Suspense timeout="0">
                <template v-for="(product, index) in products">
                <div class="row d-flex align-items-center vh-100" :id="'product_' + product.id">
                    <div class="row justify-content-center gap-5">
                        <div class="col-12">
                                <ProductCard :product="product" />
                        </div>
                        <div class="col-2 d-flex justify-content-center">
                            <router-link v-if="index == 0" to="#products" class="slider_products"><i
                                    class="fa-solid fa-up-long fa-xl"></i></router-link>
                            <router-link v-else :to="'#product_' + (product.id - 1)" class="slider_products"><i
                                    class="fa-solid fa-up-long fa-xl"></i></router-link>
                        </div>
                        <div class="col-2 d-flex justify-content-center">
                            <router-link v-if="index == products.length - 1" to="#footer" class="slider_products"><i
                                    class="fa-solid fa-down-long fa-xl"></i></router-link>
                            <router-link v-else :to="'#product_' + (index + 2)" class="slider_products"><i
                                    class="fa-solid fa-down-long fa-xl"></i></router-link>
                        </div>
                    </div>
                </div>
            </template>
            </Suspense>
        </div>
    </div>
</template>
<script setup>
import { defineAsyncComponent } from 'vue'
import { useFetch } from '@vueuse/core'
import Spinner from '../elements/Spinner.vue'
const ProductCard = defineAsyncComponent(() => import('./ProductCard.vue'))
async function fetchAPI(url) {
    const { data } = await useFetch(url).json()
    const API = data.value
    return API
}
const products = await fetchAPI('http://localhost:8000/read_products')
</script>
<style>
.product_img {
    width: 100%;
    box-shadow: 1px 1px 20px var(--light-gray-azuko-rgb);
}

.product_card_info {
    min-height: 25vh;
    background-color: var(--dark-gray-rgb);
    padding: 20px;
}

.product_card_info p {
    color: var(--periwinkle-purple-rgb);
    text-shadow: var(--periwinkle-purple-shadow);
}

.product_card_info ul {
    list-style-type: ' — ';
    font-size: 1.2em;
    color: var(--light-gray-azuko-rgb);
    font-weight: 300;
}

.product_card_info p {
    text-align: center;
    font-size: 1.4em;
}

.available_soon_text {
    font-size: 10vh;
    font-weight: 200;
    color: var(--periwinkle-purple-rgb);
    text-shadow: 5px 5px 30px var(--periwinkle-purple-rgb);
}

.product_price {
    color: var(--tiger-orange-rgb);
    text-shadow: 1px 1px 3px var(--tiger-orange-rgb);
    font-weight: 600;
}

.product_card_info .old_price {
    color: var(--dark-gray-azuko-rgb);
    text-shadow: var(--dark-gray-azuko-shadow);
    font-size: .8em;
}
</style>