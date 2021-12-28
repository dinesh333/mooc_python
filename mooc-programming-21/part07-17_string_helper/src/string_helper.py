# Please write a module named string_helper, which contains the following functions:

# The function change_case(orig_string: str) creates and returns a new version of the parameter string. The lowercase letters in the original should be uppercase, and uppercase letters should be lowercase.

# The function split_in_half(orig_string: str splits the parameter string in half, and returns the results in a tuple. If the original has an odd number of characters, the first half should be shorter.

# The function remove_special_characters(orig_string: str) returns a new version of the parameter string, with all special characters removed. Only lowercase and uppercase letters, numbers and spaces are allowed in the returned string.


from string import ascii_lowercase, ascii_uppercase, digits

def change_case(orig_string: str):
    new_string = ''
    for letter in orig_string:
        if letter in ascii_uppercase:
            new_string += letter.lower()
        elif letter in ascii_lowercase:
            new_string += letter.upper()
        else:
            new_string += letter
    return new_string
    
def split_in_half(orig_string: str):
    length = len(orig_string)
    midpoint = length//2
    first = orig_string[:midpoint]
    last = orig_string[midpoint:]
    return (first, last)

def remove_special_characters(orig_string: str):
    new_string = ''
    for character in orig_string:
        if character == ' ' or character in ascii_lowercase or character in ascii_uppercase or character in digits:
            new_string += character
    return new_string