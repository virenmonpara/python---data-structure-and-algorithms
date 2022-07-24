def fib(num):
    f1 = 0
    f2 = 1
    fs = 0
    while fs <= num:
        fs = f1+f2
        f1 = f2
        f2 = fs
        if fs == num:
            print(f"hurray, {num} is fibonacci number:")
            break
    else:
        print(f"{num} is not fibonacci number")


fib(6)
