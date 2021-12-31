# Please write a function named lengths(strings: list) which takes a list of strings as its argument. The function should return a dictionary with the strings in the list as the keys and their lengths as the values.

# The function should be implemented with a dictionary comprehension. The maximum length of the function is two lines of code, including the header line beginning with the def keyword.

# The function should work as follows:

# word_list = ["once", "upon" , "a", "time", "in"]

# word_lengths = lengths(word_list)
# print(word_lengths)
# Sample output
# {'once': 4, 'upon': 4, 'a': 1, 'time': 4, 'in': 2}

def lengths(strings: list):
    return {word: len(word) for word in strings}