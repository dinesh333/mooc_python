# Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list.

# Write your solution here
def longest(strings: list):
    longest = strings[0]
    for i in strings:
        if len(i) > len(longest):
            longest = i
    return longest