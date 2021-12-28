# Please write a function named histogram, which takes a string as its argument. The function should print out a histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented by a star on the specific line for that letter.

# Write your solution here
def histogram(str):
    dict = {}
    for letter in str:
        if letter not in dict:
            dict[letter] = ''
        dict[letter] += '*'
    
    for key, value in dict.items():
        print(f'{key} {value}')