# i have learned (only algoritm not code!!) from youtube video (link is given below)
# https://youtu.be/g_xesqdQqvA

def bubble_sort(lst):
    for i in range(len(lst)):
        switches = False  # to check if there is any switch in the list
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                switches = True
        if switches == False:
            break
    return lst


lst = [2, 4, 68, 0, -5, 9, -6, 10, 125, 2548, 254684]
print(bubble_sort(lst))
