
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

run_timing()