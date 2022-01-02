# The exercise template contains the class definition for a ClimbingRoute. It works as follows:

# route1 = ClimbingRoute("Edge", 38, "6A+")
# route2 = ClimbingRoute("Smooth operator", 9, "7A")
# route3 = ClimbingRoute("Synchro", 14, "8C+")


# print(route1)
# print(route2)
# print(route3.name, route3.length, route3.grade)
# Sample output
# Edge, length 38 metres, grade 6A+
# Smooth operator, length 9 metres, grade 7A
# Synchro 14 8B+

# Sort by length
# Please write a function named sort_by_length(routes: list) which returns a new list of routes, sorted by length from longest to shortest.

# The function should work as follows:

# r1 = ClimbingRoute("Edge", 38, "6A+")
# r2 = ClimbingRoute("Smooth operator", 11, "7A")
# r3 = ClimbingRoute("Synchro", 14, "8C+")
# r4 = ClimbingRoute("Small steps", 12, "6A+")

# routes = [r1, r2, r3, r4]

# for route in sort_by_length(routes):
#     print(route)
# Sample output
# Edge, length 38 metres, grade 6A+
# Synchro, length 14 metres, grade 8C+
# Small steps, length 12 metres, grade 6A+
# Smooth operator, length 9 metres, grade 7A

# Sort by difficulty
# Please write a function named sort_by_difficulty(routes: list) which returns a new list of routes, sorted by difficulty, i.e. grade, from hardest to easiest. For routes with the same grade, the longer one is more difficult. The scale of climbing route grades is 4, 4+, 5, 5+, 6A, 6A+, ..., which in practice works out as the alphabetical order for strings.

# The function should work as follows:

# r1 = ClimbingRoute("Edge", 38, "6A+")
# r2 = ClimbingRoute("Smooth operator", 11, "7A")
# r3 = ClimbingRoute("Synchro", 14, "8C+")
# r4 = ClimbingRoute("Small steps", 12, "6A+")

# routes = [r1, r2, r3, r4]
# for route in sort_by_difficulty(routes):
#     print(route)
# Sample output
# Synchro, length 14 metres, grade 8C+
# Smooth operator, length 11 metres, grade 7A
# Edge, length 38 metres, grade 6A+
# Small steps, length 12 metres, grade 6A+

# Hint: if the order is based on a list or a tuple, by default Python sorts the items first based on the first item, next based on the second item, and so forth:

# my_list = [("a", 4),("a", 2),("b", 30), ("b", 0) ]
# print(sorted(my_list))
# Sample output
# [('a', 2), ('a', 4), ('b', 0), ('b', 30)]

class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

def order_by_length(route: ClimbingRoute):
    return route.length

def sort_by_length(routes: list):
    return sorted(routes, key=order_by_length, reverse=True)

def sort_by_difficulty(routes: list):
    def order_by_difficulty(route: ClimbingRoute):
        return [route.grade, route.length]
    return sorted(routes, key=order_by_difficulty, reverse=True)

if __name__ == '__main__':
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")

    routes = [r1, r2, r3, r4]
    for route in sort_by_difficulty(routes):
        print(route)    