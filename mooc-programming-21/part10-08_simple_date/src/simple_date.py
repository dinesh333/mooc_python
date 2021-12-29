# In this exercise you are asked to implement the class SimpleDate which allows you to handle dates. For simplicity's sake we assume here that each month has 30 days.

# Because of this simplification you should not use the datetime module from the Python standard library. You will implement similar functionality by yourself instead.

# Part 1: Comparisons
# Please implement the outline of the class, along with methods allowing for comparisons with the operators <, >, == and !=. You can use the following code to test your implementation:

# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(28, 12, 1985)
# d3 = SimpleDate(28, 12, 1985)

# print(d1)
# print(d2)
# print(d1 == d2)
# print(d1 != d2)
# print(d1 == d3)
# print(d1 < d2)
# print(d1 > d2)
# Sample output
# 4.10.2020
# 28.12.1985
# False
# True
# False
# False
# True

# Part 2: Increment
# Please implement the addition operator + which allows you to add a given number of days to a SimpleDate object. The operator should return a new SimpleDate object. The original object should not be changed.

# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(28, 12, 1985)

# d3 = d1 + 3
# d4 = d2 + 400

# print(d1)
# print(d2)
# print(d3)
# print(d4)
# Sample output
# 4.10.2020
# 28.12.1985
# 7.10.2020
# 8.2.1987

# Part 3: Difference
# Please implement the subtraction operator - which allows you to find out the difference in days between two SimpleDate objects. As we assumed each month to have 30 days, a year within the confines of this exercise is 12*30 = 360 days long.

# You can use the following code to test your program:

# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(2, 11, 2020)
# d3 = SimpleDate(28, 12, 1985)

# print(d2-d1)
# print(d1-d2)
# print(d1-d3)
# Sample output
# 28
# 28
# 12516

####################################################################################################################################
####################################################################################################################################

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year
    
    def __str__(self):
        return f'{self.__day}.{self.__month}.{self.__year}'
    
    def __lt__(self, another: 'SimpleDate'):
        if self.__year < another.__year:
            return True
        elif self.__year == another.__year:
            if self.__month < another.__month:
                return True
            elif self.__month == another.__month:
                if self.__day < another.__day:
                    return True

        return False

    def __gt__(self, another: 'SimpleDate'):
        if self.__eq__(another) == False and self.__lt__(another) == False:
            return True
        return False

    def __eq__(self, another: 'SimpleDate'):
        if self.__day == another.__day and \
            self.__month == another.__month and \
                self.__year == another.__year:
                return True
        return False

    def __ne__(self, another: 'SimpleDate'):
        if self.__eq__(another) == False:
            return True
        return False

    def __convert_curr_date_to_days(self):
        return ((self.__year-1)*12*30) + ((self.__month-1)*30) + self.__day

    def __add__(self, days_to_add: int):
        days = self.__convert_curr_date_to_days()
        days += days_to_add
        year = (days//360)+1
        month = ((days//30)%12)+1
        day = days%30
        return SimpleDate(day, month, year)

    def __sub__(self, another: 'SimpleDate'):
        curr_days = self.__convert_curr_date_to_days()
        another_days = another.__convert_curr_date_to_days()
        return abs(curr_days - another_days)