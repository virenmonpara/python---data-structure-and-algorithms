test_str = "iamvirenmonpara"

# printing original string
print("The original string is : " + test_str)

# using naive method to get
# Maximum frequency character in String
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
x = max(all_freq, key=all_freq.get)

# printing result
print("The maximum of all characters is : " + str(x))
