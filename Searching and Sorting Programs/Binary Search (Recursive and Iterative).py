def search(list, n):
    l = 0    # 0th place in list
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2  # for integer output
        if list[mid] == n:
            # by defining global we make it global variale so we don't need to return pos
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid


list = [4, 7, 8, 12, 15, 15, 49, 70]
n = 7

if search(list, n):
    print("Found at position", pos+1)
else:
    print("Not Found")


####################################################################################
# # Modifications needed for the older Python 2 are found in comments.

# # Returns index of x in arr if present, else -1
# def binary_search(arr, low, high, x):

# 	# Check base case
# 	if high >= low:

# 		mid = (high + low) // 2

# 		# If element is present at the middle itself
# 		if arr[mid] == x:
# 			return mid

# 		# If element is smaller than mid, then it can only
# 		# be present in left subarray
# 		elif arr[mid] > x:
# 			return binary_search(arr, low, mid - 1, x)

# 		# Else the element can only be present in right subarray
# 		else:
# 			return binary_search(arr, mid + 1, high, x)

# 	else:
# 		# Element is not present in the array
# 		return -1

# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 10

# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)

# if result != -1:
# 	print("Element is present at index", str(result))
# else:
# 	print("Element is not present in array")
