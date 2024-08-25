import random


def choose_word():
    word_list = ["Python", "Shadowfox", "Internship", "Intermediate", "Task"]
    return random.choice(word_list)


def setup_game():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempt = 7
    return word, guessed_letters, incorrect_guesses, max_attempt


def display_hangman(attempts):
    stages = [
        """
        
            -----
            |   |
            o   |
           /|\\  |
           / \\  |
                |
        ----------
        """,
        """
    
            -----
            |   |
            o   |
           /|\\  |
           /    |
                |
        ----------
        """,
        """
    
             -----
             |   |
             o   |
            /|\\  |
                 |
                 |
        ----------
        """,
        """
    
            -----
            |   |
            o   |
           /|   |
                |
                |
        ----------
        """,
        """
            -----
            |   |
            o   |
            |   |
                |
                |
        ----------
        """,
        """
            -----
            |   |
            o   |
                |
                |
                |
        ----------
        """,
        """
            -----
            |   |
                |
                |
                |
                |
        ----------
        """,

    ]
    return stages[attempts]


def display_interface(word, guessed_letters, incorrect_guesses):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(display_word)
    print(display_hangman(incorrect_guesses))


def get_input(guessed_letters):
    while True:
        guess = input("Guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter")
        elif guess in guessed_letters:
            print("You have already guessed it")
        else:
            return guess


def check_guess(word, guess, guessed_letters, incorrect_guesses):
    if guess in word:
        guessed_letters.append(guess)
        print(f"Good guess! :) The letter {guess} is in the word.")
    else:
        incorrect_guesses += 1
        print(f"Sorry! :( The letter {guess} ain't in the word.")
    return incorrect_guesses


def win_or_loss(word, guessed_letters, incorrect_guesses, max_attempt):
    if set(guessed_letters) == set(word):
        print(f"Congratulations! You've guessed the word: {word}")
        return True
    elif incorrect_guesses >= max_attempt:
        print(f"Game Over!")
        return True
    return False


def play_game():
    word, guessed_letters, incorrect_guesses, max_attempt = setup_game()

    while True:
        display_interface(word, guessed_letters, incorrect_guesses)
        guess = get_input(guessed_letters)
        incorrect_guesses = check_guess(word, guess, guessed_letters, incorrect_guesses)

        if win_or_loss(word, guessed_letters, incorrect_guesses, max_attempt):
            break


def again():
    while True:
        choice = input("Do you want to play again?:")
        print("Enter 'y' for YES and 'n' for NO")
        if choice == 'y':
            return True
        else:
            return False


def main():
    print("WELCOME TO HANGMAN!")
    while True:
        play_game()
        if not again():
            print("Thanks for playing......")
            break


if __name__ == '__main__':
    main()