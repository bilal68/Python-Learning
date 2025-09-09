from collections import Counter
from pathlib import Path


def count_word_frequency(text: str) -> Counter:
    words = [w.strip(".,!?;:\"'()[]{}").lower() for w in text.split() if w.strip()]
    return Counter(words)

# Function to read a file
def read_file(path: str) -> str:
    """Reads and returns the file content as a string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# Function to check if a file exists
def file_exists(path: str) -> bool:
    """Returns True if the file exists, otherwise False."""
    return Path(path).exists()


# Example usage
if __name__ == "__main__":
    filename = "wordFrequency.txt"

    if file_exists(filename):
        content = read_file(filename)
        print("File words:\n", count_word_frequency(content))

    else:
        print(f"File '{filename}' does not exist.")

