// Mobile nav toggle
const burger = document.querySelector('.burger');
const navLinks = document.querySelector('.nav-links');

burger?.addEventListener('click', () => {
  const isOpen = navLinks.style.display === 'flex';
  navLinks.style.display = isOpen ? 'none' : 'flex';
  if (!isOpen) {
    navLinks.style.cssText +=
      'flex-direction:column; position:absolute; top:60px; right:32px; background:var(--paper); border:1px solid var(--line); padding:16px 24px; gap:14px; z-index:60;';
  }
});

// Close mobile nav when a link is clicked
navLinks?.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    if (window.innerWidth <= 760) navLinks.style.display = 'none';
  });
});

// Contact form -> POST to existing /api/contact Flask route
const contactForm = document.getElementById('contactForm');
const formStatus = document.getElementById('formStatus');

contactForm?.addEventListener('submit', async function (e) {
  e.preventDefault();
  const btn = this.querySelector('button');
  const original = btn.innerHTML;
  const formData = new FormData(this);
  const payload = Object.fromEntries(formData.entries());

  btn.disabled = true;
  btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

  try {
    const res = await fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const result = await res.json();

    if (res.ok && result.status === 'success') {
      btn.innerHTML = '<i class="fas fa-check"></i> Sent';
      if (formStatus) formStatus.textContent = '// message sent successfully';
      this.reset();
    } else {
      throw new Error(result.message || 'Failed to send');
    }
  } catch (err) {
    btn.innerHTML = '<i class="fas fa-triangle-exclamation"></i> Failed — try again';
    if (formStatus) formStatus.textContent = '// ' + err.message;
  } finally {
    setTimeout(() => {
      btn.disabled = false;
      btn.innerHTML = original;
    }, 2500);
  }
});
