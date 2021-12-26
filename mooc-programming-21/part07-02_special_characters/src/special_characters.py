# Write your solution here
from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    first = ''
    second = ''
    third = ''
    for character in my_string:
        if character in ascii_letters:
            first += character
        elif character in punctuation:
            second += character
        else:
            third += character
    return (first, second, third)