from Display import Display
from SequenceGenerator import SequenceGenerator
from Statistics import Statistics


class Application:
    def __init__(self, n):
        # The constructor accepts an integer 'n' to define the size of the data.
        self.n = n

    def run(self):
        # Generate data
        generator = SequenceGenerator(self.n)
        generator.generate()  # Calls the generate() method from SequenceGenerator
        data = generator.get_data()  # Retrieves the generated sequence of data

        # Calculate statistics
        stats = Statistics(data)  # Creates a Statistics object with the generated data
        stats.calculate_variation_series()  # Calculates the sorted (variation) series
        stats.calculate_statistics()  # Calculates the frequency distribution and related statistics

        # Display results
        Display.display_sequence(data)  # Displays the original generated sequence
        Display.display_variation_series(stats.get_variation_series())  # Displays the sorted (variation) series
        Display.display_statistics(stats.get_distribution())  # Displays the frequency distribution, cumulative, and relative frequencies
