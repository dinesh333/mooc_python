# The file fruits.csv contains names of fruits, and their prices, in the format specified in this example:

# Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents. In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float.

# NB: the function does not take any arguments. The file you are working with is always named fruits.csv.

# write your solution here
def read_fruits():
    dict = {}
    with open("fruits.csv") as file:
        for line in file:
            line = line.replace('\n','')
            fruit_price = line.split(';')
            dict[fruit_price[0]] = float(fruit_price[1])
        return dict