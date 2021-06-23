def how_many_different_numbers(list):
    s = set()
    for el in list:
        s.add(el)
    return len(s)

print(how_many_different_numbers([1,2,3,4,2,3,4]))

print(how_many_different_numbers([1,2,1,2,1,2,1,2]))


