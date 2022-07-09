# print fibonacci series of n numbers = [1,1,2,3,5,8,13,21,......]

def fibonacci(i):
    lst = [1]
    i0 = 0
    i1 = 1
    for x in range(i-1):
        i2 = i0+i1
        lst.append(i2)
        i0 = i1
        i1 = i2
    return print(lst)


fibonacci(10)
