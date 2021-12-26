# Write your solution here
def distinct_numbers(list):
    distinct_list = []
    for i in list:
        if i not in distinct_list:
            distinct_list.append(i)
    distinct_list.sort()
    return distinct_list