# Please write a function named formatted, which takes a list of floating point numbers as its argument. The
#  function returns a new list, which contains each element of the original list in string format, rounded 
# to two decimal points. The order of the items in the list should remain unchanged.

# Hint: use f-strings to format the floating point numbers into suitable strings.

# Write your solution here
def formatted(float_list):
    formatted_list = []
    for i in range(len(float_list)):
        formatted_list.append(f'{float_list[i]:.2f}')
    return formatted_list