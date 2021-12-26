# Write your solution here
def double_items(numbers: list) -> list:
    doubled = []
    for i in range(len(numbers)):
        doubled.append(numbers[i]*2)
    return doubled

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)