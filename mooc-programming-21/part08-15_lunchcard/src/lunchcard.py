# At Unicafe, the student cafeteria at the University of Helsinki, students can pay 
# for their lunch with a special debit card.

# In this exercise you will write a class called LunchCard, with the purpose of 
# emulating the functions provided by the cafeteria's debit card.

# Part 1: The structure of the new class
# Please create a new class named LunchCard.

# First write the constructor for the class. It should take the initial balance 
# available on the card as an argument, and save it as an attribute. This is provided 
# for you in the skeleton below.

# Next, write a __str__ method, which returns a string containing the balance: 
# "The balance is X euros". The available balance should be printed out with one decimal 
# place precision. Please see the example below for usage.

# Part 2: Paying for lunch
# Please implement the following methods in your LunchCard class:

# eat_lunch subtracts 2.60 euros from the balance on the card
# eat_special subtracts 4.60 euros from the balance on the card

# Make sure the balance is never allowed to reach numbers below zero. If there is not 
# enough money on the card to pay for the lunch, the price of the lunch should not be subtracted from the balance.

# Part 3: Depositing money on the card
# Implement the deposit_money method in your LunchCard class.

# The method increases the balance on the card by the amount given as an argument.

# The method should account for arguments below zero by raising an exception of type ValueError:

# Part 4: Multiple cards
# Please write a main function which contains the following sequence of events:

# Create a lunch card for Peter. The initial balance on the card is 20 euros.
# Create a lunch card for Grace. The initial balance on the card is 30 euros.
# Peter eats a special
# Grace eats a regular lunch
# Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
# Peter deposits 20 euros
# Grace eats the special
# Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
# Peter eats a regular lunch
# Peter eats a regular lunch
# Grace deposits 50 euros
# Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f'The balance is {self.balance:.1f} euros'

    def eat_lunch(self):
        if (self.balance-2.60) > 0:
            self.balance -= 2.60

    def eat_special(self):
        if (self.balance-4.60) > 0:
            self.balance -= 4.60

    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError('You cannot deposit an amount of money less than zero')
        self.balance += amount

peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')
peters_card.deposit_money(20)
graces_card.eat_special()
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')