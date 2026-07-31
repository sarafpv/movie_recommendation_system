import os
import pickle

from rapidfuzz import process
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================================
#                   LOAD PICKLE FILES
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

MODEL_DIR = os.path.join(BASE_DIR, "model")


with open(os.path.join(MODEL_DIR, "movies.pkl"), "rb") as file:
    movies = pickle.load(file)

with open(os.path.join(MODEL_DIR, "indices.pkl"), "rb") as file:
    indices = pickle.load(file)

with open(os.path.join(MODEL_DIR, "tfidf.pkl"), "rb") as file:
    tfidf = pickle.load(file)

with open(os.path.join(MODEL_DIR, "tfidf_matrix.pkl"), "rb") as file:
    tfidf_matrix = pickle.load(file)


print("Recommendation Engine Loaded Successfully")


# ==========================================================
#           FIND CLOSEST MOVIE TITLE
# ==========================================================

def find_movie(movie_name):

    movie_titles = movies["title"].tolist()

    result = process.extractOne(
        movie_name,
        movie_titles,
        score_cutoff=60
    )

    if result is None:
        return None

    return result[0]


# ==========================================================
#           RECOMMEND MOVIES
# ==========================================================

def recommend_movies(movie_name, n=5):

    movie_name = find_movie(movie_name)

    if movie_name is None:
        return []

    idx = indices[movie_name]

    similarity = cosine_similarity(
        tfidf_matrix[idx],
        tfidf_matrix
    ).flatten()

    movie_indices = similarity.argsort()[::-1][1:n + 1]

    recommendations = []

    for i in movie_indices:

        movie = movies.iloc[i]

        recommendations.append({

            "title": movie["title"],

            "overview": movie["overview"],

            "genres": movie["genres"],

            "tagline": movie["tagline"],

            "rating": movie["vote_average"],

            "popularity": movie["popularity"]

        })

    return recommendations


# ==========================================================
#           GET COMPLETE MOVIE
# ==========================================================

def get_movie(movie_name):

    movie_name = find_movie(movie_name)

    if movie_name is None:
        return None

    idx = indices[movie_name]

    return movies.iloc[idx]


# ==========================================================
#           CHECK MOVIE EXISTS
# ==========================================================

def movie_exists(movie_name):

    return find_movie(movie_name) is not None


# ==========================================================
#           TOTAL MOVIES
# ==========================================================

def total_movies():

    return len(movies)