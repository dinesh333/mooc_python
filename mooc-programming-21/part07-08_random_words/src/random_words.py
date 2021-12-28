# The exercise template contains the file words.txt, which contains some English language words, one on each line.

# Please write a function named words(n: int, beginning: str), which returns a list containing n random words from the words.txt file. All words should begin with the string specified by the second argument.

# The same word should not appear twice in the list. If there are not enough words beginning with the specified string, the function should raise a ValueError exception.

# An example of the function in action:

# word_list = words(3, "ca")
# for word in word_list:
#     print(word)
# Sample output
# cat
# car
# carbon


# Write your solution here
from random import sample

def words(n: int, beginning: str) -> list:
    found_words = []
    with open('words.txt') as word_file:
        for line in word_file:
            word = line.replace('\n', '')
            if word.startswith(beginning):
                found_words.append(word)

    if len(found_words) < n:
        raise ValueError(f'Could not find {n} words that start with {beginning}. Only found {len(found_words)} words.')
    
    return sample(found_words, n)