// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://macpavingandsealcoating.com',
  trailingSlash: 'always', // Previene URLs duplicadas con trailing slash
  integrations: [
    sitemap({
      changefreq: 'weekly',
      priority: 0.7,
      lastmod: new Date(),
      entryLimit: 45000,
      filter: (page) => {
        // Excluir archivos que no deben estar en el sitemap
        const excludePatterns = [
          '/admin/', '/private/', '.py', '.csv', '.xlsx', '/assets/',
          '.DS_Store', 'K{', '.webp', '.png', '.jpg', '.jpeg', '.svg',
          '/node_modules/', '/.vscode/', '/.git/', '/public/'
        ];

        return !excludePatterns.some(pattern => page.includes(pattern));
      },
      // Removemos customPages para evitar duplicados
      // Astro detectará automáticamente todas las páginas .astro
    })
  ],
  server: {
    port: 4321,
    host: true
  },
  vite: {
    server: {
      watch: {
        usePolling: true
      }
    },
    resolve: {
      alias: {
        "@": new URL("./src", import.meta.url).pathname
      }
    }
  }
});
