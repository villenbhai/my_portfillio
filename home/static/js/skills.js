// skill.js
document.addEventListener('DOMContentLoaded', () => {
  const progressFills = document.querySelectorAll('.progress-fill');

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if(entry.isIntersecting) {
        const el = entry.target;
        const width = el.style.width;
        el.style.width = '0';
        setTimeout(() => {
          el.style.width = width;
        }, 150);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.6 });

  progressFills.forEach(fill => {
    observer.observe(fill);
  });
});
