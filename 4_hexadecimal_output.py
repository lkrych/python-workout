
def hex_output(num: str) -> int:
    sum = 0
    for idx, integer in enumerate(num[::-1]):
        sum += int(integer) * (16 ** (idx))
    return sum

print(hex_output('50'))