import re


def matching(str1, str2):
    match, j = 0, 0
    for i in str1:
        # this will check if character extracted from
        # str1 is present in str2 or not(str2.find(i)
        # return -1 if not found otherwise return the
        # starting occurrence index of that character
        # in str2) and j == str1.find(i) is used to
        # avoid the counting of the duplicate characters
        # present in str1 found in str2
        if str2.find(i) >= 0 and j == str1.find(i):
            match += 1
        j += 1
    return print(match)


str1 = "abcdefgh"
str2 = "aabbbcdijkl"
print(matching(str1, str2))

"""
# short method using re
# Count the Number of matching characters in
# a pair of string
ip1 = "geeks"
ip2 = "geeksonly"

c = 0
for i in ip1:
    if re.search(i, ip2):
        c = c+1
print("No. of matching characters are ", c)
"""
