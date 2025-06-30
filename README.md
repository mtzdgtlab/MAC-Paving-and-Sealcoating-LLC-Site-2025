# MAC Paving and Sealcoating - Official Website

![MAC Paving Logo](public/assets/logo.png)

Professional asphalt paving, sealcoating, concrete, and paver services across New Jersey. Built with Astro for optimal performance and SEO.

## 🌐 Live Website

**Production:** [https://macpavingandsealcoating.com](https://macpavingandsealcoating.com)

## 🏗️ About the Project

This is the official website for MAC Paving and Sealcoating LLC, a New Jersey-based company specializing in:

- **Asphalt Paving** - Driveways, parking lots, resurfacing
- **Sealcoating** - Protective coating and maintenance
- **Concrete Work** - Sidewalks, curbs, aprons
- **Paver Installation** - Decorative driveways and patios
- **Landscaping** - Drainage solutions and outdoor improvements

### 🎯 Key Features

- **SEO Optimized** - Comprehensive meta tags, structured data, and sitemap
- **Mobile Responsive** - Optimized for all devices
- **Fast Performance** - Built with Astro for lightning-fast loading
- **Service Area Coverage** - 60+ cities across North Jersey
- **Contact Forms** - Multiple conversion-optimized contact forms
- **Video Backgrounds** - Professional video content showcasing work quality
- **Schema Markup** - Rich snippets for better search visibility

## 🚀 Tech Stack

- **Framework:** [Astro 5.10.0](https://astro.build)
- **Language:** TypeScript
- **Styling:** Custom CSS with Bootstrap grid
- **Testing:** Vitest
- **Linting:** ESLint with Astro plugin
- **Build Tool:** Vite

## 📁 Project Structure

```text
/
├── public/                  # Static assets
│   ├── assets/
│   │   ├── css/            # Stylesheets
│   │   ├── js/             # JavaScript files
│   │   ├── imgs/           # Images organized by sections
│   │   └── fonts/          # Web fonts
│   └── robots.txt
├── src/
│   ├── assets/             # Processed assets
│   ├── components/         # Reusable Astro components
│   │   ├── About.astro
│   │   ├── Footer.astro
│   │   ├── Navbar.astro
│   │   ├── LargeForm.astro
│   │   ├── TestimonialsSlider.astro
│   │   └── ...
│   └── pages/              # Route-based pages
│       ├── index.astro     # Homepage
│       ├── contact.astro   # Contact page
│       ├── services.astro  # Services overview
│       └── services/       # Individual service pages
│           ├── asphalt-paving.astro
│           ├── concrete.astro
│           ├── landscaping.astro
│           ├── pavers.astro
│           └── sealer.astro
├── tests/                  # Test files
├── astro.config.mjs        # Astro configuration
└── package.json
```

## 🧞 Development Commands

All commands are run from the root of the project:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Install dependencies                             |
| `npm run dev`             | Start dev server at `localhost:4321`            |
| `npm run build`           | Build production site to `./dist/`              |
| `npm run preview`         | Preview build locally before deploying          |
| `npm run lint`            | Run ESLint on TypeScript, JavaScript, and Astro files |
| `npm run test`            | Run Vitest tests                                 |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |

## 🛠️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd astro-mac-repository
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Open browser**
   Navigate to `http://localhost:4321`

## 🔧 Configuration

### Astro Config (`astro.config.mjs`)

- **Site URL:** `https://macpavingandsealcoating.com`
- **Trailing Slash:** Always (prevents duplicate URLs)
- **Sitemap:** Auto-generated with custom filtering
- **Port:** 4321 with host access enabled

### SEO Features

- Comprehensive meta tags on all pages
- Structured data (JSON-LD) for local business
- Service area coverage (60+ NJ cities)
- Canonical URLs for all pages
- Open Graph and Twitter meta tags

## 📱 Responsive Design

The website is fully responsive with:

- **Desktop:** Full-featured experience with video backgrounds
- **Mobile:** Optimized layouts and touch-friendly navigation
- **Tablet:** Adaptive grid systems and appropriate scaling

## 🎨 Styling Architecture

- **CSS Framework:** Custom CSS with Bootstrap grid system
- **Animations:** AOS (Animate On Scroll) library
- **Sliders:** Swiper.js for carousels
- **Icons:** Custom icon font (Icomoon)
- **Responsive Images:** Astro's optimized image processing

## � Performance Features

- **Image Optimization:** WebP format with fallbacks
- **Code Splitting:** Automatic with Astro
- **CSS/JS Minification:** Production builds
- **Lazy Loading:** Images and components
- **Preconnect:** External resources (fonts, CDNs)

## 🧪 Testing

- **Framework:** Vitest
- **Test Files:** Located in `/tests/` directory
- **Coverage:** Basic component and functionality tests

## 📈 SEO & Analytics

- **Local Business Schema:** Complete structured data
- **Service Pages:** Individual pages for each service
- **Area Coverage:** Dedicated content for service areas
- **Contact Information:** Consistent NAP (Name, Address, Phone)
- **Call-to-Action:** Strategic placement throughout site

## 🚀 Deployment

The site is configured for static site deployment and can be deployed to:

- **Netlify** (recommended for Astro)
- **Vercel**
- **GitHub Pages**
- **Traditional web hosting**

Build command: `npm run build`
Output directory: `dist/`

## 📞 Contact Information

**MAC Paving and Sealcoating LLC**
- **Phone:** (201) 755-7836
- **Website:** [macpavingandsealcoating.com](https://macpavingandsealcoating.com)
- **Service Area:** Northern New Jersey

## 📄 License

© 2025 MAC Paving and Sealcoating LLC. All rights reserved.

---

For technical support or development questions, please refer to the [Astro documentation](https://docs.astro.build) or contact the development team.
