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