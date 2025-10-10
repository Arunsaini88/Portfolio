from flask import Flask, render_template, request, jsonify, send_file
from flask_mail import Mail, Message
import os
from datetime import datetime, UTC
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Email configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', os.getenv('MAIL_USERNAME'))
app.config['MAIL_RECIPIENT'] = os.getenv('MAIL_RECIPIENT', 'as9389872806@gmail.com')

mail = Mail(app)
    
# Portfolio data
portfolio_data = {
    'name': 'ARUN SAINI',
    'title': 'Python Developer | AI/ML Engineer | Backend Developer',
    'phone': '+919389872806',
    'email': 'as9389872806@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/arun-saini-22392322b/',
    'github': 'https://github.com/Arunsaini88',
    'location': 'Dehrsdun, India',

    'summary': 'Innovative Python Developer with 1 year of professional experience building enterprise-grade applications. Currently leading development of comprehensive Kubernetes management GUI application with advanced visualization features. Proven ability to work independently on complex projects while transitioning into AI/ML engineering.',

    'skills': {
        'Programming': ['Python (Advanced)', 'JavaScript', 'Java', 'C/C++'],
        'Backend': ['Django', 'Flask', 'FastAPI', 'RESTful APIs'],
        'Desktop': ['PyQt6', 'GUI Development', 'PyInstaller'],
        'Cloud/DevOps': ['AWS (EC2, Lambda)', 'Docker', 'Kubernetes APIs'],
        'Databases': ['MySQL', 'SQLite', 'Database Optimization'],
        'AI/ML': ['PyTorch', 'TensorFlow', 'LangChain', 'Vector databases'],
        'Frontend': ['React.js', 'HTML5', 'CSS3', 'Responsive Design'],
        'Tools': ['Git', 'GitHub', 'API Integration', 'AI Tools (Claude, GPT)']
    },

    'experience': [
        {
            'company': 'QappaLabs',
            'role': 'Software Developer',
            'period': 'Sep 2024 - Present',
            'achievements': [
                'Leading development of enterprise Kubernetes GUI management application using Python and PyQt6',
                'Integrating Kubernetes APIs for full cluster management, deployment, and resource monitoring',
                'Building advanced features including cluster flow visualization and YAML comparison tools',
                'Managing complete project lifecycle independently from conception to cross-platform deployment',
                'Reduced manual kubectl operations by 80% through intuitive GUI design'
            ]
        }
    ],

    'projects': [
        {
            'name': 'Kubernetes Management GUI Application',
            'tech': 'Python, PyQt6, Kubernetes APIs',
            'description': 'Enterprise-grade desktop application for cluster management with real-time monitoring',
            'highlights': [
                'Cluster flow graph visualization and YAML validation tools for DevOps optimization'
            ],
            'demo': 'https://github.com/qappalabs/orchetrix/releases'
        },
        {
            'name': 'Celebrity Booking Platform',
            'tech': 'Django Oscar, Razorpay, MySQL',
            'description': 'Specialized platform connecting users with celebrities for events, advertisements, receptions, and promotional activities',
            'highlights': [
                'Celebrity profile management with availability and pricing system',
                'Integrated Razorpay payment gateway for secure booking transactions',
                'Cash on Delivery (COD) payment option for flexible payment methods',
                'Booking management system for events, ads, receptions, and appearances',
                'User-friendly interface for browsing and booking celebrities',
                'Customized Django Oscar framework tailored for service-based bookings'
            ]
        },
        {
            'name': 'Django Oscar E-Commerce Platform',
            'tech': 'Django Oscar, Razorpay, MySQL',
            'description': 'Fully customized Django Oscar e-commerce platform with integrated payment solutions for online product sales',
            'highlights': [
                'Complete e-commerce functionality with product catalog and inventory management',
                'Integrated Razorpay payment gateway for secure online transactions',
                'Cash on Delivery (COD) payment option for customer convenience',
                'User-friendly shopping experience with responsive design',
                'Secure payment processing with order tracking and management system',
                'Customized Django Oscar framework optimized for product-based commerce'
            ]
        },
        {
            'name': 'Job Portal Web Application',
            'tech': 'Django, JavaScript',
            'description': 'Full-stack portal with dual interfaces, resume upload, and application tracking systems',
            'highlights': []
        },
        {
            'name': 'Trip Tracking Application',
            'tech': 'Django',
            'description': 'Personal trip management with image upload and geolocation features',
            'highlights': [],
            'demo': '#'
        }
    ],

    'education': [
        {
            'degree': 'B.Tech Computer Science & Engineering',
            'institution': 'Khwaja Moinuddin Chishti Language University',
            'period': '2021-2024'
        },
        {
            'degree': 'Diploma Computer Science & Engineering',
            'institution': 'Government Polytechnic College Saharanpur',
            'period': '2019-2021'
        }
    ],

    'certifications': [
        'AI Engineer Course (Currently Pursuing) - Machine Learning & AI Foundation',
        'Python Training & Internship - Linux World Pvt. Ltd.'
    ]
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')

        # Validate input
        if not name or not email or not message:
            return jsonify({'status': 'error', 'message': 'All fields are required'}), 400

        # Send email if mail is configured
        if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
            # Email to you (portfolio owner)
            msg = Message(
                subject=f'Portfolio Contact: Message from {name}',
                recipients=[app.config['MAIL_RECIPIENT']],
                reply_to=email
            )
            msg.body = f"""
New contact form submission from your portfolio:

Name: {name}
Email: {email}

Message:
{message}

---
Sent from your portfolio website
"""
            mail.send(msg)

            # Confirmation email to sender
            confirmation = Message(
                subject='Thanks for contacting me!',
                recipients=[email]
            )
            confirmation.body = f"""
Hi {name},

Thank you for reaching out! I've received your message and will get back to you as soon as possible.

Best regards,
Arun Saini
Python Developer | AI/ML Engineer

---
This is an automated confirmation email.
"""
            mail.send(confirmation)

            return jsonify({'status': 'success', 'message': 'Message sent successfully!'})
        else:
            # If email not configured, just log it (in production you might want to save to database)
            print(f"Contact form submission - Name: {name}, Email: {email}, Message: {message}")
            return jsonify({'status': 'success', 'message': 'Message received! (Email not configured)'}), 200

    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Failed to send message. Please try again later.'}), 500
    
@app.route('/download-resume')
def download_resume():
    """Route to download resume (PDF or DOCX)"""
    resume = 'ARUN_SAINI'
    # Try PDF first, then DOCX
    for ext in ['.pdf', '.docx']:
        resume_path = os.path.join(app.root_path, 'static', resume + ext)
        if os.path.exists(resume_path):
            return send_file(resume_path, as_attachment=True, download_name=resume + ext)
    return jsonify({'error': 'Resume not found'}), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.context_processor
def inject_now():
    return {'now': datetime.now(UTC), 'year': datetime.now().year}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
