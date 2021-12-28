# In this exercise we are handling tuples just like the ones described in the previous exercise.

# Please write a function named older_people(people: list, year: int), which selects all those people on the list who were born before the year given as an argument. The function should return the names of these people in a new list.

# Write your solution here
def older_people(people: list, year: int):
    younger = []
    for person in people:
        if person[1] < year:
            younger.append(person[0])
    return younger