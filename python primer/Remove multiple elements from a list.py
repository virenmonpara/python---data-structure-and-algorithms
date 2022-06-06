# remove even numbers from a list
list = [10, 58, 5, 215, 2, 68, 7]
list1 = list.copy()
for i in list1:
    if i % 2 == 0:
        list.remove(i)
print(list)

# remove even numbers from a list
list1 = [11, 5, 17, 18, 23, 50]
# excluding all even numbers
list1 = [im for im in list1 if im % 2 != 0]
print(*list1)
