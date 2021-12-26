# Write your solution here
def older_people(people: list, year: int):
    younger = []
    for person in people:
        if person[1] < year:
            younger.append(person[0])
    return younger