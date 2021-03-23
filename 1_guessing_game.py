import random

def guessing_game():
    r = random.randint(1,101)
    g = guess()
    while g != r:
        if g < r:
            print("too low")
        elif g > r: 
            print("too high")
        g = guess()
        continue
    print("just right")

def guess():
    return int(input('Guess a number: '))

guessing_game()
