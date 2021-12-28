# Please write a function named read_input, which asks the user for input until the user types in an integer which falls within the bounds given as arguments to the function. The function should return the final valid integer value typed in by the user.

# An example of the function in action:

# Write your solution here
def read_input(message, low, high):
    while True:
        try:
            num = int(input(message))
            if num >= low and num <= high:
                return num
        except ValueError:
            pass

        print(f'You must type in an integer between {low} and {high}')