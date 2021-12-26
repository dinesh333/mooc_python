'''
In this exercise you will write a program for printing out grade statistics for a university course.

The program asks the user for results from different students on the course. These include exam points and numbers of exercises completed. The program then prints out statistics based on the results.

Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100.

The program kees asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.

And example of how the data is typed in:

Sample output
Exam points and exercises completed: 15 87
Exam points and exercises completed: 10 55
Exam points and exercises completed: 11 40
Exam points and exercises completed: 4 17
Exam points and exercises completed:
Statistics:

When the user types in an empty line, the program prints out statistics. They are formulated as follows:

The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point, 20% grants two points, and so forth. Completing all 100 exercises grants 10 exercise points. The number of exercise points granted is an integer value, rounded down.

The grade for the course is determined based on the following table:

exam points + exercise points	grade
0–14	                        0 (i.e. fail)
15–17	                        1
18–20	                        2
21–23	                        3
24–27	                        4
28–30	                        5
There is also an exam cutoff threshold. If a student received less than 10 points from the exam, they automatically fail the course, regardless of their total number of points.

With the example input from above the program would print out the following statistics:

Sample output
Statistics:
Points average: 14.5
Pass percentage: 75.0
Grade distribution:
  5:
  4:
  3: *
  2:
  1: **
  0: *
Floating point numbers should be printed out with one decimal precision.
'''

def convert_exercise_completed_to_points(exercise : int):
    return exercise // 10

def calculate_grade(exam : int, exercise : int):
    total = exam + exercise
    if exam < 10 or total <= 14:
        return 0
    elif total <= 17:
        return 1
    elif total <= 20:
        return 2    
    elif total <= 23:
        return 3
    elif total <= 27:
        return 4
    elif total <= 30:
        return 5
    else:
        return None

def points_avg(exam_points : list, exercise_points: list):
    sum = 0
    for i in range(len(exam_points)):
        sum += exam_points[i] + exercise_points[i]
    return sum/len(exam_points)

def pass_percent(exam_points : list, exercise_points : list):
    pass_count = 0
    for i in range(len(exam_points)):
        grade = calculate_grade(exam_points[i], exercise_points[i])
        if grade > 0:
            pass_count += 1
    return (pass_count/len(exam_points))*100

def grade_distribution(exam_points : list, exercise_points : list):
    grades = []
    for i in range(len(exam_points)):
        grade = calculate_grade(exam_points[i], exercise_points[i])
        grades.append(grade)
    
    print('Grade distribution:')
    grade = 5
    while grade >= 0:
        stars = '*'*grades.count(grade)
        print(f'  {grade}: {stars}')
        grade -= 1

def generate_stats(exam_points : list, exercise_points : list):
    print('Statistics:')
    print(f'Points average: {points_avg(exam_points, exercise_points):.1f}')
    print(f'Pass percentage: {pass_percent(exam_points, exercise_points):.1f}')
    grade_distribution(exam_points, exercise_points)

def main():
    exam_points = []
    exercise_points = []

    while True:
        points = input('Exam points and exercises completed: ')
        if points == '':
            break
        exam_points.append(int(points.split()[0]))
        exercise_completed = int(points.split()[1])
        exercise_points.append(convert_exercise_completed_to_points(exercise_completed))

    generate_stats(exam_points, exercise_points)

main()