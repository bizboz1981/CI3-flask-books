// This script is used to display the flash message for 3 seconds and then hide it
document.addEventListener('DOMContentLoaded', function() {
    var flashMessage = document.getElementById('flash-message');   // Get the flash message element by its ID
    if (flashMessage) {    // Check if the flash message element exists
        flashMessage.style.display = 'block';   // Display the flash message

        // Hide the flash message after 3 seconds (3000 milliseconds)
        setTimeout(function() {
            flashMessage.style.display = 'none';
        }, 3000);
    }
});
