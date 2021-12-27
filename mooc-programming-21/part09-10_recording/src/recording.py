# Please create a class named Recording which models a single recording. The class 
# should have one private variable: __length of type integer.

# Please implement the following:

# a constructor which takes the length as an argument
# a getter method length which returns the length of the recording
# a setter method which sets the length of the recording

class Recording:
    def __init__(self, length: int):
        if length < 0:
            raise ValueError('Length of recording cannot be below 0.')
        self.__length = length
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length: int):
        if length < 0:
            raise ValueError('Length of recording cannot be below 0.')
        self.__length = length