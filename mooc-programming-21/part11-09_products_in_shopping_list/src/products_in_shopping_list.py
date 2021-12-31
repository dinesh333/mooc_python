# In part 10 you created an iterable shopping list, and we just learnt that an object created from an iterable class can be used with list comprehensions. The exercise template contains a stripped down version of the ShoppingList with just enough functionality to fulfil the requirements of this exercise.

# Please write a function named products(shopping_list, amount: int) which takes a ShoppingList object and an integer value as its arguments. The function returns a list of product names. The list should include only the products with at least the number of items specified by the amount parameter.

# The function should be implemented using list comprehensions. The maximum length of the function is two lines of code, including the header line beginning with the def keyword. The ShoppingList class definition should not be modified.

# The function should work as follows:

# my_list = ShoppingList()
# my_list.add("bananas", 10)
# my_list.add("apples", 5)
# my_list.add("alcohol free beer", 24)
# my_list.add("pineapple", 1)

# print("the shopping list contains at least 8 of the following items:")
# for product in products(my_list, 8):
#     print(product)
# Sample output
# the shopping list contains at least 8 of the following items:
# bananas
# alcohol free beer

# WRITE YOUR SOLUTION HERE:
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.products):
            product = self.products[self.n]
            self.n += 1
            return product
        else:
            raise StopIteration

def products_in_shopping_list(shopping_list: ShoppingList, amount: int):
    return [product[0] for product in shopping_list if product[1]>=amount]