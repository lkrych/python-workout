import random

def create_password_generator(s):
    def create_password(len):
        output = []
        for i in range(len):
            output.append(random.choice(s))
        return ''.join(output)
    return create_password


alpha_pass = create_password_generator('abcdef')
symbol_pass = create_password_generator('!@#$%')

print(alpha_pass(5))
print(alpha_pass(10))

print(symbol_pass(5))
print(symbol_pass(10))


