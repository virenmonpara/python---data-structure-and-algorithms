def array_mul_div(arr, length, divider):
    # intialize multiplication
    mul = 1
    for i in range(length):
        mul *= arr[i]
    # return remainder
    return mul % divider


arr = [1, 2, 3, 33, 45]
divider = int(input("Enter divider: "))
print(array_mul_div(arr, len(arr), divider))
