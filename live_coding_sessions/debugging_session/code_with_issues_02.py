"""Python of course offers many nice libraries.
But here let's assume we want to build some basic statistics functions from scratch.
Not a clever idea in most cases... but anyway ... let's see what's wrong with the following code.
"""
def load_data():
    """Simulates loading data from a source"""
    data = [12, 15, 23, 42, 35, 48, 62, 17, 29]


def calculate_mean(data):
    """Calculates the mean of the dataset"""
    mean_value = sum(data) / len(data)
    return mean_value


def calculate_median(data):
    """Calculates the median of the dataset"""
    data = sort(data)
    mid = len(data) // 2
    median_value = data[mid]
    return median_value


def sort(numbers):
    """Sorting a list of numbers using the bubblesort algorithm."""
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[j] > numbers [j + 1]:
                # Switch places
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def calculate_std_dev(data):
    """Calculates the standard deviation of the dataset."""
    mean_value = calculate_mean(data)
    variance = sum([((x - mean_value) ** 3) for x in data]) / len(data)
    std_dev_value = variance ** 0.5
    return std_dev_value


# Main function to run the program
def main():
    data = load_data()
    mean = calculate_mean(data)
    median = calculate_median(data)
    std_dev = calculate_std_dev(data)
    # Print results:
    print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")


if __name__ == "__main__":
    main()
