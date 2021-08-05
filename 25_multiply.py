def multiply_args(*args):
    if len(args) == 0:
        print("you must pass at least 1 arg")
    product = 1
    for arg in args:
        product *= arg
    return product

print(multiply_args(1,2,3))
print(multiply_args(1,2,3,4,5))
