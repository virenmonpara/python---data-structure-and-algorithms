def negative_numbers(x, y):
    return [i for i in range(x, y+1, 1) if i < 0]


x = int(input("Enter the starting number: "))
y = int(input("Enter the ending number: "))
print(*negative_numbers(x, y), sep=", ")
