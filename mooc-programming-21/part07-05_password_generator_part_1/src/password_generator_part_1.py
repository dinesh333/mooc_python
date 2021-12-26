# Write your solution here
import string
from random import randint

def generate_password(length: int) -> string:
    lowercase_chars = list(string.ascii_lowercase)
    password = ''
    for i in range(length):
        random_index = randint(0, len(lowercase_chars)-1)
        password += lowercase_chars[random_index]
    return password