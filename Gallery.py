import sys
import play21
import Hangman
import guess_num
import comp_guess


while True:
    choice = ""
    choice = input("B for Black Jack, N to Let Comp Guess, H for Hangman, G to Guess the Number, or Q to quit?").upper()
    if choice == "B":
        play21.play_game()
    elif choice == "H":
        Hangman.hangman()
    elif choice == "N":
        comp_guess.comp_guess_game()
    elif choice == "G":
        guess_num.guess()
    elif choice == "Q":
        print("Goodbye!")
        sys.exit()
    else:
        print("Try again.")