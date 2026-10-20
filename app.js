/**
 * ResQTravel — Interactive UI Logic
 * Handles: notifications, drag-drop, modals, toasts, constraints, and micro-interactions
 */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide icons
  lucide.createIcons();

  // ─── Element References ───────────────────────────────
  const notifBell = document.getElementById('notifBell');
  const notifDropdown = document.getElementById('notifDropdown');
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const navLinks = document.getElementById('navLinks');
  const alertDismiss = document.getElementById('alertDismiss');
  const heroAlert = document.getElementById('heroAlert');
  const dropArea = document.getElementById('dropArea');
  const constraintInput = document.getElementById('constraintInput');
  const addConstraintBtn = document.getElementById('addConstraintBtn');
  const constraintChips = document.getElementById('constraintChips');
  const rebookBtn1 = document.getElementById('rebookBtn1');
  const rebookModal = document.getElementById('rebookModal');
  const modalClose = document.getElementById('modalClose');
  const modalCancel = document.getElementById('modalCancel');
  const confirmRebook = document.getElementById('confirmRebook');
  const successToast = document.getElementById('successToast');
  const toastClose = document.getElementById('toastClose');

  // ─── Notification Bell Toggle ─────────────────────────
  notifBell.addEventListener('click', (e) => {
    e.stopPropagation();
    notifDropdown.classList.toggle('visible');
  });

  document.addEventListener('click', (e) => {
    if (!notifDropdown.contains(e.target) && !notifBell.contains(e.target)) {
      notifDropdown.classList.remove('visible');
    }
  });

  // ─── Mobile Menu Toggle ───────────────────────────────
  mobileMenuBtn.addEventListener('click', () => {
    navLinks.classList.toggle('mobile-open');
  });

  // ─── Nav Links Active State ───────────────────────────
  document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
      link.classList.add('active');
      navLinks.classList.remove('mobile-open');
    });
  });

  // ─── Alert Banner Dismiss ────────────────────────────
  alertDismiss.addEventListener('click', () => {
    heroAlert.style.transition = 'all 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
    heroAlert.style.maxHeight = heroAlert.scrollHeight + 'px';
    requestAnimationFrame(() => {
      heroAlert.style.maxHeight = '0';
      heroAlert.style.opacity = '0';
      heroAlert.style.marginBottom = '0';
      heroAlert.style.overflow = 'hidden';
    });
    setTimeout(() => heroAlert.style.display = 'none', 400);
  });

  // ─── Drag & Drop Zone ────────────────────────────────
  const dropEvents = ['dragenter', 'dragover', 'dragleave', 'drop'];
  dropEvents.forEach(event => {
    dropArea.addEventListener(event, (e) => {
      e.preventDefault();
      e.stopPropagation();
    });
  });

  ['dragenter', 'dragover'].forEach(event => {
    dropArea.addEventListener(event, () => dropArea.classList.add('dragover'));
  });

  ['dragleave', 'drop'].forEach(event => {
    dropArea.addEventListener(event, () => dropArea.classList.remove('dragover'));
  });

  dropArea.addEventListener('drop', (e) => {
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      handleFileUpload(files);
    }
  });

  function handleFileUpload(files) {
    const tagsContainer = document.querySelector('.ingested-tags');
    Array.from(files).forEach(file => {
      const tag = document.createElement('span');
      tag.className = 'ingested-tag';
      const iconName = file.type.startsWith('image') ? 'image' : 'file-text';
      tag.innerHTML = `<i data-lucide="${iconName}"></i> ${file.name} <i data-lucide="x" class="tag-remove"></i>`;
      tagsContainer.appendChild(tag);
      lucide.createIcons({ nodes: [tag] });

      // Animate in
      tag.style.animation = 'scale-in 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)';
      
      // Tag removal
      tag.querySelector('.tag-remove').addEventListener('click', () => {
        tag.style.transition = 'all 0.2s';
        tag.style.opacity = '0';
        tag.style.transform = 'scale(0.8)';
        setTimeout(() => tag.remove(), 200);
      });
    });
  }

  // Existing tag removal
  document.querySelectorAll('.ingested-tag .tag-remove').forEach(btn => {
    btn.addEventListener('click', () => {
      const tag = btn.closest('.ingested-tag');
      tag.style.transition = 'all 0.2s';
      tag.style.opacity = '0';
      tag.style.transform = 'scale(0.8)';
      setTimeout(() => tag.remove(), 200);
    });
  });

  // ─── Constraint Input ─────────────────────────────────
  function addConstraint() {
    const value = constraintInput.value.trim();
    if (!value) return;

    const chip = document.createElement('span');
    chip.className = 'constraint-chip';
    chip.innerHTML = `<i data-lucide="text"></i> ${value} <button class="chip-remove" aria-label="Remove"><i data-lucide="x"></i></button>`;
    constraintChips.appendChild(chip);
    lucide.createIcons({ nodes: [chip] });
    constraintInput.value = '';

    // Animate
    chip.style.animation = 'scale-in 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)';

    // Remove handler
    chip.querySelector('.chip-remove').addEventListener('click', () => {
      chip.style.transition = 'all 0.2s';
      chip.style.opacity = '0';
      chip.style.transform = 'scale(0.8)';
      setTimeout(() => chip.remove(), 200);
    });
  }

  addConstraintBtn.addEventListener('click', addConstraint);
  constraintInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') addConstraint();
  });

  // Existing chip removal
  document.querySelectorAll('.chip-remove').forEach(btn => {
    btn.addEventListener('click', () => {
      const chip = btn.closest('.constraint-chip');
      chip.style.transition = 'all 0.2s';
      chip.style.opacity = '0';
      chip.style.transform = 'scale(0.8)';
      setTimeout(() => chip.remove(), 200);
    });
  });

  // ─── Rebook Modal ─────────────────────────────────────
  // All "1-Click Rebook" buttons open the modal
  document.querySelectorAll('.rebook-btn, .option-actions .btn-primary').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      rebookModal.classList.add('visible');
      document.body.style.overflow = 'hidden';
    });
  });

  function closeModal() {
    rebookModal.classList.remove('visible');
    document.body.style.overflow = '';
  }

  modalClose.addEventListener('click', closeModal);
  modalCancel.addEventListener('click', closeModal);
  rebookModal.addEventListener('click', (e) => {
    if (e.target === rebookModal) closeModal();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
  });

  // ─── Confirm Rebook → Toast ───────────────────────────
  confirmRebook.addEventListener('click', () => {
    // Button loading state
    const originalContent = confirmRebook.innerHTML;
    confirmRebook.innerHTML = '<span class="loading-spinner"></span> Rebooking...';
    confirmRebook.disabled = true;
    confirmRebook.style.opacity = '0.7';

    setTimeout(() => {
      closeModal();
      confirmRebook.innerHTML = originalContent;
      confirmRebook.disabled = false;
      confirmRebook.style.opacity = '';

      // Show success toast
      successToast.classList.add('visible');
      setTimeout(() => {
        successToast.classList.remove('visible');
      }, 5000);
    }, 1500);
  });

  toastClose.addEventListener('click', () => {
    successToast.classList.remove('visible');
  });

  // ─── Dispatch Button Feedback ─────────────────────────
  document.querySelectorAll('.btn-dispatch').forEach(btn => {
    btn.addEventListener('click', function() {
      const original = this.innerHTML;
      if (this.classList.contains('edit')) return;

      this.innerHTML = '<i data-lucide="check"></i> Sent!';
      this.style.opacity = '0.7';
      this.disabled = true;
      lucide.createIcons({ nodes: [this] });

      setTimeout(() => {
        this.innerHTML = original;
        this.style.opacity = '';
        this.disabled = false;
        lucide.createIcons({ nodes: [this] });
      }, 2000);
    });
  });

  // ─── Hover shimmer on recommended card ────────────────
  const recommendedCard = document.querySelector('.option-card.recommended');
  if (recommendedCard) {
    recommendedCard.addEventListener('mouseenter', () => {
      recommendedCard.style.transition = 'all 0.3s cubic-bezier(0.16, 1, 0.3, 1)';
    });
  }

  // ─── Scroll-triggered animations ──────────────────────
  const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -40px 0px' };
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animationPlayState = 'running';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.option-card, .dispatch-card, .card').forEach(el => {
    observer.observe(el);
  });

  // ─── Timeline Leg Click → Subtle Expand Effect ────────
  document.querySelectorAll('.leg-card').forEach(card => {
    card.addEventListener('click', () => {
      const details = card.querySelector('.leg-details');
      if (details) {
        const isCollapsed = details.style.maxHeight === '0px';
        if (isCollapsed) {
          details.style.maxHeight = details.scrollHeight + 'px';
          details.style.opacity = '1';
        }
      }
    });
  });

  // ─── Ripple Effect on Primary Buttons ─────────────────
  document.querySelectorAll('.btn-primary, .btn-dispatch:not(.edit)').forEach(btn => {
    btn.addEventListener('click', function(e) {
      const ripple = document.createElement('span');
      const rect = this.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      ripple.style.cssText = `
        position: absolute;
        border-radius: 50%;
        background: rgba(255,255,255,0.3);
        width: ${size}px;
        height: ${size}px;
        left: ${e.clientX - rect.left - size/2}px;
        top: ${e.clientY - rect.top - size/2}px;
        transform: scale(0);
        animation: ripple-anim 0.6s ease-out;
        pointer-events: none;
      `;
      this.style.position = 'relative';
      this.style.overflow = 'hidden';
      this.appendChild(ripple);
      setTimeout(() => ripple.remove(), 600);
    });
  });

  // Ripple keyframes
  const rippleStyle = document.createElement('style');
  rippleStyle.textContent = `
    @keyframes ripple-anim {
      to { transform: scale(4); opacity: 0; }
    }
    .loading-spinner {
      display: inline-block;
      width: 16px;
      height: 16px;
      border: 2px solid rgba(255,255,255,0.3);
      border-top-color: white;
      border-radius: 50%;
      animation: spin 0.6s linear infinite;
    }
    @keyframes spin {
      to { transform: rotate(360deg); }
    }
  `;
  document.head.appendChild(rippleStyle);

  // ─── Auto-update "detected X min ago" ─────────────────
  const alertTimeAgo = document.querySelector('.alert-time-ago');
  if (alertTimeAgo) {
    let minutes = 4;
    setInterval(() => {
      minutes++;
      alertTimeAgo.textContent = `Detected ${minutes} min ago`;
    }, 60000);
  }

  // ─── Animate score rings on scroll ────────────────────
  const scoreRings = document.querySelectorAll('.score-ring');
  const scoreObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const fill = entry.target.querySelector('.score-fill');
        const score = entry.target.dataset.score;
        if (fill && score) {
          fill.style.strokeDasharray = `0, 100`;
          requestAnimationFrame(() => {
            fill.style.strokeDasharray = `${score}, 100`;
          });
        }
        scoreObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  scoreRings.forEach(ring => scoreObserver.observe(ring));
});
