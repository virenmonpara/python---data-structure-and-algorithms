def even(list):
    a = []
    for i in list:
        if i % 2 == 0:
            a.append(i)
    return a


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers in the list are: \n", even(list))
