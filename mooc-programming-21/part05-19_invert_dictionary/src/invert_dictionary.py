# Write your solution here
def invert(dictionary: dict):
    dictionary_copy = {}

    for key, value in dictionary.items():
        dictionary_copy[key] = value

    dictionary.clear()

    for key, value in dictionary_copy.items():
        dictionary[value] = key