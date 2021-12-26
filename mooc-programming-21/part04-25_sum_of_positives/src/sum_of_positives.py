# Write your solution here
def sum_of_positives(list):
    sum = 0
    for i in list:
        if i > 0:
            sum += i
    return sum