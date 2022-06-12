# here i have used three different ways to sort the list
def selection_sort(lst):
    new_lst = []  # we can create a new list and append the sorted list to it
    for i in range(len(lst)):
        # find the index of the minimum element in the list
        min_index = lst.index(min(lst))
        # remove the minimum element from the list and append it to the new list
        new_lst.append(lst.pop(min_index))
    return new_lst


def selection_sort2(lst):
    new_lst = []
    for i in range(0, len(lst)):
        min = lst[0]
        for j in range(0, len(lst)):
            if lst[j] < min:
                min = lst[j]  # find the minimum element in the list
        lst.remove(min)  # remove the minimum element from the list
        new_lst.append(min)  # append the minimum element to the new list
    return new_lst


def selection_sort3(lst):
    for i in range(0, len(lst)):
        min = lst[i]
        for j in range(i+1, len(lst)):
            if lst[j] < min:
                min = lst[j]  # find the minimum element in the list
        if lst.index(min) != i:  # if the minimum element is not at the correct position
            lst[i], lst[lst.index(min)] = lst[lst.index(min)], lst[i]
    return lst


lst = [4, 6, 2, 8, 7]
print(selection_sort(lst))
lst = [4, 6, 2, 8, 7]
print(selection_sort2(lst))
lst = [4, 6, 2, 8, 7]
print(selection_sort2(lst))
