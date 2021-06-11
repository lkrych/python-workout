def ubbi_dubbi(w):
    ubb = []
    for c in w:
        if c in 'aeiou':
            ubb.append('ub')
        ubb.append(c)
    return "".join(ubb)

print(ubbi_dubbi("elephant"))
print(ubbi_dubbi("soap"))
print(ubbi_dubbi("octopus"))