# Write your solution here
def everything_reversed(list):
    reversed_list = []
    i = len(list) - 1
    while i >= 0:
        word = list[i]
        reversed_list.append(word[::-1])
        i -= 1
    return reversed_list