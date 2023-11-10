<template>
    <div class="main-1" id="main-1">
        <div class="title d-flex justify-content-center align-items-center vh-100 p-5">
            <span class="text-center">Welcome to Azuko</span>
            
            <a href="#" class="slider_buttons slider_button_up_disabled"><i class="fa-solid fa-up-long fa-xl"></i></a>
            <a href="/home#main-2" class="slider_buttons slider_button_down_1"><i
                    class="fa-solid fa-down-long fa-xl"></i></a>
        </div>
    </div>
</template>
<style>
.main-1 .title span,
#projects.title span,
#products.title span {
    font-size: 10vh;
    color: var(--periwinkle-purple-rgb);
    opacity: .65;
    font-weight: bold;
    letter-spacing: .5vw;
    text-shadow: 5px 5px 50px var(--periwinkle-purple-rgb);
}

@media screen and (max-width: 1200px) {

    .main-1 .title span,
    .projects .title span {
        font-size: 7vh;
        text-shadow: 5px 5px 30px var(--periwinkle-purple-rgb);
    }
}

@media screen and (max-width: 1000px) {

    .main-1 .title span,
    .projects .title span {
        font-size: 5vh;
        text-shadow: 5px 5px 15px var(--periwinkle-purple-rgb);
    }
}
</style>