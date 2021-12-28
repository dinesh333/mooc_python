# Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary. The keys of the dictionary should be the numbers between start_index and end_index inclusive

# The value mapped to each key should be the key times ten.

# Write your solution here
def times_ten(start_index: int, end_index: int):
    dict = {}
    for num in range(start_index, end_index+1):
        dict[num] = num*10
    return dict