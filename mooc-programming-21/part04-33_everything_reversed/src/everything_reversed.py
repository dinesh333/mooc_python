# Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.


# Write your solution here
def everything_reversed(list):
    reversed_list = []
    i = len(list) - 1
    while i >= 0:
        word = list[i]
        reversed_list.append(word[::-1])
        i -= 1
    return reversed_list