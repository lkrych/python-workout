import random

def guessing_game(num_guesses, highest_num):
    #randint is inclusive
    print(f"You have {num_guesses} to guess a number between 1 and {highest_num}")
    r = random.randint(1,highest_num)
    while num_guesses != 0:
        g = guess()
        if g == r:
            print("you are correct!")
            exit
        if g < r:
            print("too low")
        elif g > r: 
            print("too high")
        num_guesses -= 1
    print("You did not guess the correct number")

def guess():
    return int(input('Guess a number: '))

guessing_game(3, 10)
