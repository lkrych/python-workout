def strsort(s):
    arr = s.split()
    arr.sort()
    return "".join(arr)

print(strsort("cba"))