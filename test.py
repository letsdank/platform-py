def first_method(l):
    l.append(1)

def second_method(l):
    l.append(2)

l = []
first_method(l)
second_method(l)

print(l) # Works!