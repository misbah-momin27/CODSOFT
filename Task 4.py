movies = {
    '3 Idiots': ['comedy', 'drama'],
    'Zindagi Na Milegi Dobara': ['adventure', 'drama', 'comedy'],
    'Bahubali': ['action', 'fantasy', 'drama'],
    'Kabir Singh': ['romance', 'drama'],
    'Article 15': ['crime', 'drama', 'mystery'],
    'Tumbbad': ['horror', 'fantasy', 'thriller'],
    'Squid Game': ['sci-fi', 'adventure']
}
def calculate_overlap(user_input, movie_features):
    return len(set(movie_features) & set(user_input.split()))
def recommend_movie(user_input, movies_data):
    best_match = None
    max_overlap = 0

    for movie, features in movies_data.items():
        overlap = calculate_overlap(user_input, features)
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = movie
    return best_match

user_input = input("Enter your favourite genre: ")

#getting the recommended movies
recommended_movie = recommend_movie(user_input, movies)

if recommended_movie:
    print(f"Recommended movie for you is {recommended_movie}")
else:
    print("Oops!, no recommendations found.")

