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
app.config['MAIL_RECIPIENT'] = os.getenv('MAIL_RECIPIENT', os.getenv('MAIL_USERNAME'))

mail = Mail(app)

# Portfolio data
portfolio_data = {
    'name': 'ARUN SAINI',
    'title': 'Python Backend & AI/ML Engineer',
    'phone': os.getenv('PORTFOLIO_PHONE', ''),
    'email': os.getenv('PORTFOLIO_EMAIL', ''),
    'linkedin': 'https://www.linkedin.com/in/arun-saini-22392322b/',
    'github': 'https://github.com/Arunsaini88',
    'location': 'New Delhi, India',

    'summary': 'Python backend and AI/ML engineer building large-scale financial data pipelines and enterprise tooling for ~19 months. Currently developing options backtesting infrastructure at a fast-moving trading startup, with a growing focus on applied AI/ML — RAG systems, agents, and LLM-backed tooling.',

    'skills': {
        'Programming': ['Python (Advanced)', 'JavaScript', 'Java', 'C/C++'],
        'Backend': ['Django', 'Flask', 'FastAPI', 'RESTful APIs'],
        'AI/ML': ['LangChain', 'Gemini', 'PyTorch', 'Vector databases'],
        'Frontend': ['React.js', 'React Native', 'HTML5/CSS3'],
        'Databases': ['PostgreSQL/Neon', 'MySQL', 'SQLite'],
        'Cloud/DevOps': ['AWS (EC2, Lambda)', 'Docker', 'Kubernetes APIs', 'Railway', 'Vercel'],
    },

    'experience': [
        {
            'company': 'CSV Trade Trail Private Limited',
            'role': 'Software Developer',
            'period': 'Dec 2025 - Present',
            'achievements': [
                'Building large-scale options backtesting pipelines — pivot creation, occurrence analysis, and strategy-oriented data flows.',
                'Developing Python backend services for market data handling, high-frequency trading logs, and historical datasets.',
                'Working directly with the team lead and founder on feature planning and technical decisions in a startup environment.',
                'Producing dashboard-ready datasets to support strategy development and performance analysis.',
            ]
        },
        {
            'company': 'QappaLabs',
            'role': 'Software Developer',
            'period': 'Jan 2025 - Dec 2025',
            'achievements': [
                'Led development of Orchetrix, an open-source Kubernetes management GUI, using Python and PyQt6.',
                'Integrated Kubernetes APIs for full cluster management, deployment, and resource monitoring.',
                'Built cluster flow visualization and YAML comparison tooling — ~98% page-load reduction, ~70% faster cluster connect.',
                'Owned the project independently end-to-end, from design through cross-platform deployment — 255+ commits.',
            ]
        }
    ],

    'projects': [
        {
            'name': 'Orchetrix',
            'tech': 'Python, PyQt6, Kubernetes APIs',
            'description': 'Open-source Kubernetes management GUI with cluster flow visualization and YAML diffing.',
            'highlights': [
                '255+ commits, ~98% page-load reduction, ~70% faster cluster connect',
            ],
            'repo': 'https://github.com/qappalabs/orchetrix/releases',
        },
        {
            'name': 'RAG Monitoring Assistant',
            'tech': 'Python, LangChain',
            'description': 'Retrieval-augmented assistant for monitoring workflows — grounds LLM responses in live system context instead of static prompts.',
            'highlights': [],
            'repo': 'https://github.com/Arunsaini88/RAG_Monitoring_Assistant',
        },
        {
            'name': 'Cold Email AI',
            'tech': 'React, FastAPI, Gemini',
            'description': "SaaS tool that generates personalized cold outreach emails from a prospect's profile and context using an LLM pipeline.",
            'highlights': [],
            'repo': 'https://github.com/Arunsaini88/Cold_Email_AI_Frontend',
            'demo': 'https://cold-email-ai-frontend.vercel.app',
        },
        {
            'name': 'AI Social Media Manager',
            'tech': 'Python, LLM Agent',
            'description': 'Agent that plans and drafts social content on a schedule, reducing manual content-calendar work.',
            'highlights': [],
            'repo': 'https://github.com/Arunsaini88/AI_Social_Media_Manager_Agent',
        },
        {
            'name': 'Django E-Commerce Platform',
            'tech': 'Django Oscar, Razorpay, MySQL',
            'description': 'Fully customized Django Oscar storefront with product catalog, inventory, and integrated Razorpay + COD checkout.',
            'highlights': [],
            'repo': 'https://github.com/Arunsaini88/Django_E-com',
        },
        {
            'name': 'Trip Tracking App',
            'tech': 'Django',
            'description': 'Personal trip management app with image upload and geolocation tagging for each stop.',
            'highlights': [],
            'repo': 'https://github.com/Arunsaini88/Trip-App',
        },
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

        if not name or not email or not message:
            return jsonify({'status': 'error', 'message': 'All fields are required'}), 400

        if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
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

            confirmation = Message(
                subject='Thanks for contacting me!',
                recipients=[email]
            )
            confirmation.body = f"""
                                    Hi {name},

                                    Thank you for reaching out! I've received your message and will get back to you as soon as possible.

                                    Best regards,
                                    Arun Saini
                                    Python Backend & AI/ML Engineer

                                    ---
                                    This is an automated confirmation email.
                                """
            mail.send(confirmation)

            return jsonify({'status': 'success', 'message': 'Message sent successfully!'})
        else:
            print(f"Contact form submission - Name: {name}, Email: {email}, Message: {message}")
            return jsonify({'status': 'success', 'message': 'Message received! (Email not configured)'}), 200

    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Failed to send message. Please try again later.'}), 500


@app.route('/download-resume')
def download_resume():
    """Route to download resume (PDF or DOCX)"""
    resume = 'ARUN_SAINI'
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
