# The exercise template contains the function balanced_brackets which takes a string as its argument. It checks if the round brackets, or parentheses, within the string are balanced. That is, for each opening bracket ( there should be a closing bracket ), and all pairs of brackets should be matched in order, i.e. the bracket pairs must not be crossed.

# def balanced_brackets(my_string: str):
#     if len(my_string) == 0:
#         return True
#     if not (my_string[0] == '(' and my_string[-1] == ')'):
#         return False

#     # remove first and last character
#     return balanced_brackets(my_string[1:-1])

# ok = balanced_brackets("(((())))")
# print(ok)

# # there is one closing bracket too many, so this produces False
# ok = balanced_brackets("()())")
# print(ok)

# # this one starts with a closing bracket, False again
# ok = balanced_brackets(")()")
# print(ok)

# # this produces False because the function only handles entirely nested brackets
# ok = balanced_brackets("()(())")
# print(ok)
# Sample output
# True
# False
# False
# False

# Please expand the function so that it also works with square brackets []. The function should also ignore all characters which are not brackets () or []. The different types of brackets must be matched correctly in order.

# Please have a look at the examples below::

# ok = balanced_brackets("([([])])")
# print(ok)

# ok = balanced_brackets("(python version [3.7]) please use this one!")
# print(ok)

# # this is no good, the closing bracket doesn't match
# ok = balanced_brackets("(()]")
# print(ok)

# # different types of brackets are mismatched
# ok = balanced_brackets("([bad egg)]")
# print(ok)
# NB: the function only needs to handle entirely nested brackets. The string (x + 1)(y + 1) should produce False as the brackets are not nested within each other.

# Sample output
# True
# True
# False
# False

# def balanced_brackets(my_string: str):
#     if len(my_string) == 0:
#         return True
#     if not (my_string[0] == '(' and my_string[-1] == ')'):
#         return False

#     # remove first and last character
#     return balanced_brackets(my_string[1:-1])

def balanced_brackets(my_string: str):
    my_string = ''.join([character for character in my_string if character in '()[]'])

    if len(my_string) == 0:
        return True

    if not (my_string[0] == '(' and my_string[-1] == ')') and not (my_string[0] == '[' and my_string[-1] == ']'):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])