# Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user. Please see the example below.



# Write your solution here
name = input('Whom should I sign this to: ')
location = input('Where shall I save it: ')
with open(location, 'w') as file:
    file.write(f'Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')