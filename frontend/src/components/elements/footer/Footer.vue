<template>
    <footer id="footer">
        <div class="container-fluid">
            <Suspense timeout="0">
                <div class="row d-flex justify-content-center align-items-center">

                    <div class="col-xxl-2 col-xl-8 col-lg-10 col-md-10 col-sm-10 d-flex justify-content-center">
                        <img class="footer_left_img" src="/src/assets/images/logos/footer_logo_azuko.png" alt="AZUKO">
                    </div>

                    <div class="col-xxl-8 col-xl-8 col-lg-9 col-md-10 col-sm-12">
                        <div class="row d-flex justify-content-center">
                            <template v-for="menu in menus">
                                <div class="col-xxl-4 col-xl-6 col-lg-8 col-md-10 col-sm-12 footer_col text-uppercase">
                                    <FooterMenu :menu="menu" />
                                </div>
                            </template>
                        </div>
                    </div>

                    <div class="col-xxl-2 col-xl-8 col-lg-10 col-md-10 col-sm-10 d-flex flex-column align-items-center">
                        <FooterRightMenu :menu="right_menu" />
                    </div>
                </div>
                <template #fallback>
                    <Spinner />
                </template>
            </Suspense>
        </div>
    </footer>
</template>
<script setup>
import { defineAsyncComponent } from 'vue'
import Spinner from '../Spinner.vue'
const FooterMenu = defineAsyncComponent(() => import('./FooterMenu.vue'))
const FooterRightMenu = defineAsyncComponent(() => import('./FooterRightMenu.vue'))
const menus = [
    {
        'title': 'MENU', 'links': [
            { 'url': 'home', 'text': 'home' },
            { 'url': 'playlist', 'text': 'playlist' },
            { 'url': 'projects', 'text': 'projects' },
            { 'url': 'products', 'text': 'products' },
            { 'url': 'extras', 'text': 'extras' },
        ]
    },
    {
        'title': 'PLAYLIST', 'links': [
            { 'url': 'playlist#albums', 'text': 'albums' },
            { 'url': 'playlist#singles', 'text': 'singles' },
            { 'url': 'playlist#featurings', 'text': 'featurings' }
        ]
    },
    {
        'title': 'PROJECTS', 'links': [
            { 'url': 'projects/#albums_carousel_div', 'text': 'albums' },
            { 'url': 'projects/#singles_cards', 'text': 'singles' },
            { 'url': 'projects/#featurings_cards', 'text': 'featurings' }
        ]
    },
    {
        'title': 'PRODUCTS', 'links': [
            { 'url': 'products/1', 'text': 'Beats' },
            { 'url': 'products/2', 'text': 'Mixing' },
            { 'url': 'products/3', 'text': 'Mastering' },
            { 'url': 'products/4', 'text': 'Mixing & Mastering' },
            { 'url': 'products/5', 'text': 'Ghostwriting' }
        ]
    },
    {
        'title': 'PRODUCTS FAQ', 'links': [
            { 'url': 'products/#product_1', 'text': 'About Beats' },
            { 'url': 'products/#product_2', 'text': 'About Mixing' },
            { 'url': 'products/#product_3', 'text': 'About Mastering' },
            { 'url': 'products/#product_4', 'text': 'About Mixing & Mastering' },
            { 'url': 'products/#product_5', 'text': 'About Ghostwriting' }
        ]
    },
    {
        'title': 'ALBUMS', 'links': [
            { 'url': 'playlist/albums/1', 'text': 'FUNNY but NOBODY' },
            { 'url': 'playlist/albums/2', 'text': 'with love from Azuko' },
            { 'url': 'playlist/albums/3', 'text': 'ВРЕМЯ ПЕРЕМЕН' },
            { 'url': 'playlist/albums/4', 'text': 'Highway Of Love (Deluxe)' },
            { 'url': 'playlist/albums/5', 'text': 'Highway Of Love' },
            { 'url': 'playlist/albums/6', 'text': 'Mileran Vibes' },
            { 'url': 'playlist/albums/7', 'text': 'Life Is Full Of Lies 2' }
        ]
    },
    {
        'title': 'EXTRAS', 'links': [
            { 'url': 'extras', 'text': 'Genres & Keys' }
        ]
    },
]
const right_menu = {
    'mail': 'tazumaki@mail.ru',
    'mail_subject': 'Сайт Azuko',
    'links': [
        { 'url': 'https://vk.com/azuko_1', 'icon': 'fa-vk' },
        { 'url': 'https://t.me/azukio_1', 'icon': 'fa-telegram' },
        { 'url': 'https://www.youtube.com/channel/UC70lHhSyH9O9JM1RL7bCn_Q', 'icon': 'fa-youtube' }
    ]
}
</script>
<style>
footer {
    background-color: var(--darker-gray-azuko-rgb);
    padding: 30px;
}

footer hr {
    color: var(--light-gray-azuko-rgb);
}

.footer_title {
    color: var(--periwinkle-purple-rgb);
    text-shadow: 1px 1px 5px var(--periwinkle-purple-rgb);
    font-weight: bold;
    font-size: 1.3em;
    text-align: center;
}

.footer_link {
    text-decoration: none;
    text-transform: none;
    color: var(--light-gray-azuko-rgb);
    transition: .3s;
}

.footer_link:hover {
    color: rgb(110, 110, 110);
    transform: scale(1.05);
    text-shadow: 1px 1px 2px var(--light-gray-azuko-rgb);
}

footer .footer_col ul {
    list-style-type: none;
    text-align: center;
    padding: 0;
}

.support_description {
    color: var(--light-gray-azuko-rgb);
    font-weight: 700;
    font-size: 1.3em;
    text-align: center;
    text-shadow: var(--black-shadow);
}

.contacts a {
    text-decoration: none;
    color: var(--periwinkle-purple-rgb);
    text-shadow: var(--black-shadow);
    transition: .3s;
}

.contacts a:hover {
    color: var(--periwinkle-purple-rgb-deep);
}

.all_rights {
    color: var(--periwinkle-purple-rgb);
    text-shadow: var(--periwinkle-purple-shadow);
}

#footer .footer_left_img {
    width: 100%;
}

@media screen and (max-width: 1000px) {
    #footer .footer_left_img {
        width: 50%;
    }
}

@media screen and (max-width: 1300px) {
    #footer .footer_left_img {
        width: 80%;
    }
}

@media screen and (max-width: 1150px) {
    #footer .footer_left_img {
        width: 65%;
    }
}
</style>