# Write your solution here
def line(num, str):
    if str == "":
        print('*'*num)
    else:
        print(str[0]*num)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "abc")