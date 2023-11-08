import '../assets/bundle.min.css'
import '../../node_modules/bootstrap/dist/js/bootstrap.bundle'

import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import Home from './components/home/Home.vue'

const routes = [
    { path: '/home', component: Home }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

const app = createApp(App)
app.use(router)
app.mount('#root')