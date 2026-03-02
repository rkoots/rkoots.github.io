// RKoots Technical Knowledge Hub - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
  // Mobile Menu Toggle
  const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
  const mobileNav = document.getElementById('mobile-nav');
  const mobileNavClose = document.getElementById('mobile-nav-close');
  
  // Create overlay for mobile menu
  const overlay = document.createElement('div');
  overlay.className = 'mobile-nav-overlay';
  document.body.appendChild(overlay);
  
  function openMobileMenu() {
    mobileNav.classList.add('is-open');
    overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }
  
  function closeMobileMenu() {
    mobileNav.classList.remove('is-open');
    overlay.classList.remove('is-open');
    document.body.style.overflow = '';
  }
  
  if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', openMobileMenu);
  }
  
  if (mobileNavClose) {
    mobileNavClose.addEventListener('click', closeMobileMenu);
  }
  
  if (overlay) {
    overlay.addEventListener('click', closeMobileMenu);
  }
  
  // Close mobile menu on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && mobileNav.classList.contains('is-open')) {
      closeMobileMenu();
    }
  });
  
  // Search Modal
  const searchToggle = document.getElementById('search-toggle');
  const searchModal = document.getElementById('search-modal');
  const searchModalClose = document.getElementById('search-modal-close');
  const searchInput = document.getElementById('search-input');
  
  function openSearchModal() {
    searchModal.classList.add('is-open');
    if (searchInput) {
      setTimeout(() => searchInput.focus(), 300);
    }
  }
  
  function closeSearchModal() {
    searchModal.classList.remove('is-open');
    if (searchInput) {
      searchInput.value = '';
    }
  }
  
  if (searchToggle && searchModal) {
    searchToggle.addEventListener('click', openSearchModal);
  }
  
  if (searchModalClose && searchModal) {
    searchModalClose.addEventListener('click', closeSearchModal);
  }
  
  // Close search modal on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && searchModal && searchModal.classList.contains('is-open')) {
      closeSearchModal();
    }
  });
  
  // Close search modal on backdrop click
  searchModal.addEventListener('click', function(e) {
    if (e.target === searchModal) {
      closeSearchModal();
    }
  });
  
  // Header scroll effect
  const header = document.getElementById('site-header');
  let lastScrollY = window.scrollY;
  
  function handleScroll() {
    const currentScrollY = window.scrollY;
    
    if (currentScrollY > 100) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
    
    lastScrollY = currentScrollY;
  }
  
  window.addEventListener('scroll', handleScroll, { passive: true });
  
  // Smooth scroll for anchor links
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          const headerHeight = header.offsetHeight;
          const targetPosition = target.offsetTop - headerHeight - 20;
          
          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
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
      
      // Show success message
      const successMessage = document.createElement('div');
      successMessage.className = 'newsletter-success';
      successMessage.innerHTML = `
        <div style="background: #28a745; color: white; padding: 15px; border-radius: 8px; margin-top: 10px; animation: slideIn 0.3s ease-out;">
          <i class="fas fa-check-circle"></i> Thank you for subscribing! Check your email for confirmation.
        </div>
      `;
      
      this.appendChild(successMessage);
      this.reset();
      
      // Remove message after 5 seconds
      setTimeout(() => {
        successMessage.style.animation = 'slideOut 0.3s ease-out forwards';
        setTimeout(() => successMessage.remove(), 300);
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
  
  // Add hover effect to cards
  const cards = document.querySelectorAll('.featured-card, .category-card');
  cards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-8px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0) scale(1)';
    });
  });
});

// Add CSS animations
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
    transition: opacity 0.3s ease, transform 0.3s ease;
  }
  
  pre:hover .copy-code-btn {
    opacity: 1;
  }
  
  .copy-code-btn:hover {
    background: rgba(0, 0, 0, 0.9);
    transform: scale(1.1);
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
    animation: tooltipFadeIn 0.2s ease-out;
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
  
  @keyframes slideIn {
    from {
      transform: translateY(-20px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }
  
  @keyframes slideOut {
    from {
      transform: translateY(0);
      opacity: 1;
    }
    to {
      transform: translateY(-20px);
      opacity: 0;
    }
  }
  
  @keyframes tooltipFadeIn {
    from {
      opacity: 0;
      transform: translateY(5px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @keyframes pulse {
    0%, 100% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.05);
    }
  }
  
  .featured-card,
  .category-card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .btn:hover {
    animation: pulse 0.6s ease-in-out;
  }
`;

document.head.appendChild(style);