# Please write a program which asks the user for their date of birth, and then prints out how old the user was on the eve of the new millennium. The program should ask for the day, month and year separately, and print out the age in days. Please have a look at the examples below:

# Sample output
# Day: 10
# Month: 9
# Year: 1979
# You were 7417 days old on the eve of the new millennium.

# Sample output
# Day: 28
# Month: 3
# Year: 2005
# You weren't born yet on the eve of the new millennium.

# You may assume all day-month-year combinations given as an argument will be valid dates. That is, there will not be a date like February 31st.


from datetime import datetime

def calculate_age(year: int, month: int, day: int):
    birthday = datetime(year, month, day)
    millenium = datetime(1999, 12, 31)
    difference = millenium - birthday
    return difference.days

day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

age_by_millenium = calculate_age(year, month, day)
if age_by_millenium > 0:
    print(f'You were {age_by_millenium} days old on the eve of the new millennium.')
else:
    print(f"You weren't born yet on the eve of the new millennium.")