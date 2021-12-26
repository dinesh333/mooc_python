# Write your solution here
from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = list(range(lower, upper+1))
    print(numbers)
    numbers = sample(numbers, amount)
    return sorted(numbers)