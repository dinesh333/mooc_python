# Please create a class named ListHelper which contains the following two class methods.

# greatest_frequency(my_list: list) returns the most common item on the list
# doubles(my_list: list) returns the number of unique items which appear at least twice on the list
# It should be possible to use these methods without creating an instance of the class. An example of how the methods could be used:

# numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
# print(ListHelper.greatest_frequency(numbers))
# print(ListHelper.doubles(numbers))
# Sample output
# 5
# 3

class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        greatest_count = 1
        greatest_count_element = my_list[0]
        for element in my_list:
            if my_list.count(element) > greatest_count:
                greatest_count = my_list.count(element)
                greatest_count_element = element
        return greatest_count_element
    
    @classmethod
    def doubles(cls, my_list: list):
        my_set = set(my_list)
        count_at_least_double = 0
        for element in my_set:
            if my_list.count(element) >= 2:
                count_at_least_double += 1
        return count_at_least_double