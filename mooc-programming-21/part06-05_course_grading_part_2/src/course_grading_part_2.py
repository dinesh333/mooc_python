# Let's expand the program created in the previous exercise. Now also the exam points awarded to each student are contained in a CSV file. The contents of the file follow this format:

# In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the exam, which equals a total of 9 points.

# The program should again ask the user for the names of the files. Then the program should process the files and print out a grade for each student.

# Each completed exercise is counted towards exercise points, so that completing at least 10 % of the total exercices awards 1 point, completing at least 20 % awards 2 points, etc. Completing all 40 exercises awards 10 points. The number of points awarded is always an integer number.

# The final grade for the course is determined based on the sum of exam and exercise points according to the following table:


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

def convert_dict_values_list_str_to_int(dict):
    for key, value in dict.items():
        for list_index, list_value in enumerate(value):
            value[list_index] = int(list_value)

def points_to_grade(points):
    grade = -1
    if points <= 14:
        return 0
    elif points <= 17:
        return 1
    elif points <= 20:
        return 2
    elif points <= 23:
        return 3
    elif points <= 27:
        return 4
    else:
        return 5

def main():
    if True:
        student_file = input('Student information: ')
        exercises_file = input('Exercises completed: ')
        exam_file = input('Exam points: ')
    else:
        student_file = 'students1.csv'
        exercises_file = 'exercises1.csv'
        exam_file = 'exam_points1.csv'
    
    students = read_file(student_file)
    exercises = read_file(exercises_file)
    exams = read_file(exam_file)
    
    convert_dict_values_list_str_to_int(exercises)
    convert_dict_values_list_str_to_int(exams)

    for id, name in students.items():
        exercise_points = int(((sum(exercises[id])/40)*100)//10)
        exam_points = sum(exams[id])
        grade = points_to_grade(exercise_points+exam_points)
        print(f'{name[0]} {name[1]} {grade}')

main()