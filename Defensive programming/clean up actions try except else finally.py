def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

x=float(input("enter divident: "))
y=float(input("enter divisor: "))
divide(x,y)