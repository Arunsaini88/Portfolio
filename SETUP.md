# Portfolio Setup Instructions

## Quick Start

Follow these steps to get your portfolio running locally:

### 1. Install Python Dependencies

```bash
# Navigate to the portfolio directory
cd d:\assignments\Portfolio

# Install required packages
pip install -r requirements.txt
```

### 2. Add Your Resume

Place your resume PDF in the static folder:
```
static/ARUN_SAINI_Resume.pdf
```

This enables the "Download Resume" button on your portfolio.

### 3. Add Profile Images (Optional)

Add these images to enhance your portfolio:

- `static/img/og-image.jpg` - Social media preview image (1200x630px recommended)
- `static/favicon.png` - Browser tab icon (32x32px or 64x64px)

### 4. Update Your Information

Edit `app.py` to customize:

- **LinkedIn URL** (line 12): Replace with your actual LinkedIn profile
- **GitHub URL**: Update in the HTML template if you have a GitHub profile
- **Project demo links**: Add actual URLs for your live projects
- **Any other personal information**

### 5. Run the Application

```bash
python app.py
```

Your portfolio will be available at: **http://localhost:5000**

## Customization

### Change Colors

Edit `static/css/style.css` and modify the CSS variables:

```css
:root {
    --primary-color: #3498db;
    --secondary-color: #2ecc71;
    --dark-bg: #0a192f;
    --accent: #64ffda;
    /* Change these to your preferred colors */
}
```

### Add More Projects

Edit the `projects` list in `app.py`:

```python
{
    'name': 'Project Name',
    'tech': 'Technologies Used',
    'description': 'Project description',
    'highlights': ['Key feature 1', 'Key feature 2'],
    'demo': 'https://your-demo-link.com'
}
```

### Update Skills

Modify the `skills` dictionary in `app.py` to add/remove skills:

```python
'skills': {
    'Programming': ['Python', 'JavaScript', ...],
    'Backend': ['Django', 'Flask', ...],
    # Add more categories
}
```

## Testing

### Test Locally

1. Open http://localhost:5000
2. Click all navigation links
3. Test the contact form
4. Try the "Download Resume" button
5. Check mobile view (resize browser or use DevTools)

### Test on Mobile

Use your phone's browser to access:
- Find your computer's IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
- Access from phone: `http://YOUR_IP:5000`

## Next Steps

1. ✅ Test all features locally
2. ✅ Add your resume PDF
3. ✅ Update LinkedIn and social links
4. ✅ Add profile images
5. ✅ Customize colors (optional)
6. 🚀 Deploy to production (see DEPLOYMENT.md)

## Troubleshooting

### Port Already in Use
```bash
# Change port in app.py (last line)
app.run(debug=True, host='0.0.0.0', port=5001)  # Use different port
```

### Module Not Found Error
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Static Files Not Loading
- Make sure you're using `python app.py` from the Portfolio directory
- Check that the `static` folder exists
- Verify file paths in templates use `url_for('static', filename='...')`

### Resume Download Not Working
- Ensure resume PDF exists at: `static/ARUN_SAINI_Resume.pdf`
- Check file permissions
- Verify filename matches exactly (case-sensitive)

## File Structure

```
Portfolio/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview
├── SETUP.md                    # This file
├── DEPLOYMENT.md              # Deployment instructions
├── Procfile                    # Heroku deployment
├── runtime.txt                 # Python version
├── Dockerfile                  # Docker container
├── templates/
│   ├── index.html             # Main page template
│   ├── 404.html               # Error page
│   └── 500.html               # Server error page
└── static/
    ├── css/
    │   └── style.css          # Styles
    ├── js/
    │   └── script.js          # JavaScript
    ├── img/                    # Images folder
    │   ├── og-image.jpg       # Social preview (add this)
    │   └── favicon.png        # Browser icon (add this)
    └── ARUN_SAINI_Resume.pdf  # Your resume (add this)
```

## Need Help?

- Check README.md for general information
- See DEPLOYMENT.md for deployment options
- Open an issue if you encounter problems

---

Happy coding! 🚀
