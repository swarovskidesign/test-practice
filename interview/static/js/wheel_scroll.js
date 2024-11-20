const slides = document.querySelectorAll('.slide');
let currentSlide = 0;
let isScrolling = false;

function scrollToSlide(index) {
    isScrolling = true;
    slides[index].scrollIntoView({ behavior: 'smooth' });
    setTimeout(() => {
        isScrolling = false;
    }, 600);
}

window.addEventListener('wheel', (event) => {
    if (isScrolling) return;

    const direction = Math.sign(event.deltaY);
    const newSlide = currentSlide + direction;

    if (newSlide >= 0 && newSlide < slides.length) {
        currentSlide = newSlide;
        scrollToSlide(currentSlide);
    }
});