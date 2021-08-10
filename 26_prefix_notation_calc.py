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
    op, a, b =  to_solve.split()
    a = int(a)
    b = int(b)

    return operations[op](a,b)

print(calc('+ 3 4'))
