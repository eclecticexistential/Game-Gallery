import random

def play_again():
    answer = input("Would you like to play again?").lower()
    if answer == 'yes':
        comp_guess_game()
    elif answer == 'no':
        import Gallery


def comp_guess_game():
    hidden_number = int(input("Provide a number between 1 and 10. Let's see if the computer can guess it in four attempts."))
    computer_guess = random.randint(1, 10)
    guesses = list()

    while True:
        guesses.append(computer_guess)
        if computer_guess == hidden_number:
            if len(guesses) == 1:
                print("The computer guessed your secret number {} on the first try!".format(hidden_number))
                play_again()
                break
            else:
                print("The computer guessed your secret number {} in {} attempts.".format(hidden_number,len(guesses)))
                play_again()
                break
        elif len(guesses) <= 3:
            if computer_guess < hidden_number:
                print("The computer's guess is {}. Let's tell them it's too low.".format(computer_guess))
                x = computer_guess+1
                computer_guess = random.randint(x,10)

            elif computer_guess > hidden_number:
                print("The computer's guess is {}. Let's tell them it's too high.".format(computer_guess))
                x = computer_guess-1
                computer_guess = random.randint(1,x)
        else:
            print("""You win!
The computer was unable to guess your number {} in 4 guesses.
""".format(hidden_number))
            play_again()
            break