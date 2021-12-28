# Please write a function named triangle, which draws a triangle of hashes, and takes one argument. The triangle should be as tall and as wide as the value of the argument.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

# Copy here code of line function from previous exercise
def line(num, str):
    if str == "":
        print('*'*num)
    else:
        print(str[0]*num)

def triangle(size):
    # You should call function line here with proper parameters
    i = 0
    while i < size:
        line(i+1, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
