def mysum(*input: int):
    sum = 0
    for num in input:
        sum += num
    return sum

print(mysum(1,2,3))
