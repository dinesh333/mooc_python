# The exercise template contains an outline for a class named Money. This exercise asks you to implement some additional methods and to fix some small problems in the template.

# Part 1: Fix the string representation
# The __str__ method in the class definition doesn't work quite right. Given the following two Money objects, the latter is printed out wrong:

# e1 = Money(4, 10)
# e2 = Money(2, 5)  # two euros and five cents

# print(e1)
# print(e2)
# Sample output
# 4.10
# 2.5

# Please fix the method so that it prints out

# Sample output
# 4.10 eur
# 2.05 eur

# Part 2: Equal amounts
# Please define a new method named __eq__(self, another) which allows you to use the == comparison operator on Money objects. You can test your implementation with the following code:

# e1 = Money(4, 10)
# e2 = Money(2, 5)
# e3 = Money(4, 10)

# print(e1)
# print(e2)
# print(e3)
# print(e1 == e2)
# print(e1 == e3)
# Sample output
# 4.10 eur
# 2.05 eur
# 4.10 eur
# False
# True

# Part 3: Other comparison operators
# Please implement the appropriate methods for the comparison operators <, > and !=.

# e1 = Money(4, 10)
# e2 = Money(2, 5)

# print(e1 != e2)
# print(e1 < e2)
# print(e1 > e2)
# Sample output
# True
# False
# True

# Part 4: Addition and subtraction
# Please implement the addition and subtraction operators + and - for Money objects. Both should return a new object of type Money. Neither the object itself nor the object passed as an argument should be changed as a result.

# NB: the value of a Money object cannot be negative. If an attempt to subtract would result in a negative result, the method should raise a ValueError exception.

# e1 = Money(4, 5)
# e2 = Money(2, 95)

# e3 = e1 + e2
# e4 = e1 - e2

# print(e3)
# print(e4)

# e5 = e2-e1
# Sample output
# 7.00 eur
# 1.10 eur
# Traceback (most recent call last):
# File "money.py", line 416, in 
# e5 = e2-e1
# File "money.py", line 404, in sub
# raise ValueError(f"a negative result is not allowed")
# ValueError: a negative result is not allowed

# Part 5: The value must not be directly accessible
# The class still has a small integrity issue. The user can "cheat" by accessing the attributes directly and changing the value stored in the Money object:

# print(e1)
# e1.euros = 1000
# print(e1)
# Sample output
# 4.05 eur
# 1000.05 eur

# Please encapsulate the implementation of the attributes defined in the class so that the cheat used above is not possible. The class should have no public attributes, and no getter or setter methods for the euros or the cents.

####################################################################################################################################
####################################################################################################################################
# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __str__(self):
        return f"{self.euros}.{self.cents}"
