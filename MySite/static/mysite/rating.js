document.getElementById("ratingForm").addEventListener("submit", function(event) {
    event.preventDefault();
    showPopup();
  });
  
  document.querySelector(".close").addEventListener("click", function() {
    hidePopup();
  });
  
  function showPopup() {
    document.getElementById("popup").style.display = "block";
  }
  
  function hidePopup() {
    document.getElementById("popup").style.display = "none";
  }

  //Login
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

//Rating calculation
// Get DOM elements
const ratingsForm = document.getElementById('ratings-form');
const ratingsResult = document.getElementById('ratings-result');

// Add event listener to ratings form
ratingsForm.addEventListener('submit', (e) => {
  e.preventDefault();

  // Get course code and title values
  const courseCode = document.getElementById('course-code').value;
  const courseTitle = document.getElementById('course-title').value;

  // Perform ratings calculation (replace this with your own logic)
  const ratings = calculateRatings(courseCode, courseTitle);

  // Display ratings result
  ratingsResult.textContent = `Cumulative Ratings for ${courseCode} - ${courseTitle}: ${ratings}`;
});

// Calculate ratings function (example logic)
function calculateRatings(courseCode, courseTitle) {
  // Replace this with your own logic to calculate ratings
  // Example: return the sum of all ratings for the given course
  return 4.5; // Replace with your calculated ratings value
}

