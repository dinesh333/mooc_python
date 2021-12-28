# Please write a function named anagrams, which takes two strings as arguments. The function returns True if the
#  strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.
# Write your solution here
def anagrams(first, second):
    return sorted(first) == sorted(second)