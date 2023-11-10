<template>
    <div :class="'row justify-content-center align-items-center ' + full_screen" :style="'padding-top: ' + style" :id="projects_info.cover + '_cards'">
        <div class="col-12">
            <div class="row justify-content-center gap-4">
                <div class="col-12 d-flex justify-content-center">
                    <img :src="'/src/assets/images/logos/' + projects_info.cover + '_logo.png'" :alt="projects_info.alt"
                        width="300">
                </div>

                <template v-for="(project, index) in projects">
                    <div class="col-xxl-4 col-xl-7 col-lg-8 col-md-9 col-sm-10 p-0" v-if="index < 2">
                        <ProjectsTracksCard :project="project" />
                    </div>

                    <div :class="'col-xxl-4 col-xl-7 col-lg-8 col-md-9 col-sm-10 p-0 ' + disabled_card" v-else>
                        <ProjectsTracksCard :project="project" />
                    </div>
                </template>

                <div class="col-12">
                    <div class="row justify-content-center column-gap-0 align-items-center flex-xxl-row flex-xl-row
                    flex-lg-column flex-md-column flex-sm-column gap-lg-3 gap-md-3 gap-sm-3">
                        <div class="col-xxl-1 col-xl-2 col-lg-4 col-md-7 col-sm-7 d-flex justify-content-end">
                            <router-link :to="'/projects' + projects_info.up_link" class="slider_products"><i
                                    class="fa-solid fa-up-long fa-xl"></i></router-link>
                        </div>
                        <div class="col-2 col-xl-2 col-lg-4 col-md-7 col-sm-7 d-flex justify-content-center">
                            <router-link v-on:click="show(more_less)" class="slider_products show_more_button fw-bold d-flex justify-content-center align-items-center"
                                :id="'show_more_' + projects_info.cover + '_button'" :to="'/projects' + projects_info.show_more_link">
                                <span v-if="loading" class="loader_tracks mx-2"></span> 
                                <span v-if="loading">LOADING</span>
                                <span v-else>{{ more_less }}</span>
                            </router-link>
                        </div>
                        <div class="col-xxl-1 col-xl-2 col-lg-4 col-md-7 col-sm-7 d-flex justify-content-start">
                            <router-link :to="'/projects' + projects_info.down_link" class="slider_products"><i
                                    class="fa-solid fa-down-long fa-xl"></i></router-link>
                        </div>
                    </div>
                </div>

            </div>
        </div>

    </div>
</template>
<script>
import { defineAsyncComponent } from 'vue'
export default {
    props: {
        projects: Array,
        projects_info: Object
    },
    data() {
        return {
            full_screen: 'vh-100',
            disabled_card: 'disabled_card',
            more_less: 'SHOW MORE',
            style: '',
            loading: false
        }
    },
    methods: {
        show(more_less) {
            this.loading = !false
            setTimeout(() => {
                if (more_less == 'SHOW MORE') {
                this.full_screen = 'mt-5'
                this.disabled_card = ''
                this.more_less = 'SHOW LESS'
                this.style = '25vh'
                this.loading = !true
            } else {
                this.full_screen = 'vh-100',
                this.disabled_card = 'disabled_card',
                this.more_less = 'SHOW MORE'
                this.style = ''
                this.loading = !true
            } 
            }, 1000);
        }
    },
    components: {
        ProjectsTracksCard: defineAsyncComponent(() => import('./ProjectsTracksCard.vue')),
        Spinner: defineAsyncComponent(() => import('../elements/Spinner.vue'))
    }
}
</script>
<style>
.loader_tracks {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: inline-block;
  position: relative;
  background: linear-gradient(0deg, transparent 0%, var(--dark-gray-rgb) 100%);
  box-sizing: border-box;
  animation: rotation .4s linear infinite;
}
.loader_tracks::after {
  content: '';  
  box-sizing: border-box;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--periwinkle-purple-rgb);
}
@keyframes rotation {
  0% { transform: rotate(0deg) }
  100% { transform: rotate(360deg)}
} 

.card_single,
.card_featuring {
    transition: .3s;
}

.card_single:hover,
.card_featuring:hover {
    transform: scale(1.05);
    box-shadow: 3px 3px 10px var(--black-rgb);
}

.show_more_button {
    width: 100%;
    padding-left: 0 !important;
    padding-right: 0 !important;
    text-align: center;
    background-color: var(--periwinkle-purple-rgb);
    border-radius: 10px !important;
    cursor: pointer;
}

.show_more_button:hover {
    background-color: var(--periwinkle-purple-rgb-deep);
    box-shadow: 3px 3px 10px var(--black-rgb);
    transform: scale(1.05);
}

.show_more_button:hover .loader_tracks::after {
    background: var(--periwinkle-purple-rgb-deep);
}

.show_more_button:focus {
    transform: scale(.95);
}

.single_info_span,
.featuring_info_span {
    font-style: normal;
    background-color: var(--periwinkle-purple-rgb);
    padding: 2px 10px;
    border-radius: 3px;
    color: var(--white-rgb);
    text-shadow: var(--black-shadow);
    font-weight: 400;
    margin-right: 5px;
}

.disabled_card {
    display: none;
}

.project_left_part {
    width: 40%;
    transition: .3s;
}

.project_right_part {
    transition: 1s;
    width: 60%;
    background-color: var(--dark-gray-rgb);
    font-size: .9em;
}

.project_right_part p {
    font-size: 1em;
    color: var(--white-rgb);
    text-shadow: var(--black-shadow);
}

.project_left_part,
.project_right_part {
    filter: brightness(.9);
}

.project_left_part img {
    width: 100%;
}

.card_single:hover>.project_left_part,
.card_single:hover>.project_right_part,
.card_featuring:hover>.project_left_part,
.card_featuring:hover>.project_right_part {
    filter: brightness(1);
}
</style>