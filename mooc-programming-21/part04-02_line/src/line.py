# Please write a function named line, which takes two arguments: an integer and a string. The 
# function prints out a line of text, the length of which is specified by the first argument. 
# The character used to draw the line should be the first character in the second argument. 
# If the second argument is an empty string, the line should consist of stars.

# Write your solution here
def line(num, str):
    if str == "":
        print('*'*num)
    else:
        print(str[0]*num)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "abc")