# The exercise template contains a class named ExamSubmission which, as the name 
# implies, models an examinee's submission in an exam. The class has two attributes 
# defined: examinee (str) and points (int).

# Please write a function named passed(submissions: list, lowest_passing: int) 
# which takes a list of exam submissions and an integer number representing the 
# lowest passing grade as its arguments.

# The function should create and return a new list, which contains only the passed 
# submissions from the original list. Please do not change the list given as an 
# argument, or make any changes to the ExamSubmission class definition.

class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f'ExamSubmission (examinee: {self.examinee}, points: {self.points})'

def passed(submissions: list, lowest_passing: int):
    passing = []
    for sub in submissions:
        if sub.points >= lowest_passing:
            passing.append(sub)
    return passing

if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing)