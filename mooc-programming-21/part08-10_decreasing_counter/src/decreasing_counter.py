# This exercise has multiple parts. You can submit the parts separately. 
# Each part is worth one exercise point.

# The exercise template contains a partially completed class DecreasingCounter:

# Part 1: Decreasing the value of the counter
# Please complete the method decrease defined in the template, so that it decreases the value 
# stored in the counter by one.

# Part 2: The counter must not have a negative value
# Please add functionality to your decrease method, so that the value of the counter will never 
# reach negative values. If the value of the counter is 0, it will not be further decreased.

# Part 3: Setting the value to zero
# Please add a method set_to_zero which sets the value of the counter to 0:

# Part 4: Resetting the counter
# Please add a method reset_original_value() which resets the counter to its initial state:

class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.initial_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        self.value = self.value - 1 if self.value > 0 else 0
    
    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.initial_value