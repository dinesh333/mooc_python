# Write your solution here
def oldest_person(people: list):
    oldest_age = people[0][1]
    oldest_name = people[0][0]
    for person in people:
        if oldest_age > person[1]:
            oldest_age = person[1]
            oldest_name = person[0]
    return oldest_name