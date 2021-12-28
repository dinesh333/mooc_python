# Please write a function named palindromes, which takes a string argument and returns True if the string 
# is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.

# Please also write a main function which asks the user to type in words until they type in a palindrome:

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