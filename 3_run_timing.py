
def run_timing():
    run_times = []
    while True:
        try:
            time = float(input("Enter 10km run time: "))
            run_times.append(time)
        except ValueError as _:
            break
    
    try:
        print(f'Average of {sum(run_times)/len(run_times)}, over {len(run_times)} runs')
    except ZeroDivisionError as _:
        print("There was an error with your input")

run_timing()