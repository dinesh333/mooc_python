# Write your solution here
def longest(strings: list):
    longest = strings[0]
    for i in strings:
        if len(i) > len(longest):
            longest = i
    return longest