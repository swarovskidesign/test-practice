document.addEventListener('DOMContentLoaded', () => {
    const rangeInput = document.querySelector('input[type="range"]');
    const hiddenTexts = document.querySelectorAll('.hidden-text');

    function updateVisibleTexts(value) {
        hiddenTexts.forEach((text, index) => {
            if (index <= value) {
                text.classList.add('show');
            } else {
                text.classList.remove('show');
            }
        });
    }

    updateVisibleTexts(rangeInput.value);

    rangeInput.addEventListener('input', () => {
        updateVisibleTexts(rangeInput.value);
    });
});
