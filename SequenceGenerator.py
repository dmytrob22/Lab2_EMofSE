import random  # Importing the random module to generate random numbers

class SequenceGenerator:  # Define a class to generate a sequence of numbers
    def __init__(self, n, value_range=(1, 5)):  # Constructor to initialize the object
        self.n = n  # The number of elements in the sequence (excluding the extra 10)
        self.value_range = value_range  # Tuple representing the range of values (default: (1, 5))
        self.data = []  # This will store the generated sequence of numbers

    def generate(self):  # Method to generate a sequence of numbers
        # Generate a list of random integers. The length of the list is `n + 10`.
        # Each integer is randomly chosen between value_range[0] and value_range[1].
        self.data = [random.randint(self.value_range[0], self.value_range[1]) for _ in range(self.n + 10)]

    def get_data(self):  # Method to return the generated data
        return self.data  # Return the generated sequence
