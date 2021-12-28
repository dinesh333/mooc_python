# The file solutions.csv contains some solutions to mathematics problems:

# As you can see above, on each line the format is name_of_student;problem;result. All the operations are either addition or subtraction, and each has exactly two operands.

# Please write a function named filter_solutions() which

# Reads the contents of the file solutions.csv
# writes those lines which have a correct result into the file correct.csv
# writes those lines which have an incorrect result into the file incorrect.csv
# Using the example above, the file correct.csv would contain the lines

# The other two would be in the file incorrect.csv.

# Please write the lines in the same order as they appear in the original file. Do not change the original file.

# NB: the function should have the exact same result, no matter how many times it is called. That is, it shouldn't matter if the function is called once

# or multiple times in a row

# After the execution, the contents of the files correct.csv and incorrect.csv should be exactly the same in either case.


def read_file(file_name: str) -> list:
    with open(file_name) as file:
        content = []
        for line in file:
            line = line.replace('\n','')
            line = line.split(';')
            content.append(line)
        return content

def evaluate_data(content: list, correct_file_name: str, incorrect_file_name: str):
    open(correct_file_name, 'w').close()
    open(incorrect_file_name, 'w').close()
    correct_file = open(correct_file_name, 'w')
    incorrect_file = open(incorrect_file_name, 'w')
    for solution in content:
        sol = ';'.join(solution)
        sol += '\n'
        if eval(solution[1]) == int(solution[2]):
            correct_file.write(sol)
        else:
            incorrect_file.write(sol)
    correct_file.close()
    incorrect_file.close()

def filter_solutions():
    content = read_file('solutions.csv')
    evaluate_data(content, 'correct.csv', 'incorrect.csv')