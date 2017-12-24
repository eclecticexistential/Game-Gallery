from collections import OrderedDict
import words
import Gallery

def hangman():
    word = words.get_words()
    placeHolder = "_ " * len(word)
    bodyParts = 10
    rightGuess = 0
    guessedLetters = []

    while True:
        print("The word you are looking for is: " + str(placeHolder))
        print("You have " + str(bodyParts) + " guesses left.")
        guess = input("Guess a letter: ").lower()
        # right = "no"
        for letter in word:
            if letter == guess:
                counter = word.index(letter)
                placeHolder[counter] = guess

        # if right == "no":
        #     bodyParts -= 1
        #     for guessed in guessedLetters:
        #         if guess == guessed:
        #             print("You have already guessed that letter.")
        #             break
        #         else:
        #             guessedLetters += guess
        #             break

        if rightGuess == len(word):
            print("YAAY! You guessed right! The word was {}.".format(word))
            play_again()
            break

        elif bodyParts == 0:
            print("The man was hung by these letters {}. Game over ;(".format(",".join(guessedLetters)))
            play_again()
            break


def play_again():
    answer = input("Would you like to play again?").lower()
    if answer == 'yes':
        hangman()
    elif answer == 'no':
        Gallery.gallery()