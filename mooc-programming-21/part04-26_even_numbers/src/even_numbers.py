# Write your solution here
def even_numbers(list):
    even = []
    for i in list:
        if i%2 == 0:
            even.append(i)
    return even
