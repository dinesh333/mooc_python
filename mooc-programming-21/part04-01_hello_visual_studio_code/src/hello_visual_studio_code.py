# Write your solution here
while True:
    editor = input('Editor: ')
    editor = editor.lower()
    if editor in ['word', 'notepad']:
        print('awful')
    elif editor == 'visual studio code':
        print('an excellent choice!')
        break
    else:
        print('not good')