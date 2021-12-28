# Please write a program which asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:

# in the order the items were added
# ordered from smallest to greatest
# The program exits when the user types in 0.

# Write your solution here
list = []
while True:
    item = int(input('New item: '))
    if item == 0:
        print('Bye!')
        break
    list.append(item)
    print(f'The list now: {list}')
    print(f'The list in order: {sorted(list)}')