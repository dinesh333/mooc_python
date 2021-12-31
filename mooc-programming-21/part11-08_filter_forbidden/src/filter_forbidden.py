# Please write a function named filter_forbidden(string: str, forbidden: str) which takes two strings as its arguments. The function should return a new version of the first string. It should not contain any characters from the second string.

# The function should be implemented using list comprehensions. The maximum length of the function is three lines of code, including the header line beginning with the def keyword.

# Please have a look at the example below.

# sentence = "Once! upon, a time: there was a python!??!?!"
# filtered = filter_forbidden(sentence, "!?:,.")
# print(filtered)
# Sample output
# Once upon a time there was a python

def filter_forbidden(string: str, forbidden: str):
    filtered = [character for character in string if character not in forbidden]
    return ''.join(filtered)