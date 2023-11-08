<template>
    <router-link :to="'/products/#product_' + product.id">
        <img loading="lazy" :src="'/src/assets/images/products/' + product.id + '.jpg'" class="card-img-top img_product"
            :alt="product.name">
    </router-link>
    <div class="product_info">
        <p class="m-0 text-uppercase text-center d-flex align-items-center justify-content-center">
            <span class="product_name">{{ product.price }}&nbsp;<i class="fa-solid fa-ruble-sign"></i></span>
            &nbsp;&nbsp;
            <span class="text-decoration-line-through old_price" v-if="product.old_price">
                {{ product.old_price }}
                <i class="fa-solid fa-ruble-sign"></i>
            </span>
            <span class="d-none" v-else></span>
        </p>
    </div>
</template>
<script setup>
defineProps({
    product: Object
})
</script>
<style></style>