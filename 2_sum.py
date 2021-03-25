from typing import List, Tuple

def mysum(input: List[int], starting_val: int = 0) -> int:
    sum = starting_val
    for num in input:
        sum += num
    return sum

def myaverage(input: List[int], starting_val: int = 0) -> int:
    sum = starting_val
    for num in input:
        sum += num
    return sum/len(input)

def statsOnStrings(input: List[str]) -> Tuple[int, int, int]:
    input.sort(key=len)
    shortest = len(input[0])
    longest = len(input[len(input) - 1])
    len_map = list(map(lambda x: len(x), input))
    average_word_length = myaverage(len_map)
    return (shortest, longest, average_word_length)


# print("mysum")
# print(mysum([1,2,3]))
# print(mysum([1,2,3], 4))

# print("myaverage")
# print(myaverage([1,2,3]))
# print(myaverage([1,2,3], 4))

print(statsOnStrings(["one", "fish", "two", "fish", "red", "fish", "barracuda"]))
