def get_mean_and_max(numbers):
    """Takes a list of numbers and returns a tuple of (mean, maximum)."""
    mean = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return mean, maximum

def main():
    print("Hello, I am Humzah Syedzaidi, and my Student ID is R02188601.")

    sample_numbers = [4,8,15,16,23,42]
    mean, maximum = get_mean_and_max(sample_numbers)

    print(f"Numbers:{sample_numbers}")
    print(f"Mean: {mean}")
    print(f"Maximum: {maximum}")

if __name__ == "__main__":
    main()