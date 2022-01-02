# Please write a generator function named even_numbers(beginning: int, maximum: int) which takes two integers as its arguments. The function should produce even numbers starting from beginning and ending with, at most, maximum.

# Two examples of how the function works:

# numbers = even_numbers(2, 10)
# for number in numbers:
#     print(number)
# Sample output
# 2
# 4
# 6
# 8
# 10

# numbers = even_numbers(11, 21)
# for number in numbers:
#     print(number)
# Sample output
# 12
# 14
# 16
# 18
# 20

def even_numbers(beginning: int, maximum: int):
    while beginning <= maximum:
        if beginning%2 == 0:
            yield beginning
        beginning += 1

if __name__ == '__main__':
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)