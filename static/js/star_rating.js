// This script is used to handle the star rating system in the review form.
document.addEventListener('DOMContentLoaded', (event) => {
    const stars = document.querySelectorAll('.star');    // Select all elements with the class 'star'
    const ratingInput = document.getElementById('rating');    // Get the rating input element by its ID

    stars.forEach(star => {    // Iterate over each star element
        star.addEventListener('click', () => {        // Add a click event listener to each star
            const rating = parseInt(star.getAttribute('data-value'), 10);            // Get the rating value from the clicked star's data-value attribute
            ratingInput.value = rating;            // Set the rating input's value to the selected rating
            stars.forEach(s => s.classList.remove('selected'));            // Remove the 'selected' class from all stars
            star.classList.add('selected');            // Add the 'selected' class to the clicked star
            for (let i = 0; i < rating; i++) {            // Add the 'selected' class to all stars up to the selected rating
                stars[i].classList.add('selected');
            }
        });
    });
});