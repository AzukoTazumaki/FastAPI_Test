import { fileURLToPath, URL } from 'node:url'
import vuePlugin from '@vitejs/plugin-vue'
import vueJsxPlugin from '@vitejs/plugin-vue-jsx'
import { defineConfig } from 'vite'

export default defineConfig({
    server: {
        open: './templates/index.html'
    },
    plugins: [
        vuePlugin(),
        vueJsxPlugin(),
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    }
})