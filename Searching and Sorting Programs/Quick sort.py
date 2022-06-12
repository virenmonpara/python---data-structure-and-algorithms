# i have learned this code from youtube video (link is given below)
#https://youtu.be/kFeXwkgnQ9U

def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr #returns list with one or zero element
    else:
        pivot = arr.pop() # choose last element as pivot

    less_then_pivot = [] 
    greater_then_pivot = []

    for i in arr:
        if i <= pivot: # if element is less than pivot add to less_then_pivot
            less_then_pivot.append(i)
        else: # if element is greater than pivot add to greater_then_pivot
            greater_then_pivot.append(i) 
    return quick_sort(less_then_pivot)+[pivot]+quick_sort(greater_then_pivot)


print(quick_sort([0,9,3,8,2,7,5]))
