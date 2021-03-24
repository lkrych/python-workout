import random

def guessing_game():
    #randint is inclusive
    r = random.randint(1,100)
    while True:
        g = guess()
        if g == r:
            break
        if g < r:
            print("too low")
        elif g > r: 
            print("too high")
        continue
    print("just right")

def guess():
    return int(input('Guess a number: '))

guessing_game()
