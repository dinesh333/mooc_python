# Write your solution here
def longest_series_of_neighbours(list):
    longest_length = 1
    current_length = 1
    for i in range(len(list)-1):
        if list[i]+1 == list[i+1] or list[i]-1 == list[i+1]:
            current_length += 1
            if current_length > longest_length:
                longest_length = current_length
        else:
            current_length = 1
    return longest_length