def passwd_to_dict():
    d = {}
    for line in open("/etc/passwd"):
        split = line.split(":")
        if len(split) > 3:
            d[split[0]] = split[2]
    print(d)
    return d

passwd_to_dict()
