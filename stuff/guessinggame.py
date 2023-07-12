from random import randint
number = randint(1, 100)
question = "What's your guess?"
print("I've thought of a number between 1 and 100. Try to guess it.")
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
        
