import { fileURLToPath, URL } from 'node:url'
import vuePlugin from '@vitejs/plugin-vue'
import vueJsxPlugin from '@vitejs/plugin-vue-jsx'
import { defineConfig } from 'vite'

export default defineConfig({
    server: {
        open: './index.html',
        host: true,
        port: 3000
    },
    preview: {
        port: 8080
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