
def hex_output(num: str) -> int:
    sum = 0
    for idx, integer in enumerate(reversed(num)):
        sum += int(integer, 16) * (16 ** (idx))
    return sum

def name_triangle():
    name = input("what is your name? ")
    for idx, _ in enumerate(name):
        print(name[:idx + 1])

name_triangle()