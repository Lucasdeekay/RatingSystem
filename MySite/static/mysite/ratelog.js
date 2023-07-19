// Get DOM elements
const loginBtn = document.getElementById('login-btn');
const registerBtn = document.getElementById('register-btn');
const loginForm = document.getElementById('login-form');
const registerForm = document.getElementById('register-form');
const loginLink = document.getElementById('login-link');
const registerLink = document.getElementById('register-link');

// Add event listeners to toggle buttons
loginBtn.addEventListener('click', () => {
  // Show login form, hide register form
  loginForm.style.display = 'block';
  registerForm.style.display = 'none';

  // Update button classes
  loginBtn.classList.add('active');
  registerBtn.classList.remove('active');
});

registerBtn.addEventListener('click', () => {
  // Show register form, hide login form
  registerForm.style.display = 'block';
  loginForm.style.display = 'none';

  // Update button classes
  registerBtn.classList.add('active');
  loginBtn.classList.remove('active');
});

// Add event listeners to login/register links
loginLink.addEventListener('click', () => {
  // Show login form, hide register form
  loginForm.style.display = 'block';
  registerForm.style.display = 'none';

  // Update button classes
  loginBtn.classList.add('active');
  registerBtn.classList.remove('active');
});

registerLink.addEventListener('click', () => {
  // Show register form, hide login form
  registerForm.style.display = 'block';
  loginForm.style.display = 'none';

  // Update button classes
  registerBtn.classList.add('active');
  loginBtn.classList.remove('active');
});
