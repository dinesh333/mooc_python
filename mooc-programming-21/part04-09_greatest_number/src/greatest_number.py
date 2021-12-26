# Write your solution here
def greatest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
    else:
        return None

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(3, 5, 7)
    print(greatest)