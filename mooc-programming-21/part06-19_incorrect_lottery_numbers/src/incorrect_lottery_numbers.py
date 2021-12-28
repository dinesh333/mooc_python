# The file lottery_numbers.csv containts winning lottery numbers in the following format:

# Sample data
# week 1;5,7,11,13,23,24,30
# week 2;9,13,14,24,34,35,37
# ...etc...

# Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 inclusive.

# The file has been corrupted. Lines in the file may contain the following kinds of errors (these exact lines may not be present in the file, but errors in a similar format will be):

# The week number is incorrect:
# week zzc;1,5,13,22,24,25,26

# One or more numbers are not correct:
# week 22;1,**,5,6,13,2b,34

# Too few numbers:
# week 13;4,6,17,19,24,33

# The numbers are too small or large:
# week 39;5,9,15,35,39,41,105

# The same number appears twice:
# week 41;5,12,3,35,12,14,36

# Please write a function named filter_incorrect(), which creates a file called correct_numbers.csv. The file should contain only those lines from the original file which are in the correct format.

# Write your solution here

def is_week_valid(week: str):
    try:
        week = int(week)
        return True
    except:
        return False

def are_numbers_valid(numbers: list):
    try:
        numbers = numbers.split(',')

        if len(numbers) != 7:
            return False
        
        for num in numbers:
            number = int(num)
            if number < 1 or number > 39 or numbers.count(num) > 1:
                return False

        return True
    
    except:
        return False

def filter_incorrect():
    open('correct_numbers.csv', 'w').close()
    correct_file = open('correct_numbers.csv', 'a')
    with open('lottery_numbers.csv') as lottery_file:
        for line in lottery_file:
            original_line = line
            line = line.replace('\n','')
            parts = line.split(';')
            week = parts[0].split(' ')[1]
            numbers = parts[1]
            if is_week_valid(week) and are_numbers_valid(numbers):
                correct_file.write(original_line)
    correct_file.close()