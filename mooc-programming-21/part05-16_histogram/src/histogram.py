# Write your solution here
def histogram(str):
    dict = {}
    for letter in str:
        if letter not in dict:
            dict[letter] = ''
        dict[letter] += '*'
    
    for key, value in dict.items():
        print(f'{key} {value}')