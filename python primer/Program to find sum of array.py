# find sum of elements in given arrayay
def _sum(array):
    # initialize sum
    sum = 0
    # iterate through the arrayay
    for i in array:
        sum+= i
    return sum


# driver code
array1 = [1, 3, 4, 5]
print('Sum of the arrayay is ', _sum(array1))
