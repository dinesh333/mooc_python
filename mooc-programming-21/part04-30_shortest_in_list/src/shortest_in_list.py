# Write your solution here
def shortest(list):
    shortest = list[0]
    for word in list:
        if len(word) < len(shortest):
            shortest = word
    return shortest