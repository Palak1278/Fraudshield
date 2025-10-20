// Accordion toggle
const accordions = document.querySelectorAll(".accordion");
accordions.forEach(acc => {
  acc.addEventListener("click", () => {
    const panel = acc.nextElementSibling;
    panel.style.display = panel.style.display === "block" ? "none" : "block";
  });
});

// Popup behavior
const popup = document.getElementById("popup");
const closePopup = document.getElementById("closePopup");
const popupMinimized = document.getElementById("popupMinimized");

closePopup.addEventListener("click", () => {
  popup.style.display = "none";
  popupMinimized.style.display = "block";
});

popupMinimized.addEventListener("click", () => {
  popup.style.display = "block";
  popupMinimized.style.display = "none";
});

window.addEventListener("load", () => {
  setTimeout(() => {
    popup.style.display = "none";
    popupMinimized.style.display = "block";
  }, 5500);
});