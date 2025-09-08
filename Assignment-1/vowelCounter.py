def count_vowels(text: str) -> int:
    """Count the number of vowels in a given text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    # Read string
    try:
        raw = input("Enter a string: ").strip()
        value = str(raw)
    except ValueError:
        print("Error: please enter a valid string.")
    else:
        vowel_count = count_vowels(value)
        print(f"The number of vowels in the given string is: {vowel_count}")