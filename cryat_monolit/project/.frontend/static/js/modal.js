const modalCreate = document.getElementById("modal");
const closeButtonCreate = document.querySelector("#modal .close");

document.getElementById("openModal").onclick = function() {
    modalCreate.style.display = "block";
}

closeButtonCreate.onclick = function() {
    modalCreate.style.display = "none";
}

window.addEventListener("click", function(event) {
    if (event.target === modalCreate) {
        modalCreate.style.display = "none";
    }
});

const modalSend = document.getElementById("sendModal");
const closeButtonSend = document.querySelector("#sendModal .close-send");

document.getElementById("send").onclick = function() {
    modalSend.style.display = "block";
}

closeButtonSend.onclick = function() {
    modalSend.style.display = "none";
}

window.addEventListener("click", function(event) {
    if (event.target === modalSend) {
        modalSend.style.display = "none";
    }
});

const modalBetween = document.getElementById("betweenModal");
const closeButtonBetween = document.querySelector("#betweenModal .close");
const openButtonBetween = document.getElementById("between");

openButtonBetween.onclick = function() {
    modalBetween.style.display = "block";
}

closeButtonBetween.onclick = function() {
    modalBetween.style.display = "none";
}

window.addEventListener("click", function(event) {
    if (event.target === modalBetween) {
        modalBetween.style.display = "none";
    }
});

const modalExchange = document.getElementById("exchangeModal");
const closeButtonExchange = document.querySelector("#exchangeModal .close-send");

document.getElementById("exchange").onclick = function() {
    modalExchange.style.display = "block";
}

closeButtonExchange.onclick = function() {
    modalExchange.style.display = "none";
}

window.addEventListener("click", function(event) {
    if (event.target === modalExchange) {
        modalExchange.style.display = "none";
    }
});