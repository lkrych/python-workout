def dictdiff(d1, d2):
    diff = {}
    all_keys = d1.keys() | d2.keys() #use the union operator to collect all keys

    for key in all_keys:
        if d1.get(key) != d2.get(key):
            diff[key] = [d1.get(key), d2.get(key)]
    
    return diff
x = {'a': 1, 'b': 2, 'c': 3}
y = {'a': 2, 'b': 2, 'd': 4}
print(dictdiff(x, y))

