// static/js/darkModeToggle.js

document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('darkModeToggle');
  if (!toggle) return;  // Safety check if button is missing

  const isDark = localStorage.getItem('dark-mode') === 'true';

  // Apply saved mode on load
  if (isDark) {
    document.body.classList.add('dark-mode');
  }

  toggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('dark-mode', document.body.classList.contains('dark-mode'));
  });
});
