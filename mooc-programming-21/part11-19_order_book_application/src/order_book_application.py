# In this exercise you will create aa interactive application for administering the tasks ordered from a software company. The implementation is completely up to you, but you may use the building blocks from the previous exercise in your application. The examples in the last section of part 10 can also prove useful.

# Without error handling
# The application should work exactly as follows:

# Sample output
# commands:
# 0 exit
# 1 add order
# 2 list finished tasks
# 3 list unfinished tasks
# 4 mark task as finished
# 5 programmers
# 6 status of programmer

# command: 1
# description: program the next facebook
# programmer and workload estimate: jonah 1000
# added!

# command: 1
# description: program mobile app for workload accounting
# programmer and workload estimate: eric 25
# added!

# command: 1
# description: program an app for music theory revision
# programmer and workload estimate: nina 12
# added!

# command: 1
# description: program the next twitter
# programmer and workload estimate: jonah 55
# added!

# command: 2
# no finished tasks

# command: 3
# 1: program the next facebook (1000 hours), programmer jonah NOT FINISHED
# 2: program mobile app for workload accounting (25 hours), programmer eric NOT FINISHED
# 3: program an app for music theory revision (12 hours), programmer nina NOT FINISHED
# 4: program the next twitter (55 hours), programmer jonah NOT FINISHED

# command: 4
# id: 2
# marked as finished

# command: 4
# id: 4
# marked as finished

# command: 2
# 2: program mobile app for workload accounting (25 hours), programmer eric FINISHED
# 4: program the next twitter (55 hours), programmer jonah FINISHED

# command: 3
# 1: program the next facebook (1000 hours), programmer jonah NOT FINISHED
# 3: program an app for music theory revision (12 hours), programmer nina NOT FINISHED

# command: 5
# jonah
# eric
# nina

# command: 6
# programmer: jonah
# tasks: finished 2 not finished 1, hours: done 55 scheduled 1000

# The first exercise point is granted for a working application when all user input is flawless.

# Handling errors in user input
# To gain the second exercise point for this exercise your application is expected to recover from erroneus user input. Any input which does not follow the specified format should produce an error message erroneous input, and result in yet another repeat of the loop asking for a new command:

# Sample output
# command: 1
# description: program mobile app for workload accounting
# programmer and workload estimate: eric xxx
# erroneous input

# command: 1
# description: program mobile app for workload accounting
# programmer and workload estimate: eric
# erroneous input

# command: 4
# id: 1000000
# erroneous input

# command: 4
# id: XXXX
# erroneous input

# command: 6
# programmer: unknownprogrammer
# erroneous input

class Task:
    total_tasks = 0
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        Task.total_tasks += 1
        self.id = Task.total_tasks
        self.__finished = False

    def is_finished(self):
        return self.__finished

    def finished_status(self):
        finished = 'NOT FINISHED'
        if self.__finished:
            finished = 'FINISHED'
        return finished

    def mark_finished(self):
        self.__finished = True

    def __str__(self):
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished_status()}'

class OrderBook:
    def __init__(self):
        self.__tasks = []
    
    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self.__tasks.append(task)

    def all_orders(self):
        return self.__tasks
    
    def programmers(self):
        return list(set([task.programmer for task in self.__tasks]))

    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError(f'Order with {id} does not exist')

    def finished_orders(self):
        return [task for task in self.__tasks if task.is_finished() == True]

    def unfinished_orders(self):
        return [task for task in self.__tasks if task.is_finished() == False]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError(f'No such {programmer} exists')
        tasks = [task for task in self.__tasks if task.programmer == programmer]
        finished = 0
        unfinished = 0
        finished_workload = 0
        unfinished_workload = 0
        for task in tasks:
            if task.is_finished():
                finished += 1
                finished_workload += task.workload
            else:
                unfinished += 1
                unfinished_workload += task.workload
        return (finished, unfinished, finished_workload, unfinished_workload)

class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()

    def __error(self):
        print('erroneous input')

    def help(self):
        print('commands:')
        print('0 exit')
        print('1 add order')
        print('2 list finished tasks')
        print('3 list unfinished tasks')
        print('4 mark task as finished')
        print('5 programmers')
        print('6 status of programmer')

    def add_order(self):
        description = input('description: ')
        prog_load = input('programmer and workload estimate: ')
        prog_load = prog_load.split(' ')
        programmer = prog_load[0]
        try:
            workload = int(prog_load[1])
        except:
            self.__error()
            return
        self.__orderbook.add_order(description, programmer, workload)
        print('added!')

    def list_finished_tasks(self):
        if len(self.__orderbook.finished_orders()):
            for task in self.__orderbook.finished_orders():
                print(task)
        else:
            print('no finished tasks')

    def list_unfinished_tasks(self):
        if len(self.__orderbook.unfinished_orders()):
            for task in self.__orderbook.unfinished_orders():
                print(task)
        else:
            print('no unfinished tasks')

    def mark_finished(self):
        try:
            id = int(input('id: '))
        except:
            self.__error()
            return

        ids = [task.id for task in self.__orderbook.all_orders()]
        if id not in ids:
            self.__error()
            return

        self.__orderbook.mark_finished(id)
        print('marked as finished')

    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)

    def programmer_status(self):
        programmer = input('programmer: ')
        if programmer not in self.__orderbook.programmers():
            self.__error()
            return
        f, u, fw, uw = self.__orderbook.status_of_programmer(programmer)
        print(f'tasks: finished {f} not finished {u}, hours: done {fw} scheduled {uw}')

    def execute(self):
        self.help()
        while True:
            print()
            command = int(input('command: '))
            if command == 0:
                break
            elif command == 1:
                self.add_order()
            elif command == 2:
                self.list_finished_tasks()
            elif command == 3:
                self.list_unfinished_tasks()
            elif command == 4:
                self.mark_finished()
            elif command == 5:
                self.programmers()
            elif command == 6:
                self.programmer_status()
            else:
                self.help()

app = OrderBookApplication()
app.execute()