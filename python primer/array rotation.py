def array_rotation(arr, x):
    for i in range(x):
        arr.append(arr[0])
        del arr[0]
    return arr


arr = [1, 2, 3, 4, 5]
x = int(input("Enter the number of rotations: "))
print(array_rotation(arr, x))
