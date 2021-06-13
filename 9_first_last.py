def firstlast(seq):
    return seq[:1] + seq[-1:]

def sum(seq):
    sum = 0
    for el in seq:
        sum += el
    return sum

def sum_even_odd_idxs(seq):
    evens = seq[::2]
    odds = seq[1::2]
    return [sum(odds), sum(evens)]

def plus_minus(seq):
    plus = True
    res = seq[0]
    for idx, el in enumerate(seq[1:]):
        if plus:
            res += el
            plus = False
        else:
            res -= el
            plus = True
    return res
#print(firstlast('abc'))
#print(firstlast([1,2,3]))
#print(firstlast((1,2,3)))

#print(sum_even_odd_idxs([1,2,3,4,5,6]))
print(plus_minus([10,20,30,40,50,60]))
