# In this exercise you will write an improved version of the Spell checker from the previous part.

# Just like in the previous version, the program should ask the user to type in a line of text. Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them. Additionally, the program should print out a list of suggestions for the misspelled words.

# Please have a look at the following two examples.

# Sample output
# write text: We use ptython to make a spell checker

# We use *ptython* to make a spell checker
# suggestions:
# ptython: python, pythons, typhon
# Sample output
# write text: this is acually a good and usefull program

# this is *acually* a good and *usefull* program
# suggestions:
# acually: actually, tactually, factually
# usefull: usefully, useful, museful
# The suggestions should be determined with the function get_close_matches from the Python standard library module difflib.

# Write your solution here
from difflib import get_close_matches

def put_file_lines_in_list(file_name):
    with open(file_name) as file:
        file_as_list = []
        for line in file:
            line = line.replace('\n', '')
            file_as_list.append(line)
    return file_as_list

def main():
    text = input('Write text: ')
    text_list = text.split(' ')
    all_words = put_file_lines_in_list('wordlist.txt')
    for index, word in enumerate(all_words):
        all_words[index] = word.lower()
    output = ''
    misspelled_words = []
    for text in text_list:
        if text.lower() in all_words:
            output += text
        else:
            output += '*' + text + '*'
            misspelled_words.append(text)
        output += ' '
    print(output)
    
    print('suggestions:')
    for word in misspelled_words:
        close_matches = get_close_matches(word, all_words)
        close_matches = ', '.join(close_matches)
        print(f'{word}: {close_matches}')
        
main()