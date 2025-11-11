import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  root: '.',          // bygger från frontend-mappen
  publicDir: 'public', // anger att public/ innehåller statiska filer
  plugins: [react()]
})
