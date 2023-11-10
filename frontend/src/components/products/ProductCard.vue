<template>
    <div class="row justify-content-lg-center justify-content-md-center justify-content-sm-center align-items-center gap-xxl-0 gap-xl-0 gap-lg-4 gap-md-4 gap-sm-4">
        <div class="col-xxl-5 col-xl-5 col-lg-7 col-md-8 col-sm-9">
            <img loading="lazy" class="rounded-3 product_img" :src="'/src/assets/images/products/' + product.id + '.jpg'"
                alt="">
        </div>
        <div class="offset-xxl-1 offset-xl-0 col-xxl-6 col-xl-6 col-lg-7 col-md-8 col-sm-9">
            <div class="d-flex justify-content-center align-items-center products_title_div">
                <p class="m-0 text-center products_title">{{ product.name }}</p>
            </div>
            <div class="product_card_info d-flex justify-content-center align-items-center">
                <div>
                    <p class="m-0 mb-3" v-if="product.old_price">
                        Price:&nbsp;
                        <span class="product_price">{{ product.price }}<i class="fa-solid fa-ruble-sign"></i></span>&nbsp;
                        <span class="text-decoration-line-through old_price">{{ product.old_price }}<i
                                class="fa-solid fa-ruble-sign"></i></span>
                    </p>
                    <p class="m-0 mb-3" v-else>
                        Price:&nbsp;<span class="product_price">{{ product.price }}<i
                                class="fa-solid fa-ruble-sign"></i></span>
                    </p>
                    <ul class="m-0">
                        <li v-for="description in product.description">{{ description }}</li>
                    </ul>

                </div>
            </div>
            <div class="d-flex justify-content-center align-items-center other_products_div">
                <link-router :to="'/products/' + product.id">
                    <button class="other_products_button">EXPLORE</button>
                </link-router>
            </div>
        </div>
    </div>
</template>
<script setup>
defineProps({
    product: Object
})
</script>