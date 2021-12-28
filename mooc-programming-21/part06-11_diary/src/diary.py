# Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. When the program is executed, it should first read any entries already in the file.

# NB: the automatic tests for this exercise will change the contents of the file. If you want to keep its contents, first make a copy of the file under a different name.

# Write your solution here
def read_file(file_name):
    with open(file_name) as diary:
        print('Entries:')
        for line in diary:
            print(line.replace('\n', ''))
        diary.close()

def update_file(file_name, entry):
    with open(file_name, 'a') as diary:
        diary.write(entry + '\n')
        diary.close()

while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    choice = int(input('Function: '))
    if choice == 1:
        entry = input('Diary entry: ')
        update_file('diary.txt', entry)
        print('Diary saved')
    elif choice == 2:
        read_file('diary.txt')
    elif choice == 0:
        print('Bye now!')
        break