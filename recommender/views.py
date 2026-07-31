from django.shortcuts import render, redirect

from .utils.recommender import recommend_movies


# ==========================================================
#                       HOME PAGE
# ==========================================================

def home(request):

    return render(request, "home.html")


# ==========================================================
#               RECOMMENDATION PAGE
# ==========================================================

def recommend(request):

    # Only allow POST requests
    if request.method != "POST":
        return redirect("home")

    # Get movie name from form
    movie_name = request.POST.get("movie", "").strip()

    if not movie_name:
        return redirect("home")

    # Get recommendations from ML model
    recommendations = recommend_movies(movie_name)

    # Movie not found
    if not recommendations:

        return render(

            request,

            "recommendations.html",

            {

                "searched_movie": movie_name,

                "recommendations": [],

                "error": "Movie Not Found"

            }

        )

    # Send recommendations to HTML
    context = {

        "searched_movie": movie_name,

        "recommendations": recommendations

    }

    return render(

        request,

        "recommendations.html",

        context

    )