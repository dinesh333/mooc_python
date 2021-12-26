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

