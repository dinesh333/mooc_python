# Write your solution here

def remove_smallest(numbers: list):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    numbers.remove(smallest)