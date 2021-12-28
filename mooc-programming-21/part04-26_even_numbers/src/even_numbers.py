# Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.

# Write your solution here
def even_numbers(list):
    even = []
    for i in list:
        if i%2 == 0:
            even.append(i)
    return even
