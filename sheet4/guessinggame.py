from random import randint
from gasp.utils import read_yesorno

while True:
    question = "Make a guess: "
    nquestion = "What would you like the range to be? "
    n = (int(input(nquestion)))
    number = randint(1, n)
    print("I've thought of a number between 1 and " + str(n) + ". Try to guess it.")
    guess = 0
    guesses = 0
    while True:
        guess = (int(input(question)))
        if guess < number:
            print("That's too low.")
            guesses = guesses +1
        if guess > number:
            print("That's too high.")
            guesses = guesses +1
        if guess == number:
            print("That was my number. Well done!")
            guesses = guesses +1
            print("You took " + str(guesses) + " guesses.")
            break
    if read_yesorno("Would you like another game?"):
        print("Bet")
    else:
        print("Okay, Bye!")
        break