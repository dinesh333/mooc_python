# Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary. The number is the key, and the factorial of that number is the value mapped to it.

# A reminder: the factorial of the number n is written n! and is calculated by multiplying the number by each integer smaller than itself. For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.

# Write your solution here

def factorials(n: int):
    dict = {}
    for num in range(1, n+1):
        result = 1
        for i in range(1, num+1):
            result *= i
        dict[num] = result
    return dict