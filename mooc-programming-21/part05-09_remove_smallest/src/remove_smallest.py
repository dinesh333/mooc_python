# Please write a function named remove_smallest(numbers: list), which takes a list of integers as its argument.

# The functions should find and remove the smallest item in the list. You may assume there is a single smallest item in the list.

# The function should not have a return value - it should directly modify the list it receives as a parameter.

# Write your solution here

def remove_smallest(numbers: list):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    numbers.remove(smallest)