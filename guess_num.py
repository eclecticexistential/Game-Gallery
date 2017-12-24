import random
import Gallery

counter = 0
name = ""

def play_again(name,counter):
    answer = input("Would you like to play again "+name+"?").lower()
    if answer == 'yes':
        guess()
    elif answer == 'no':
        Gallery.gallery()

def guess():
    global counter
    global name
    if counter == 0:
        print("Hello. What is your name?")
        name = input()

    secretNumber = random.randint(1,20)
    print("Well, " + name + ", I am thinking of a number between 1 and 20. Can you guess it with 6 attempts?")

    counter += 1

    for guessesTaken in range(1, 7):
        while True:
            try:
                guesses_left = 7 - guessesTaken
                print(guesses_left, "guesses remaining.")
                guess = int(input('Take a guess.'))
            except ValueError:
                print("You did not enter a number.")
                continue
            break
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break #This condition is the correct guess!

    if guess == secretNumber:
        print('Good job! You guessed the secret number {} in {} guesses.'.format(secretNumber,guessesTaken))
        play_again(name,counter)
    else:
        print('Nope. The number I was thinking of was {}.'.format(secretNumber))