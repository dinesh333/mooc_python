# Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.


# Write your solution here
def sum_of_positives(list):
    sum = 0
    for i in list:
        if i > 0:
            sum += i
    return sum