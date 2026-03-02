// RKoots Technical Knowledge Hub - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
  // Mobile Menu Toggle
  const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
  const mobileNav = document.getElementById('mobile-nav');
  const mobileNavClose = document.getElementById('mobile-nav-close');
  
  if (mobileMenuToggle && mobileNav) {
    mobileMenuToggle.addEventListener('click', function() {
      mobileNav.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    });
  }
  
  if (mobileNavClose && mobileNav) {
    mobileNavClose.addEventListener('click', function() {
      mobileNav.classList.remove('is-open');
      document.body.style.overflow = '';
    });
  }
  
  // Search Modal
  const searchToggle = document.getElementById('search-toggle');
  const searchModal = document.getElementById('search-modal');
  const searchModalClose = document.getElementById('search-modal-close');
  const searchInput = document.getElementById('search-input');
  
  if (searchToggle && searchModal) {
    searchToggle.addEventListener('click', function() {
      searchModal.classList.add('is-open');
      if (searchInput) {
        searchInput.focus();
      }
    });
  }
  
  if (searchModalClose && searchModal) {
    searchModalClose.addEventListener('click', function() {
      searchModal.classList.remove('is-open');
    });
  }
  
  // Close search modal on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && searchModal && searchModal.classList.contains('is-open')) {
      searchModal.classList.remove('is-open');
    }
  });
  
  // Smooth scroll for anchor links
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });
  
  // Add active class to navigation based on current page
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');
  
  navLinks.forEach(link => {
    const linkPath = new URL(link.href).pathname;
    if (linkPath === currentPath || (currentPath === '/' && linkPath === '/')) {
      link.classList.add('active');
    }
  });
  
  // Newsletter form submission
  const newsletterForms = document.querySelectorAll('.newsletter-form');
  newsletterForms.forEach(form => {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      const email = this.querySelector('input[type="email"]').value;
      
      // Show success message (in a real implementation, this would submit to a service)
      const successMessage = document.createElement('div');
      successMessage.className = 'newsletter-success';
      successMessage.innerHTML = `
        <div style="background: #28a745; color: white; padding: 15px; border-radius: 8px; margin-top: 10px;">
          <i class="fas fa-check-circle"></i> Thank you for subscribing! Check your email for confirmation.
        </div>
      `;
      
      this.appendChild(successMessage);
      this.reset();
      
      // Remove message after 5 seconds
      setTimeout(() => {
        successMessage.remove();
      }, 5000);
    });
  });
  
  // Copy code functionality
  const codeBlocks = document.querySelectorAll('pre code');
  codeBlocks.forEach(block => {
    const button = document.createElement('button');
    button.className = 'copy-code-btn';
    button.innerHTML = '<i class="fas fa-copy"></i>';
    button.title = 'Copy code';
    
    const pre = block.parentElement;
    pre.style.position = 'relative';
    pre.appendChild(button);
    
    button.addEventListener('click', function() {
      navigator.clipboard.writeText(block.textContent).then(() => {
        button.innerHTML = '<i class="fas fa-check"></i>';
        button.title = 'Copied!';
        
        setTimeout(() => {
          button.innerHTML = '<i class="fas fa-copy"></i>';
          button.title = 'Copy code';
        }, 2000);
      });
    });
  });
  
  // Performance optimization: Lazy load images
  const images = document.querySelectorAll('img[data-src]');
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.classList.remove('lazy');
        imageObserver.unobserve(img);
      }
    });
  });
  
  images.forEach(img => imageObserver.observe(img));
  
  // Initialize tooltips if needed
  const tooltipElements = document.querySelectorAll('[data-tooltip]');
  tooltipElements.forEach(element => {
    element.addEventListener('mouseenter', function() {
      const tooltip = document.createElement('div');
      tooltip.className = 'tooltip';
      tooltip.textContent = this.dataset.tooltip;
      document.body.appendChild(tooltip);
      
      const rect = this.getBoundingClientRect();
      tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
      tooltip.style.top = rect.top - tooltip.offsetHeight - 10 + 'px';
      
      this.tooltipElement = tooltip;
    });
    
    element.addEventListener('mouseleave', function() {
      if (this.tooltipElement) {
        this.tooltipElement.remove();
        this.tooltipElement = null;
      }
    });
  });
});

// Add CSS for copy button and tooltips
const style = document.createElement('style');
style.textContent = `
  .copy-code-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    background: rgba(0, 0, 0, 0.7);
    color: white;
    border: none;
    padding: 8px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 12px;
    opacity: 0;
    transition: opacity 0.3s ease;
  }
  
  pre:hover .copy-code-btn {
    opacity: 1;
  }
  
  .copy-code-btn:hover {
    background: rgba(0, 0, 0, 0.9);
  }
  
  .tooltip {
    position: absolute;
    background: #333;
    color: white;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 12px;
    white-space: nowrap;
    z-index: 1000;
    pointer-events: none;
  }
  
  .nav-link.active,
  .mobile-nav-link.active {
    color: #667eea !important;
    font-weight: 600;
  }
  
  .lazy {
    opacity: 0;
    transition: opacity 0.3s;
  }
  
  .lazy.loaded {
    opacity: 1;
  }
`;

document.head.appendChild(style);