// ==========================================================
//                  HOME.JS
// ==========================================================

document.addEventListener("DOMContentLoaded", () => {

    console.log("Home Page Loaded");

    initializeSearch();

});


// ==========================================================
//              SEARCH FORM VALIDATION
// ==========================================================

function initializeSearch() {

    const form = document.querySelector(".search-form");

    if (!form) return;

    form.addEventListener("submit", function (event) {

        const input = form.querySelector("input");

        const movieName = input.value.trim();

        if (movieName === "") {

            event.preventDefault();

            alert("Please enter a movie name.");

            input.focus();

            return;

        }

        console.log("Searching for:", movieName);

    });

}


// ==========================================================
//          FUTURE FEATURES
// ==========================================================

// Search Autocomplete

// Voice Search

// Loading Spinner

// Popular Search Suggestions

// Search History