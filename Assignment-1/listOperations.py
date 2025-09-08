def list_sum(numbers):
    """Returns the sum of a list of numbers."""
    return sum(numbers)

def list_average(numbers):
    """Returns the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def list_max(numbers):
    """Returns the maximum value in a list of numbers."""
    return max(numbers) if numbers else None

def reverse_list(lst):
    """Returns a reversed copy of the input list."""
    return lst[::-1]

# Example usage:
if __name__ == "__main__":
    numbers = [1, 5, 3, 8, 2]
    print("Sum:", list_sum(numbers))
    print("Average:", list_average(numbers))
    print("Maximum:", list_max(numbers))

    my_list = ['a', 'b', 'c']
    print("Reversed list:", reverse_list(my_list))