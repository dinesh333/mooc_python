# Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each tuple, the first element is the name of a person, and the second element is their year of birth. The function should find the oldest person on the list and return their name.

# Write your solution here
def oldest_person(people: list):
    oldest_age = people[0][1]
    oldest_name = people[0][0]
    for person in people:
        if oldest_age > person[1]:
            oldest_age = person[1]
            oldest_name = person[0]
    return oldest_name