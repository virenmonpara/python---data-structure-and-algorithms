# How to check if a given number is Fibonacci number?
# easy method (found out by myself)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


z = int(input("Enter the number to check wather it is Fibonacci number: "))
n = 0  # defining initiation of fibonacci number
while fibonacci(n) <= z:
    y = fibonacci(n)
    n += 1
# compare the number with the fibonacci number
if y == z:
    print("Yes, The number is Fibonacci number")
else:
    print("No, The number is not Fibonacci number")

"""

# short method (found out on geeksforgeeks)
import math
def is_perfect_square(a):
    b=int(math.sqrt(a))
    return b*b==a
def isfibonacci(n):
    return is_perfect_square(5*n*n+4) or is_perfect_square(5*n*n-4)

z = int(input("Enter the number to check wather it is Fibonacci number: "))
if isfibonacci(z)==True:
    print("Yes, The number is Fibonacci number")
else:
    print("No, The number is not Fibonacci number")
    
"""
