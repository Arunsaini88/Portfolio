// Mobile Navigation Toggle
const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav-links');
const navLinks = document.querySelectorAll('.nav-links li');

burger.addEventListener('click', () => {
    // Toggle Nav
    nav.classList.toggle('active');

    // Burger Animation
    burger.classList.toggle('toggle');
});

// Close mobile menu when clicking a link
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        nav.classList.remove('active');
        burger.classList.remove('toggle');
    });
});

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar Background on Scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'rgba(10, 25, 47, 0.98)';
    } else {
        navbar.style.background = 'rgba(10, 25, 47, 0.95)';
    }
});

// Intersection Observer for Animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 1s ease forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all sections
document.querySelectorAll('section').forEach(section => {
    observer.observe(section);
});

// Animate skill tags on scroll
const skillTags = document.querySelectorAll('.skill-tag');
const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.style.animation = 'fadeInUp 0.5s ease forwards';
            }, index * 50);
            skillObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

skillTags.forEach(tag => {
    tag.style.opacity = '0';
    skillObserver.observe(tag);
});

// Create custom dialog box
function showDialog(message, type = 'success') {
    // Remove any existing dialog
    const existingDialog = document.querySelector('.custom-dialog');
    if (existingDialog) {
        existingDialog.remove();
    }

    // Create dialog
    const dialog = document.createElement('div');
    dialog.className = `custom-dialog ${type}`;
    dialog.innerHTML = `
        <div class="dialog-content">
            <div class="dialog-icon">
                ${type === 'success' ? '<i class="fas fa-check-circle"></i>' : '<i class="fas fa-exclamation-circle"></i>'}
            </div>
            <p class="dialog-message">${message}</p>
            <button class="dialog-close-btn">OK</button>
        </div>
    `;
    document.body.appendChild(dialog);

    // Add styles
    if (!document.getElementById('dialog-styles')) {
        const style = document.createElement('style');
        style.id = 'dialog-styles';
        style.textContent = `
            .custom-dialog {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.7);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 10000;
                animation: fadeIn 0.3s ease;
            }
            .dialog-content {
                background: #0a192f;
                border: 2px solid #64ffda;
                border-radius: 10px;
                padding: 30px;
                max-width: 400px;
                width: 90%;
                text-align: center;
                animation: slideUp 0.3s ease;
            }
            .dialog-icon {
                font-size: 48px;
                margin-bottom: 20px;
            }
            .custom-dialog.success .dialog-icon {
                color: #64ffda;
            }
            .custom-dialog.error .dialog-icon {
                color: #ff6b6b;
            }
            .dialog-message {
                color: #8892b0;
                font-size: 16px;
                margin-bottom: 20px;
                line-height: 1.6;
            }
            .dialog-close-btn {
                background: #64ffda;
                color: #0a192f;
                border: none;
                padding: 10px 30px;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.3s ease;
            }
            .dialog-close-btn:hover {
                background: #52e4c2;
                transform: translateY(-2px);
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @keyframes slideUp {
                from { transform: translateY(50px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }
        `;
        document.head.appendChild(style);
    }

    // Close dialog
    const closeBtn = dialog.querySelector('.dialog-close-btn');
    closeBtn.addEventListener('click', () => {
        dialog.style.animation = 'fadeOut 0.3s ease';
        setTimeout(() => dialog.remove(), 300);
    });

    // Close on background click
    dialog.addEventListener('click', (e) => {
        if (e.target === dialog) {
            dialog.style.animation = 'fadeOut 0.3s ease';
            setTimeout(() => dialog.remove(), 300);
        }
    });
}

// Contact Form Handling
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    const submitBtn = contactForm.querySelector('button[type="submit"]');
    const originalBtnText = submitBtn.innerHTML;

    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Disable button to prevent double submission
        if (submitBtn.disabled) {
            return;
        }
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

        const formData = {
            name: contactForm.name.value,
            email: contactForm.email.value,
            message: contactForm.message.value
        };

        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();

            if (data.status === 'success') {
                showDialog('Thank you for your message! I will get back to you soon.', 'success');
                contactForm.reset();
            } else {
                showDialog(data.message || 'Sorry, there was an error sending your message. Please try emailing directly.', 'error');
            }
        } catch (error) {
            showDialog('Sorry, there was an error sending your message. Please try emailing directly.', 'error');
        } finally {
            // Re-enable button after response
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnText;
        }
    });
}

// Typing Effect for Hero Title
const glitchText = document.querySelector('.glitch');
if (glitchText) {
    const text = glitchText.textContent;
    glitchText.textContent = '';
    let index = 0;

    function typeWriter() {
        if (index < text.length) {
            glitchText.textContent += text.charAt(index);
            index++;
            setTimeout(typeWriter, 100);
        }
    }

    setTimeout(typeWriter, 500);
}

// Parallax Effect for Hero Section
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero-content');
    if (hero) {
        hero.style.transform = `translateY(${scrolled * 0.5}px)`;
        hero.style.opacity = 1 - scrolled / 700;
    }
});

// Project Card Hover Effect
const projectCards = document.querySelectorAll('.project-card');
projectCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px) scale(1.02)';
    });

    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
    });
});

// Add active class to current section in nav
window.addEventListener('scroll', () => {
    let current = '';
    const sections = document.querySelectorAll('section');

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(li => {
        const link = li.querySelector('a');
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Counter Animation for Stats
const stats = document.querySelectorAll('.stat-item h3');
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const target = entry.target;
            const text = target.textContent;
            const number = parseInt(text);

            if (!isNaN(number)) {
                let current = 0;
                const increment = number / 50;
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= number) {
                        target.textContent = text;
                        clearInterval(timer);
                    } else {
                        target.textContent = Math.floor(current) + (text.includes('+') ? '+' : '') + (text.includes('%') ? '%' : '');
                    }
                }, 30);
            }
            statsObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

stats.forEach(stat => {
    statsObserver.observe(stat);
});

// Easter Egg - Konami Code
let konamiCode = [];
const konamiPattern = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];

document.addEventListener('keydown', (e) => {
    konamiCode.push(e.key);
    konamiCode.splice(-konamiPattern.length - 1, konamiCode.length - konamiPattern.length);

    if (konamiCode.join('') === konamiPattern.join('')) {
        document.body.style.animation = 'rainbow 2s linear infinite';
        setTimeout(() => {
            document.body.style.animation = '';
        }, 5000);
    }
});

// Add rainbow animation
const style = document.createElement('style');
style.textContent = `
    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
`;
document.head.appendChild(style);

console.log('%c👋 Hi there! Thanks for checking out my portfolio!', 'font-size: 20px; color: #64ffda; font-weight: bold;');
console.log('%cBuilt with Flask, Python, and lots of ☕', 'font-size: 14px; color: #8892b0;');
