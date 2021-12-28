# This program works with two CSV files. One of them contains information about some students on a course:

# The other contains the number of exercises each student has completed each week:

# As you can see above, both CSV files also have a header row, which tells you what each column contains.

# Please write a program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student. If the files have the contents in the examples above, the program should print out the following:

# write your solution here

def read_file(file_name):
    with open(file_name) as file:
        dict = {}
        for line in file:
            line = line.replace('\n', '')
            line_as_list = line.split(';')
            if line_as_list[0] == 'id':
                continue
            dict[line_as_list[0]] = line_as_list[1:]
        return dict

#Convert list of strings to list of ints in place
def list_str_to_int(list):
    for index, value in enumerate(list):
        list[index] = int(value)

def main():
    if True:
        student_file = input('Student information: ')
        exercises_file = input('Exercises completed: ')
    else:
        student_file = 'students1.csv'
        exercises_file = 'exercises1.csv'
    
    students = read_file(student_file)
    exercises = read_file(exercises_file)

    #Dictionary exercises has list of strings as value. Convert list of strings to list of ints
    for id, exercises_list in exercises.items():
        list_str_to_int(exercises_list)
    
    for id, name in students.items():
        exercises_total = sum(exercises[id])
        print(f'{name[0]} {name[1]} {exercises_total}')

main()