def first_method(l):
    l.append({'type': 'foo'})

def second_method(l):
    l.append({'type': 'bar'})

l = []
first_method(l)
second_method(l)

print(l) # Works!