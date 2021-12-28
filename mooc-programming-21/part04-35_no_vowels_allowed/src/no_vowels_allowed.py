# Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.

# You can assume the string will contain only characters from the lowercase English alphabet a...z.

# Write your solution here
def no_vowels(str):
    new_str = ''
    for i in str:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            new_str += i
    return new_str