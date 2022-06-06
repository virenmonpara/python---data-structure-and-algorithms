
def countX(lst, x):
    count = 0
    for i in lst:
        if (i == x):
            count = count + 1
    return count


# Driver Code
lst = [6, 10, 8, 10, 8, 20, 10, 8, 6, 6, 6]
x = 10
print('{} has occurred {} times'.format(x, countX(lst, x)))
