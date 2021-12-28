# In this exercise you will create a small expansion to the phone book application. The code from the above example is in the exercise template. Please add a command which lets the user search the phone book by number. After the addition the application should work as follows:

# Sample output
# commands:
# 0 exit
# 1 add entry
# 2 search
# 3 search by number

# command: 1
# name: Eric
# number: 02-123456

# command: 1
# name: Eric
# number: 045-4356713

# command: 3
# number: 02-123456
# Eric

# command: 3
# number: 0100100
# unknown number

# command: 0

# Please implement this addition with respect to the current structure of the program. This means that in the PhoneBookApplication class you should add an appropriate helper method to allow for the new functionality, and also add a new branch to the while loop. In the PhoneBook class you should add a method which allows for searching with a number.

####################################################################################################################################
####################################################################################################################################
# WRITE YOUR SOLUTION HERE:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]


    def all_entries(self):
        return self.__persons

class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers
        return names

    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")
                
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")

        # add the names and numbers from the file to the phone book
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())


    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            else:
                self.help()

# when you run the tests, nothing apart from these two lines should be placed in the main function, outside any class definitions 
application = PhoneBookApplication()
application.execute()
