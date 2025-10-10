# Arun Saini - Portfolio Website

A modern, responsive portfolio website built with Flask and Python to showcase professional experience, projects, and skills.

## Features

- **Responsive Design**: Fully responsive layout that works on all devices
- **Modern UI**: Clean, professional design with smooth animations
- **Interactive Elements**: Hover effects, smooth scrolling, and dynamic content
- **Contact Form**: Built-in contact form for easy communication
- **Project Showcase**: Dedicated section to highlight key projects
- **Skills Visualization**: Organized display of technical skills by category

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **Icons**: Font Awesome 6
- **Animations**: CSS animations and JavaScript interactions

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Portfolio
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
Portfolio/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── templates/
│   └── index.html         # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css      # Styles
│   └── js/
│       └── script.js      # JavaScript functionality
```

## Customization

### Update Portfolio Data

Edit the `portfolio_data` dictionary in `app.py` to update:
- Personal information
- Skills
- Projects
- Experience
- Education
- Certifications

### Styling

Modify `static/css/style.css` to customize:
- Colors (CSS variables in `:root`)
- Fonts
- Layouts
- Animations

### Add New Sections

1. Add new section in `templates/index.html`
2. Add corresponding styles in `static/css/style.css`
3. Update navigation links

## Deployment

### Deploy to Heroku

1. Create a `Procfile`:
```
web: gunicorn app:app
```

2. Add gunicorn to requirements.txt:
```bash
pip install gunicorn
pip freeze > requirements.txt
```

3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Deploy to PythonAnywhere

1. Upload files to PythonAnywhere
2. Create a web app with Flask
3. Configure WSGI file to point to your app
4. Reload the web app

### Deploy to Vercel/Netlify (Static Version)

For a static version, you can export the rendered HTML and deploy to static hosting platforms.

## Contact Form Setup

The contact form currently returns a success message. To enable email functionality:

1. Install Flask-Mail:
```bash
pip install Flask-Mail
```

2. Update `app.py` with email configuration
3. Implement email sending in the `/api/contact` route

## License

This project is open source and available under the MIT License.

## Contact

**Arun Saini**
- Email: as9389872806@gmail.com
- Phone: +919389872806
- Location: Saharanpur, India

---

Built with ❤️ using Flask & Python

