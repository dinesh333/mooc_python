# Please write a function named sort_by_remaining_stock(items: list). The function takes a list of tuples as its argument. The tuples consist of the name, price and remaining stock of a product. The function should return a new list, where the items are sorted according to the stock remaining, lowest value first. The original list should not be changed.

# The function should work as follows:

# products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

# for product in sort_by_remaining_stock(products):
#     print(f"{product[0]} {product[2]} pcs")
# Sample output

# orange 2 pcs
# apple 3 pcs
# banana 12 pcs
# watermelon 22 pcspcs

def sort_by_remaining_stock(items: list):
    def order_by_stock(item):
        return item[2]
    return sorted(items, key=order_by_stock)

if __name__ == '__main__':
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

    for product in sort_by_remaining_stock(products):
        print(f"{product[0]} {product[2]} pcs")