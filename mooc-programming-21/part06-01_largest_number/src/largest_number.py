# The file numbers.txt contains integer numbers, one number per line.

# Please write a function named largest, which reads the file and returns the largest number in the file.

# Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.

# write your solution here

def largest():
    numbers = []
    with open("numbers.txt") as new_file:
        for line in new_file:
            numbers.append(int(line))
    if len(numbers) > 0:
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        return largest