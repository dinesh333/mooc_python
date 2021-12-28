# In this exercise you will validate Finnish Personal Identity Codes (PIC).

# Please write a function named is_it_valid(pic: str), which returns True or False based on whether the PIC given as an argument is valid or not. Finnish PICs follow the format ddmmyyXyyyz, where ddmmyy contains the date of birth, X is the marker for century, yyy is the personal identifier and z is a control character.

# The program should check the validity by these three criteria:

# The first half of the code is a valid, existing date in the format ddmmyy.
# The century marker is either + (1800s), - (1900s) or A (2000s).
# The control character is valid.
# The control character is calculated by taking the nine-digit number created by the date of birth and the personal identifier, dividing this by 31, and selecting the character at the index specified by the remainder from the string 0123456789ABCDEFHJKLMNPRSTUVWXY. For example, if the remainder was 12, the control character would be C.

# More examples and explanations of the uses of the PIC are available at the Digital and Population Data Services Agency.

# NB! Please make sure you do not share your own PIC, for example in the code you use for testing or through the course support channels.

# Here are some valid PICs you can use for testing:

# 230827-906F
# 120488+246L
# 310823A9877


# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    try:
        dd = int(pic[0:2])
        mm = int(pic[2:4])
        yy = int(pic[4:6])
        X = pic[6]
        yyy = int(pic[7:10])
        z = pic[10]
        nums = pic[0:6] + pic[7:10]
        index = int(nums)%31
        control = '0123456789ABCDEFHJKLMNPRSTUVWXY'[index]

        if dd < 1 or dd > 31 or mm < 1 or mm > 12 or X not in ('-','+','A') or z != control:
            return False
        
        century = 0
        if X == '-':
            century = 1800
        elif X == '+':
            century = 1900
        elif X == 'A':
            century = 2000
        
        dob_year = century + yy

        datetime(dob_year, mm, dd)

        return True
    except:
        return False