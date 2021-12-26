# Write your solution here
def formatted(float_list):
    formatted_list = []
    for i in range(len(float_list)):
        formatted_list.append(f'{float_list[i]:.2f}')
    return formatted_list