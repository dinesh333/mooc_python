# Write your solution here
def same_chars(str, first_index, second_index):
    if first_index >= len(str) or second_index >= len(str):
        return False
    if str[first_index] == str[second_index]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))