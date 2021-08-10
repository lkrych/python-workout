# calculates in prefix notation
# ex + 3 4 = 3 + 4 = 7

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def exp(a,b):
    return a ** b

def calc(to_solve):
    operations = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div,
            '%': mod,
            '**': exp}
    op, a, b =  to_solve.split()
    a = int(a)
    b = int(b)

    return operations[op](a,b)

print(calc('+ 3 4'))
