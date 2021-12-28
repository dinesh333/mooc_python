# Please write a program which asks the user to type in some text. Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them. Please see the two examples below:

# The case of the letters should be irrelevant to the functioning of your program.

# The exercise template includes the file wordlist.txt, which contains all the words the spell checker should accept as correct.

# write your solution here
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
    for text in text_list:
        if text.lower() in all_words:
            output += text
        else:
            output += '*' + text + '*'
        output += ' '
    print(output)

main()