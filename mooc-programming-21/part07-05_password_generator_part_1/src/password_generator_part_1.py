# Please write a function which creates passwords of a desired length, consisting of lowercase characters a to z.

# An example of how the function should work:

# for i in range(10):
#     print(generate_password(8))
# Sample output
# lttehepy
# olsxttjl
# cbjncrzo
# dwxqjdgu
# gpfdcecs
# jabyvgar
# xnbbonbl
# ktmsjyww
# ejhprmel
# rjkoacib

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