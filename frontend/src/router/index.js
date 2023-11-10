import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/home/Home.vue'
import Playlist from '../components/playlist/Playlist.vue'
import Projects from '../components/projects/Projects.vue'
import Products from '../components/products/Products.vue'

const router = createRouter({
    scrollBehavior(to, from, savedPosition) {
        return new Promise((resolve, reject) => {
            if (to.hash) {
                setTimeout(() => {
                    resolve({ behavior: 'smooth', el: to.hash })
                }, 50)
            } else {
                setTimeout(() => {
                    resolve({ top: 0 })
                }, 1100)
            }
        })
    },
    history: createWebHistory(),
    routes: [
        {
            path: '/home',
            component: Home,
            meta: {
                enterClass: 'animate__animated animate__fadeIn',
                leaveClass: 'animate__animated animate__fadeOut'
            }
        },
        {
            path: '/playlist',
            component: Playlist,
            meta: {
                enterClass: 'animate__animated animate__fadeIn',
                leaveClass: 'animate__animated animate__fadeOut'
            }
        },
        {
            path: '/projects',
            component: Projects,
            meta: {
                enterClass: 'animate__animated animate__fadeIn',
                leaveClass: 'animate__animated animate__fadeOut'
            }
        },
        {
            path: '/products',
            component: Products,
            meta: {
                enterClass: 'animate__animated animate__fadeIn',
                leaveClass: 'animate__animated animate__fadeOut'
            }
        }
    ],
})

export default router