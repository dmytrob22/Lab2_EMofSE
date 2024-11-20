class Display:
    @staticmethod
    def display_sequence(data):
        print("Generated Sequence:")
        print(data)

    @staticmethod
    def display_variation_series(variation_series):
        print("\nVariation Series (Sorted Data):")
        print(variation_series)

    @staticmethod
    def display_statistics(distribution):
        print("\nStatistical Distribution:")

        print(f"{'Value':<10}{'Frequency':<12}{'Cumulative Freq':<18}{'Relative Freq (%)':<18}")

        for row in distribution:
            print(f"{row['Value']:<10}{row['Frequency']:<12}{row['Cumulative Frequency']:<18}{row['Relative Frequency (%)']:<18.2f}")
