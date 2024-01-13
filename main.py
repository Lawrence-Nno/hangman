def hangman():
    """
    This python script runs the popular Hangman Game on the console
    :return: A string, the end result
    """

    # imports other game components from hangman.py and random
    from hangman import hangman_ascii, hangman_word, word_bank_animal, word_bank_regular, word_bank_hard
    import random

    # The countdown a 'fail' while loop will run on
    hangman_countdown = 0

    # Welcome message
    print(hangman_word)

    # Determines the kind of words the player will guess
    level = input("Welcome, Enter '1' to Guess Names of Animals\n'2' for regular words\n'3' for Hard words\n")
    if level == '1':
        word = random.choice(word_bank_animal)
    elif level == '2':
        word = random.choice(word_bank_regular)
    else:
        word = random.choice(word_bank_hard)

    # This variable will display some parts of the word containing the guessed letter, if a letter was guessed right
    shown_word = []

    # This string will hold the already guessed letters
    already_guessed = ""
    for char in word:
        shown_word.append("_")

    while hangman_countdown < 7:
        guessed_letter = input("Guess a letter:\n")

        # Adds the guessed letter to the already_guessed string
        already_guessed += ' '.join(guessed_letter)

        if guessed_letter in word:
            for index, char in enumerate(word):
                if guessed_letter == char:
                    shown_word[index] = char

            # Prints the word with the letters that has been guessed correctly
            display_word = ' '.join(shown_word)
            print(display_word)

            # Checks if all the letters has been guessed correctly
            if '_' not in shown_word:
                print("You win!")

                # Checks if the player wants to play on or exit the game
                play_on = input("\n\n Do you wish to Play On?\nType 'y' to Play On or type 'n' to Exit")
                if play_on.lower() == 'y':
                    hangman()
                else:
                    break
        else:
            # Prints the hangman dying ascii art
            print(hangman_ascii[hangman_countdown])
            print("I just lost a life, PLEASE HELP!")
            # prints the already guessed letters to aid the player not to re-enter them
            print(f"You have already guessed {already_guessed}")
            hangman_countdown += 1
            if hangman_countdown == 7:
                print(f"You Lost! The correct word is {word}")
                play_on = input("\n\nDo you wish to Play On?\nType 'y' to Play On or type 'n' to Exit\n")
                if play_on.lower() == 'y':
                    hangman()
                else:
                    break


if __name__ == '__main__':
    hangman()


