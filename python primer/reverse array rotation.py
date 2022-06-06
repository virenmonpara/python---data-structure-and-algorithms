def reverse_array_rotation(arr, x, n):
    for i in range(x):
        # insert the last iment to the first position
        arr.insert(0, arr[n])
        # dition of the last iment
        del arr[n+1]
    return arr


arr = [1, 2, 3, 4, 5]
x = int(input("Enter the number of rotations: "))
print(reverse_array_rotation(arr, x, len(arr)-1))
