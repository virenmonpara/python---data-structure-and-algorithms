def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")
    elif x < 0:
        raise ValueError("x cannot be negative")
    else:
        return print(x**0.5)


i = eval(input("enter number to get sqrt"))

sqrt(i)
