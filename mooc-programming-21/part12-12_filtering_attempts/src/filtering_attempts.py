# In this exercise we will continue with the CourseAttempt class.

# Accepted attempts
# Please write a function named accepted(attempts: list) which takes a list of CourseAttempt objects as its argument. The function should return a new list of CourseAttempt objects, including only those items from the original list whose grade is at least 1.

# s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
# s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
# s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)

# for attempt in accepted([s1, s2, s3]):
#     print(attempt)
# Sample output
# Peter Python, grade for the course Introduction to Programming 3
# Olivia C. Objective grade for the course Introduction to Programming 5

# Please implement the function using the filter function.

# Attempts with grade
# Please write a function named attempts_with_grade(attempts: list, grade: int) which takes a list of CourseAttempt objects and an integer as its arguments. The function should return a new list containing only those CourseAttempt objects from the original list whose grade matches the second argument.

# s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
# s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
# s3 = CourseAttempt("Peter Python", "Introduction to AI", 3)
# s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)

# for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
#     print(attempt)
# Sample output
# Peter Python, grade for the course Introduction to Programming 3
# Peter Python, grade for the course Introduction to AI 3
# Olivia C. Objective, grade for the course Data Structures and Algorithms 3

# Please implement the function using the filter function.

# Students who passed the course
# Please write a function named passed_students(attempts: list, course: str) which takes a list of CourseAttempt objects and a course name as its arguments. The function should return an alphabetically ordered list of names of those students who passed the course, i.e. their grade for the given course was higher than 0.

# s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
# s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
# s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
# s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

# for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
#     print(attempt)
# Sample output
# Jack Java
# Olivia C. Objective

# Please implement the function using the filter and map functions.

class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list):
    attempts = filter(lambda attempt: attempt.grade >= 1, attempts)
    return list(attempts)

def attempts_with_grade(attempts: list, grade: int):
    attempts = filter(lambda attempt: attempt.grade == grade, attempts)
    return list(attempts)

def passed_students(attempts: list, course: str):
    attempts = filter(lambda attempt: attempt.course_name == course and attempt.grade > 0, attempts)
    attempts = map(lambda attempt: attempt.student_name, attempts)
    attempts = list(attempts)
    attempts.sort()
    return attempts