# myxml('foo') -> <foo></foo>
# myxml('foo', 'bar') -> <foo>bar</foo>
# myxml('foo', 'bar', a=1, b=2, c=3) -> <foo a="1" b="2" c="3">bar</foo>
# output will always be a string
def myxml(tag, content='', **kwargs):
    xml = ""
    attr = "".join([f' {k}="{v}"' for k,v in kwargs.items()])
    xml = f'<{tag}{attr}>{content}</{tag}>'

    return xml


print(myxml('foo'))
print(myxml('foo', 'bar'))
print(myxml('foo', 'bar', a=1, b=2, c=3))
