# How to check if a given number is Fibonacci number?
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


z = int(input("Enter the number to check wather it is Fibonacci number: "))
n = 0
while fibonacci(n) <= z:
    y = fibonacci(n)
    n += 1
if y == z:
    print("The number is Fibonacci number")
else:
    print("The number is not Fibonacci number")
