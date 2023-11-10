import './public/bundle.min.css'
import 'bootstrap/dist/js/bootstrap.bundle'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'

const app = createApp(App)
app.use(router)
app.mount('#root')