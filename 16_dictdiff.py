def dictdiff(d1, d2):
    diff = {}
    for k,v in d1.items():
        if k not in d2:
            diff[k] = [v, None]
        elif v != d2[k]:
            diff[k] = [v, d2[k]]
    for k,v in d2.items():
        if k not in d1:
            diff[k] = [v, None]
    return diff
x = {'a': 1, 'b': 2, 'c': 3}
y = {'a': 2, 'b': 2, 'd': 4}
print(dictdiff(x, y))

