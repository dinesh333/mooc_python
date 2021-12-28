# The file matrix.txt contains a matrix in the format specified in the example below:

# Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.

# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. For example, calling row_sums when the matrix in the file is defined as

# the function should return the list [6, 9].

# Hint: you can also include other helper functions in your program. It is very worthwhile to spend a moment considering which functionalities are shared by the three functions you are asked to write. Notice that the three functions named above do not take any arguments, but any helper functions you write may take arguments. The file you are working with is always named matrix.txt.

# NB: If Visual Studio Code can't find the file and you have checked that there are no spelling errors, take a look at the instructions before this exercise.

# write your solution here

def list_total(nums):
    total = 0
    for n in nums:
        total += n
    return total

def list_max(nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max

def matrix_sum():
    with open("matrix.txt") as file:
        file_total = 0
        for line in file:
            line = line.replace('\n','')
            nums_str = line.split(',')
            nums = []
            for n in nums_str:
                nums.append(int(n))
            file_total += list_total(nums)
        return file_total

def matrix_max():
    with open("matrix.txt") as file:
        file_max = -100000000
        for line in file:
            line = line.replace('\n','')
            nums_str = line.split(',')
            nums = []
            for n in nums_str:
                nums.append(int(n))
            if list_max(nums) > file_max:
                file_max = list_max(nums)
        return file_max

def row_sums():
    with open("matrix.txt") as file:
        file_row_sums = []
        for line in file:
            line = line.replace('\n','')
            nums_str = line.split(',')
            nums = []
            for n in nums_str:
                nums.append(int(n))
            file_row_sums.append(list_total(nums))
        return file_row_sums

# print(matrix_sum())
# print(matrix_max())
# print(row_sums())