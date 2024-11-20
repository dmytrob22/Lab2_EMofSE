from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data
        self.variation_series = []
        self.distribution = []

    def calculate_variation_series(self):
        self.variation_series = sorted(self.data)

    def calculate_statistics(self):
        # Use Counter to count the occurrences (frequency) of each unique value in the variation series

        counts = Counter(self.variation_series)
        cumulative_frequency = 0
        total = len(self.variation_series)

        self.distribution = []

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
        return self.variation_series

    def get_distribution(self):
        return self.distribution
