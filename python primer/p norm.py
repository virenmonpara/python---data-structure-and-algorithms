def norm(v, p):
    return sum(v**p for v in v)**(1/p)


v = [5, 7, 5]
p = len(v) or 2
print(norm(v, p))
