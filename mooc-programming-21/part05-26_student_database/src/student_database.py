# In this series of exercises you will create a simple student database. Before diving in, please spend a moment reading through the instructions and thinking about what sort of data structures are necessary for organising the data stored by your program.

# Part 1: adding students
# First write a function named add_student, which adds a new student to the database. Also write a preliminary version of the function print_student, which prints out the information of a single student.

# Part 2: adding completed courses
# Please write a function named add_course, which adds a completed course to the information of a specific student in the database. The course data is a tuple consisting of the name of the course and the grade:

# Part 3: repeating courses
# Courses with grade 0 should be ignored when adding course information. Additionally, if the course is already in the database in that specific student's information, the grade recorded in the database should never be lowered if the course is repeated.

# Part 4: summary of database
# Please write a function named summary, which prints out a summary based on all the information stored in the database.

# Write your solution here
def add_student(students, name):
    students[name] = []

def print_student(students, name):
    if name not in students:
        print(name + ': no such person in the database')
        return
    if len(students[name]) == 0:
        print(name + ':')
        print(' no completed courses')
    else:
        print(name + ':')
        print(f' {len(students[name])} completed courses:')
        sum_grades = 0
        for course in students[name]:
            print(f'  {course[0]} {course[1]}')
            sum_grades += course[1]
        print(f' average grade {(sum_grades/len(students[name])):.1f}')

def avg_grade(students, name):
    if name in students and len(students[name]) > 0:
        sum_grades = 0
        for course in students[name]:
            sum_grades += course[1]
        return (sum_grades/len(students[name]))


def add_course(students, name, course_and_grade):
    new_course, new_grade = course_and_grade
    if new_grade != 0:
        courses = students[name]
        #Loop through the student's courses, and if the new course to be added exists there
        #already, then only add if the new grade is higher than the old grade
        for index, course in enumerate(courses):
            if new_course == course[0]:
                if new_grade > course[1]:
                    courses.pop(index)
                    courses.insert(index, course_and_grade)
                    students[name] = courses
                return
        courses.append(course_and_grade)
        students[name] = courses

def summary(students):
    if len(students) > 0:
        print(f'students {len(students)}')
        max_courses_student = None
        max_courses = 0
        max_avg_grade_student = None
        max_avg_grade = 0.0
        for student, courses in students.items():
            if len(courses) > max_courses:
                max_courses = len(courses)
                max_courses_student = student

            student_avg_grade = avg_grade(students, student)
            if student_avg_grade > max_avg_grade:
                max_avg_grade_student = student
                max_avg_grade = student_avg_grade
        print(f'most courses completed {max_courses} {max_courses_student}')
        print(f'best average grade {max_avg_grade:.1f} {max_avg_grade_student}')

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)