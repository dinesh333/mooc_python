# Please write a program which asks the user to type in a string. The program then prints each input character on a separate line. After each character there should be a star (*) printed on its own line.
# Write your solution here
str = input('Please type in a string: ')
for char in str:
    print(char)
    print('*')