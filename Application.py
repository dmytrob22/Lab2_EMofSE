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
        generator.generate()
        data = generator.get_data()

        # Calculate statistics
        stats = Statistics(data)
        stats.calculate_variation_series()
        stats.calculate_statistics()

        # Display results
        Display.display_sequence(data)
        Display.display_variation_series(stats.get_variation_series())
        Display.display_statistics(stats.get_distribution())
