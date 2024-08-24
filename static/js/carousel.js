document.addEventListener('DOMContentLoaded', function () {
    var carouselElement = document.querySelector('#bookCarousel');
    var carousel = new bootstrap.Carousel(carouselElement, {
        interval: 5000,
        wrap: true
    });
});