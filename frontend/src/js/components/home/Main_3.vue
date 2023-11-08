<template>
    <div class="main-3" id="main-3">

        <div class="container">
            <div class="row d-flex align-items-center">

                <div class="col-12">
                    <div class="d-flex justify-content-center align-items-center products_title_div">
                        <p class="m-0 text-center products_title">PRODUCTS</p>
                    </div>
                    <div class="products_main_div">
                        <div class="row d-flex justify-content-around products_div">


                            <div class="col-xxl-3 col-xl-4 col-md-5 col-sm-9 p-0 py-3" v-for="product in products">
                                <ProductCard :product="product" />
                            </div>


                        </div>
                    </div>
                    <div class="d-flex justify-content-center align-items-center other_products_div">
                        <router-link to="/products"><button class="other_products_button">OTHER
                                PRODUCTS</button></router-link>
                    </div>
                </div>

            </div>
        </div>

    </div>
</template>
<script setup>
import ProductCard from './ProductCard.vue';
defineProps({
    products: Array
})
</script>
<style>
.who_is_azuko {
    background-color: var(--dark-gray-rgb);
    padding: 30px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    color: var(--periwinkle-purple-rgb);
}

.who_is_azuko .who_is_azuko_img {
    filter: grayscale(1);
}

.who_is_azuko_div {
    background-color: var(--dark-gray-azuko-rgb);
    color: var(--periwinkle-purple-rgb);
    padding: 10px 15px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}

.who_is_azuko_title {
    font-weight: bold;
    font-size: 1.5em;
    text-shadow: 1px 1px 5px var(--periwinkle-purple-rgb);
}

.who_is_azuko_description {
    font-size: 1.1em;
    text-shadow: var(--black-shadow);
    font-weight: 200;
    text-align: start;
    background-color: var(--dark-gray-azuko-rgb);
    padding: 15px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
}

.products_div .col-6:nth-of-type(1) {
    padding-left: 0 !important;
    padding-right: 15px;
}

.products_div .col-6:nth-of-type(2) {
    padding-left: 15px;
    padding-right: 0 !important;
}

.product_info {
    background-color: var(--dark-gray-azuko-rgb);
    padding: 10px 20px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    color: var(--periwinkle-purple-rgb);
}

.img_product {
    border-top-left-radius: 10px !important;
    border-top-right-radius: 10px !important;
}

.products_title_div {
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    background-color: var(--dark-gray-azuko-rgb);
    padding: 10px 30px;
    color: var(--periwinkle-purple-rgb);
}

.products_main_div {
    padding: 30px 43px;
    background-color: var(--dark-gray-rgb);
}

.product_name {
    font-weight: bold;
    font-size: 1.3em;
    text-shadow: 1px 1px 5px var(--periwinkle-purple-rgb);
}

.other_products_div {
    background-color: var(--dark-gray-azuko-rgb);
    padding: 15px 30px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
}

.other_products_button,
.order_service_button {
    background-color: var(--periwinkle-purple-rgb);
    color: var(--dark-gray-azuko-rgb);
    padding: 10px 40px;
    border: none;
    font-weight: 800;
    font-size: 1em;
    box-shadow: 2px 2px 2px rgb(0, 0, 0);
    border-radius: 10px;
    transition: .3s;
}

.order_service_button {
    padding: 10px 40px;
}

.other_products_button:hover,
.order_service_button:hover {
    background-color: var(--periwinkle-purple-rgb-deep);
}

.old_price {
    color: var(--dark-gray-rgb);
    text-shadow: var(--dark-gray-shadow);
    font-size: 1em;
}

.img_release {
    border-radius: 20px !important;
}
</style>