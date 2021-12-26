#Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.

# Write your solution here
def spruce(num):
    print('a spruce!')
    characters = 1
    spaces = num - 1
    counter = 1
    while counter <= num:
        print(' '*spaces + '*'*characters)
        spaces -= 1
        characters += 2
        counter += 1
    print(' '*(num-1) + '*')

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)