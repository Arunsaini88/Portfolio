# Deployment Guide

This guide covers deploying your portfolio to various platforms.

## Prerequisites

- Your resume PDF at `static/ARUN_SAINI_Resume.pdf`
- Git repository initialized
- GitHub account (recommended)

## Option 1: Deploy to Render (Recommended - Free Tier)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio commit"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy on Render**:
   - Go to [render.com](https://render.com)
   - Sign up/Login with GitHub
   - Click "New +" → "Web Service"
   - Connect your repository
   - Render will auto-detect the `render.yaml` configuration
   - Click "Create Web Service"
   - Your site will be live at `https://your-app-name.onrender.com`

## Option 2: Deploy to Heroku

1. **Install Heroku CLI**:
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login and Create App**:
   ```bash
   heroku login
   heroku create your-portfolio-name
   ```

3. **Deploy**:
   ```bash
   git push heroku main
   ```

4. **Open your app**:
   ```bash
   heroku open
   ```

## Option 3: Deploy to PythonAnywhere

1. **Sign up** at [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload files**:
   - Use the Files tab to upload your project
   - Or clone from GitHub

3. **Create Web App**:
   - Go to Web tab → "Add a new web app"
   - Choose "Flask"
   - Python version: 3.10

4. **Configure WSGI**:
   Edit `/var/www/yourusername_pythonanywhere_com_wsgi.py`:
   ```python
   import sys
   path = '/home/yourusername/Portfolio'
   if path not in sys.path:
       sys.path.append(path)

   from app import app as application
   ```

5. **Install requirements**:
   ```bash
   pip3.10 install --user -r requirements.txt
   ```

6. **Reload** the web app

## Option 4: Deploy to Railway

1. **Push to GitHub** (if not already done)

2. **Deploy on Railway**:
   - Go to [railway.app](https://railway.app)
   - Click "Start a New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will auto-detect Flask
   - Click "Deploy"

## Option 5: Deploy to Google Cloud Run

1. **Install Google Cloud SDK**

2. **Create Dockerfile** (already provided)

3. **Deploy**:
   ```bash
   gcloud run deploy portfolio \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

## Custom Domain Setup

### For Render:
1. Go to Settings → Custom Domains
2. Add your domain
3. Update DNS records with provided values

### For Heroku:
```bash
heroku domains:add www.yourdomain.com
```

### For PythonAnywhere:
1. Upgrade to paid account
2. Go to Web tab → Add custom domain

## Environment Variables

If you add features that need environment variables:

### Render/Heroku/Railway:
Set in the dashboard under Environment Variables

### PythonAnywhere:
Add to WSGI file or use python-dotenv

## Important Files

- `Procfile`: Heroku configuration
- `runtime.txt`: Python version specification
- `render.yaml`: Render configuration
- `vercel.json`: Vercel configuration (if using Vercel)
- `requirements.txt`: Python dependencies

## Post-Deployment Checklist

- [ ] Test all navigation links
- [ ] Verify contact form works
- [ ] Test resume download
- [ ] Check mobile responsiveness
- [ ] Test all social media links
- [ ] Verify SEO meta tags
- [ ] Set up custom domain (optional)
- [ ] Add Google Analytics (optional)
- [ ] Submit to Google Search Console (optional)

## Troubleshooting

### Port Issues:
Make sure your app uses `PORT` environment variable:
```python
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

### Static Files Not Loading:
Check that paths use `url_for('static', filename='...')`

### 502 Bad Gateway:
- Check logs: `heroku logs --tail` or platform equivalent
- Verify gunicorn is installed
- Check Procfile syntax

## Monitoring

### Render:
- View logs in dashboard
- Set up alerts

### Heroku:
```bash
heroku logs --tail
```

### PythonAnywhere:
- View error and access logs in Logs tab

## Free Tier Limits

- **Render**: 750 hours/month, sleeps after 15 min inactivity
- **Heroku**: 550-1000 hours/month (with credit card verification)
- **PythonAnywhere**: 1 web app, custom domain requires paid plan
- **Railway**: $5 free credit/month

## Recommended: Render

Render is recommended for its:
- Easy deployment
- Free SSL certificates
- Auto-deploy from GitHub
- Good performance on free tier
- Simple dashboard

---

Need help? Check the official documentation for your chosen platform!
