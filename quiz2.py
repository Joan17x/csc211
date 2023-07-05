name = input("Username:")
import time
import random
score = 0
while True:
    x = random.randint(1,10)
    y = random.randint(1,10)
    question = ("What is " + str(x) + " times " + str(y) + "?")
    answer = int(input(question))
    if answer == (x * y):
        print("Correct!")
        score += 1
    else:
        print("incorrect. The answer is " + str(x * y) + ".")
        score -= 2
    if score < 0:
        score = 0

    print(name + " has " + str(score) + " points")
    if score == 10:
        print("Congrats! You completed the quiz.")
        break
