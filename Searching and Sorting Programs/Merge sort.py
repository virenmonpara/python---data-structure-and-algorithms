import sys


def merge_sort(A):
    merge_sort2(A, 0, len(A)-1)


def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last)//2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)


def merge(A, first, middle, last):
    L = A[first:middle+1]
    R = A[middle+1:last+1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = j = 0

    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


A = [5, 9, 1, 2, 4, 8, 6, 3, 7]
print(A)
merge_sort(A)
print(A)

############################################################################
# def merge_sort(a):
#     merge_sort2(a, 0, len(a) - 1)


# def merge_sort2(a, first, last):
#     if first < last:
#         middle = (first + last) // 2
#         merge_sort2(a, first, middle)
#         merge_sort2(a, middle + 1, last)
#         merge(a, first, middle, last)


# def merge(a, first, middle, last):
#     l = a[first:middle]
#     r = a[middle:last+1]
#     l.append(float('inf'))
#     r.append(float('inf'))
#     i = j = 0
#     for k in range(first, last+1):
#         if l[i] <= r[j]:
#             a[k] = l[i]
#             i += 1
#         else:
#             a[k] = r[j]
#             j += 1


# a = [-7, 11, 6, 0, -3, 5, 10, 2]
# merge_sort(a)
# print(a)
