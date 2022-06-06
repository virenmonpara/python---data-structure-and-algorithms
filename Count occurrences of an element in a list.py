
def countX(lst, x):
    count = 0
    for i in lst:
        if (i == x):
            count = count + 1
    return count


# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))
