# Write your solution here
def find_movies(database: list, search_term: str):
    movies = []
    
    for movie in database:
        if search_term.lower() in movie['name'].lower():
            movies.append(movie)
    
    return movies