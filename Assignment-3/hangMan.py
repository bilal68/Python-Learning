import random


def choose_secret_word(word_list):
    return random.choice(word_list).lower()


def make_revealed(word):
    return ["_" for _ in word]


def format_revealed(revealed):
    return " ".join(revealed)


def get_guess(guessed_letters: set[str]) -> str:
    while True:
        guess = input("Your guess: ").strip().lower()

        if len(guess) != 1:
            print("Please enter exactly one character.")
            continue

        # Option A: allow any alphabetic letter
        if not guess.isalpha():
            print("Please enter a letter (a–z).")
            continue

        # Option B (stricter): uncomment to restrict to ASCII a–z only
        # if not ('a' <= guess <= 'z'):
        #     print("Please enter a letter (a–z).")
        #     continue

        if guess in guessed_letters:
            print(f"You already tried '{guess}'. Pick a new letter.")
            continue

        return guess


def apply_guess(
    secret_word: str,
    revealed: list[str],
    guessed_letters: set[str],
    wrong_letters: set[str],
    letter: str,
) -> bool:
    """Update revealed in-place. Return True if guess was correct."""
    guessed_letters.add(letter)
    hit = False
    for i, ch in enumerate(secret_word):
        if ch == letter:
            revealed[i] = letter
            hit = True
        if not hit:
            wrong_letters.add(letter)
    return hit


def has_won(revealed: list[str]) -> bool:
    return "_" not in revealed
def has_lost(wrong_count: int, max_wrong: int) -> bool:
    return wrong_count >= max_wrong 


if __name__ == "__main__":
    words = [ "java","kotlin","python","javascript"]
    secret_word = choose_secret_word(words)
    revealed = make_revealed(secret_word)
    guessed_letters: set[str] = set()
    wrong_letters: set[str] = set()
    max_wrong = 6
    wrong_count = 0
    print("Welcome to Hangman!")
    print("Guess the word:", format_revealed(revealed))  # For testing purposes

    while True:
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        
        hit = apply_guess(secret_word, revealed, guessed_letters, wrong_letters, guess)

        # 3) miss burns a life
        if hit:
            print("\n" + format_revealed(revealed))
        else:
            wrong_count += 1
            print("\nIncorrect!")
            print(format_revealed(revealed))

        # 4) end checks
        if has_won(revealed):
            print("\n🎉 You win! The word was:", secret_word)
            break

        if has_lost(wrong_count, max_wrong):
            print("\n💀 You lost. The word was:", secret_word)
            break
