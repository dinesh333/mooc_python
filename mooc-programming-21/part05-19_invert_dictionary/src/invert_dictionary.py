# Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. The dictionary should be inverted in place so that values become keys and keys become values.


# Write your solution here
def invert(dictionary: dict):
    dictionary_copy = {}

    for key, value in dictionary.items():
        dictionary_copy[key] = value

    dictionary.clear()

    for key, value in dictionary_copy.items():
        dictionary[value] = key