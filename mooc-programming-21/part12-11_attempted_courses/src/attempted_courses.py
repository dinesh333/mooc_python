# The exercise template contains the class definition for a CourseAttempt. It works like this:

# attempt = CourseAttempt("Peter Python", "Introduction to Programming", 5)
# print(attempt.student_name)
# print(attempt.course_name
# print(attempt.grade)
# print(attempt)
# Sample output
# Peter Python
# Introduction to Programming
# 5
# Peter Python, grade for the course Introduction to Programming 5

# Names of students
# Please write a function named names_of_students(attempts: list) which takes a list of CourseAttempt objects as its argument. The function should return a new list with the names of the students who have attempted the course.

# s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
# s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
# s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

# for name in names_of_students([s1, s2, s3]):
#     print(name)
# Sample output
# Peter Python
# Olivia C. Objective
# Peter Python

# Please implement the function using the map function.

# Courses
# Please write a function named course_names(attempts: list) which takes a list of CourseAttempt objects as its argument. The function should return a new list containing the names of the courses on the original list in alphabetical order. Each course name should appear only once on the list.

# s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
# s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
# s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

# for name in course_names([s1, s2, s3]):
#     print(name)
# Sample output
# Advanced Course in Programming
# Introduction to Programming

# Please implement the function using the map function. That alone will likely not be enough, however. You will need something else, too, to make sure the course names are unique.

class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def names_of_students(attempts: list):
    names = map(lambda attempt: attempt.student_name, attempts)
    return list(names)

def course_names(attempts: list):
    def get_course(attempt: CourseAttempt):
        return attempt.course_name
    courses = map(get_course, attempts)
    courses = list(set(list(courses)))
    courses.sort()
    return courses