
def get_final_line(file):
    print(f"finding last line of {file}")
    with open(file, 'r') as f:
        last_line = f.readlines()[-1]
        print(last_line)

get_final_line('test1.txt')
get_final_line('test2.txt')

