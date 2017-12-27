import words
import Gallery


def hangman():
    word = words.get_words()
    placeHolder = "_" * len(word)
    hidden_word = list(placeHolder)

    bodyParts = 10
    rightGuess = []
    badGuess = []

    while True:
        print("The word you are looking for is: {}".format(" ".join(hidden_word)))
        print("You have " + str(bodyParts) + " guesses left.")
        guess = input("Guess a letter: ").lower()
        if guess in rightGuess or guess in badGuess:
            print("You have already guessed that letter!")
            continue
        right = "no"
        counter = 0
        for letter in word:
            if letter == guess:
                right = "yes"
                for position in hidden_word:
                    hidden_word[counter] = letter
                    rightGuess += guess
                    break
            counter += 1


        if right == "no":
            bodyParts -= 1
            for guessed in badGuess:
                if guess == guessed:
                    print("You have already guessed that letter.")
                    break
                else:
                    badGuess += guess
                    break

        if len(rightGuess) == len(word):
            print("YAAY! You guessed right! The word was {}.".format(word))
            play_again()
            break

        elif bodyParts == 0:
            print("The man was hung by these letters {}. Game over ;(".format(",".join(badGuess)))
            play_again()
            break


def play_again():
    answer = input("Would you like to play again?").lower()
    if answer == 'yes':
        hangman()
    elif answer == 'no':
        Gallery.gallery()