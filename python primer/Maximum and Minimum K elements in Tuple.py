def max_min(tup, x):
    lst = list(sorted(tup))
    min = []
    max = []
    for i in range(x):
        min.append(lst[i])
        max.append(lst[-i-1])
    print(min+max, '\n\nanother example')


tup = (3, 7, 1, 18, 9)
x = 2
max_min(tup, x)

# ----------------------------------------------------------------------------------------------------------------------
# onother example
# initializing tuple
test_tup = (5, 20, 3, 7, 6, 8)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# initializing K
K = 2

# Maximum and Minimum K elements in Tuple
# Using sorted() + loop
res = []
test_tup = list(sorted(test_tup))

for idx, val in enumerate(test_tup):
    if idx < K or idx >= len(test_tup) - K:
        res.append(val)
res = tuple(res)

# printing result
print("The extracted values : " + str(res))
