// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://macpavingandsealcoating.com',
  integrations: [
    sitemap({
      changefreq: 'weekly',
      priority: 0.7,
      lastmod: new Date(),
      entryLimit: 45000,
      filter: (page) => {
        // Excluir archivos que no deben estar en el sitemap
        return !page.includes('/admin/') && 
               !page.includes('/private/') &&
               !page.includes('.py') &&
               !page.includes('.csv') &&
               !page.includes('.xlsx') &&
               !page.includes('/assets/') &&
               !page.includes('.DS_Store') &&
               !page.includes('K{') && // Excluir URLs mal formadas
               !page.includes('.webp') &&
               !page.includes('.png') &&
               !page.includes('.jpg') &&
               !page.includes('.jpeg') &&
               !page.includes('.svg') &&
               !page.includes('/node_modules/') &&
               !page.includes('/.vscode/') &&
               !page.includes('/.git/');
      },
      customPages: [
        // Páginas principales
        'https://macpavingandsealcoating.com/',
        'https://macpavingandsealcoating.com/services',
        'https://macpavingandsealcoating.com/contact',
        
        // Páginas de categoría de servicios
        'https://macpavingandsealcoating.com/services/asphalt-paving',
        'https://macpavingandsealcoating.com/services/concrete',
        'https://macpavingandsealcoating.com/services/pavers',
        'https://macpavingandsealcoating.com/services/sealer',
        'https://macpavingandsealcoating.com/services/landscaping',
        
        // Servicios de Asphalt Paving
        'https://macpavingandsealcoating.com/services/asphalt-paving/installation',
        'https://macpavingandsealcoating.com/services/asphalt-paving/resurfacing',
        'https://macpavingandsealcoating.com/services/asphalt-paving/replacement',
        'https://macpavingandsealcoating.com/services/asphalt-paving/extension',
        
        // Servicios de Concrete
        'https://macpavingandsealcoating.com/services/concrete/walkways',
        'https://macpavingandsealcoating.com/services/concrete/sidewalks',
        'https://macpavingandsealcoating.com/services/concrete/curbs',
        'https://macpavingandsealcoating.com/services/concrete/aprons',
        
        // Servicios de Pavers
        'https://macpavingandsealcoating.com/services/pavers/installation',
        'https://macpavingandsealcoating.com/services/pavers/maintenance',
        'https://macpavingandsealcoating.com/services/pavers/belgium-blocks',
        
        // Servicios de Sealer
        'https://macpavingandsealcoating.com/services/sealer/sealcoating',
        'https://macpavingandsealcoating.com/services/sealer/crack-filling',
        'https://macpavingandsealcoating.com/services/sealer/line-striping',
        
        // Servicios de Landscaping
        'https://macpavingandsealcoating.com/services/landscaping/sod-installation',
        'https://macpavingandsealcoating.com/services/landscaping/drainage',
        'https://macpavingandsealcoating.com/services/landscaping/hauling',
        'https://macpavingandsealcoating.com/services/landscaping/power-wash',
        'https://macpavingandsealcoating.com/services/landscaping/top-soil',
      ]
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
    }
  }
});
