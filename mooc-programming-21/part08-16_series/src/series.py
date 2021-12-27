# Part 1: A class named Series
# Please write a class named Series with the following functionality:
# The constructor should take the title, the number of seasons and a list of 
# genres for the series as its arguments.

# Part 2: Adding reviews
# Please implement the method rate(rating: int) which lets you add a rating between 0 and 5 
# to any series object. You will also need to adjust the __str__ method so that in case there 
# are ratings, the method prints out the number of ratings added, and their average rounded to 
# one decimal point.

# Part 3: Searching for series
# Please implement these two functions which allow you to search through a list of 
# series: minimum_grade(rating: float, series_list: list) and includes_genre(genre: str, series_list: list).

class Series:
    def __init__(self, title:str, seasons:int, genres:list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
    
    def __str__(self):
        to_print = ''
        to_print += f'{self.title} ({self.seasons} seasons)\n'
        genres_str = ', '.join(self.genres)
        to_print += f'genres: {genres_str}\n'
        if len(self.ratings) > 0:
            to_print += f'{len(self.ratings)} ratings, average {self.get_avg_rating()} points'
        else:
            to_print += 'no ratings'
        return to_print

    def get_avg_rating(self):
        if len(self.ratings) > 0:
            avg_ratings = sum(self.ratings)/len(self.ratings)
            return round(avg_ratings, 1)
        else:
            return -1

    def rate(self, rating: int):
        self.ratings.append(rating)

def minimum_grade(grade:float, series_list:list):
    found = []
    for series in series_list:
        if series.get_avg_rating() > grade:
            found.append(series)
    return found

def includes_genre(genre: str, series_list: list):
    found = []
    for series in series_list:
        for ser_genre in series.genres:
            if ser_genre == genre:
                found.append(series)
                break
    return found