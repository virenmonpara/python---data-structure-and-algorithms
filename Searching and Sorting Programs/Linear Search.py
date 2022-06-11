def linear_search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            # by defining global we make it global variale so we don't need to return pos
            globals()['pos'] = i+1
            return True


# driver code
list = [1, 2, 68, 125, 2548, 12647, 231696645]
n = 125
if linear_search(list, n):
    print("your number's position is: ", pos)
else:
    print('number is not found in list')


# another simple way
if n in list:
    print(list.index(n)+1)
