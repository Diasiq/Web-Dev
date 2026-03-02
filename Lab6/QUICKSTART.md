# Quick Start Guide - Album Browser

## Prerequisites

- Node.js 18+ installed
- Angular CLI installed: `npm install -g @angular/cli`
- Git installed (for version control)

## Installation Steps

1. **Navigate to the project directory:**
   ```bash
   cd album-browser
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

## Running the Application

### Development Server
```bash
ng serve
```
Open your browser and navigate to: `http://localhost:4200/`

The application will automatically reload when you make changes to source files.

### Production Build
```bash
ng build --configuration production
```

The build artifacts will be stored in the `dist/` directory.

## Project Navigation

Once the app is running:

1. **Home Page** - Start page with welcome message and introduction
2. **Albums Page** - Browse all 100 albums from the API
   - Click any album to view details
   - Click Delete to remove an album
3. **Album Details** - Edit album title and view photos
   - Edit the title field
   - Click "Save Changes" to update
   - Click "View Photos" to see album photos
4. **Album Photos** - Grid view of all photos in the album
   - Hover over photos to see full titles
   - Click "Back to Album Details" to return
5. **About Page** - Information about the application

## Key Features

- ✅ Real data from JSONPlaceholder API
- ✅ Responsive design (works on mobile and desktop)
- ✅ Loading indicators while fetching data
- ✅ Error handling and retry functionality
- ✅ CRUD operations (Read, Update, Delete)
- ✅ Clean, modern UI

## Troubleshooting

### Issue: Port 4200 already in use
```bash
ng serve --port 4201
```

### Issue: Module not found errors
```bash
npm ci  # Clean install
ng serve
```

### Issue: Build errors
```bash
ng build --watch    # Watch mode for development
ng build --aot      # Ahead-of-time compilation
```

## Project Files Structure

```
src/app/
├── components/           # 5 Angular components
│   ├── home/            # Welcome page
│   ├── about/           # About page
│   ├── albums/          # Album list
│   ├── album-detail/    # Album details
│   └── album-photos/    # Photo gallery
├── services/             # Service layer
│   └── album.service.ts # API communication
├── models/               # TypeScript interfaces
│   ├── album.model.ts
│   └── photo.model.ts
├── app.routes.ts        # Routing configuration
├── app.ts              # Root component
└── app.html            # Root template
```

## API Used

**JSONPlaceholder** - Free fake REST API
- Base URL: https://jsonplaceholder.typicode.com
- 100 sample albums
- Photos for each album
- Simulated PUT/DELETE operations

## Commands Reference

```bash
# Start development server
ng serve

# Build for production
ng build --configuration production

# Run tests
ng test

# Run end-to-end tests
ng e2e

# Generate a new component
ng generate component component-name

# Generate a service
ng generate service service-name
```

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Learning Resources

- [Angular Documentation](https://angular.dev)
- [Angular Routing Guide](https://angular.dev/guide/routing)
- [Angular HttpClient](https://angular.dev/guide/http)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/)
- [RxJS Documentation](https://rxjs.dev)

## Getting Help

1. Check the console for error messages
2. Review the Network tab in Developer Tools
3. Verify the API is accessible: https://jsonplaceholder.typicode.com/albums
4. Check that `ng serve` is running on the correct port

## Tips for Development

- Use Chrome DevTools to debug
- Check the Network tab to monitor API calls
- Use Angular DevTools extension for Angular debugging
- Keep the console open to catch errors early
- Test on mobile viewport to check responsiveness

## Deployment

### Deploy to GitHub Pages
```bash
ng build --configuration production --base-href "/album-browser/"
```

### Deploy to Vercel/Netlify
1. Connect your GitHub repository
2. Build command: `npm run build`
3. Output directory: `dist/album-browser`

---

**Ready to develop!** Start with `ng serve` and enjoy the Album Browser app.
