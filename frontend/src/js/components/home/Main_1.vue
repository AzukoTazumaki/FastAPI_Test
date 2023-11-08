<template>
    <div class="main-1" id="main-1">
        <div class="title d-flex justify-content-center align-items-center p-5">
            <span class="text-center">WELCOME TO AZUKO</span>
        </div>
    </div>
</template>
<style>
.main-1 .title span,
.projects .title span {
    font-size: 10vh;
    color: var(--periwinkle-purple-rgb);
    opacity: .85;
    font-weight: bold;
    letter-spacing: .5vw;
    text-shadow: 1px 1px 5px var(--periwinkle-purple-rgb);
}

@media screen and (max-width: 1200px) {

    .main-1 .title span,
    .projects .title span {
        font-size: 7vh;
    }
}

@media screen and (max-width: 1000px) {

    .main-1 .title span,
    .projects .title span {
        font-size: 5vh;
    }
}
</style>