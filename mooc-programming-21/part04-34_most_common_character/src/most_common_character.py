# Write your solution here

def most_common_character(str):
    most_common_char = None
    count_most_common_char = 0
    for char in str:
        if str.count(char) > count_most_common_char:
            count_most_common_char = str.count(char)
            most_common_char = char
    return most_common_char