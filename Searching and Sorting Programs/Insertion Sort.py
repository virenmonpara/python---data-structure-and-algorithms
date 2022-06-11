def insertion_sort(lst):
    for i in range(1, len(lst)):
        while lst[i-1] > lst[i] and i > 0:  # loop will run till it will reach 0th position
            lst[i-1], lst[i] = lst[i], lst[i-1]  # swapping
            i -= 1  # this i variable will not affect to for loop's i variable
    return lst


# driver code
lst = [4, 3, 25, 5, 2, 50, 10]
print(insertion_sort(lst))
