# The exercise template contains the class definition ExamResult. The class has the following public attributes:

# name
# grade1
# grade2
# grade3
# Please write a function named best_results(results: list) which takes a list of ExamResult objects as its argument.

# The function should return a new list containing only the best result from each ExamResult object. The function should use a list comprehension to achieve this.

# The maximum length of the function is two lines of code, including the header line beginning with the def keyword.

# The function should work as follows:

# result1 = ExamResult("Peter",5,3,4)
# result2 = ExamResult("Pippa",3,4,1)
# result3 = ExamResult("Paul",2,1,3)
# results = [result1, result2, result3]
# print(best_results(results))
# Sample output
# [5, 4, 3]

class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def __str__(self):
        return (f'Name:{self.name}, grade1: {self.grade1}' +
            f', grade2: {self.grade2}, grade3: {self.grade3}')

def best_results(results: list):
    return [max([result.grade1, result.grade2, result.grade3]) for result in results]