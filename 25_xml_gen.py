# myxml('foo') -> <foo></foo>
# myxml('foo', 'bar') -> <foo>bar</foo>
# myxml('foo', 'bar', a=1, b=2, c=3) -> <foo a="1" b="2" c="3">bar</foo>
# output will always be a string
def myxml(*args, **kwargs):
    xml = ""
    attr = ""

    if len(kwargs) > 0:
        for idx, kwarg in enumerate(kwargs.items()):
            #add space for first attr
            if idx == 0:
                attr += " "
            attr += f'{kwarg[0]}="{kwarg[1]}"'
    if len(args) == 1:
        xml = f'<{args[0]}{attr}></{args[0]}>'
    elif len(args) == 2:
        xml = f'<{args[0]}{attr}>{args[1]}</{args[0]}>'

    return xml


print(myxml('foo'))
print(myxml('foo', 'bar'))
print(myxml('foo', 'bar', a=1, b=2, c=3))
