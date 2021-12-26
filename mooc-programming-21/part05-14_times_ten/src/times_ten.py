# Write your solution here
def times_ten(start_index: int, end_index: int):
    dict = {}
    for num in range(start_index, end_index+1):
        dict[num] = num*10
    return dict