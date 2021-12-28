# The exercise template contains the following skeleton for the Stopwatch class:

# class Stopwatch:
#     def __init__(self):
#         self.seconds = 0
#         self.minutes = 0
# Please add to the class definition so that it works as follows:

# watch = Stopwatch()
# for i in range(3600):
#     print(watch)
#     watch.tick()
# Sample output
# 00:00
# 00:01
# 00:02
# ... many more lines printed out
# 00:59
# 01:00
# 01:01
# ... many, many more lines printed out
# 59:58
# 59:59
# 00:00
# 00:01

# So, the method tick adds one second to the stopwatch. The maximum value for both seconds and minutes is 59. Your class definition should also contain a __str__ method, which returns a string representation of the state of the stopwatch, as shown in the example above.


# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
    
    def __str__(self):
        return f'{self.minutes:02d}:{self.seconds:02d}'