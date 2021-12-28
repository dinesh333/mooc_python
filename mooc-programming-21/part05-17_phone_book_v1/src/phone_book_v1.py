# Please write a phone book application.
# Each name can be attached to a single number only. If a new entry with the same name is added, the number attached to the old entry is replaced with the new number.

# Write your solution here
phonebook = {}
while True:
    selection = int(input('command (1 search, 2 add, 3 quit): '))
    if selection == 1:
        name = input('name: ')
        if name in phonebook:
            print(phonebook[name])
        else:
            print('no number')
    elif selection == 2:
        name = input('name: ')
        number = input('number: ')
        phonebook[name] = number
        print('ok!')
    elif selection == 3:
        print('quitting...')
        break

