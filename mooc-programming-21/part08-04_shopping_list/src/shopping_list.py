# The exercise template contains a pre-defined ShoppingList class, which can be used to model a shopping list. Your task is to add a method to the class definition. You do not need to change any methods already defined.

# Assuming we have a ShoppingList object referenced in a variable named shopping_list, the object can be handled with the following methods:


# print(shopping_list.number_of_items())
# print(shopping_list.item(1))
# print(shopping_list.amount(1))
# print(shopping_list.item(2))
# print(shopping_list.amount(2))
# Sample output
# 2
# Bananas
# 4
# Milk
# 1

# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------
def total_units(my_list: ShoppingList):
    total_units = 0
    for i in range(1, my_list.number_of_items()+1):
        total_units += my_list.amount(i)
    return total_units

if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    print(total_units(my_list))