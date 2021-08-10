# calculates in prefix notation
# ex + 3 4 = 3 + 4 = 7
import operator

def calc(to_solve):
    operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '%': operator.mod,
            '**': operator.pow}
    split =  to_solve.split()
    op = split[0]
    args = list(map(lambda x: int(x), split[1:]))

    curr_val = operations[op](args[0], args[1])

    for arg in args[2:]:
        curr_val = operations[op](curr_val, arg)
        

    return curr_val

print(calc('+ 3 4'))
print(calc(' + 3 5 7'))
print(calc(' / 100 5 5'))
