# Please write an improved version of your password generator. The function now takes three arguments:

# If the second argument is True, the generated password should also contain one or more numbers.
# If the third argument is True, the generated password should also contain one or more of these special characters: !?=+-()#.
# Despite these two additional arguments, the password should always contain at least one lowercase alphabet. You may assume the function will only be called with combinations of arguments that are possible to formulate into passwords following these rules. That is, the arguments will not specify e.g. a password of length 2 which contains both a number and a special characters, for then there would not be space for the mandatory lowercase letter.

# An example of how the function should work:

# for i in range(10):
#     print(generate_strong_password(8, True, True))
# Sample output
# 2?0n+u31
# u=m4nl94
# n#=i6r#(
# da9?zvm?
# 7h)!)g?!
# a=59x2n5
# (jr6n3b5
# 9n(4i+2!
# 32+qba#=
# n?b0a7ey

# Write your solution here
from string import ascii_lowercase
from random import randint, shuffle

def generate_strong_password(length: int, contain_numbers: bool, contain_specialchars: bool) -> string:
    how_many_lowercase_chars = 1
    how_many_numbers = 0
    how_many_specialchars = 0

    if contain_numbers == True and contain_specialchars == True:
        how_many_numbers = randint(1, length-2)
        max_specialchars = length - 1 - how_many_numbers
        how_many_specialchars = randint(1, max_specialchars)
        how_many_lowercase_chars = length - how_many_numbers - how_many_specialchars
    elif contain_numbers == True:
        how_many_numbers = randint(1, length-1)
        how_many_lowercase_chars += (length - 1 - how_many_numbers)
    elif contain_specialchars == True:
        how_many_specialchars = randint(1, length-1)
        how_many_lowercase_chars += (length - 1 - how_many_specialchars)
    else:
        how_many_lowercase_chars = length

    password = []
    special_chars = list('!?=+-()#')
    lowercase_chars = list(ascii_lowercase)

    for i in range(how_many_numbers):
        password.append(str(randint(0, 9)))
    
    for i in range(how_many_specialchars):
        random_index = randint(0, len(special_chars)-1)
        password.append(special_chars[random_index])
    
    for i in range(how_many_lowercase_chars):
        random_index = randint(0, len(lowercase_chars)-1)
        password.append(lowercase_chars[random_index])
    
    shuffle(password)

    return ''.join(password)