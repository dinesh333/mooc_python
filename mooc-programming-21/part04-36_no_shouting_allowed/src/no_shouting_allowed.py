# The Python string method isupper() returns True if a string consists of only uppercase characters.


# Write your solution here
def no_shouting(list_str):
    new_lst = []
    for str in list_str:
        if not str.isupper():
            new_lst.append(str)
    return new_lst