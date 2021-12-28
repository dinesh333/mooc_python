#Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.

# Write your solution here
list = []
while True:
    word = input('Word: ')
    if word in list:
        break
    else:
        list.append(word)
print(f'You typed in {len(list)} different words')