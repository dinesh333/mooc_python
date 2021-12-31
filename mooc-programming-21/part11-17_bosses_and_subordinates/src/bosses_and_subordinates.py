# The class Employee models an employee of a company:

# class Employee:
#     def __init__(self, name: str):
#         self.name = name
#         self.subordinates = []

#     def add_subordinate(self, employee: 'Employee'):
#         self.subordinates.append(employee)
# Please write a function named count_subordinates(employee: Employee) which recursively counts the number of subordinates each employee has.

# An example of the function in action:

# if __name__ == "__main__":
#     t1 = Employee("Sally")
#     t2 = Employee("Eric")
#     t3 = Employee("Matthew")
#     t4 = Employee("Emily")
#     t5 = Employee("Adele")
#     t6 = Employee("Claire")
#     t1.add_subordinate(t4)
#     t1.add_subordinate(t6)
#     t4.add_subordinate(t2)
#     t4.add_subordinate(t3)
#     t4.add_subordinate(t5)
#     print(count_subordinates(t1))
#     print(count_subordinates(t4))
#     print(count_subordinates(t5))
# Sample output
# 5
# 3
# 0

class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    sub = 0
    for emp in employee.subordinates:
        sub += 1
        sub += count_subordinates(emp)
    return sub

if __name__ == "__main__":
    t1 = Employee("Sally")
    t2 = Employee("Eric")
    t3 = Employee("Matthew")
    t4 = Employee("Emily")
    t5 = Employee("Adele")
    t6 = Employee("Claire")
    t1.add_subordinate(t4)
    t1.add_subordinate(t6)
    t4.add_subordinate(t2)
    t4.add_subordinate(t3)
    t4.add_subordinate(t5)
    print(count_subordinates(t1))
    print(count_subordinates(t4))
    print(count_subordinates(t5))