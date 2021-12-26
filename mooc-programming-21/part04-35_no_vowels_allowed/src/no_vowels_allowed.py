# Write your solution here
def no_vowels(str):
    new_str = ''
    for i in str:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            new_str += i
    return new_str