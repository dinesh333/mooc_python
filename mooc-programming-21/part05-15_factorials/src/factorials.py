# Write your solution here

def factorials(n: int):
    dict = {}
    for num in range(1, n+1):
        result = 1
        for i in range(1, num+1):
            result *= i
        dict[num] = result
    return dict