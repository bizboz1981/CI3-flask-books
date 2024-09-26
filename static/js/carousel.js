document.addEventListener('DOMContentLoaded', function () {// Wait for the DOM to be fully loaded before executing the script
    var carouselElement = document.querySelector('#bookCarousel');    // Select the carousel element by its ID
    var carousel = new bootstrap.Carousel(carouselElement, {    // Initialize the Bootstrap carousel with the selected element
        interval: 5000,        // Set the interval for automatic slide transition to 5000 milliseconds (5 seconds)
        wrap: true        // Enable continuous cycling of the carousel items
    });
});