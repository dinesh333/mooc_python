# Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

# Copy here code of line function from previous exercise and use it in your solution
def line(num, str):
    if str == "":
        print('*'*num)
    else:
        print(str[0]*num)

def shape(tri_h, tri_c, squ_h, squ_c):
    i = 0
    while i < tri_h:
        line(i+1, tri_c)
        i += 1
    j = 0
    while j < squ_h:
        line(tri_h, squ_c)
        j += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")