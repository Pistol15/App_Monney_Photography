const overlay = document.getElementById("overlay");
const closeBtn = document.getElementById("closeMenu");
const openBtn = document.getElementById("openMenu");

openBtn.onclick = () => {
    overlay.classList.add("active");
};

closeBtn.onclick = () => {
    overlay.classList.remove("active");
};

overlay.addEventListener("click", (e) => {
    if (e.target === overlay) {
        overlay.classList.remove("active");
    }
});