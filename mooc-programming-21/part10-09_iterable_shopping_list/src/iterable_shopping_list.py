# The exercise template contains the ShoppingList class from the exercise in part 8. Please adjust the class so that it is iterable and can thus be used as follows:

# shopping_list = ShoppingList()
# shopping_list.add("bananas", 10)
# shopping_list.add("apples", 5)
# shopping_list.add("pineapple", 1)

# for product in shopping_list:
#     print(f"{product[0]}: {product[1]} units")
# Sample output
# bananas: 10 units
# apples: 5 units
# pineapple: 1 units

# The __next__ method of your iterator should return tuples, where the first item is the name of the product and the second item is the amount.

####################################################################################################################################
####################################################################################################################################
# TEE RATKAISUSI TÄHÄN:
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def product(self, n: int):
        return self.products[n - 1][0]

    def number(self, n: int):
        return self.products[n - 1][1]
