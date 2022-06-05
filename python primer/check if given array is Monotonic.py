
def is_array_monotronic(array):
    return (all(array[i] <= array[i+1] for i in range(len(array)-1)) or
            all(array[i] >= array[i+1] for i in range(len(array)-1)))


array = [6, 5, 4, 3, 1, 3, 2, 1]
print(is_array_monotronic(array))
