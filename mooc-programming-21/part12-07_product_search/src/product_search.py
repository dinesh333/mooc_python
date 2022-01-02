# This exercise deals with products which are stored in tuples. The examples all assume a variable named products, which is assigned the following value:

# products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22), ("kale", 0.99, 1)]
# Each tuple contains three items: name, price and amount.

# Please write a function named search(products: list, criterion: callable). The second argument to the function is a function itself, and it should be able to process a tuple as defined above, and return a Boolean value. The search function should return a new list containing those tuples from the original which fulfil the criterion.

# If we wanted to include only products whose price was under 4 euros, we could use the following criterion function:

# def price_under_4_euros(product):
#     return product[1] < 4
# The function returns True if the second item in the tuple is less than four in value.

# An example of the search function in use:

# for product in search(products, price_under_4_euros):
#     print(product)
# Sample output
# ('apple', 3.95, 3)
# ('kale', 0.99, 1)

# The criterion function can also be a lambda function. If we wanted to search for only those products whose amount was at least 11, we could write the following:

# for product in search(products, lambda t: t[2]>10):
#     print(product)
# Sample output
# ('banana', 5.95, 12)
# ('watermelon', 4.95, 22)

def search(products: list, criterion: callable):
    return [product for product in products if criterion(product)]