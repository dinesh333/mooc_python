# In this exercise you will create another version of the PhoneBookApplication. You will add addresses to the data which can be attached to a name. For simplicity's sake the functionality for saving to file has been removed, and some other methods have been renamed to better accommodate the change.

# Part 1: A separate class for a person's data
# Please change the way the data of a person is handled. Implement a class named Person, which takes care of the phone numbers and addresses of persons. The class should work as follows:

# person = Person("Eric")
# print(person.name())
# print(person.numbers())
# print(person.address())
# person.add_number("040-123456")
# person.add_address("Mannerheimintie 10 Helsinki")
# print(person.numbers())
# print(person.address())
# Sample output
# Eric
# []
# None
# ['040-123456']
# Mannerheimintie 10 Helsinki

# Part 2: PhoneBook uses the class Person
# Please change the internal implementation of your application so that your PhoneBook class uses objects of class Person to store the data in the phone book. That is, the attribute __persons should still contain a dictionary, but the values should be Person-objects and not lists. The user of your application should notice no difference; the changes must not affect the user interface.

# WARNING: whenever you make structural changes to your code, as described in this exercise, always take baby steps and test at every possible stage. Do not try and make all the changes at once. That is a sure way of running into serious problems with your code.

# A suitable first step might be to write some code for checking the functionality of the PhoneBook class directly. For example, the following should at least not cause any errors:

# phonebook = PhoneBook()
# phonebook.add_number("Eric", "02-123456")
# print(phonebook.get_entry("Eric"))
# print(phonebook.get_entry("Emily"))
# Notice the new name for the method for fetching an entry from the phone book. The automatic tests do not check what the printout from your get_entry method is, but make sure no errors are raised by the above code, and that the result makes sense within your implementation.

# When you've made the necessary changes in your program and have absolutely verified the functionality within the PhoneBook class, you can move on to the user interface, and see if everything still works as expected.

# Part 3: Adding an address
# Please implement the functionality for adding an address to an entry in your phone book. The program should work as follows:

# Sample output
# commands:
# 0 exit
# 1 add number
# 2 search
# 3 add address

# command: 1
# name: Eric
# number: 02-123456

# command: 3
# name: Emily
# address: Viherlaaksontie 7, Espoo

# command: 2
# name: Eric
# 02-123456
# address unknown

# command: 2
# name: Emily
# number unknown
# Viherlaaksontie 7, Espoo

# command: 3
# name: Eric
# address: Linnankatu 75, Turku

# command: 2
# name: Eric
# 02-123456
# Linnankatu 75, Turku

# command: 2
# name: Wilhelm
# address unknown
# number unknown

# command: 0

####################################################################################################################################
####################################################################################################################################

# Tee ratkaisusi tähän:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = []
        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")

    def add_number(self):
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

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
