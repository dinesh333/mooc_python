# Write your solution here
def palindromes(string):
    return string == string[::-1]


while True:
    word = input('Please type in a palindrome: ')
    if(palindromes(word)):
        print(f'{word} is a palindrome!')
        break
    else:
        print("that wasn't a palindrome")