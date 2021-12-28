# In this exercise you are asked to create a program for working with numbers, similarly to the exercise completed at the end of part 2 in the Introduction to Programming course. This time you will define a class for the purpose.

# Part 1: Count the numbers
# Please write a class named NumberStats with the following methods:

# the method add_number adds a new number to the statistical record
# the method count_numbers returns the count of how many numbers have been added
# At this point there is no need to store the numbers themselves in any data structure. It is enough to simply remember how many have been added. The add_number method does take an argument, but there is no need to process the actual value in any way just yet.

# The exercise template contains the following skeleton for the class definition:
# class  NumberStats:
#     def __init__(self):
#         self.numbers = 0

#     def add_number(self, number:int):
#         pass

#     def count_numbers(self):
#         pass
# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())
# Sample output
# Numbers added: 4

# Part 2: The sum and the mean
# Please add the following methods to your class definition:

# the method get_sum should return the sum of the numbers added (if no numbers have been added, the method should return 0)
# the method average should return the mean of the numbers added (if no numbers have been added, the method should return 0)
# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())
# print("Sum of numbers:", stats.get_sum())
# print("Mean of numbers:", stats.average())
# Sample output
# Numbers added: 4
# Sum of numbers: 11
# Mean of numbers: 2.75

# Part 3: User input
# Please write a main program which keeps asking the user for integer numbers until the user types in -1. The program should then print out the sum and the mean of the numbers typed in.

# Your program should use a NumberStats object to keep a record of the numbers added.

# NB: you do not need to change the NumberStats class in this part of the exercise, provided it passed the tests for the previous part of the exercise. Use an instance of the class to complete this part.

# NB2: your main program should not be contained in a if __name__ == "__main__" block, or the tests will not work.

# Sample output
# Please type in integer numbers:
# 4
# 2
# 5
# 2
# -1
# Sum of numbers: 13
# Mean of numbers: 4.5

# Part 4: Multiple sums
# Please add to your main program so that it also counts separately the sum of the even and the odd numbers added.

# NB: do not change your NumberStats class definition in this part of exercise, either. Instead, define three NumberStats objects. One of them should keep track of all the numbers, another should track the even numbers, and the third should track the odd numbers typed in.

# NB2: your main program should not be contained in a if __name__ == "__main__" block, or the tests will not work.

# Please have look at this example of how your main function should work:

# Sample output
# Please type in integer numbers:
# 4
# 2
# 5
# 2
# -1
# Sum of numbers: 13
# Mean of numbers: 3.25
# Sum of even numbers: 8
# Sum of odd numbers: 5


# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers) if len(self.numbers) > 0 else 0

    def average(self):
        return sum(self.numbers)/len(self.numbers) if len(self.numbers) > 0 else 0

print('Please type in integer numbers:')
stats = NumberStats()
evens = NumberStats()
odds = NumberStats()
while True:
    number = int(input(''))
    if number == -1:
        break
    stats.add_number(number)
    evens.add_number(number) if number%2==0 else odds.add_number(number)

print(f'Sum of numbers: {stats.get_sum()}')
print(f'Mean of numbers: {stats.average()}')
print(f'Sum of even numbers: {evens.get_sum()}')
print(f'Sum of odd numbers: {odds.get_sum()}')