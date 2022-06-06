def ispalindrome(x):
    return x == x[::-1]


# Driver code
x = "rotator"
ans = ispalindrome(x)

if ans:
    print("Yes, it is palindrom")
else:
    print("No, it is not palindrom")
