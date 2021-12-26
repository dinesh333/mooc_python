# Please write a program which first asks the user for the number of items to be added. Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out.

# Write your solution here
num_of_items = int(input('How many items: '))
items = []
i = 0
while i < num_of_items:
    num = int(input(f'Item {i+1}: '))
    items.append(num)
    i += 1
print(items)