# initialize list
test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# printing original list
print(test_list)

# initialize column number K
K = 2

# Get Kth Column of Matrix
# using list comprehension
res = [sub[K] for sub in test_list]

# printing result
print("The Kth column of matrix is : " + str(res))
