// Get DOM elements
const ratingForm = document.getElementById('rating-form');
const submitButton = document.querySelector('button[type="submit"]');
const popup = document.getElementById('popup');
const popupClose = document.getElementById('popup-close');

popup.style.display = 'none';

// Submit form event listener
ratingForm.addEventListener('submit', (e) => {
  // Show popup message
  popup.style.display = 'block';
});

// Close popup event listener
popupClose.addEventListener('click', () => {
  popup.style.display = 'none';
});
