import random
from numpy import base_repr

def guessing_game(num_guesses: int, highest_num:int ):
    #randint is inclusive
    r = random.randint(1,highest_num)
    base = random.choice([2, 10, 16])
    r = base_repr(r, base=base)
    print(f"You have {num_guesses} to guess a number between 1 and {highest_num}")
    print(f"You must enter your input with base: {base}")
    while num_guesses != 0:
        g = guess(base)
        comp = compare(g, r, base)
        if comp == "=":
            print("you are correct!")
            exit(0)
        if comp == ">":
            print("too high")
        elif comp == "<": 
            print("too low")
        num_guesses -= 1
    print(f"You did not guess the correct number, it was {r}")

def guess(base: int):
    user_input = input(f'Guess a number (please use base {base}): ')
    if base == 16:
        # in case folks use lower case hex input
        user_input = user_input.upper()
    return user_input

def compare(x: str, y: str, base: int):
    cmp = int(x, base) - int(y, base)
    if cmp == 0:
        return "="
    elif cmp > 0:
        return ">"
    else:
        return "<"

guessing_game(3, 16)
