import sys
import play21
import Hangman
import talk
import guess_num
import comp_guess


def gallery():
    choice = input("B for Black Jack, N to Let Comp Guess, H for Hangman, G to Guess the Number, C for ChatBot, or Q to quit?").upper()
    if choice == "B":
        play21
    elif choice == "H":
        Hangman.hangman()
    elif choice == "C":
        talk.convo()
    elif choice == "N":
        comp_guess.comp_guess_game()
    elif choice == "G":
        guess_num.guess()
    elif choice == "Q":
        sys.exit()
    else:
        print("Try again.")

gallery()