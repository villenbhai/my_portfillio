document.addEventListener('DOMContentLoaded', () => {
  // Create the trailing cursor dot element
  const cursorDot = document.createElement('div');
  cursorDot.id = 'cursor-dot';
  document.body.appendChild(cursorDot);

  let mouseX = 0;
  let mouseY = 0;
  let dotX = 0;
  let dotY = 0;
  const delay = 8; // Higher value means slower trailing

  // Update mouse coordinates on mousemove
  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursorDot.style.display = 'block';
  });

  // Animate the trailing dot position
  function animate() {
    dotX += (mouseX - dotX) / delay;
    dotY += (mouseY - dotY) / delay;
    cursorDot.style.transform = `translate3d(${dotX}px, ${dotY}px, 0)`;
    requestAnimationFrame(animate);
  }

  animate();
});
