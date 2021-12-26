# write your solution here
def read_fruits():
    dict = {}
    with open("fruits.csv") as file:
        for line in file:
            line = line.replace('\n','')
            fruit_price = line.split(';')
            dict[fruit_price[0]] = float(fruit_price[1])
        return dict