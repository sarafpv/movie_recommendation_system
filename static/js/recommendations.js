// ==========================================================
//              RECOMMENDATIONS.JS
// ==========================================================

document.addEventListener("DOMContentLoaded", () => {

    console.log("Recommendations Page Loaded");

    initializeMovieCards();

});


// ==========================================================
//          MOVIE CARD HOVER EFFECT
// ==========================================================

function initializeMovieCards() {

    const movieCards = document.querySelectorAll(".movie-card");

    movieCards.forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.cursor = "pointer";

        });

    });

}


// ==========================================================
//          FUTURE FEATURES
// ==========================================================

// View Details Animation

// Wishlist Button

// Like Button

// Sort Movies

// Filter by Genre

// Infinite Scroll

// Loading Animation