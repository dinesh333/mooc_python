#Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at each index in the two original lists. You may assume both lists have the same number of items.

# Write your solution here
def list_sum(list1, list2):
    list_add = []
    for i in range(len(list1)):
        add = list1[i] + list2[i]
        list_add.append(add)
    return list_add