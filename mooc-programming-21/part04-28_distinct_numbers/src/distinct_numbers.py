# Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns 
# a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.
# Write your solution here
def distinct_numbers(list):
    distinct_list = []
    for i in list:
        if i not in distinct_list:
            distinct_list.append(i)
    distinct_list.sort()
    return distinct_list