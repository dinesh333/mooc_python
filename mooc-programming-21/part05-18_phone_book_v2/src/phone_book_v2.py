# Please write an improved version of the phone book application. Each entry should now accommodate multiple phone numbers. The application should work otherwise exactly as above, but this time all numbers attached to a name should be printed.

# Write your solution here
phonebook = {}
while True:
    selection = int(input('command (1 search, 2 add, 3 quit): '))
    if selection == 1:
        name = input('name: ')
        if name in phonebook:
            for phone in phonebook[name]:
                print(phone)
        else:
            print('no number')
    elif selection == 2:
        name = input('name: ')
        number = input('number: ')
        if name not in phonebook:
            phonebook[name] = []
        phonebook[name].append(number)
        print('ok!')
    elif selection == 3:
        print('quitting...')
        break