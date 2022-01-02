# Please write a function named sort_by_ratings(items: list) which takes a list of dictionaries as its argument. The structure of the dictionaries is identical to the previous exercise. This function should sort the dictionaries in descending order based on the shows' ratings. The function should not change the original list, but return a new list instead.

# shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

# print("Rating according to IMDB")
# for show in sort_by_ratings(shows):
#     print(f"{show['name']}  {show['rating']}")
# Sample output
# Rating according to IMDB
# Friends 8.9
# Simpsons 8.7
# Dexter 8.6

def sort_by_ratings(items: list):
    def order_by_ratings(item: dict):
        return item['rating']
    return sorted(items, key=order_by_ratings, reverse=True)