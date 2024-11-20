from collections import Counter  # Import Counter class from collections module for frequency counting

class Statistics:
    def __init__(self, data):
        self.data = data  # Store the input data (list of numbers)
        self.variation_series = []  # This will store the sorted variation series
        self.distribution = []  # This will store the statistical distribution

    def calculate_variation_series(self):
        # Sort the data in ascending order to create the variation series
        self.variation_series = sorted(self.data)

    def calculate_statistics(self):
        # Use Counter to count the occurrences (frequency) of each unique value in the variation series
        counts = Counter(self.variation_series)
        cumulative_frequency = 0  # Initialize cumulative frequency to 0
        total = len(self.variation_series)  # Total number of data points

        self.distribution = []  # Reset the distribution list

        # Iterate over the sorted items in the counts dictionary (sorted by value)
        for value, frequency in sorted(counts.items()):
            # Update the cumulative frequency
            cumulative_frequency += frequency
            # Calculate the relative frequency as a percentage
            relative_frequency = (frequency / total) * 100
            # Append the statistics for this value to the distribution list
            self.distribution.append({
                'Value': value,
                'Frequency': frequency,
                'Cumulative Frequency': cumulative_frequency,
                'Relative Frequency (%)': relative_frequency
            })

    def get_variation_series(self):
        # Return the sorted variation series (ascending order)
        return self.variation_series

    def get_distribution(self):
        # Return the statistical distribution containing the frequency, cumulative frequency, and relative frequency
        return self.distribution
