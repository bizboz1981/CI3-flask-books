document.addEventListener('DOMContentLoaded', (event) => {
    const stars = document.querySelectorAll('.star');
    const ratingInput = document.getElementById('rating');

    stars.forEach(star => {
        star.addEventListener('click', () => {
            const rating = parseInt(star.getAttribute('data-value'), 10);
            ratingInput.value = rating;

            stars.forEach(s => s.classList.remove('selected'));
            star.classList.add('selected');
            for (let i = 0; i < rating; i++) {
                stars[i].classList.add('selected');
            }
        });
    });
});