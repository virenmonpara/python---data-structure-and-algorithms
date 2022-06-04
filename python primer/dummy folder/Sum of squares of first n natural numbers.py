# write a python programm for Sum of squares of first n natural numbers

def square(n):
    # long code
    sum=0
    for i in range(1,n,1):
        sum=sum+i*i
        return print(sum)
    
    # short code
    return print(sum(i**2 for i in range(1,n+1)))

x=int(input("Enter the number: "))
square(x)

