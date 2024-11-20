class Display:
    @staticmethod
    def display_sequence(data):
        # This method is responsible for displaying the generated sequence.
        print("Generated Sequence:")
        print(data)

    @staticmethod
    def display_variation_series(variation_series):
        # This method displays the variation series, which is the sorted data.
        print("\nVariation Series (Sorted Data):")
        print(variation_series)

    @staticmethod
    def display_statistics(distribution):
        # This method displays the statistical distribution including frequency, cumulative frequency, and relative frequency.
        print("\nStatistical Distribution:")

        # Printing the headers with proper spacing.
        print(f"{'Value':<10}{'Frequency':<12}{'Cumulative Freq':<18}{'Relative Freq (%)':<18}")

        # Iterating over each row in the distribution and printing the values.
        for row in distribution:
            # Printing the values with left alignment and formatting the relative frequency to 2 decimal places.
            print(
                f"{row['Value']:<10}{row['Frequency']:<12}{row['Cumulative Frequency']:<18}{row['Relative Frequency (%)']:<18.2f}")
