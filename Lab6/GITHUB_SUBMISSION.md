# GitHub Submission Instructions

## Step 1: Create GitHub Repository

### Option A: Create via GitHub.com
1. Go to [GitHub.com](https://github.com/new)
2. Click "New repository"
3. Repository name: `lab6` (or `Web-Dev-Lab6`)
4. Description: "Album Browser - Angular Routing & HTTP Lab"
5. Choose: Public or Private (per course requirements)
6. Do NOT initialize with README (we already have one)
7. Click "Create repository"

### Option B: Create via GitHub CLI
```bash
gh repo create lab6 --public --source=. --remote=origin --push
```

---

## Step 2: Add Remote and Push

Navigate to the album-browser directory:

```bash
cd "c:\Users\Dias Tursunofff\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\Web Dev\lab6\album-browser"
```

Add the GitHub remote:

```bash
git remote add origin https://github.com/YOUR_USERNAME/lab6.git
```

Rename the branch to main (if needed):

```bash
git branch -M main
```

Push to GitHub:

```bash
git push -u origin main
```

---

## Step 3: Verify Repository Structure

Your GitHub repository should show:

```
lab6/
├── src/
│   ├── app/
│   │   ├── components/
│   │   ├── models/
│   │   ├── services/
│   │   └── ... (other app files)
│   └── ... (other src files)
├── public/
├── angular.json
├── package.json
├── package-lock.json
├── tsconfig.json
├── README.md
├── .gitignore
└── ... (other config files)
```

**Important:** `node_modules/` should NOT be visible (excluded by .gitignore)

---

## Step 4: Add Collaborators (If Required)

If your instructor needs to be a collaborator:

1. Go to Settings → Collaborators
2. Click "Add people"
3. Enter instructor's GitHub username
4. Select "Maintain" or "Admin" access

---

## Step 5: Create a README for GitHub

The main `album-browser` directory already has a comprehensive README.md. You can also add one to the `lab6` folder for context:

**File:** `lab6/README.md`

```markdown
# Lab 6: Album Browser

## Overview
This is a solution for Lab 6: Routing & HTTP Submission of the Web Development course.

## Project
Album Browser is an Angular single-page application (SPA) that demonstrates:
- Angular Router configuration with multiple routes
- HTTP Client for REST API integration
- Service-based architecture
- CRUD operations
- Responsive design

## Quick Start

```bash
cd album-browser
npm install
ng serve
```

Navigate to `http://localhost:4200/`

## Features
- Browse 100+ albums from JSONPlaceholder API
- View album details and edit titles
- Explore photos in a grid layout
- Delete albums
- Responsive mobile-friendly design

## Technologies
- Angular 19+
- TypeScript
- RxJS
- Angular Router
- HttpClient
- CSS3

## Project Structure

```
album-browser/
├── src/
│   ├── app/
│   │   ├── components/
│   │   │   ├── home/
│   │   │   ├── about/
│   │   │   ├── albums/
│   │   │   ├── album-detail/
│   │   │   └── album-photos/
│   │   ├── services/
│   │   │   └── album.service.ts
│   │   ├── models/
│   │   │   ├── album.model.ts
│   │   │   └── photo.model.ts
│   │   └── ... (other app files)
│   └── ... (other src files)
└── ... (config files)
```

## Learning Outcomes
- ✅ Configure Angular Router with route parameters
- ✅ Implement navigation with routerLink
- ✅ Use HttpClient for REST API calls
- ✅ Work with Observables
- ✅ Create service layer for data
- ✅ Implement CRUD operations
- ✅ Build responsive UX

## Documentation
- [IMPLEMENTATION_SUMMARY.md](./IMPLEMENTATION_SUMMARY.md) - Detailed implementation guide
- [QUICKSTART.md](./QUICKSTART.md) - Quick start guide
- [CHECKLIST.md](./CHECKLIST.md) - Completion checklist

## Submission
- Repository: GitHub
- Status: ✅ Complete
- Date: March 3, 2026

---

For detailed information, see `album-browser/README.md`
```

---

## Step 6: Verify Files Are Uploaded

After pushing to GitHub, verify:

```bash
# Check that remote is set
git remote -v

# Check recent commits
git log --oneline -5

# Verify branch
git branch -a
```

---

## Step 7: Share with Instructor

Send your instructor the GitHub repository URL:

```
https://github.com/YOUR_USERNAME/lab6
```

Or use GitHub's invite feature to add them as a collaborator.

---

## Step 8: Optional - Add an About Section

Edit the repository settings:

1. Go to Settings → About
2. Add Description: "Album Browser - Angular Lab 6"
3. Add Topics: `angular`, `routing`, `http`, `typescript`, `spa`
4. Add Website: (if deploying)

---

## Troubleshooting

### Issue: "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/lab6.git
```

### Issue: "Permission denied (publickey)"
Set up SSH keys:
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to GitHub Settings → SSH Keys
cat ~/.ssh/id_ed25519.pub
```

Then use SSH URL for remote:
```bash
git remote set-url origin git@github.com:YOUR_USERNAME/lab6.git
```

### Issue: Large node_modules in repository
```bash
# Remove from git (but keep locally)
git rm --cached -r node_modules/
git commit -m "Remove node_modules from tracking"

# Ensure .gitignore has this line:
echo "node_modules/" >> .gitignore
```

---

## Optional: Continuous Deployment

### Deploy to GitHub Pages
```bash
# Install gh-pages
npm install --save-dev gh-pages

# Update package.json with:
"scripts": {
  "build": "ng build",
  "deploy": "gh-pages -d dist/album-browser"
}

# Deploy
npm run build
npm run deploy
```

Then enable GitHub Pages in Settings.

### Deploy to Vercel
1. Connect GitHub to Vercel
2. Select your repository
3. Framework: Angular
4. Build command: `npm run build`
5. Output directory: `dist/album-browser`
6. Deploy

---

## Verification Checklist

Before submitting to instructor:

- [ ] Repository created on GitHub
- [ ] Remote added to local repo
- [ ] All files pushed to GitHub
- [ ] node_modules is NOT in repository
- [ ] README.md is visible on GitHub
- [ ] All components are visible in src/app/components/
- [ ] Service file visible in src/app/services/
- [ ] Model files visible in src/app/models/
- [ ] Can clone and run locally:
  ```bash
  git clone https://github.com/YOUR_USERNAME/lab6.git
  cd lab6/album-browser
  npm install
  ng serve
  ```
- [ ] Instructor can access the repository

---

## Final Notes

✅ **Your project is well-organized and ready for submission!**

The lab includes:
- **Routing:** 6 configured routes
- **HTTP:** Service with 5 API methods
- **Components:** 5 fully functional components
- **CRUD:** Create, Read, Update, Delete operations
- **Code Quality:** Clean, typed, organized
- **Documentation:** Multiple guide files

---

## Contact

For questions about the submission process:
1. Check GitHub's help: https://docs.github.com
2. Review Angular docs: https://angular.dev
3. Ask your course instructor

Good luck with your submission! 🚀
