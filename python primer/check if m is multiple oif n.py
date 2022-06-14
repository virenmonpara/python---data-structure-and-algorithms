def is_multiple(n, m):
    if m % n == 0:
        return True
    else:
        return False


m = int(input("Enter a number: "))
n = int(input("Enter a number to check if it is multiple of m: "))
print(is_multiple(n, m))
