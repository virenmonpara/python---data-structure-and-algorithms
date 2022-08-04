from memory_profiler import memory_usage

print(f'Memory usage before: {memory_usage()}MB')

# print fibonacci series of n numbers = [0,1,1,2,3,5,8,13,21,......]

def fibonacci(i):
    lst = [0, 1]
    i0 = 0
    i1 = 1
    for x in range(i-1):
        i2 = i0+i1
        lst.append(i2)
        i0 = i1
        i1 = i2
    return lst


result = fibonacci(10005)

print(f'Memory usage after: {memory_usage()}MB')
