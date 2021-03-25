from typing import List

def mysum(input: List[int], starting_val: int = 0) -> int:
    sum = starting_val
    for num in input:
        sum += num
    return sum

print(mysum([1,2,3]))
print(mysum([1,2,3],4))
