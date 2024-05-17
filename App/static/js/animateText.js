const textContainer = document.getElementById('animated-text');
const texts = ["What if you found yourself in a place where a dream became reality?",
               "The absurd becomes the norm.",
               "Where did everyone go?"];
let currentIndex = 0;
let charIndex = 0;
let deleting = false;

function type() {
    if (!deleting && charIndex < texts[currentIndex].length) {
        textContainer.textContent += texts[currentIndex].charAt(charIndex);
        charIndex++;
        setTimeout(type, 100);
    } else if (deleting && charIndex > 0) {
        textContainer.textContent = texts[currentIndex].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(type, 50);
    } else {
        deleting = !deleting;
        if (!deleting) {
            currentIndex = (currentIndex + 1) % texts.length;
            setTimeout(type, 3500);
        } else {
            setTimeout(type, 1000);
        }
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    setTimeout(type, 3500);
});