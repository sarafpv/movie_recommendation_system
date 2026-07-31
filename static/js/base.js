// ==========================================================
//                  BASE.JS
//      Common JavaScript for the Entire Website
// ==========================================================

document.addEventListener("DOMContentLoaded", () => {

    console.log("Movie Recommendation System Loaded");

    highlightCurrentPage();

    updateFooterYear();

});


// ==========================================================
//          Highlight Current Navigation Link
// ==========================================================

function highlightCurrentPage() {

    const currentPath = window.location.pathname;

    const navLinks = document.querySelectorAll(".nav-links a");

    navLinks.forEach(link => {

        if (link.getAttribute("href") === currentPath) {

            link.classList.add("active");

        }

    });

}


// ==========================================================
//              Update Footer Year Automatically
// ==========================================================

function updateFooterYear() {

    const year = document.getElementById("current-year");

    if (year) {

        year.textContent = new Date().getFullYear();

    }

}