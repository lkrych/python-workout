
def mysum(*seqs):
    if not seqs:
        return seqs
    res = seqs[0]
    for s in seqs[1:]:
        res += s
    return res

print(mysum('abc','def'))
print(mysum([1,2,3], [4,5,6]))
print(mysum(1,2,3,4,5,6))
