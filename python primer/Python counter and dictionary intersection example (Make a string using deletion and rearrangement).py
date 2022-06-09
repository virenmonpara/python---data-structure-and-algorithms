# Python counter and dictionary intersection example
# (Make a string using deletion and rearrangement)
from collections import Counter


def str1_in_str2(str1, str2):
    # convert both strings into dictionaries
    # output will be like str1="aabbcc",
    # dict1={'a':2,'b':2,'c':2}
    # str2 = 'abbbcc', dict2={'a':1,'b':3,'c':2}
    dict1 = Counter(str1)
    dict2 = Counter(str2)

    # take intersection of two dictionaries
    # output will be result = {'a':1,'b':2,'c':2}
    result = dict1 & dict2

    # compare resultant dictionary with first
    # dictionary comparison first compares keys
    # and then compares their corresponding values
    return result == dict1

# driver code
print(str1_in_str2('ram', 'hellomra'))
