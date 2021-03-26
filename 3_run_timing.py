from decimal import Decimal

def run_timing():
    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input("Enter 10km run time: ")
        if not one_run:
            break

        try:
            number_of_runs += 1
            total_time += float(one_run)
        except ValueError as _:
            break
    try:
        print(f'Average of {(total_time/number_of_runs):.2f}, over {number_of_runs} runs')
    except ZeroDivisionError as _:
        print("There was an error with your input")

def decimal_input():
    user_input = []
    while True:
        user_in = input("Enter 10km run time: ")

        if not user_in:
            break

        try:
            user_input.append(
                Decimal(user_in)
            )
        except ValueError as _:
            print("There was an error with your input")
            exit(1)
    try:
        print(f'Total time is {sum(user_input)}')
    except ZeroDivisionError as _:
        print("There was an error with your input")

decimal_input()